"""
Evaluate Condition - Single Condition Evaluation Script
========================================================
Evaluates one experimental condition against the gold standard.

Performs:
- Data validation (checks for errors requiring re-runs)
- Move-level metrics (3 classes: 1, 2, 3)
- Step-level metrics (11 classes: 1a, 1b, 1c, 2a, 2b, 2c, 2d, 3a, 3b, 3c, 3d)
- Outputs: Markdown summary, CSV details, JSON metrics

Following Kim & Lu (2024) evaluation methodology.

Author: Larry Grullon-Polanco
Date: 2025
"""

import json
import pandas as pd
from pathlib import Path
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    classification_report,
)

# ============================================================================
# CONFIGURATION
# ============================================================================

CONDITION = "three_shot"  # Options: zero_shot, three_shot, eight_shot, fine_tuned
DATASET = "validation"  # Options: validation, test
RESEARCH_QUESTION = "rq1"  # Options: rq1, rq2_run_01, rq2_run_02, etc.

# Article ranges
ARTICLE_RANGES = {
    "validation": range(1, 11),  # Articles 1-10
    "test": range(11, 21),  # Articles 11-20
}

# ============================================================================


class EvaluationError(Exception):
    """Custom exception for evaluation errors requiring article re-run."""

    pass


def load_gold_standard(article_num, dataset):
    """
    Load gold standard annotations for an article.

    Args:
        article_num: Article number (e.g., 1, 11)
        dataset: 'validation' or 'test'

    Returns:
        dict: Gold standard data with sentences
    """
    article_id = f"text{article_num:03d}"
    gold_file = Path(f"gold_standard/CaRS-50/{dataset}/json/{article_id}.json")

    if not gold_file.exists():
        raise FileNotFoundError(f"Gold standard not found: {gold_file}")

    with open(gold_file, "r", encoding="utf-8") as f:
        return json.load(f)


def load_predictions(article_num, condition, research_question, dataset):
    """
    Load model predictions for an article.

    Args:
        article_num: Article number
        condition: Experimental condition
        research_question: 'rq1' or 'rq2_run_XX'
        dataset: 'validation' or 'test'

    Returns:
        dict: Parsed predictions with sentences
    """
    article_id = f"text{article_num:03d}"

    # Determine folder based on research question
    if research_question == "rq1":
        folder = f"rq1_{dataset}"
    else:
        folder = research_question  # e.g., 'rq2_run_01'

    pred_file = Path(f"outputs/{condition}/{folder}/parsed/{article_id}.json")

    if not pred_file.exists():
        raise FileNotFoundError(f"Predictions not found: {pred_file}")

    with open(pred_file, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_article(gold, pred, article_id):
    """
    Validate article data for errors requiring re-run.

    Args:
        gold: Gold standard data
        pred: Prediction data
        article_id: Article identifier

    Raises:
        EvaluationError: If validation fails
    """
    errors = []

    # Check 1: Multi-tags (CaRS-50 has no multi-tags)
    for sent in pred["sentences"]:
        if len(sent["tags"]) > 1:
            errors.append(
                f"Multi-tag detected in sentence {sent['sentence_num']}: {sent['tags']}"
            )

    # Check 2: Sentence count mismatch
    gold_count = len(gold["sentences"])
    pred_count = len(pred["sentences"])
    if gold_count != pred_count:
        errors.append(
            f"Sentence count mismatch: gold={gold_count}, predicted={pred_count}"
        )

    # Check 3: Parse warnings
    if pred["parse_stats"]["warnings"]:
        errors.append(f"Parser warnings: {len(pred['parse_stats']['warnings'])} issues")

    # Check 4: Invalid tags
    if pred["parse_stats"]["invalid_tags"] > 0:
        errors.append(f"Invalid tags: {pred['parse_stats']['invalid_tags']}")

    if errors:
        error_msg = f"\n❌ VALIDATION FAILED for {article_id}:\n"
        error_msg += "\n".join(f"  - {err}" for err in errors)
        error_msg += "\n\n⚠️  This article needs to be re-run.\n"
        raise EvaluationError(error_msg)


def align_sentences(gold, pred):
    """
    Align gold and predicted sentences for evaluation.

    Args:
        gold: Gold standard data
        pred: Prediction data

    Returns:
        tuple: (gold_moves, pred_moves, gold_steps, pred_steps, sentence_details)
    """
    gold_moves = []
    pred_moves = []
    gold_steps = []
    pred_steps = []
    sentence_details = []

    for gold_sent, pred_sent in zip(gold["sentences"], pred["sentences"]):
        gold_moves.append(gold_sent["move"])
        pred_moves.append(pred_sent["move"])
        gold_steps.append(gold_sent["step"])
        pred_steps.append(pred_sent["primary_tag"])

        sentence_details.append(
            {
                "sentence_num": gold_sent["sentence_num"],
                "text": gold_sent["text"][:80] + "...",  # Truncate for readability
                "gold_move": gold_sent["move"],
                "pred_move": pred_sent["move"],
                "gold_step": gold_sent["step"],
                "pred_step": pred_sent["primary_tag"],
                "move_correct": gold_sent["move"] == pred_sent["move"],
                "step_correct": gold_sent["step"] == pred_sent["primary_tag"],
            }
        )

    return gold_moves, pred_moves, gold_steps, pred_steps, sentence_details


def calculate_metrics(y_true, y_pred, labels):
    """
    Calculate precision, recall, F1, and accuracy.

    Args:
        y_true: True labels
        y_pred: Predicted labels
        labels: List of possible labels

    Returns:
        dict: Metrics dictionary
    """
    # Overall accuracy
    accuracy = accuracy_score(y_true, y_pred)

    # Per-class metrics
    precision, recall, f1, support = precision_recall_fscore_support(
        y_true, y_pred, labels=labels, average=None, zero_division=0
    )

    # Weighted averages
    (
        weighted_precision,
        weighted_recall,
        weighted_f1,
        _,
    ) = precision_recall_fscore_support(
        y_true, y_pred, labels=labels, average="weighted", zero_division=0
    )

    # Build per-class results
    per_class = {}
    for i, label in enumerate(labels):
        per_class[label] = {
            "precision": float(precision[i]),
            "recall": float(recall[i]),
            "f1": float(f1[i]),
            "support": int(support[i]),
        }

    return {
        "accuracy": float(accuracy),
        "weighted_precision": float(weighted_precision),
        "weighted_recall": float(weighted_recall),
        "weighted_f1": float(weighted_f1),
        "per_class": per_class,
    }


def evaluate_article(article_num, condition, research_question, dataset):
    """
    Evaluate a single article.

    Args:
        article_num: Article number
        condition: Experimental condition
        research_question: RQ identifier
        dataset: Dataset name

    Returns:
        dict: Article evaluation results
    """
    article_id = f"text{article_num:03d}"

    # Load data
    gold = load_gold_standard(article_num, dataset)
    pred = load_predictions(article_num, condition, research_question, dataset)

    # Validate
    validate_article(gold, pred, article_id)

    # Align sentences
    gold_moves, pred_moves, gold_steps, pred_steps, details = align_sentences(
        gold, pred
    )

    # Calculate move-level metrics
    move_labels = ["1", "2", "3"]
    move_metrics = calculate_metrics(gold_moves, pred_moves, move_labels)

    # Calculate step-level metrics
    step_labels = ["1a", "1b", "1c", "2a", "2b", "2c", "2d", "3a", "3b", "3c", "3d"]
    step_metrics = calculate_metrics(gold_steps, pred_steps, step_labels)

    return {
        "article_id": article_id,
        "sentence_count": len(gold["sentences"]),
        "move_metrics": move_metrics,
        "step_metrics": step_metrics,
        "sentence_details": details,
    }


def aggregate_results(article_results):
    """
    Aggregate results across all articles.

    Args:
        article_results: List of article result dicts

    Returns:
        dict: Aggregated metrics
    """
    # Collect all sentences across articles
    all_gold_moves = []
    all_pred_moves = []
    all_gold_steps = []
    all_pred_steps = []
    all_details = []

    for article in article_results:
        for detail in article["sentence_details"]:
            all_gold_moves.append(detail["gold_move"])
            all_pred_moves.append(detail["pred_move"])
            all_gold_steps.append(detail["gold_step"])
            all_pred_steps.append(detail["pred_step"])
            all_details.append(detail)

    # Calculate overall metrics
    move_labels = ["1", "2", "3"]
    step_labels = ["1a", "1b", "1c", "2a", "2b", "2c", "2d", "3a", "3b", "3c", "3d"]

    move_metrics = calculate_metrics(all_gold_moves, all_pred_moves, move_labels)
    step_metrics = calculate_metrics(all_gold_steps, all_pred_steps, step_labels)

    return {
        "total_articles": len(article_results),
        "total_sentences": len(all_details),
        "move_metrics": move_metrics,
        "step_metrics": step_metrics,
        "article_results": article_results,
        "all_sentence_details": all_details,
    }


def save_markdown_summary(results, output_file, condition, dataset, research_question):
    """
    Save human-readable markdown summary.

    Args:
        results: Aggregated results
        output_file: Path to output file
        condition: Condition name
        dataset: Dataset name
        research_question: RQ identifier
    """
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Evaluation Results\n\n")
        f.write(f"**Condition:** {condition}  \n")
        f.write(f"**Dataset:** {dataset}  \n")
        f.write(f"**Research Question:** {research_question}  \n")
        f.write(f"**Articles Evaluated:** {results['total_articles']}  \n")
        f.write(f"**Total Sentences:** {results['total_sentences']}  \n\n")

        f.write("---\n\n")

        # Move-level results
        f.write("## Move-Level Results (3 classes)\n\n")
        move = results["move_metrics"]
        f.write(
            f"**Overall Accuracy:** {move['accuracy']:.4f} ({move['accuracy']*100:.2f}%)  \n\n"
        )
        f.write(f"**Weighted Precision:** {move['weighted_precision']:.4f}  \n")
        f.write(f"**Weighted Recall:** {move['weighted_recall']:.4f}  \n")
        f.write(f"**Weighted F1:** {move['weighted_f1']:.4f}  \n\n")

        f.write("### Per-Move Performance\n\n")
        f.write("| Move | Precision | Recall | F1 | Support |\n")
        f.write("|------|-----------|--------|----|---------|\n")
        for label in ["1", "2", "3"]:
            metrics = move["per_class"][label]
            f.write(
                f"| {label} | {metrics['precision']:.4f} | {metrics['recall']:.4f} | "
                f"{metrics['f1']:.4f} | {metrics['support']} |\n"
            )

        f.write("\n---\n\n")

        # Step-level results
        f.write("## Step-Level Results (11 classes)\n\n")
        step = results["step_metrics"]
        f.write(
            f"**Overall Accuracy:** {step['accuracy']:.4f} ({step['accuracy']*100:.2f}%)  \n\n"
        )
        f.write(f"**Weighted Precision:** {step['weighted_precision']:.4f}  \n")
        f.write(f"**Weighted Recall:** {step['weighted_recall']:.4f}  \n")
        f.write(f"**Weighted F1:** {step['weighted_f1']:.4f}  \n\n")

        f.write("### Per-Step Performance\n\n")
        f.write("| Step | Precision | Recall | F1 | Support |\n")
        f.write("|------|-----------|--------|----|---------|\n")
        step_labels = ["1a", "1b", "1c", "2a", "2b", "2c", "2d", "3a", "3b", "3c", "3d"]
        for label in step_labels:
            metrics = step["per_class"][label]
            f.write(
                f"| {label} | {metrics['precision']:.4f} | {metrics['recall']:.4f} | "
                f"{metrics['f1']:.4f} | {metrics['support']} |\n"
            )

        f.write("\n---\n\n")

        # Article breakdown
        f.write("## Article-Level Breakdown\n\n")
        f.write("| Article | Sentences | Move Accuracy | Step Accuracy |\n")
        f.write("|---------|-----------|---------------|---------------|\n")
        for article in results["article_results"]:
            move_acc = article["move_metrics"]["accuracy"]
            step_acc = article["step_metrics"]["accuracy"]
            f.write(
                f"| {article['article_id']} | {article['sentence_count']} | "
                f"{move_acc:.4f} | {step_acc:.4f} |\n"
            )


def save_csv_details(results, output_file):
    """
    Save detailed sentence-level results to CSV.

    Args:
        results: Aggregated results
        output_file: Path to output file
    """
    df = pd.DataFrame(results["all_sentence_details"])
    df.to_csv(output_file, index=False)


def save_json_metrics(results, output_file, condition, dataset, research_question):
    """
    Save machine-readable metrics to JSON.

    Args:
        results: Aggregated results
        output_file: Path to output file
        condition: Condition name
        dataset: Dataset name
        research_question: RQ identifier
    """
    output_data = {
        "condition": condition,
        "dataset": dataset,
        "research_question": research_question,
        "total_articles": results["total_articles"],
        "total_sentences": results["total_sentences"],
        "move_metrics": results["move_metrics"],
        "step_metrics": results["step_metrics"],
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)


def main():
    """Main execution."""

    print("=" * 70)
    print(f"Evaluating Condition: {CONDITION}")
    print(f"Dataset: {DATASET}")
    print(f"Research Question: {RESEARCH_QUESTION}")
    print("=" * 70)
    print()

    # Determine article range
    article_range = ARTICLE_RANGES[DATASET]
    print(f"Articles to evaluate: {min(article_range)}-{max(article_range)}")
    print()

    # Create output directory
    output_dir = Path("evaluation_results")
    output_dir.mkdir(exist_ok=True)

    # Evaluate each article
    article_results = []
    failed_articles = []

    print("Evaluating articles...")
    print("-" * 70)

    for article_num in article_range:
        article_id = f"text{article_num:03d}"
        print(f"  {article_id}...", end=" ", flush=True)

        try:
            result = evaluate_article(
                article_num, CONDITION, RESEARCH_QUESTION, DATASET
            )
            article_results.append(result)
            print(f"✓ ({result['sentence_count']} sentences)")

        except EvaluationError as e:
            print(f"✗ FAILED")
            print(str(e))
            failed_articles.append(article_id)

        except Exception as e:
            print(f"✗ ERROR: {e}")
            failed_articles.append(article_id)

    print()

    # Check if any articles failed
    if failed_articles:
        print("=" * 70)
        print("⚠️  EVALUATION INCOMPLETE")
        print("=" * 70)
        print(f"\nFailed articles ({len(failed_articles)}):")
        for article_id in failed_articles:
            print(f"  - {article_id}")
        print("\n⚠️  Re-run failed articles before continuing.\n")
        return

    # Aggregate results
    print("Aggregating results...")
    results = aggregate_results(article_results)

    # Generate output filename base
    output_base = f"{CONDITION}_{RESEARCH_QUESTION}_{DATASET}"

    # Save outputs
    print("Saving results...")
    save_markdown_summary(
        results,
        output_dir / f"{output_base}.md",
        CONDITION,
        DATASET,
        RESEARCH_QUESTION,
    )
    print(f"  ✓ Markdown summary: evaluation_results/{output_base}.md")

    save_csv_details(results, output_dir / f"{output_base}.csv")
    print(f"  ✓ CSV details: evaluation_results/{output_base}.csv")

    save_json_metrics(
        results,
        output_dir / f"{output_base}.json",
        CONDITION,
        DATASET,
        RESEARCH_QUESTION,
    )
    print(f"  ✓ JSON metrics: evaluation_results/{output_base}.json")

    print()
    print("=" * 70)
    print("EVALUATION COMPLETE")
    print("=" * 70)
    print(f"\nMove-Level Accuracy: {results['move_metrics']['accuracy']:.4f}")
    print(f"Step-Level Accuracy: {results['step_metrics']['accuracy']:.4f}")
    print()


if __name__ == "__main__":
    main()
