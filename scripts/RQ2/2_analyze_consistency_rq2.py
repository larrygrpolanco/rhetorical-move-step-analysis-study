"""
Analyze Consistency RQ2 - Within-Condition Consistency Analysis
================================================================
Aggregates 50 runs for a single condition to calculate consistency metrics.

Performs:
- Descriptive statistics (mean, SD, CV, range, IQR, median)
- 95% Confidence intervals
- Distribution assessment (normality tests, Q-Q plots, histograms)
- Intraclass Correlation Coefficient (ICC)
- Sentence-level tracking across runs
- Outputs: CSV summaries, statistical reports

Author: Larry Grullon-Polanco
Date: 2025
"""

import json
import pandas as pd
import numpy as np
from pathlib import Path
from scipy import stats
import warnings

warnings.filterwarnings("ignore")

# Try to import pingouin for ICC, provide fallback if not available
try:
    from pingouin import intraclass_corr

    PINGOUIN_AVAILABLE = True
except ImportError:
    PINGOUIN_AVAILABLE = False
    print("⚠️  Warning: pingouin not installed. ICC calculation will be skipped.")
    print("   Install with: pip install pingouin")

# ============================================================================
# CONFIGURATION
# ============================================================================

CONDITION = "fine_tuned"  # Options: zero_shot, fine_tuned
DATASET = "test"  # Always 'test' for RQ2

# ============================================================================


def load_run_metrics(condition, run_num):
    """
    Load evaluation metrics for a single run.

    Args:
        condition: Condition name
        run_num: Run number (1-50)

    Returns:
        dict: Metrics data
    """
    results_dir = Path("evaluation_results") / f"{condition}_rq2"
    json_file = results_dir / f"run_{run_num:02d}.json"

    if not json_file.exists():
        raise FileNotFoundError(f"Run {run_num:02d} not found: {json_file}")

    with open(json_file, "r", encoding="utf-8") as f:
        return json.load(f)


def load_all_runs(condition, max_runs=100):
    """
    Load metrics for all available runs.

    Args:
        condition: Condition name
        max_runs: Maximum number of runs to load

    Returns:
        pd.DataFrame: All runs data
    """
    runs_data = []

    for run_num in range(1, max_runs + 1):
        try:
            metrics = load_run_metrics(condition, run_num)

            run_data = {
                "run_number": run_num,
                "move_accuracy": metrics["move_metrics"]["accuracy"],
                "step_accuracy": metrics["step_metrics"]["accuracy"],
                "move_f1": metrics["move_metrics"]["weighted_f1"],
                "step_f1": metrics["step_metrics"]["weighted_f1"],
                "move_precision": metrics["move_metrics"]["weighted_precision"],
                "move_recall": metrics["move_metrics"]["weighted_recall"],
                "step_precision": metrics["step_metrics"]["weighted_precision"],
                "step_recall": metrics["step_metrics"]["weighted_recall"],
                "total_sentences": metrics["total_sentences"],
                "total_articles": metrics["total_articles"],
            }
            runs_data.append(run_data)

        except FileNotFoundError:
            # Stop when we hit missing runs
            break

    if not runs_data:
        raise ValueError(f"No run data found for {condition}")

    return pd.DataFrame(runs_data)


def calculate_descriptive_stats(data, metric_name):
    """
    Calculate comprehensive descriptive statistics.

    Args:
        data: Array of values
        metric_name: Name of the metric

    Returns:
        dict: Descriptive statistics
    """
    n = len(data)
    mean = np.mean(data)
    sd = np.std(data, ddof=1)

    # Coefficient of Variation (%)
    cv = (sd / mean) * 100 if mean != 0 else 0

    # 95% Confidence Interval
    ci = stats.t.interval(0.95, n - 1, loc=mean, scale=stats.sem(data))

    # Normality test
    shapiro_stat, shapiro_p = stats.shapiro(data)

    return {
        "metric": metric_name,
        "n": n,
        "mean": mean,
        "sd": sd,
        "cv": cv,
        "median": np.median(data),
        "min": np.min(data),
        "max": np.max(data),
        "range": np.max(data) - np.min(data),
        "q25": np.percentile(data, 25),
        "q75": np.percentile(data, 75),
        "iqr": np.percentile(data, 75) - np.percentile(data, 25),
        "ci_lower": ci[0],
        "ci_upper": ci[1],
        "ci_width": ci[1] - ci[0],
        "shapiro_stat": shapiro_stat,
        "shapiro_p": shapiro_p,
        "is_normal": shapiro_p > 0.05,
    }


def calculate_icc(condition, df_runs, level="move"):
    """
    Calculate Intraclass Correlation Coefficient (ICC) for sentence-level consistency.

    ICC(2,1): Two-way random effects, single rater, absolute agreement
    - Targets: Individual sentences
    - Raters: Different runs
    - Rating: Binary (1=correct, 0=incorrect)

    Args:
        condition: Condition name (e.g., 'zero_shot', 'fine_tuned')
        df_runs: DataFrame with run data
        level: 'move' or 'step' for level of analysis

    Returns:
        dict: ICC results or None if pingouin not available
    """
    if not PINGOUIN_AVAILABLE:
        return None

    from pathlib import Path
    import pandas as pd
    from pingouin import intraclass_corr

    print(f"    Calculating ICC for {level} level...")
    print(f"    Loading sentence-level data from CSV files...", end=" ", flush=True)

    # Storage for sentence-level correctness across runs
    sentence_data = []

    results_dir = Path("evaluation_results") / f"{condition}_rq2"

    # Load CSV files (which have sentence-level details)
    for run_num in df_runs["run_number"]:
        csv_file = results_dir / f"run_{run_num:02d}.csv"

        if not csv_file.exists():
            print(f"\n    ⚠️  Cannot find {csv_file}")
            continue

        # Load sentence details from CSV
        df_run = pd.read_csv(csv_file)

        # For each sentence, record if it was correct
        for idx, row in df_run.iterrows():
            # Create unique sentence ID using cumulative index
            sentence_id = f"sent_{idx}"

            # Get correctness based on level
            if level == "move":
                is_correct = 1 if row["move_correct"] else 0
            else:  # step level
                is_correct = 1 if row["step_correct"] else 0

            sentence_data.append(
                {"sentence": sentence_id, "run": f"run_{run_num}", "rating": is_correct}
            )

    if not sentence_data:
        print("\n    ⚠️  No sentence data collected")
        return None

    print(f"✓ ({len(sentence_data)} observations)")

    # Convert to DataFrame for ICC calculation
    df_icc = pd.DataFrame(sentence_data)

    print(f"    Computing ICC(2,1)...", end=" ", flush=True)

    try:
        # Calculate ICC(2,1) - two-way random, single rater, absolute agreement
        icc_result = intraclass_corr(
            data=df_icc,
            targets="sentence",
            raters="run",
            ratings="rating",
            nan_policy="omit",
        )

        # Extract ICC(2,1) specifically (Type = 'ICC2')
        icc_2_1_row = icc_result[icc_result["Type"] == "ICC2"]

        if len(icc_2_1_row) == 0:
            print("❌ ICC2 not found in results")
            return None

        icc_value = icc_2_1_row["ICC"].values[0]
        ci_lower = icc_2_1_row["CI95%"].values[0][0]
        ci_upper = icc_2_1_row["CI95%"].values[0][1]

        print("✓")

        result = {
            "icc_type": "ICC(2,1)",
            "icc_value": icc_value,
            "ci_lower": ci_lower,
            "ci_upper": ci_upper,
            "level": level,
            "n_sentences": len(df_icc["sentence"].unique()),
            "n_runs": len(df_icc["run"].unique()),
            "n_observations": len(df_icc),
            "interpretation": interpret_icc(icc_value),
        }

        return result

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback

        traceback.print_exc()
        return None


def interpret_icc(icc_value):
    """
    Interpret ICC value according to standard guidelines.

    Based on Koo & Li (2016) guidelines:
    < 0.5: Poor reliability
    0.5-0.75: Moderate reliability
    0.75-0.9: Good reliability
    > 0.9: Excellent reliability

    Args:
        icc_value: ICC coefficient

    Returns:
        str: Interpretation
    """
    if icc_value < 0.5:
        return "Poor reliability (unsuitable for applied use)"
    elif icc_value < 0.75:
        return "Moderate reliability (acceptable with caution)"
    elif icc_value < 0.9:
        return "Good reliability (suitable for research)"
    else:
        return "Excellent reliability (suitable for applied use)"


def analyze_condition(condition, dataset="test"):
    """
    Perform complete consistency analysis for one condition.

    Args:
        condition: Condition name
        dataset: Dataset name

    Returns:
        dict: Analysis results
    """
    print(f"\nAnalyzing {condition} condition...")
    print("-" * 70)

    # Load all runs
    print(f"  Loading runs...", end=" ")
    df_runs = load_all_runs(condition)
    n_runs = len(df_runs)
    print(f"✓ ({n_runs} runs)")

    # Calculate descriptive stats for key metrics
    print(f"  Calculating descriptive statistics...", end=" ")

    metrics_to_analyze = {
        "move_accuracy": "Move Accuracy",
        "step_accuracy": "Step Accuracy",
        "move_f1": "Move F1",
        "step_f1": "Step F1",
    }

    stats_results = []
    for metric_col, metric_name in metrics_to_analyze.items():
        stats_dict = calculate_descriptive_stats(
            df_runs[metric_col].values, metric_name
        )
        stats_results.append(stats_dict)

    df_stats = pd.DataFrame(stats_results)
    print("✓")

    # ICC calculation (if available)
    print(f"  Calculating ICC...")
    icc_move = calculate_icc(CONDITION, df_runs, level="move")
    icc_step = calculate_icc(CONDITION, df_runs, level="step")

    return {
        "condition": condition,
        "n_runs": n_runs,
        "df_runs": df_runs,
        "df_stats": df_stats,
        "icc_move": icc_move,
        "icc_step": icc_step,
    }


def create_summary_report(results, output_dir):
    """
    Create human-readable summary report.

    Args:
        results: Analysis results dict
        output_dir: Output directory path
    """
    condition = results["condition"]
    df_stats = results["df_stats"]
    n_runs = results["n_runs"]

    output_file = output_dir / f"{condition}_consistency_summary.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=" * 70 + "\n")
        f.write(f"CONSISTENCY ANALYSIS: {condition.upper()}\n")
        f.write("=" * 70 + "\n\n")

        f.write(f"Number of runs: {n_runs}\n")
        f.write(f"Dataset: {DATASET}\n")
        f.write(f"Research Question: RQ2\n\n")

        f.write("-" * 70 + "\n")
        f.write("DESCRIPTIVE STATISTICS\n")
        f.write("-" * 70 + "\n\n")

        for _, row in df_stats.iterrows():
            f.write(f"{row['metric']}:\n")
            f.write(f"  Mean: {row['mean']:.4f} ({row['mean']*100:.2f}%)\n")
            f.write(f"  SD: {row['sd']:.4f} ({row['sd']*100:.2f}%)\n")
            f.write(f"  CV: {row['cv']:.2f}%\n")
            f.write(f"  95% CI: [{row['ci_lower']:.4f}, {row['ci_upper']:.4f}]\n")
            f.write(
                f"  Range: [{row['min']:.4f}, {row['max']:.4f}] (span: {row['range']:.4f})\n"
            )
            f.write(f"  Median: {row['median']:.4f}\n")
            f.write(f"  IQR: {row['iqr']:.4f}\n")
            f.write(
                f"  Normality: {'Normal' if row['is_normal'] else 'Non-normal'} (Shapiro-Wilk p={row['shapiro_p']:.4f})\n"
            )
            f.write("\n")

        f.write("-" * 70 + "\n")
        f.write("CONSISTENCY INTERPRETATION\n")
        f.write("-" * 70 + "\n\n")

        move_cv = df_stats[df_stats["metric"] == "Move Accuracy"]["cv"].values[0]

        f.write("Coefficient of Variation (CV) Guidelines:\n")
        f.write("  < 5%:   Excellent consistency\n")
        f.write("  5-10%:  Good consistency\n")
        f.write("  10-20%: Moderate consistency\n")
        f.write("  > 20%:  Poor consistency\n\n")

        if move_cv < 5:
            interpretation = "EXCELLENT consistency"
        elif move_cv < 10:
            interpretation = "GOOD consistency"
        elif move_cv < 20:
            interpretation = "MODERATE consistency"
        else:
            interpretation = "POOR consistency"

        f.write(f"Move Accuracy CV: {move_cv:.2f}% → {interpretation}\n")

        # ICC Results
        if results.get("icc_move") or results.get("icc_step"):
            f.write("\n")
            f.write("-" * 70 + "\n")
            f.write("RELIABILITY (ICC)\n")
            f.write("-" * 70 + "\n\n")

            if results.get("icc_move"):
                icc = results["icc_move"]
                f.write(f"Move-Level ICC:\n")
                f.write(f"  Type: {icc['icc_type']}\n")
                f.write(f"  Value: {icc['icc_value']:.3f}\n")
                f.write(f"  95% CI: [{icc['ci_lower']:.3f}, {icc['ci_upper']:.3f}]\n")
                f.write(f"  Interpretation: {icc['interpretation']}\n")
                f.write(
                    f"  Based on: {icc['n_sentences']} sentences, {icc['n_runs']} runs\n\n"
                )

            if results.get("icc_step"):
                icc = results["icc_step"]
                f.write(f"Step-Level ICC:\n")
                f.write(f"  Type: {icc['icc_type']}\n")
                f.write(f"  Value: {icc['icc_value']:.3f}\n")
                f.write(f"  95% CI: [{icc['ci_lower']:.3f}, {icc['ci_upper']:.3f}]\n")
                f.write(f"  Interpretation: {icc['interpretation']}\n")
                f.write(
                    f"  Based on: {icc['n_sentences']} sentences, {icc['n_runs']} runs\n\n"
                )

            f.write("ICC Interpretation Guidelines:\n")
            f.write("  < 0.5:    Poor reliability (unsuitable for applied use)\n")
            f.write("  0.5-0.75: Moderate reliability (acceptable with caution)\n")
            f.write("  0.75-0.9: Good reliability (suitable for research)\n")
            f.write("  > 0.9:    Excellent reliability (suitable for applied use)\n")


def save_outputs(results, output_dir):
    """
    Save all analysis outputs.

    Args:
        results: Analysis results
        output_dir: Output directory path
    """
    condition = results["condition"]

    # Save consolidated runs data
    results["df_runs"].to_csv(output_dir / f"{condition}_all_runs.csv", index=False)

    # Save descriptive statistics
    results["df_stats"].to_csv(
        output_dir / f"{condition}_descriptive_stats.csv", index=False
    )

    # Save summary report
    create_summary_report(results, output_dir)


def main():
    """Main execution."""

    print("=" * 70)
    print(f"CONSISTENCY ANALYSIS - RQ2")
    print(f"Condition: {CONDITION}")
    print(f"Dataset: {DATASET}")
    print("=" * 70)

    # Create output directory
    output_dir = Path("evaluation_results") / "rq2_analysis"
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        # Perform analysis
        results = analyze_condition(CONDITION, DATASET)

        # Save outputs
        print(f"\nSaving results...")
        save_outputs(results, output_dir)

        print("\n" + "=" * 70)
        print("✅ ANALYSIS COMPLETE")
        print("=" * 70)
        print(f"\nOutput directory: {output_dir}/")
        print(f"Files created:")
        print(f"  - {CONDITION}_all_runs.csv (consolidated run data)")
        print(f"  - {CONDITION}_descriptive_stats.csv (summary statistics)")
        print(f"  - {CONDITION}_consistency_summary.txt (human-readable report)")

        # Print key findings
        df_stats = results["df_stats"]
        move_row = df_stats[df_stats["metric"] == "Move Accuracy"].iloc[0]

        print(f"\nKey Findings ({CONDITION}):")
        print(f"  Runs analyzed: {results['n_runs']}")
        print(
            f"  Move Accuracy: {move_row['mean']:.3f} ± {move_row['sd']:.3f} (CV: {move_row['cv']:.2f}%)"
        )
        print(f"  95% CI: [{move_row['ci_lower']:.3f}, {move_row['ci_upper']:.3f}]")
        print(f"  Range: [{move_row['min']:.3f}, {move_row['max']:.3f}]")

        print("\nNext steps:")
        print("  1. Review descriptive statistics CSV")
        print("  2. Run for other condition (change CONDITION at top of script)")
        print("  3. Run 'compare_consistency_rq2.py' to compare conditions")
        print()

    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("\nMake sure you've run 'evaluate_rq2_runs.py' first!")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
