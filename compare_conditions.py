"""
Compare Conditions - Multi-Condition Comparison Script
=======================================================
Compares multiple experimental conditions using statistical tests.

Performs:
- Auto-discovers all evaluated conditions for a dataset
- Side-by-side comparison of metrics
- McNemar's test for statistical significance (Kim & Lu 2024 methodology)
- Outputs: Markdown summary with tables and test results

Author: Larry Grullon-Polanco
Date: 2025
"""

import json
import pandas as pd
from pathlib import Path
from itertools import combinations
from statsmodels.stats.contingency_tables import mcnemar

# ============================================================================
# CONFIGURATION
# ============================================================================

DATASET = "validation"  # Options: validation, test
RESEARCH_QUESTION = "rq1"  # Options: rq1, rq2_run_01, etc.

# ============================================================================


def discover_conditions(dataset, research_question):
    """
    Auto-discover all available conditions for a dataset.

    Args:
        dataset: Dataset name
        research_question: RQ identifier

    Returns:
        list: Condition names that have been evaluated
    """
    results_dir = Path("evaluation_results")
    if not results_dir.exists():
        raise FileNotFoundError(
            "No evaluation_results/ directory found. Run evaluate_condition.py first."
        )

    # Look for JSON metric files matching pattern
    pattern = f"*_{research_question}_{dataset}.json"
    json_files = list(results_dir.glob(pattern))

    if not json_files:
        raise FileNotFoundError(
            f"No evaluation results found for {research_question} {dataset}. "
            f"Run evaluate_condition.py first."
        )

    # Extract condition names from filenames
    conditions = []
    for json_file in json_files:
        # Filename format: {condition}_{research_question}_{dataset}.json
        parts = json_file.stem.split("_")
        # The condition is everything before research_question
        # For example: zero_shot_rq1_validation -> zero_shot
        # Or: three_shot_rq1_validation -> three_shot
        condition = "_".join(parts[: -(2)])  # Remove last 2 parts (rq + dataset)
        conditions.append(condition)

    return sorted(conditions)


def load_condition_metrics(condition, dataset, research_question):
    """
    Load metrics for a specific condition.

    Args:
        condition: Condition name
        dataset: Dataset name
        research_question: RQ identifier

    Returns:
        dict: Metrics data
    """
    results_dir = Path("evaluation_results")
    json_file = results_dir / f"{condition}_{research_question}_{dataset}.json"

    if not json_file.exists():
        raise FileNotFoundError(f"Metrics not found: {json_file}")

    with open(json_file, "r", encoding="utf-8") as f:
        return json.load(f)


def load_condition_details(condition, dataset, research_question):
    """
    Load sentence-level details for McNemar's test.

    Args:
        condition: Condition name
        dataset: Dataset name
        research_question: RQ identifier

    Returns:
        pd.DataFrame: Sentence-level results
    """
    results_dir = Path("evaluation_results")
    csv_file = results_dir / f"{condition}_{research_question}_{dataset}.csv"

    if not csv_file.exists():
        raise FileNotFoundError(f"Details not found: {csv_file}")

    return pd.read_csv(csv_file)


def create_comparison_table(conditions, dataset, research_question, level="move"):
    """
    Create comparison table for all conditions.

    Args:
        conditions: List of condition names
        dataset: Dataset name
        research_question: RQ identifier
        level: 'move' or 'step'

    Returns:
        pd.DataFrame: Comparison table
    """
    rows = []

    for condition in conditions:
        metrics = load_condition_metrics(condition, dataset, research_question)

        if level == "move":
            m = metrics["move_metrics"]
        else:
            m = metrics["step_metrics"]

        rows.append(
            {
                "Condition": condition,
                "Accuracy": f"{m['accuracy']:.4f}",
                "Precision": f"{m['weighted_precision']:.4f}",
                "Recall": f"{m['weighted_recall']:.4f}",
                "F1": f"{m['weighted_f1']:.4f}",
                "Sentences": metrics["total_sentences"],
            }
        )

    return pd.DataFrame(rows)


def create_per_class_comparison(
    conditions, dataset, research_question, level="move"
):
    """
    Create per-class comparison table.

    Args:
        conditions: List of condition names
        dataset: Dataset name
        research_question: RQ identifier
        level: 'move' or 'step'

    Returns:
        dict: Per-class comparison tables (precision, recall, f1)
    """
    if level == "move":
        labels = ["1", "2", "3"]
    else:
        labels = ["1a", "1b", "1c", "2a", "2b", "2c", "2d", "3a", "3b", "3c", "3d"]

    # Create separate tables for each metric
    precision_data = {label: [] for label in labels}
    recall_data = {label: [] for label in labels}
    f1_data = {label: [] for label in labels}

    for condition in conditions:
        metrics = load_condition_metrics(condition, dataset, research_question)

        if level == "move":
            per_class = metrics["move_metrics"]["per_class"]
        else:
            per_class = metrics["step_metrics"]["per_class"]

        for label in labels:
            precision_data[label].append(f"{per_class[label]['precision']:.4f}")
            recall_data[label].append(f"{per_class[label]['recall']:.4f}")
            f1_data[label].append(f"{per_class[label]['f1']:.4f}")

    # Convert to DataFrames
    precision_df = pd.DataFrame(precision_data, index=conditions)
    recall_df = pd.DataFrame(recall_data, index=conditions)
    f1_df = pd.DataFrame(f1_data, index=conditions)

    return {
        "precision": precision_df,
        "recall": recall_df,
        "f1": f1_df,
    }


def run_mcnemar_test(cond1, cond2, dataset, research_question, level="move"):
    """
    Run McNemar's test between two conditions.

    Args:
        cond1: First condition name
        cond2: Second condition name
        dataset: Dataset name
        research_question: RQ identifier
        level: 'move' or 'step'

    Returns:
        dict: Test results
    """
    # Load sentence-level details for both conditions
    df1 = load_condition_details(cond1, dataset, research_question)
    df2 = load_condition_details(cond2, dataset, research_question)

    # Ensure same sentences are being compared
    if len(df1) != len(df2):
        raise ValueError(
            f"Sentence count mismatch: {cond1}={len(df1)}, {cond2}={len(df2)}"
        )

    # Get correctness arrays
    if level == "move":
        correct1 = df1["move_correct"].values
        correct2 = df2["move_correct"].values
    else:
        correct1 = df1["step_correct"].values
        correct2 = df2["step_correct"].values

    # Build contingency table for McNemar's test
    # Format: [[both_correct, cond1_correct_cond2_wrong],
    #          [cond1_wrong_cond2_correct, both_wrong]]
    both_correct = sum(correct1 & correct2)
    cond1_only = sum(correct1 & ~correct2)
    cond2_only = sum(~correct1 & correct2)
    both_wrong = sum(~correct1 & ~correct2)

    contingency = [[both_correct, cond1_only], [cond2_only, both_wrong]]

    # Run McNemar's test
    result = mcnemar(contingency, exact=True)

    return {
        "condition_1": cond1,
        "condition_2": cond2,
        "statistic": float(result.statistic),
        "p_value": float(result.pvalue),
        "both_correct": int(both_correct),
        "cond1_only_correct": int(cond1_only),
        "cond2_only_correct": int(cond2_only),
        "both_wrong": int(both_wrong),
    }


def save_comparison_markdown(
    conditions, dataset, research_question, move_table, step_table, mcnemar_results, output_file
):
    """
    Save comparison results to markdown.

    Args:
        conditions: List of condition names
        dataset: Dataset name
        research_question: RQ identifier
        move_table: Move-level comparison table
        step_table: Step-level comparison table
        mcnemar_results: Dictionary with move and step McNemar results
        output_file: Output file path
    """
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Condition Comparison Results\n\n")
        f.write(f"**Dataset:** {dataset}  \n")
        f.write(f"**Research Question:** {research_question}  \n")
        f.write(f"**Conditions Compared:** {len(conditions)}  \n\n")

        f.write("**Conditions:**\n")
        for i, cond in enumerate(conditions, 1):
            f.write(f"{i}. {cond}\n")
        f.write("\n---\n\n")

        # Move-level comparison
        f.write("## Move-Level Performance Comparison\n\n")
        f.write(move_table.to_markdown(index=False))
        f.write("\n\n")

        # Step-level comparison
        f.write("## Step-Level Performance Comparison\n\n")
        f.write(step_table.to_markdown(index=False))
        f.write("\n\n")

        f.write("---\n\n")

        # Statistical tests
        f.write("## Statistical Significance Tests (McNemar's Test)\n\n")
        f.write(
            "*McNemar's test evaluates whether accuracy differences between conditions are statistically significant.*\n\n"
        )

        # Move-level McNemar's
        f.write("### Move-Level Comparisons\n\n")
        f.write("| Comparison | p-value | Significant (p<0.05)? | Statistic |\n")
        f.write("|------------|---------|----------------------|------------|\n")
        for result in mcnemar_results["move"]:
            comparison = f"{result['condition_1']} vs {result['condition_2']}"
            p_value = result["p_value"]
            significant = "✓ Yes" if p_value < 0.05 else "No"
            f.write(
                f"| {comparison} | {p_value:.4f} | {significant} | {result['statistic']:.4f} |\n"
            )
        f.write("\n")

        # Step-level McNemar's
        f.write("### Step-Level Comparisons\n\n")
        f.write("| Comparison | p-value | Significant (p<0.05)? | Statistic |\n")
        f.write("|------------|---------|----------------------|------------|\n")
        for result in mcnemar_results["step"]:
            comparison = f"{result['condition_1']} vs {result['condition_2']}"
            p_value = result["p_value"]
            significant = "✓ Yes" if p_value < 0.05 else "No"
            f.write(
                f"| {comparison} | {p_value:.4f} | {significant} | {result['statistic']:.4f} |\n"
            )
        f.write("\n")

        f.write("---\n\n")

        # Interpretation guide
        f.write("## Interpretation Guide\n\n")
        f.write("**p-value < 0.05:** Statistically significant difference  \n")
        f.write("**p-value ≥ 0.05:** No significant difference  \n\n")
        f.write(
            "McNemar's test is specifically designed for paired comparisons "
            "(same sentences evaluated by different conditions), making it appropriate "
            "for this evaluation.\n"
        )


def save_comparison_csv(mcnemar_results, output_file):
    """
    Save detailed McNemar results to CSV.

    Args:
        mcnemar_results: Dictionary with move and step results
        output_file: Output file path
    """
    # Combine move and step results
    all_results = []

    for result in mcnemar_results["move"]:
        all_results.append({"level": "move", **result})

    for result in mcnemar_results["step"]:
        all_results.append({"level": "step", **result})

    df = pd.DataFrame(all_results)
    df.to_csv(output_file, index=False)


def main():
    """Main execution."""

    print("=" * 70)
    print(f"Comparing Conditions")
    print(f"Dataset: {DATASET}")
    print(f"Research Question: {RESEARCH_QUESTION}")
    print("=" * 70)
    print()

    # Auto-discover conditions
    print("Discovering evaluated conditions...")
    try:
        conditions = discover_conditions(DATASET, RESEARCH_QUESTION)
        print(f"✓ Found {len(conditions)} conditions:")
        for cond in conditions:
            print(f"  - {cond}")
        print()
    except FileNotFoundError as e:
        print(f"✗ ERROR: {e}")
        return

    if len(conditions) < 2:
        print("⚠️  Need at least 2 conditions to compare.")
        print("   Run evaluate_condition.py for more conditions first.")
        return

    # Create comparison tables
    print("Creating comparison tables...")
    move_table = create_comparison_table(
        conditions, DATASET, RESEARCH_QUESTION, level="move"
    )
    step_table = create_comparison_table(
        conditions, DATASET, RESEARCH_QUESTION, level="step"
    )
    print("✓ Comparison tables created")
    print()

    # Run McNemar's tests for all pairs
    print("Running McNemar's tests...")
    pairs = list(combinations(conditions, 2))
    print(f"  Testing {len(pairs)} condition pairs")
    print()

    mcnemar_results = {"move": [], "step": []}

    for cond1, cond2 in pairs:
        print(f"  {cond1} vs {cond2}...", end=" ", flush=True)

        try:
            # Move-level test
            move_result = run_mcnemar_test(
                cond1, cond2, DATASET, RESEARCH_QUESTION, level="move"
            )
            mcnemar_results["move"].append(move_result)

            # Step-level test
            step_result = run_mcnemar_test(
                cond1, cond2, DATASET, RESEARCH_QUESTION, level="step"
            )
            mcnemar_results["step"].append(step_result)

            print("✓")

        except Exception as e:
            print(f"✗ ERROR: {e}")

    print()

    # Save outputs
    output_dir = Path("evaluation_results")
    output_base = f"comparison_{RESEARCH_QUESTION}_{DATASET}"

    print("Saving results...")
    save_comparison_markdown(
        conditions,
        DATASET,
        RESEARCH_QUESTION,
        move_table,
        step_table,
        mcnemar_results,
        output_dir / f"{output_base}.md",
    )
    print(f"  ✓ Markdown summary: evaluation_results/{output_base}.md")

    save_comparison_csv(mcnemar_results, output_dir / f"{output_base}.csv")
    print(f"  ✓ CSV details: evaluation_results/{output_base}.csv")

    print()
    print("=" * 70)
    print("COMPARISON COMPLETE")
    print("=" * 70)
    print(f"\nConditions compared: {', '.join(conditions)}")
    print(f"Pairwise comparisons: {len(pairs)}")
    print()


if __name__ == "__main__":
    main()
