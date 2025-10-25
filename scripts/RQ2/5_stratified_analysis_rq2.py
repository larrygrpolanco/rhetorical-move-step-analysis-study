"""
Stratified Consistency Analysis RQ2 - By Move and Step Type
============================================================
Analyzes consistency patterns stratified by:
- Move type (M1, M2, M3)
- Step type (1a, 1b, 1c, 2a, 2b, 2c, 2d, 3a, 3b, 3c, 3d)

Follows the same pattern as 4_analyze_sentences_rq2.py but groups by move/step.

Author: Larry Grullon-Polanco
Date: 2025
"""

import pandas as pd
import numpy as np
from pathlib import Path

# ============================================================================
# CONFIGURATION
# ============================================================================

CONDITIONS = ["zero_shot", "fine_tuned"]
DATASET = "test"

# ============================================================================


def load_all_sentence_data(condition, max_runs=100):
    """
    Load sentence-level data across all runs for a condition.

    (Same function as in 4_analyze_sentences_rq2.py)

    Args:
        condition: Condition name
        max_runs: Maximum number of runs to load

    Returns:
        pd.DataFrame: Combined sentence data from all runs
    """
    all_data = []
    results_dir = Path("evaluation_results") / f"{condition}_rq2"

    for run_num in range(1, max_runs + 1):
        csv_file = results_dir / f"run_{run_num:02d}.csv"

        if not csv_file.exists():
            # Stop when we hit missing runs
            break

        df = pd.read_csv(csv_file)
        df["run_number"] = run_num
        all_data.append(df)

    if not all_data:
        raise ValueError(f"No sentence data found for {condition}")

    return pd.concat(all_data, ignore_index=True)


def calculate_move_stratified_metrics(df_all, condition):
    """
    Calculate consistency metrics stratified by move type.

    Args:
        df_all: All sentence data
        condition: Condition name

    Returns:
        pd.DataFrame: Metrics by move type
    """
    results = []

    # Convert gold_move to string for consistency
    df_all["gold_move_str"] = df_all["gold_move"].astype(str)

    # Group by move type and run_number to get per-run accuracy
    for move in ["1", "2", "3"]:
        df_move = df_all[df_all["gold_move_str"] == move]

        if len(df_move) == 0:
            continue

        # Calculate accuracy per run for this move
        run_accuracies = []
        for run_num in df_move["run_number"].unique():
            df_run_move = df_move[df_move["run_number"] == run_num]
            accuracy = df_run_move["move_correct"].mean()
            run_accuracies.append(accuracy)

        # Calculate aggregate statistics
        mean_acc = np.mean(run_accuracies)
        sd_acc = np.std(run_accuracies, ddof=1)
        cv = (sd_acc / mean_acc * 100) if mean_acc > 0 else 0

        results.append(
            {
                "condition": condition,
                "move": f"M{move}",
                "n_sentences": len(df_move["sentence_num"].unique()),
                "n_runs": len(run_accuracies),
                "mean_accuracy": mean_acc,
                "sd_accuracy": sd_acc,
                "cv": cv,
                "median": np.median(run_accuracies),
                "min": np.min(run_accuracies),
                "max": np.max(run_accuracies),
                "range": np.max(run_accuracies) - np.min(run_accuracies),
            }
        )

    return pd.DataFrame(results)


def calculate_step_stratified_metrics(df_all, condition, min_support=10):
    """
    Calculate consistency metrics stratified by step type.

    Args:
        df_all: All sentence data
        condition: Condition name
        min_support: Minimum number of sentences to include step

    Returns:
        pd.DataFrame: Metrics by step type
    """
    results = []

    step_labels = ["1a", "1b", "1c", "2a", "2b", "2c", "2d", "3a", "3b", "3c", "3d"]

    for step in step_labels:
        df_step = df_all[df_all["gold_step"] == step]

        # Skip if too few sentences
        n_unique_sentences = len(df_step["sentence_num"].unique())
        if n_unique_sentences < min_support:
            continue

        # Calculate accuracy per run for this step
        run_accuracies = []
        for run_num in df_step["run_number"].unique():
            df_run_step = df_step[df_step["run_number"] == run_num]
            accuracy = df_run_step["step_correct"].mean()
            run_accuracies.append(accuracy)

        # Calculate aggregate statistics
        mean_acc = np.mean(run_accuracies)
        sd_acc = np.std(run_accuracies, ddof=1)
        cv = (sd_acc / mean_acc * 100) if mean_acc > 0 else 0

        results.append(
            {
                "condition": condition,
                "step": step,
                "move": step[0],  # Extract move number
                "n_sentences": n_unique_sentences,
                "n_runs": len(run_accuracies),
                "mean_accuracy": mean_acc,
                "sd_accuracy": sd_acc,
                "cv": cv,
                "median": np.median(run_accuracies),
                "min": np.min(run_accuracies),
                "max": np.max(run_accuracies),
                "range": np.max(run_accuracies) - np.min(run_accuracies),
            }
        )

    return pd.DataFrame(results)


def create_comparison_table(df_zs, df_ft, group_col):
    """
    Create side-by-side comparison table.

    Args:
        df_zs: Zero-shot results
        df_ft: Fine-tuned results
        group_col: 'move' or 'step'

    Returns:
        pd.DataFrame: Comparison table
    """
    # Merge on group column
    df_merged = pd.merge(df_zs, df_ft, on=group_col, suffixes=("_zs", "_ft"))

    # Calculate differences
    df_merged["cv_diff"] = df_merged["cv_zs"] - df_merged["cv_ft"]
    df_merged["accuracy_diff"] = (
        df_merged["mean_accuracy_zs"] - df_merged["mean_accuracy_ft"]
    )
    df_merged["more_consistent"] = df_merged["cv_diff"].apply(
        lambda x: "Zero-shot" if x < 0 else ("Fine-tuned" if x > 0 else "Equal")
    )

    return df_merged


def create_summary_report(results, output_file):
    """
    Create human-readable summary report.

    Args:
        results: Dictionary with analysis results
        output_file: Output file path
    """
    with open(output_file, "w") as f:
        f.write("=" * 70 + "\n")
        f.write("STRATIFIED CONSISTENCY ANALYSIS - RQ2.4\n")
        f.write("=" * 70 + "\n\n")

        f.write(f"Dataset: {DATASET}\n")
        f.write(f"Conditions: {', '.join(CONDITIONS)}\n\n")

        # Move-level results
        for condition in CONDITIONS:
            f.write("-" * 70 + "\n")
            f.write(f"CONSISTENCY BY MOVE TYPE: {condition.upper()}\n")
            f.write("-" * 70 + "\n\n")

            df_move = results[f"{condition}_by_move"]

            for _, row in df_move.iterrows():
                f.write(f"{row['move']}:\n")
                f.write(f"  Sentences: {row['n_sentences']}\n")
                f.write(f"  Runs: {row['n_runs']}\n")
                f.write(
                    f"  Mean Accuracy: {row['mean_accuracy']:.4f} ({row['mean_accuracy']*100:.2f}%)\n"
                )
                f.write(f"  SD: {row['sd_accuracy']:.4f}\n")
                f.write(f"  CV: {row['cv']:.2f}%\n")
                f.write(f"  Range: [{row['min']:.4f}, {row['max']:.4f}]\n")
                f.write("\n")

        # Cross-condition comparison
        f.write("-" * 70 + "\n")
        f.write("CROSS-CONDITION COMPARISON BY MOVE\n")
        f.write("-" * 70 + "\n\n")

        df_comp = results["comparison_by_move"]

        for _, row in df_comp.iterrows():
            f.write(f"{row['move']}:\n")
            f.write(f"  Zero-shot CV: {row['cv_zs']:.2f}%\n")
            f.write(f"  Fine-tuned CV: {row['cv_ft']:.2f}%\n")
            f.write(f"  Difference: {abs(row['cv_diff']):.2f} pp\n")
            f.write(f"  More consistent: {row['more_consistent']}\n")
            f.write("\n")

        # Step-level summary
        f.write("-" * 70 + "\n")
        f.write("STEP-LEVEL CONSISTENCY (min_support=10)\n")
        f.write("-" * 70 + "\n\n")

        for condition in CONDITIONS:
            df_step = results[f"{condition}_by_step"]
            f.write(f"{condition.upper()}:\n")
            f.write(f"  Steps analyzed: {len(df_step)}\n")
            f.write(f"  Mean CV: {df_step['cv'].mean():.2f}%\n")
            f.write(
                f"  Most consistent: {df_step.loc[df_step['cv'].idxmin(), 'step']} (CV={df_step['cv'].min():.2f}%)\n"
            )
            f.write(
                f"  Least consistent: {df_step.loc[df_step['cv'].idxmax(), 'step']} (CV={df_step['cv'].max():.2f}%)\n"
            )
            f.write("\n")

        # Key findings
        f.write("-" * 70 + "\n")
        f.write("KEY FINDINGS\n")
        f.write("-" * 70 + "\n\n")

        df_comp_move = results["comparison_by_move"]
        most_stable_move = df_comp_move.loc[
            df_comp_move[["cv_zs", "cv_ft"]].mean(axis=1).idxmin(), "move"
        ]
        least_stable_move = df_comp_move.loc[
            df_comp_move[["cv_zs", "cv_ft"]].mean(axis=1).idxmax(), "move"
        ]

        f.write(f"Most stable move (both conditions): {most_stable_move}\n")
        f.write(f"Least stable move (both conditions): {least_stable_move}\n")
        f.write("\n")

        zs_better = len(df_comp_move[df_comp_move["more_consistent"] == "Zero-shot"])
        ft_better = len(df_comp_move[df_comp_move["more_consistent"] == "Fine-tuned"])

        f.write(f"Moves where zero-shot more consistent: {zs_better}/3\n")
        f.write(f"Moves where fine-tuned more consistent: {ft_better}/3\n")


def main():
    """Main execution."""

    print("=" * 70)
    print("STRATIFIED CONSISTENCY ANALYSIS - RQ2.4")
    print("=" * 70)
    print()

    # Create output directory
    output_dir = Path("evaluation_results") / "rq2_analysis" / "stratified"
    output_dir.mkdir(parents=True, exist_ok=True)

    results = {}

    try:
        # Analyze each condition
        for condition in CONDITIONS:
            print(f"Analyzing {condition}...")
            print("-" * 70)

            # Load all sentence data
            print(f"  Loading sentence data...", end=" ", flush=True)
            df_all = load_all_sentence_data(condition)
            n_runs = df_all["run_number"].nunique()
            n_sentences = len(df_all["sentence_num"].unique())
            print(f"✓ ({n_runs} runs, {n_sentences} sentences)")

            # Move-level stratified analysis
            print(f"  Calculating move-level consistency...", end=" ", flush=True)
            df_move = calculate_move_stratified_metrics(df_all, condition)
            results[f"{condition}_by_move"] = df_move
            print("✓")

            # Step-level stratified analysis
            print(f"  Calculating step-level consistency...", end=" ", flush=True)
            df_step = calculate_step_stratified_metrics(
                df_all, condition, min_support=10
            )
            results[f"{condition}_by_step"] = df_step
            print("✓")

            # Save individual condition results
            df_move.to_csv(output_dir / f"{condition}_by_move.csv", index=False)
            df_step.to_csv(output_dir / f"{condition}_by_step.csv", index=False)

            print()

        # Cross-condition comparison
        print("Comparing conditions...", end=" ", flush=True)
        df_comp_move = create_comparison_table(
            results["zero_shot_by_move"], results["fine_tuned_by_move"], "move"
        )
        results["comparison_by_move"] = df_comp_move
        df_comp_move.to_csv(output_dir / "comparison_by_move.csv", index=False)
        print("✓")
        print()

        # Create summary report
        print("Creating summary report...", end=" ", flush=True)
        create_summary_report(results, output_dir / "stratified_analysis_summary.txt")
        print("✓")
        print()

        print("=" * 70)
        print("✅ STRATIFIED ANALYSIS COMPLETE")
        print("=" * 70)
        print(f"\nOutput directory: {output_dir}/")
        print(f"Files created:")
        print(f"  - zero_shot_by_move.csv")
        print(f"  - zero_shot_by_step.csv")
        print(f"  - fine_tuned_by_move.csv")
        print(f"  - fine_tuned_by_step.csv")
        print(f"  - comparison_by_move.csv")
        print(f"  - stratified_analysis_summary.txt")

        # Print key findings
        df_comp = results["comparison_by_move"]
        print(f"\nKey Findings:")
        print(f"  Moves analyzed: {len(df_comp)}")

        for _, row in df_comp.iterrows():
            print(
                f"  {row['move']}: {row['more_consistent']} more consistent "
                + f"(CV: ZS={row['cv_zs']:.2f}%, FT={row['cv_ft']:.2f}%)"
            )

        print("\nNext steps:")
        print("  1. Review stratified_analysis_summary.txt")
        print("  2. Use CSV files for manuscript tables/figures")
        print()

    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback

        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
