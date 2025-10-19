"""
Pilot Study Evaluation Script
==============================
Evaluates LLM move-step annotations against gold standard.

Computes move-level and step-level metrics following Kim & Lu (2024) methodology:
- Accuracy, Precision, Recall, F1 scores
- Both weighted and macro averages
- Per-move and per-step breakdowns
- Multi-tag handling: match against primary_tag

Generates markdown report in pilot_outputs/{condition}/{model}/evaluation.md

Author: Larry Grullon-Polanco
Date: 2025
"""

import json
from pathlib import Path
from collections import defaultdict, Counter
from difflib import SequenceMatcher


# ============================================================================
# CONFIGURATION - EDIT THESE VALUES
# ============================================================================

CONDITION = "a1_zero_shot"  # Which condition to evaluate
MODEL = "gpt-5mini"         # Which model to evaluate

# ============================================================================


def calculate_text_similarity(text1, text2):
    """
    Calculate similarity ratio between two texts.
    Used to verify sentence alignment.
    
    Returns:
        float: Similarity ratio between 0 and 1
    """
    return SequenceMatcher(None, text1.lower(), text2.lower()).ratio()


def load_gold_standard(article_id):
    """
    Load gold standard annotations for an article.
    
    Args:
        article_id: Article ID (e.g., "text001")
        
    Returns:
        list: Gold standard sentences
    """
    gold_path = Path(f"gold_standard/{article_id}.json")
    
    if not gold_path.exists():
        raise FileNotFoundError(f"Gold standard not found: {gold_path}")
    
    with open(gold_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_parsed_predictions(condition, model, article_id):
    """
    Load parsed LLM predictions for an article.
    
    Args:
        condition: Condition name (e.g., "a1_zero_shot")
        model: Model name (e.g., "gpt-5mini")
        article_id: Article ID (e.g., "text001")
        
    Returns:
        dict: Parsed prediction data
    """
    parsed_path = Path(f"pilot_outputs/{condition}/{model}/parsed/{article_id}.json")
    
    if not parsed_path.exists():
        raise FileNotFoundError(f"Parsed predictions not found: {parsed_path}")
    
    with open(parsed_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def align_sentences(gold_sentences, pred_data):
    """
    Align gold standard and predicted sentences.
    
    Uses sentence_num for alignment with text similarity verification.
    
    Args:
        gold_sentences: List of gold standard sentences
        pred_data: Parsed prediction data containing 'sentences' list
        
    Returns:
        tuple: (aligned_pairs, alignment_issues)
    """
    pred_sentences = pred_data['sentences']
    aligned_pairs = []
    alignment_issues = []
    
    # Check for sentence count mismatch
    if len(gold_sentences) != len(pred_sentences):
        alignment_issues.append({
            'type': 'count_mismatch',
            'message': f"Sentence count mismatch: Gold={len(gold_sentences)}, Pred={len(pred_sentences)}"
        })
    
    # Align by sentence_num
    gold_by_num = {s['sentence_num']: s for s in gold_sentences}
    pred_by_num = {s['sentence_num']: s for s in pred_sentences}
    
    all_nums = sorted(set(gold_by_num.keys()) | set(pred_by_num.keys()))
    
    for num in all_nums:
        gold_sent = gold_by_num.get(num)
        pred_sent = pred_by_num.get(num)
        
        if gold_sent is None:
            alignment_issues.append({
                'type': 'missing_gold',
                'sentence_num': num,
                'pred_text': pred_sent['text'][:50] + '...' if len(pred_sent['text']) > 50 else pred_sent['text']
            })
            continue
        
        if pred_sent is None:
            alignment_issues.append({
                'type': 'missing_pred',
                'sentence_num': num,
                'gold_text': gold_sent['text'][:50] + '...' if len(gold_sent['text']) > 50 else gold_sent['text']
            })
            continue
        
        # Check text similarity
        similarity = calculate_text_similarity(gold_sent['text'], pred_sent['text'])
        
        if similarity < 0.8:  # Flag low similarity
            alignment_issues.append({
                'type': 'low_similarity',
                'sentence_num': num,
                'similarity': similarity,
                'gold_text': gold_sent['text'][:50] + '...',
                'pred_text': pred_sent['text'][:50] + '...'
            })
        
        aligned_pairs.append({
            'sentence_num': num,
            'gold': gold_sent,
            'pred': pred_sent,
            'similarity': similarity
        })
    
    return aligned_pairs, alignment_issues


def calculate_metrics(aligned_pairs, level='move'):
    """
    Calculate classification metrics at move or step level.
    
    Following Kim & Lu (2024):
    - For multi-tag sentences: match against primary_tag only
    - Calculates: accuracy, precision, recall, F1
    - Both weighted and macro averages
    
    Args:
        aligned_pairs: List of aligned sentence pairs
        level: 'move' or 'step'
        
    Returns:
        dict: Metrics including per-class and overall statistics
    """
    # Extract true and predicted labels
    y_true = []
    y_pred = []
    
    for pair in aligned_pairs:
        if level == 'move':
            true_label = pair['gold']['move']
            pred_label = pair['pred']['move']
        else:  # step
            true_label = pair['gold']['primary_tag']
            pred_label = pair['pred']['primary_tag']
        
        y_true.append(true_label)
        y_pred.append(pred_label)
    
    # Get all unique labels
    all_labels = sorted(set(y_true) | set(y_pred))
    
    # Calculate per-class metrics
    per_class = {}
    
    for label in all_labels:
        # True Positives, False Positives, False Negatives
        tp = sum((t == label and p == label) for t, p in zip(y_true, y_pred))
        fp = sum((t != label and p == label) for t, p in zip(y_true, y_pred))
        fn = sum((t == label and p != label) for t, p in zip(y_true, y_pred))
        
        # Support (actual occurrences)
        support = sum(t == label for t in y_true)
        
        # Precision, Recall, F1
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
        
        per_class[label] = {
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'support': support,
            'tp': tp,
            'fp': fp,
            'fn': fn
        }
    
    # Overall accuracy
    correct = sum(t == p for t, p in zip(y_true, y_pred))
    total = len(y_true)
    accuracy = correct / total if total > 0 else 0.0
    
    # Weighted averages (weighted by support)
    total_support = sum(m['support'] for m in per_class.values())
    
    weighted_precision = sum(m['precision'] * m['support'] for m in per_class.values()) / total_support if total_support > 0 else 0.0
    weighted_recall = sum(m['recall'] * m['support'] for m in per_class.values()) / total_support if total_support > 0 else 0.0
    weighted_f1 = sum(m['f1'] * m['support'] for m in per_class.values()) / total_support if total_support > 0 else 0.0
    
    # Macro averages (unweighted - simple mean across classes)
    macro_precision = sum(m['precision'] for m in per_class.values()) / len(per_class) if per_class else 0.0
    macro_recall = sum(m['recall'] for m in per_class.values()) / len(per_class) if per_class else 0.0
    macro_f1 = sum(m['f1'] for m in per_class.values()) / len(per_class) if per_class else 0.0
    
    return {
        'accuracy': accuracy,
        'per_class': per_class,
        'weighted': {
            'precision': weighted_precision,
            'recall': weighted_recall,
            'f1': weighted_f1
        },
        'macro': {
            'precision': macro_precision,
            'recall': macro_recall,
            'f1': macro_f1
        },
        'total_support': total_support,
        'correct': correct,
        'total': total
    }


def calculate_multi_tag_stats(aligned_pairs):
    """
    Calculate statistics about multi-tag sentences.
    
    Following Kim & Lu (2024) reporting.
    
    Args:
        aligned_pairs: List of aligned sentence pairs
        
    Returns:
        dict: Multi-tag statistics
    """
    gold_multi = sum(len(pair['gold']['tags']) > 1 for pair in aligned_pairs)
    pred_multi = sum(len(pair['pred']['tags']) > 1 for pair in aligned_pairs)
    total = len(aligned_pairs)
    
    return {
        'gold_multi_tag': gold_multi,
        'pred_multi_tag': pred_multi,
        'total_sentences': total,
        'gold_multi_tag_pct': (gold_multi / total * 100) if total > 0 else 0.0,
        'pred_multi_tag_pct': (pred_multi / total * 100) if total > 0 else 0.0
    }


def generate_markdown_report(condition, model, all_results, output_path):
    """
    Generate comprehensive markdown evaluation report.
    
    Following Kim & Lu (2024) reporting style with explanatory notes.
    
    Args:
        condition: Condition name
        model: Model name
        all_results: Dictionary of results from all articles
        output_path: Path to save markdown file
    """
    md = []
    
    # Header
    md.append(f"# Evaluation Results: {condition} / {model}\n")
    md.append(f"*Generated: {Path.cwd()}*\n")
    md.append("---\n")
    
    # Aggregate metrics across all articles
    total_aligned = sum(len(r['aligned_pairs']) for r in all_results.values())
    total_issues = sum(len(r['alignment_issues']) for r in all_results.values())
    
    # Combine all aligned pairs for overall metrics
    all_aligned_pairs = []
    for result in all_results.values():
        all_aligned_pairs.extend(result['aligned_pairs'])
    
    # Calculate overall metrics
    move_metrics = calculate_metrics(all_aligned_pairs, level='move')
    step_metrics = calculate_metrics(all_aligned_pairs, level='step')
    multi_tag_stats = calculate_multi_tag_stats(all_aligned_pairs)
    
    # Summary Statistics
    md.append("## Summary Statistics\n")
    md.append(f"- **Articles Evaluated**: {len(all_results)}\n")
    md.append(f"- **Total Sentences**: {total_aligned}\n")
    md.append(f"- **Alignment Issues**: {total_issues}\n")
    md.append(f"- **Multi-tag Sentences (Gold)**: {multi_tag_stats['gold_multi_tag']} ({multi_tag_stats['gold_multi_tag_pct']:.1f}%)\n")
    md.append(f"- **Multi-tag Sentences (Predicted)**: {multi_tag_stats['pred_multi_tag']} ({multi_tag_stats['pred_multi_tag_pct']:.1f}%)\n")
    md.append("\n")
    
    # Move-Level Performance
    md.append("## Move-Level Performance\n")
    md.append("*Move classification evaluates broad rhetorical functions (Move 1, 2, 3)*\n\n")
    
    md.append(f"**Overall Accuracy**: {move_metrics['accuracy']:.1%}\n")
    md.append(f"- *Percentage of sentences where predicted move matches gold standard move*\n\n")
    
    md.append("### Weighted Averages\n")
    md.append("*Weighted by the number of instances of each move (accounts for class imbalance)*\n\n")
    md.append(f"- **Precision**: {move_metrics['weighted']['precision']:.1%}\n")
    md.append(f"  - *Of all sentences predicted as a given move, what % were correct?*\n")
    md.append(f"- **Recall**: {move_metrics['weighted']['recall']:.1%}\n")
    md.append(f"  - *Of all sentences that actually belong to a given move, what % were found?*\n")
    md.append(f"- **F1 Score**: {move_metrics['weighted']['f1']:.1%}\n")
    md.append(f"  - *Harmonic mean of precision and recall (balances both metrics)*\n\n")
    
    md.append("### Macro Averages\n")
    md.append("*Unweighted average across all moves (treats each move equally)*\n\n")
    md.append(f"- **Precision**: {move_metrics['macro']['precision']:.1%}\n")
    md.append(f"- **Recall**: {move_metrics['macro']['recall']:.1%}\n")
    md.append(f"- **F1 Score**: {move_metrics['macro']['f1']:.1%}\n\n")
    
    md.append("### Per-Move Breakdown\n\n")
    md.append("| Move | Precision | Recall | F1 Score | Support |\n")
    md.append("|------|-----------|--------|----------|----------|\n")
    
    for move in sorted(move_metrics['per_class'].keys()):
        m = move_metrics['per_class'][move]
        md.append(f"| {move} | {m['precision']:.1%} | {m['recall']:.1%} | {m['f1']:.1%} | {m['support']} |\n")
    
    md.append("\n*Support = number of sentences with this move in the gold standard*\n\n")
    
    # Step-Level Performance
    md.append("## Step-Level Performance\n")
    md.append("*Step classification evaluates fine-grained rhetorical functions (1a, 1b, 2a, etc.)*\n\n")
    
    md.append(f"**Overall Accuracy**: {step_metrics['accuracy']:.1%}\n")
    md.append(f"- *Percentage of sentences where predicted step matches gold standard primary step*\n\n")
    
    md.append("### Weighted Averages\n")
    md.append("*Weighted by the number of instances of each step*\n\n")
    md.append(f"- **Precision**: {step_metrics['weighted']['precision']:.1%}\n")
    md.append(f"- **Recall**: {step_metrics['weighted']['recall']:.1%}\n")
    md.append(f"- **F1 Score**: {step_metrics['weighted']['f1']:.1%}\n\n")
    
    md.append("### Macro Averages\n")
    md.append("*Unweighted average across all steps*\n\n")
    md.append(f"- **Precision**: {step_metrics['macro']['precision']:.1%}\n")
    md.append(f"- **Recall**: {step_metrics['macro']['recall']:.1%}\n")
    md.append(f"- **F1 Score**: {step_metrics['macro']['f1']:.1%}\n\n")
    
    md.append("### Per-Step Breakdown\n\n")
    md.append("| Step | Precision | Recall | F1 Score | Support |\n")
    md.append("|------|-----------|--------|----------|----------|\n")
    
    # Sort steps logically (1a, 1b, 1c, 2a, 2b, etc.)
    steps = sorted(step_metrics['per_class'].keys(), key=lambda x: (x[0], x[1:]))
    
    for step in steps:
        s = step_metrics['per_class'][step]
        md.append(f"| {step} | {s['precision']:.1%} | {s['recall']:.1%} | {s['f1']:.1%} | {s['support']} |\n")
    
    md.append("\n")
    
    # Per-Article Results
    md.append("## Per-Article Results\n\n")
    md.append("| Article | Sentences | Move Acc. | Step Acc. | Issues |\n")
    md.append("|---------|-----------|-----------|-----------|--------|\n")
    
    for article_id in sorted(all_results.keys()):
        result = all_results[article_id]
        
        # Calculate per-article metrics
        article_move = calculate_metrics(result['aligned_pairs'], level='move')
        article_step = calculate_metrics(result['aligned_pairs'], level='step')
        
        md.append(f"| {article_id} | {len(result['aligned_pairs'])} | "
                 f"{article_move['accuracy']:.1%} | {article_step['accuracy']:.1%} | "
                 f"{len(result['alignment_issues'])} |\n")
    
    md.append("\n")
    
    # Alignment Issues (if any)
    if total_issues > 0:
        md.append("## Alignment Issues\n")
        md.append("*These issues may require manual review*\n\n")
        
        for article_id, result in all_results.items():
            if result['alignment_issues']:
                md.append(f"### {article_id}\n\n")
                for issue in result['alignment_issues']:
                    if issue['type'] == 'count_mismatch':
                        md.append(f"- ⚠️ {issue['message']}\n")
                    elif issue['type'] == 'low_similarity':
                        md.append(f"- ⚠️ Sentence {issue['sentence_num']}: Low text similarity ({issue['similarity']:.2f})\n")
                        md.append(f"  - Gold: {issue['gold_text']}\n")
                        md.append(f"  - Pred: {issue['pred_text']}\n")
                    elif issue['type'] == 'missing_gold':
                        md.append(f"- ⚠️ Sentence {issue['sentence_num']}: Missing in gold standard\n")
                    elif issue['type'] == 'missing_pred':
                        md.append(f"- ⚠️ Sentence {issue['sentence_num']}: Missing in predictions\n")
                md.append("\n")
    
    # Write to file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(''.join(md))


def evaluate_condition(condition, model):
    """
    Evaluate all articles for a given condition and model.
    
    Args:
        condition: Condition name (e.g., "a1_zero_shot")
        model: Model name (e.g., "gpt-5mini")
    """
    print("=" * 70)
    print(f"Evaluating: {condition}/{model}")
    print("=" * 70)
    print()
    
    # Find all parsed files for this condition
    parsed_dir = Path(f"pilot_outputs/{condition}/{model}/parsed")
    
    if not parsed_dir.exists():
        print(f"ERROR: Parsed directory not found: {parsed_dir}")
        return
    
    parsed_files = sorted(parsed_dir.glob("*.json"))
    
    if not parsed_files:
        print(f"WARNING: No parsed files found in {parsed_dir}")
        return
    
    print(f"Found {len(parsed_files)} articles to evaluate")
    print()
    
    all_results = {}
    
    for parsed_file in parsed_files:
        article_id = parsed_file.stem
        
        print(f"Evaluating {article_id}...", end=" ")
        
        try:
            # Load data
            gold_sentences = load_gold_standard(article_id)
            pred_data = load_parsed_predictions(condition, model, article_id)
            
            # Align sentences
            aligned_pairs, alignment_issues = align_sentences(gold_sentences, pred_data)
            
            # Store results
            all_results[article_id] = {
                'aligned_pairs': aligned_pairs,
                'alignment_issues': alignment_issues
            }
            
            print(f"✓ ({len(aligned_pairs)} sentences, {len(alignment_issues)} issues)")
            
        except Exception as e:
            print(f"✗ ERROR: {e}")
    
    print()
    print("=" * 70)
    print("Generating Report")
    print("=" * 70)
    
    # Generate markdown report
    output_path = Path(f"pilot_outputs/{condition}/{model}/evaluation.md")
    generate_markdown_report(condition, model, all_results, output_path)
    
    print(f"✓ Report saved to: {output_path}")
    print()
    print("=" * 70)
    print("EVALUATION COMPLETE")
    print("=" * 70)


def main():
    """Main execution function."""
    evaluate_condition(CONDITION, MODEL)


if __name__ == "__main__":
    main()
