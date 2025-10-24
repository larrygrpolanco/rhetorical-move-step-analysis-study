"""
Stratified Consistency Analysis RQ2 - By Move and Step Type
============================================================
Analyzes consistency patterns stratified by:
- Move type (M1, M2, M3)
- Step type (1a, 1b, 1c, 2a, 2b, 2c, 2d, 3a, 3b, 3c, 3d)

Answers RQ2.4: Do consistency patterns differ by move or step type?

Author: Larry Grullon-Polanco
Date: 2025
"""

import json
import pandas as pd
import numpy as np
from pathlib import Path
from scipy import stats
import warnings

warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURATION
# ============================================================================

CONDITIONS = ["zero_shot", "fine_tuned"]
DATASET = "test"
MAX_RUNS = 50

# ============================================================================


def load_sentence_predictions(condition, run_num):
    """
    Load sentence-level predictions for a single run.
    
    Args:
        condition: Condition name
        run_num: Run number (1-50)
        
    Returns:
        list: List of sentence prediction dicts
    """
    run_dir = Path("outputs") / condition / f"rq2_run_{run_num:02d}" / "parsed"
    
    if not run_dir.exists():
        return []
    
    sentences = []
    
    # Load all article files
    for article_file in sorted(run_dir.glob("text*.json")):
        with open(article_file, 'r') as f:
            article_data = json.load(f)
        
        article_id = article_data['article_id']
        
        for sent in article_data['sentences']:
            sentence_id = f"{article_id}_s{sent['sentence_num']}"
            
            # Extract ground truth
            true_move = sent['tags'][0][0] if sent['tags'] else None
            true_step = sent.get('primary_tag')
            
            sentences.append({
                'sentence_id': sentence_id,
                'run_number': run_num,
                'true_move': true_move,
                'true_step': true_step,
                'move': sent.get('move'),
                'primary_tag': sent.get('primary_tag'),
                'text': sent.get('text', '')[:100] + '...'  # Truncated for display
            })
    
    return sentences


def load_all_sentence_data(condition, max_runs=50):
    """
    Load sentence-level data for all runs.
    
    Args:
        condition: Condition name
        max_runs: Maximum number of runs to load
        
    Returns:
        pd.DataFrame: All sentence predictions across runs
    """
    print(f"  Loading sentence data for {condition}...", end=" ")
    
    all_sentences = []
    
    for run_num in range(1, max_runs + 1):
        sentences = load_sentence_predictions(condition, run_num)
        if not sentences:
            break
        all_sentences.extend(sentences)
    
    if not all_sentences:
        print("No data found!")
        return pd.DataFrame()
    
    df = pd.DataFrame(all_sentences)
    print(f"✓ ({len(df)} observations from {run_num} runs)")
    
    return df


def load_evaluation_results(condition, max_runs=50):
    """
    Load evaluation results to get accuracy per run.
    
    Args:
        condition: Condition name
        max_runs: Maximum number of runs
        
    Returns:
        pd.DataFrame: Evaluation results
    """
    results_dir = Path("evaluation_results") / f"{condition}_rq2"
    
    runs_data = []
    
    for run_num in range(1, max_runs + 1):
        json_file = results_dir / f"run_{run_num:02d}.json"
        
        if not json_file.exists():
            break
        
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        runs_data.append({
            'run_number': run_num,
            'move_accuracy': data['move_metrics']['accuracy'],
            'step_accuracy': data['step_metrics']['accuracy']
        })
    
    return pd.DataFrame(runs_data)


def calculate_move_stratified_consistency(df_sentences, df_eval):
    """
    Calculate consistency metrics stratified by move type.
    
    Args:
        df_sentences: Sentence-level data
        df_eval: Evaluation results per run
        
    Returns:
        pd.DataFrame: Consistency by move type
    """
    # Get unique sentences and their true moves
    unique_sentences = df_sentences.groupby('sentence_id').first()[['true_move']].reset_index()
    
    # For each move type, calculate metrics
    move_stats = []
    
    for move in ['1', '2', '3']:
        # Get sentences of this move type
        move_sentences = unique_sentences[unique_sentences['true_move'] == move]['sentence_id'].tolist()
        
        if not move_sentences:
            continue
        
        # Get predictions for these sentences across all runs
        move_data = df_sentences[df_sentences['sentence_id'].isin(move_sentences)]
        
        # Calculate accuracy per run for this move
        run_accuracies = []
        for run_num in move_data['run_number'].unique():
            run_sents = move_data[move_data['run_number'] == run_num]
            accuracy = (run_sents['true_move'] == run_sents['move']).mean()
            run_accuracies.append(accuracy)
        
        # Calculate consistency metrics
        mean_acc = np.mean(run_accuracies)
        sd_acc = np.std(run_accuracies, ddof=1)
        cv = (sd_acc / mean_acc * 100) if mean_acc > 0 else 0
        
        move_stats.append({
            'move': f"M{move}",
            'n_sentences': len(move_sentences),
            'n_runs': len(run_accuracies),
            'mean_accuracy': mean_acc,
            'sd_accuracy': sd_acc,
            'cv': cv,
            'median': np.median(run_accuracies),
            'min': np.min(run_accuracies),
            'max': np.max(run_accuracies)
        })
    
    return pd.DataFrame(move_stats)


def calculate_step_stratified_consistency(df_sentences, min_support=10):
    """
    Calculate consistency metrics stratified by step type.
    
    Args:
        df_sentences: Sentence-level data
        min_support: Minimum number of sentences to include step
        
    Returns:
        pd.DataFrame: Consistency by step type
    """
    # Get unique sentences and their true steps
    unique_sentences = df_sentences.groupby('sentence_id').first()[['true_step']].reset_index()
    
    # For each step type, calculate metrics
    step_stats = []
    
    all_steps = ['1a', '1b', '1c', '2a', '2b', '2c', '2d', '3a', '3b', '3c', '3d']
    
    for step in all_steps:
        # Get sentences of this step type
        step_sentences = unique_sentences[unique_sentences['true_step'] == step]['sentence_id'].tolist()
        
        if len(step_sentences) < min_support:
            continue  # Skip rare steps
        
        # Get predictions for these sentences across all runs
        step_data = df_sentences[df_sentences['sentence_id'].isin(step_sentences)]
        
        # Calculate accuracy per run for this step
        run_accuracies = []
        for run_num in step_data['run_number'].unique():
            run_sents = step_data[step_data['run_number'] == run_num]
            accuracy = (run_sents['true_step'] == run_sents['primary_tag']).mean()
            run_accuracies.append(accuracy)
        
        # Calculate consistency metrics
        mean_acc = np.mean(run_accuracies)
        sd_acc = np.std(run_accuracies, ddof=1)
        cv = (sd_acc / mean_acc * 100) if mean_acc > 0 else 0
        
        step_stats.append({
            'step': step,
            'move': step[0],
            'n_sentences': len(step_sentences),
            'n_runs': len(run_accuracies),
            'mean_accuracy': mean_acc,
            'sd_accuracy': sd_acc,
            'cv': cv,
            'median': np.median(run_accuracies),
            'min': np.min(run_accuracies),
            'max': np.max(run_accuracies)
        })
    
    return pd.DataFrame(step_stats)


def compare_conditions_by_move(results):
    """
    Compare consistency between conditions stratified by move.
    
    Args:
        results: Dict of condition -> DataFrame
        
    Returns:
        pd.DataFrame: Comparison table
    """
    comparison = []
    
    moves = ['M1', 'M2', 'M3']
    
    for move in moves:
        row = {'move': move}
        
        for condition in CONDITIONS:
            df = results[condition]['by_move']
            move_row = df[df['move'] == move]
            
            if len(move_row) > 0:
                row[f'{condition}_cv'] = move_row['cv'].values[0]
                row[f'{condition}_accuracy'] = move_row['mean_accuracy'].values[0]
            else:
                row[f'{condition}_cv'] = np.nan
                row[f'{condition}_accuracy'] = np.nan
        
        # Calculate difference
        if len(CONDITIONS) == 2:
            cv_diff = row.get(f'{CONDITIONS[0]}_cv', np.nan) - row.get(f'{CONDITIONS[1]}_cv', np.nan)
            row['cv_difference'] = cv_diff
            row['more_consistent'] = CONDITIONS[0] if cv_diff < 0 else CONDITIONS[1]
        
        comparison.append(row)
    
    return pd.DataFrame(comparison)


def create_summary_report(results, output_dir):
    """
    Create comprehensive summary report.
    
    Args:
        results: Analysis results
        output_dir: Output directory
    """
    output_file = output_dir / "stratified_analysis_summary.txt"
    
    with open(output_file, 'w') as f:
        f.write("=" * 70 + "\n")
        f.write("STRATIFIED CONSISTENCY ANALYSIS - RQ2\n")
        f.write("=" * 70 + "\n\n")
        
        f.write(f"Dataset: {DATASET}\n")
        f.write(f"Research Question: RQ2.4\n")
        f.write(f"Conditions: {', '.join(CONDITIONS)}\n\n")
        
        # Move-level results for each condition
        for condition in CONDITIONS:
            f.write("-" * 70 + "\n")
            f.write(f"CONSISTENCY BY MOVE TYPE: {condition.upper()}\n")
            f.write("-" * 70 + "\n\n")
            
            df_move = results[condition]['by_move']
            
            for _, row in df_move.iterrows():
                f.write(f"{row['move']}:\n")
                f.write(f"  Sentences: {row['n_sentences']}\n")
                f.write(f"  Mean Accuracy: {row['mean_accuracy']:.4f} ({row['mean_accuracy']*100:.2f}%)\n")
                f.write(f"  SD: {row['sd_accuracy']:.4f}\n")
                f.write(f"  CV: {row['cv']:.2f}%\n")
                f.write(f"  Range: [{row['min']:.4f}, {row['max']:.4f}]\n")
                f.write("\n")
        
        # Cross-condition comparison
        f.write("-" * 70 + "\n")
        f.write("CROSS-CONDITION COMPARISON BY MOVE\n")
        f.write("-" * 70 + "\n\n")
        
        df_comp = results['comparison_by_move']
        f.write(df_comp.to_string(index=False))
        f.write("\n\n")
        
        # Step-level results
        for condition in CONDITIONS:
            f.write("-" * 70 + "\n")
            f.write(f"CONSISTENCY BY STEP TYPE: {condition.upper()}\n")
            f.write("-" * 70 + "\n\n")
            
            df_step = results[condition]['by_step']
            
            if len(df_step) > 0:
                f.write(df_step.to_string(index=False))
                f.write("\n\n")
            else:
                f.write("  No step-level data available\n\n")
        
        # Interpretation
        f.write("-" * 70 + "\n")
        f.write("KEY FINDINGS\n")
        f.write("-" * 70 + "\n\n")
        
        for condition in CONDITIONS:
            df_move = results[condition]['by_move']
            f.write(f"{condition.upper()}:\n")
            f.write(f"  Most consistent move: {df_move.loc[df_move['cv'].idxmin(), 'move']} ")
            f.write(f"(CV: {df_move['cv'].min():.2f}%)\n")
            f.write(f"  Least consistent move: {df_move.loc[df_move['cv'].idxmax(), 'move']} ")
            f.write(f"(CV: {df_move['cv'].max():.2f}%)\n\n")


def main():
    """Main execution."""
    
    print("=" * 70)
    print("STRATIFIED CONSISTENCY ANALYSIS - RQ2.4")
    print("=" * 70)
    
    # Create output directory
    output_dir = Path("evaluation_results") / "rq2_analysis" / "stratified"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    results = {}
    
    try:
        # Analyze each condition
        for condition in CONDITIONS:
            print(f"\nAnalyzing {condition}...")
            print("-" * 70)
            
            # Load sentence-level data
            df_sentences = load_all_sentence_data(condition, MAX_RUNS)
            
            if len(df_sentences) == 0:
                print(f"  ⚠️  No data found for {condition}")
                continue
            
            # Load evaluation results
            print(f"  Loading evaluation results...", end=" ")
            df_eval = load_evaluation_results(condition, MAX_RUNS)
            print(f"✓ ({len(df_eval)} runs)")
            
            # Calculate stratified metrics
            print(f"  Calculating move-level consistency...", end=" ")
            df_move = calculate_move_stratified_consistency(df_sentences, df_eval)
            print("✓")
            
            print(f"  Calculating step-level consistency...", end=" ")
            df_step = calculate_step_stratified_consistency(df_sentences, min_support=10)
            print("✓")
            
            results[condition] = {
                'by_move': df_move,
                'by_step': df_step,
                'df_sentences': df_sentences,
                'df_eval': df_eval
            }
            
            # Save individual condition results
            df_move.to_csv(output_dir / f"{condition}_by_move.csv", index=False)
            df_step.to_csv(output_dir / f"{condition}_by_step.csv", index=False)
        
        # Cross-condition comparison
        if len(results) == 2:
            print("\nComparing conditions...", end=" ")
            df_comp_move = compare_conditions_by_move(results)
            results['comparison_by_move'] = df_comp_move
            df_comp_move.to_csv(output_dir / "comparison_by_move.csv", index=False)
            print("✓")
        
        # Create summary report
        print("Creating summary report...", end=" ")
        create_summary_report(results, output_dir)
        print("✓")
        
        print("\n" + "=" * 70)
        print("✅ STRATIFIED ANALYSIS COMPLETE")
        print("=" * 70)
        print(f"\nOutput directory: {output_dir}/")
        print(f"Files created:")
        print(f"  - {CONDITIONS[0]}_by_move.csv")
        print(f"  - {CONDITIONS[0]}_by_step.csv")
        print(f"  - {CONDITIONS[1]}_by_move.csv")
        print(f"  - {CONDITIONS[1]}_by_step.csv")
        print(f"  - comparison_by_move.csv")
        print(f"  - stratified_analysis_summary.txt")
        print()
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
