"""
Analyze Sentences RQ2 - Sentence-Level Consistency Analysis
============================================================
Tracks consistency for each individual sentence across all 50 runs.

Performs:
- Agreement rate per sentence (% runs with correct prediction)
- Entropy calculation (label distribution uncertainty)
- Modal prediction (most common label)
- Consistency categorization (high, moderate, uncertain, problematic)
- Comparison across conditions
- Outputs: Sentence-level CSV with agreement rates

Author: Larry Grullon-Polanco
Date: 2025
"""

import pandas as pd
import numpy as np
from pathlib import Path
from scipy.stats import entropy as scipy_entropy
from collections import Counter

# ============================================================================
# CONFIGURATION
# ============================================================================

CONDITIONS = ["zero_shot", "fine_tuned"]  # Both conditions
DATASET = "test"  # Always 'test' for RQ2

# ============================================================================


def load_run_sentence_details(condition, run_num):
    """
    Load sentence-level details for a specific run.
    
    Args:
        condition: Condition name
        run_num: Run number
        
    Returns:
        pd.DataFrame: Sentence-level results
    """
    results_dir = Path("evaluation_results") / f"{condition}_rq2"
    csv_file = results_dir / f"run_{run_num:02d}.csv"
    
    if not csv_file.exists():
        raise FileNotFoundError(f"Run {run_num:02d} CSV not found: {csv_file}")
    
    return pd.read_csv(csv_file)


def load_all_sentence_data(condition, max_runs=100):
    """
    Load sentence-level data across all runs for a condition.
    
    Args:
        condition: Condition name
        max_runs: Maximum number of runs to load
        
    Returns:
        pd.DataFrame: Combined sentence data from all runs
    """
    all_data = []
    
    for run_num in range(1, max_runs + 1):
        try:
            df = load_run_sentence_details(condition, run_num)
            df['run_number'] = run_num
            all_data.append(df)
        except FileNotFoundError:
            # Stop when we hit missing runs
            break
    
    if not all_data:
        raise ValueError(f"No sentence data found for {condition}")
    
    return pd.concat(all_data, ignore_index=True)


def calculate_sentence_agreement(sentence_group, level='move'):
    """
    Calculate agreement metrics for a sentence across runs.
    
    Args:
        sentence_group: DataFrame group for one sentence
        level: 'move' or 'step'
        
    Returns:
        dict: Agreement metrics
    """
    n_runs = len(sentence_group)
    
    if level == 'move':
        gold_label = sentence_group['gold_move'].iloc[0]
        pred_labels = sentence_group['pred_move'].values
        correct = sentence_group['move_correct'].values
    else:
        gold_label = sentence_group['gold_step'].iloc[0]
        pred_labels = sentence_group['pred_step'].values
        correct = sentence_group['step_correct'].values
    
    # Agreement rate (% correct)
    agreement_rate = np.mean(correct)
    
    # Label distribution
    label_counts = Counter(pred_labels)
    label_probs = np.array([count / n_runs for count in label_counts.values()])
    
    # Shannon entropy (higher = more uncertainty)
    label_entropy = scipy_entropy(label_probs, base=2)
    
    # Modal prediction (most common)
    modal_pred = label_counts.most_common(1)[0][0]
    modal_freq = label_counts.most_common(1)[0][1] / n_runs
    
    # Consistency category
    if agreement_rate >= 0.9:
        category = "High consistency"
    elif agreement_rate >= 0.7:
        category = "Moderate consistency"
    elif agreement_rate >= 0.3:
        category = "Uncertain"
    else:
        category = "Problematic"
    
    return {
        'n_runs': n_runs,
        'gold_label': gold_label,
        'agreement_rate': agreement_rate,
        'n_correct': int(np.sum(correct)),
        'n_incorrect': int(np.sum(~correct)),
        'entropy': label_entropy,
        'modal_prediction': modal_pred,
        'modal_frequency': modal_freq,
        'unique_predictions': len(label_counts),
        'consistency_category': category,
    }


def analyze_sentence_consistency(condition, level='move'):
    """
    Analyze consistency for all sentences in a condition.
    
    Args:
        condition: Condition name
        level: 'move' or 'step'
        
    Returns:
        pd.DataFrame: Sentence-level consistency metrics
    """
    print(f"  Loading sentence data for {condition}...", end=" ")
    df_all = load_all_sentence_data(condition)
    n_runs = df_all['run_number'].nunique()
    n_sentences = df_all['sentence_num'].nunique()
    print(f"✓ ({n_runs} runs, {n_sentences} sentences)")
    
    print(f"  Calculating {level}-level agreement...", end=" ")
    
    # Group by sentence and calculate agreement
    results = []
    for sentence_num, group in df_all.groupby('sentence_num'):
        agreement = calculate_sentence_agreement(group, level)
        
        # Add sentence metadata
        result = {
            'sentence_num': sentence_num,
            'condition': condition,
            'level': level,
            'text_preview': group['text'].iloc[0] if 'text' in group.columns else '',
            **agreement
        }
        results.append(result)
    
    df_results = pd.DataFrame(results)
    print("✓")
    
    return df_results


def create_cross_condition_comparison(df_zs, df_ft):
    """
    Compare sentence consistency across conditions.
    
    Args:
        df_zs: Zero-shot sentence results
        df_ft: Fine-tuned sentence results
        
    Returns:
        pd.DataFrame: Combined comparison
    """
    # Merge on sentence_num
    df_merged = pd.merge(
        df_zs,
        df_ft,
        on=['sentence_num', 'gold_label', 'level'],
        suffixes=('_zs', '_ft')
    )
    
    # Calculate differences
    df_merged['agreement_diff'] = df_merged['agreement_rate_zs'] - df_merged['agreement_rate_ft']
    df_merged['entropy_diff'] = df_merged['entropy_zs'] - df_merged['entropy_ft']
    
    # Which condition is more consistent for each sentence
    df_merged['more_consistent'] = df_merged['agreement_diff'].apply(
        lambda x: 'Zero-shot' if x > 0 else ('Fine-tuned' if x < 0 else 'Equal')
    )
    
    return df_merged


def create_summary_stats(df_sentences, condition):
    """
    Calculate summary statistics for sentence-level consistency.
    
    Args:
        df_sentences: Sentence-level results
        condition: Condition name
        
    Returns:
        dict: Summary statistics
    """
    return {
        'condition': condition,
        'total_sentences': len(df_sentences),
        'mean_agreement': df_sentences['agreement_rate'].mean(),
        'median_agreement': df_sentences['agreement_rate'].median(),
        'sd_agreement': df_sentences['agreement_rate'].std(),
        'min_agreement': df_sentences['agreement_rate'].min(),
        'max_agreement': df_sentences['agreement_rate'].max(),
        'high_consistency_pct': (df_sentences['consistency_category'] == 'High consistency').sum() / len(df_sentences) * 100,
        'moderate_consistency_pct': (df_sentences['consistency_category'] == 'Moderate consistency').sum() / len(df_sentences) * 100,
        'uncertain_pct': (df_sentences['consistency_category'] == 'Uncertain').sum() / len(df_sentences) * 100,
        'problematic_pct': (df_sentences['consistency_category'] == 'Problematic').sum() / len(df_sentences) * 100,
        'mean_entropy': df_sentences['entropy'].mean(),
    }


def create_summary_report(df_zs_move, df_ft_move, df_comparison, output_file):
    """
    Create human-readable summary report.
    
    Args:
        df_zs_move: Zero-shot move-level results
        df_ft_move: Fine-tuned move-level results
        df_comparison: Cross-condition comparison
        output_file: Output file path
    """
    zs_stats = create_summary_stats(df_zs_move, 'zero_shot')
    ft_stats = create_summary_stats(df_ft_move, 'fine_tuned')
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=" * 70 + "\n")
        f.write("SENTENCE-LEVEL CONSISTENCY ANALYSIS - RQ2\n")
        f.write("=" * 70 + "\n\n")
        
        f.write(f"Dataset: {DATASET}\n")
        f.write(f"Total sentences: {zs_stats['total_sentences']}\n")
        f.write(f"Runs per condition: {df_zs_move['n_runs'].iloc[0]}\n\n")
        
        f.write("-" * 70 + "\n")
        f.write("1. ZERO-SHOT CONSISTENCY\n")
        f.write("-" * 70 + "\n\n")
        
        f.write(f"Mean agreement rate: {zs_stats['mean_agreement']:.3f} ({zs_stats['mean_agreement']*100:.1f}%)\n")
        f.write(f"SD: {zs_stats['sd_agreement']:.3f}\n")
        f.write(f"Range: [{zs_stats['min_agreement']:.3f}, {zs_stats['max_agreement']:.3f}]\n")
        f.write(f"Mean entropy: {zs_stats['mean_entropy']:.3f}\n\n")
        
        f.write("Sentence categories:\n")
        f.write(f"  High consistency (>90%):     {zs_stats['high_consistency_pct']:.1f}%\n")
        f.write(f"  Moderate consistency (70-90%): {zs_stats['moderate_consistency_pct']:.1f}%\n")
        f.write(f"  Uncertain (30-70%):          {zs_stats['uncertain_pct']:.1f}%\n")
        f.write(f"  Problematic (<30%):          {zs_stats['problematic_pct']:.1f}%\n\n")
        
        f.write("-" * 70 + "\n")
        f.write("2. FINE-TUNED CONSISTENCY\n")
        f.write("-" * 70 + "\n\n")
        
        f.write(f"Mean agreement rate: {ft_stats['mean_agreement']:.3f} ({ft_stats['mean_agreement']*100:.1f}%)\n")
        f.write(f"SD: {ft_stats['sd_agreement']:.3f}\n")
        f.write(f"Range: [{ft_stats['min_agreement']:.3f}, {ft_stats['max_agreement']:.3f}]\n")
        f.write(f"Mean entropy: {ft_stats['mean_entropy']:.3f}\n\n")
        
        f.write("Sentence categories:\n")
        f.write(f"  High consistency (>90%):     {ft_stats['high_consistency_pct']:.1f}%\n")
        f.write(f"  Moderate consistency (70-90%): {ft_stats['moderate_consistency_pct']:.1f}%\n")
        f.write(f"  Uncertain (30-70%):          {ft_stats['uncertain_pct']:.1f}%\n")
        f.write(f"  Problematic (<30%):          {ft_stats['problematic_pct']:.1f}%\n\n")
        
        f.write("-" * 70 + "\n")
        f.write("3. CROSS-CONDITION COMPARISON\n")
        f.write("-" * 70 + "\n\n")
        
        zs_better = (df_comparison['more_consistent'] == 'Zero-shot').sum()
        ft_better = (df_comparison['more_consistent'] == 'Fine-tuned').sum()
        equal = (df_comparison['more_consistent'] == 'Equal').sum()
        
        f.write(f"Sentences where Zero-shot is more consistent: {zs_better} ({zs_better/len(df_comparison)*100:.1f}%)\n")
        f.write(f"Sentences where Fine-tuned is more consistent: {ft_better} ({ft_better/len(df_comparison)*100:.1f}%)\n")
        f.write(f"Sentences with equal consistency: {equal} ({equal/len(df_comparison)*100:.1f}%)\n\n")
        
        # Most inconsistent sentences
        f.write("-" * 70 + "\n")
        f.write("4. MOST INCONSISTENT SENTENCES (Top 10)\n")
        f.write("-" * 70 + "\n\n")
        
        f.write("Zero-shot:\n")
        zs_worst = df_zs_move.nsmallest(10, 'agreement_rate')
        for _, row in zs_worst.iterrows():
            f.write(f"  Sentence {row['sentence_num']}: {row['agreement_rate']:.2%} agreement\n")
        f.write("\n")
        
        f.write("Fine-tuned:\n")
        ft_worst = df_ft_move.nsmallest(10, 'agreement_rate')
        for _, row in ft_worst.iterrows():
            f.write(f"  Sentence {row['sentence_num']}: {row['agreement_rate']:.2%} agreement\n")


def main():
    """Main execution."""
    
    print("=" * 70)
    print("SENTENCE-LEVEL CONSISTENCY ANALYSIS - RQ2")
    print("=" * 70)
    print()
    
    # Create output directory
    output_dir = Path("evaluation_results") / "rq2_analysis"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Analyze both conditions - Move level
        print("Analyzing MOVE-LEVEL consistency...")
        print()
        
        df_zs_move = analyze_sentence_consistency("zero_shot", level="move")
        df_ft_move = analyze_sentence_consistency("fine_tuned", level="move")
        
        print()
        print("Analyzing STEP-LEVEL consistency...")
        print()
        
        df_zs_step = analyze_sentence_consistency("zero_shot", level="step")
        df_ft_step = analyze_sentence_consistency("fine_tuned", level="step")
        
        print()
        print("Creating cross-condition comparisons...")
        
        df_comparison_move = create_cross_condition_comparison(df_zs_move, df_ft_move)
        df_comparison_step = create_cross_condition_comparison(df_zs_step, df_ft_step)
        print("  ✓ Comparisons created")
        
        print()
        print("Saving outputs...")
        
        # Save individual condition results
        df_zs_move.to_csv(output_dir / "sentences_zero_shot_move.csv", index=False)
        print("  ✓ sentences_zero_shot_move.csv")
        
        df_ft_move.to_csv(output_dir / "sentences_fine_tuned_move.csv", index=False)
        print("  ✓ sentences_fine_tuned_move.csv")
        
        df_zs_step.to_csv(output_dir / "sentences_zero_shot_step.csv", index=False)
        print("  ✓ sentences_zero_shot_step.csv")
        
        df_ft_step.to_csv(output_dir / "sentences_fine_tuned_step.csv", index=False)
        print("  ✓ sentences_fine_tuned_step.csv")
        
        # Save comparison results
        df_comparison_move.to_csv(output_dir / "sentences_comparison_move.csv", index=False)
        print("  ✓ sentences_comparison_move.csv")
        
        df_comparison_step.to_csv(output_dir / "sentences_comparison_step.csv", index=False)
        print("  ✓ sentences_comparison_step.csv")
        
        # Save summary statistics
        summary_stats = pd.DataFrame([
            create_summary_stats(df_zs_move, 'zero_shot_move'),
            create_summary_stats(df_ft_move, 'fine_tuned_move'),
            create_summary_stats(df_zs_step, 'zero_shot_step'),
            create_summary_stats(df_ft_step, 'fine_tuned_step'),
        ])
        summary_stats.to_csv(output_dir / "sentences_summary_stats.csv", index=False)
        print("  ✓ sentences_summary_stats.csv")
        
        # Create summary report
        create_summary_report(
            df_zs_move, df_ft_move, df_comparison_move,
            output_dir / "sentences_summary.txt"
        )
        print("  ✓ sentences_summary.txt")
        
        print("\n" + "=" * 70)
        print("✅ SENTENCE ANALYSIS COMPLETE")
        print("=" * 70)
        
        # Print key findings
        zs_stats = create_summary_stats(df_zs_move, 'zero_shot')
        ft_stats = create_summary_stats(df_ft_move, 'fine_tuned')
        
        print("\nKey Findings (Move-Level):")
        print(f"  Zero-shot:")
        print(f"    Mean agreement: {zs_stats['mean_agreement']:.1%}")
        print(f"    High consistency: {zs_stats['high_consistency_pct']:.1f}% of sentences")
        print(f"  Fine-tuned:")
        print(f"    Mean agreement: {ft_stats['mean_agreement']:.1%}")
        print(f"    High consistency: {ft_stats['high_consistency_pct']:.1f}% of sentences")
        
        print(f"\nOutput directory: {output_dir}/")
        print("\nNext step: Run 'visualize_rq2.py' to create figures")
        print()
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
