"""
Evaluate RQ2 Runs - Batch Evaluation for Consistency Analysis
==============================================================
Evaluates all 50 runs for a single condition (zero_shot or fine_tuned).

Auto-detects available runs and evaluates them against gold standard.
Reuses evaluation logic from RQ1 but handles multiple runs.

Performs:
- Auto-discovery of completed runs (checks outputs/ folder)
- Batch evaluation of all available runs
- Move-level and step-level metrics per run
- Outputs: Individual JSON/CSV/MD files per run

Author: Larry Grullon-Polanco
Date: 2025
"""

import json
import pandas as pd
from pathlib import Path
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
)

# ============================================================================
# CONFIGURATION
# ============================================================================

CONDITION = "fine_tuned"  # Options: zero_shot, fine_tuned
DATASET = "test"  # Always 'test' for RQ2

# Article ranges
ARTICLE_RANGES = {
    "validation": range(1, 11),  # Articles 1-10
    "test": range(11, 21),  # Articles 11-20
}

# ============================================================================


class EvaluationError(Exception):
    """Custom exception for evaluation errors requiring article re-run."""

    pass


def discover_available_runs(condition, dataset="test"):
    """
    Auto-discover which runs have been completed.

    Args:
        condition: Condition name (zero_shot or fine_tuned)
        dataset: Dataset name (test for RQ2)

    Returns:
        list: Available run numbers
    """
    outputs_dir = Path("outputs") / condition
    available_runs = []

    # Look for rq2_run_XX folders
    for run_folder in outputs_dir.glob("rq2_run_*"):
        # Extract run number from folder name (e.g., rq2_run_01 -> 1)
        run_num = int(run_folder.name.split("_")[-1])

        # Check if parsed outputs exist
        parsed_dir = run_folder / "parsed"
        if parsed_dir.exists() and list(parsed_dir.glob("*.json")):
            available_runs.append(run_num)

    return sorted(available_runs)


def load_gold_standard(article_num, dataset):
    """
    Load gold standard annotations for an article.

    Args:
        article_num: Article number (e.g., 11-20 for test set)
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


def load_predictions(article_num, condition, run_num, dataset="test"):
    """
    Load model predictions for an article from a specific run.

    Args:
        article_num: Article number
        condition: Experimental condition
        run_num: Run number (1-50)
        dataset: Dataset name

    Returns:
        dict: Parsed predictions with sentences
    """
    article_id = f"text{article_num:03d}"
    pred_file = Path(
        f"outputs/{condition}/rq2_run_{run_num:02d}/parsed/{article_id}.json"
    )

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


def evaluate_article(article_num, condition, run_num, dataset):
    """
    Evaluate a single article for a specific run.

    Args:
        article_num: Article number
        condition: Experimental condition
        run_num: Run number
        dataset: Dataset name

    Returns:
        dict: Article evaluation results
    """
    article_id = f"text{article_num:03d}"

    # Load data
    gold = load_gold_standard(article_num, dataset)
    pred = load_predictions(article_num, condition, run_num, dataset)

    # Validate
    validate_article(gold, pred, article_id)

    # Align sentences
    gold_moves, pred_moves, gold_steps, pred_steps, details = align_sentences(
        gold, pred
    )

    # Calculate metrics
    move_labels = ["1", "2", "3"]
    step_labels = ["1a", "1b", "1c", "2a", "2b", "2c", "2d", "3a", "3b", "3c", "3d"]

    move_metrics = calculate_metrics(gold_moves, pred_moves, move_labels)
    step_metrics = calculate_metrics(gold_steps, pred_steps, step_labels)

    return {
        "article_id": article_id,
        "article_num": article_num,
        "sentence_count": len(gold["sentences"]),
        "move_metrics": move_metrics,
        "step_metrics": step_metrics,
        "sentence_details": details,
    }


def aggregate_results(article_results):
    """
    Aggregate results across all articles for a single run.

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
        "per_article_metrics": article_results,
        "all_sentence_details": all_details,
    }


def get_run_output_dir(condition):
    """
    Get the output directory for a condition's runs.

    Args:
        condition: Condition name

    Returns:
        Path: Output directory path
    """
    output_dir = Path("evaluation_results") / f"{condition}_rq2"
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def save_markdown_summary(results, output_file, condition, dataset, run_num):
    """
    Save human-readable markdown summary.

    Args:
        results: Aggregated results
        output_file: Path to output file
        condition: Condition name
        dataset: Dataset name
        run_num: Run number
    """
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Evaluation Results\n\n")
        f.write(f"**Condition:** {condition}  \n")
        f.write(f"**Dataset:** {dataset}  \n")
        f.write(f"**Research Question:** RQ2  \n")
        f.write(f"**Run Number:** {run_num}  \n")
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
        for article in results["per_article_metrics"]:
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


def save_json_metrics(results, output_file, condition, dataset, run_num):
    """
    Save machine-readable metrics to JSON.

    Args:
        results: Aggregated results
        output_file: Path to output file
        condition: Condition name
        dataset: Dataset name
        run_num: Run number
    """
    output_data = {
        "condition": condition,
        "dataset": dataset,
        "research_question": "rq2",
        "run_number": run_num,
        "total_articles": results["total_articles"],
        "total_sentences": results["total_sentences"],
        "move_metrics": results["move_metrics"],
        "step_metrics": results["step_metrics"],
        "per_article_metrics": results["per_article_metrics"],
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)


def evaluate_single_run(condition, run_num, dataset, article_range):
    """
    Evaluate all articles for a single run.

    Args:
        condition: Condition name
        run_num: Run number
        dataset: Dataset name
        article_range: Range of article numbers to evaluate

    Returns:
        tuple: (success, results or error_message)
    """
    article_results = []
    failed_articles = []

    for article_num in article_range:
        article_id = f"text{article_num:03d}"

        try:
            result = evaluate_article(article_num, condition, run_num, dataset)
            article_results.append(result)

        except EvaluationError as e:
            failed_articles.append((article_id, str(e)))

        except Exception as e:
            failed_articles.append((article_id, f"ERROR: {e}"))

    # Check if any articles failed
    if failed_articles:
        error_msg = (
            f"\n⚠️  Run {run_num:02d} - {len(failed_articles)} article(s) failed:\n"
        )
        for article_id, error in failed_articles:
            error_msg += f"  - {article_id}: {error[:100]}...\n"
        return False, error_msg

    # Aggregate results
    results = aggregate_results(article_results)
    return True, results


def main():
    """Main execution."""

    print("=" * 70)
    print(f"Evaluating RQ2 Runs: {CONDITION}")
    print(f"Dataset: {DATASET}")
    print("=" * 70)
    print()

    # Auto-discover available runs
    print("Discovering available runs...")
    available_runs = discover_available_runs(CONDITION, DATASET)

    if not available_runs:
        print(f"❌ No completed runs found for {CONDITION}.")
        print(f"   Expected location: outputs/{CONDITION}/rq2_run_XX/parsed/")
        print(f"   Run 'run_condition.py' first to generate outputs.")
        return

    print(f"✓ Found {len(available_runs)} completed runs:")
    print(f"  Runs: {min(available_runs)}-{max(available_runs)}")
    print()

    # Create output directory for this condition
    output_dir = get_run_output_dir(CONDITION)
    print(f"Output directory: {output_dir}")
    print()

    # Determine article range
    article_range = ARTICLE_RANGES[DATASET]
    print(f"Articles per run: {min(article_range)}-{max(article_range)}")
    print()

    # Evaluate each run
    print("Evaluating runs...")
    print("-" * 70)

    successful_runs = 0
    failed_runs = []

    for run_num in available_runs:
        print(f"  Run {run_num:02d}...", end=" ", flush=True)

        success, result = evaluate_single_run(
            CONDITION, run_num, DATASET, article_range
        )

        if success:
            # Save outputs
            output_base = f"run_{run_num:02d}"

            save_markdown_summary(
                result,
                output_dir / f"{output_base}.md",
                CONDITION,
                DATASET,
                run_num,
            )

            save_csv_details(result, output_dir / f"{output_base}.csv")

            save_json_metrics(
                result,
                output_dir / f"{output_base}.json",
                CONDITION,
                DATASET,
                run_num,
            )

            print(
                f"✓ (Move: {result['move_metrics']['accuracy']:.3f}, "
                f"Step: {result['step_metrics']['accuracy']:.3f})"
            )
            successful_runs += 1

        else:
            print("✗ FAILED")
            failed_runs.append((run_num, result))

    print()
    print("=" * 70)

    if failed_runs:
        print("⚠️  EVALUATION INCOMPLETE")
        print("=" * 70)
        print(f"\nSuccessful runs: {successful_runs}/{len(available_runs)}")
        print(f"Failed runs: {len(failed_runs)}")
        print("\nFailed run details:")
        for run_num, error_msg in failed_runs:
            print(f"\nRun {run_num:02d}:")
            print(error_msg)
        print("\n⚠️  Re-run failed runs before proceeding to analysis.\n")
    else:
        print("✅ EVALUATION COMPLETE")
        print("=" * 70)
        print(f"\nTotal runs evaluated: {successful_runs}")
        print(f"Output directory: {output_dir}/")
        print(f"  - {successful_runs} JSON files (metrics)")
        print(f"  - {successful_runs} CSV files (sentence details)")
        print(f"  - {successful_runs} MD files (summaries)")
        print()
        print("Files organized as: run_01.json, run_02.json, etc.")
        print()
        print("Next step: Run 'analyze_consistency_rq2.py' to aggregate results.")
        print()


if __name__ == "__main__":
    main()
