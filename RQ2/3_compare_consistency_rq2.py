"""
Compare Consistency RQ2 - Between-Condition Comparison
=======================================================
Compares consistency between zero-shot and fine-tuned conditions.

Performs:
- Variance comparison (Levene's test)
- Mean accuracy comparison (Welch's t-test)
- Effect size calculation (Cohen's d)
- ICC comparison
- Comprehensive comparison table
- Outputs: Statistical test results, comparison tables

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

# Try to import pingouin for effect sizes
try:
    from pingouin import compute_effsize
    PINGOUIN_AVAILABLE = True
except ImportError:
    PINGOUIN_AVAILABLE = False
    print("⚠️  Warning: pingouin not installed. Effect size calculation will use scipy.")

# ============================================================================
# CONFIGURATION
# ============================================================================

DATASET = "test"  # Always 'test' for RQ2

# ============================================================================


def load_condition_stats(condition):
    """
    Load descriptive statistics for a condition.
    
    Args:
        condition: Condition name
        
    Returns:
        pd.DataFrame: Descriptive statistics
    """
    stats_dir = Path("evaluation_results") / "rq2_analysis"
    stats_file = stats_dir / f"{condition}_descriptive_stats.csv"
    
    if not stats_file.exists():
        raise FileNotFoundError(
            f"Statistics not found for {condition}: {stats_file}\n"
            f"Run 'analyze_consistency_rq2.py' first for this condition."
        )
    
    return pd.read_csv(stats_file)


def load_condition_runs(condition):
    """
    Load all runs data for a condition.
    
    Args:
        condition: Condition name
        
    Returns:
        pd.DataFrame: All runs data
    """
    runs_dir = Path("evaluation_results") / "rq2_analysis"
    runs_file = runs_dir / f"{condition}_all_runs.csv"
    
    if not runs_file.exists():
        raise FileNotFoundError(
            f"Runs data not found for {condition}: {runs_file}\n"
            f"Run 'analyze_consistency_rq2.py' first for this condition."
        )
    
    return pd.read_csv(runs_file)


def calculate_cohens_d(group1, group2):
    """
    Calculate Cohen's d effect size.
    
    Args:
        group1: First group data
        group2: Second group data
        
    Returns:
        float: Cohen's d
    """
    if PINGOUIN_AVAILABLE:
        return compute_effsize(group1, group2, eftype='cohen')
    else:
        # Manual calculation
        n1, n2 = len(group1), len(group2)
        var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
        pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
        return (np.mean(group1) - np.mean(group2)) / pooled_std


def interpret_cohens_d(d):
    """
    Interpret Cohen's d effect size.
    
    Args:
        d: Cohen's d value
        
    Returns:
        str: Interpretation
    """
    abs_d = abs(d)
    if abs_d < 0.2:
        return "Negligible"
    elif abs_d < 0.5:
        return "Small"
    elif abs_d < 0.8:
        return "Medium"
    else:
        return "Large"


def compare_variances(df_zs, df_ft, metric='move_accuracy'):
    """
    Compare variances using Levene's test.
    
    Args:
        df_zs: Zero-shot runs data
        df_ft: Fine-tuned runs data
        metric: Metric to compare
        
    Returns:
        dict: Variance comparison results
    """
    zs_data = df_zs[metric].values
    ft_data = df_ft[metric].values
    
    # Levene's test (robust to non-normality)
    stat, p_value = stats.levene(zs_data, ft_data)
    
    # Variance ratio
    var_zs = np.var(zs_data, ddof=1)
    var_ft = np.var(ft_data, ddof=1)
    var_ratio = var_zs / var_ft if var_ft != 0 else np.nan
    
    # F-test for variance equality (assumes normality)
    # F = larger_var / smaller_var
    if var_zs > var_ft:
        f_stat = var_zs / var_ft
        df1, df2 = len(zs_data) - 1, len(ft_data) - 1
    else:
        f_stat = var_ft / var_zs
        df1, df2 = len(ft_data) - 1, len(zs_data) - 1
    
    f_p_value = 2 * min(stats.f.cdf(f_stat, df1, df2), 1 - stats.f.cdf(f_stat, df1, df2))
    
    return {
        'metric': metric,
        'var_zero_shot': var_zs,
        'var_fine_tuned': var_ft,
        'var_ratio': var_ratio,
        'levene_statistic': stat,
        'levene_p_value': p_value,
        'significant': p_value < 0.05,
        'f_statistic': f_stat,
        'f_p_value': f_p_value,
    }


def compare_means(df_zs, df_ft, metric='move_accuracy'):
    """
    Compare means using Welch's t-test (allows unequal variances).
    
    Args:
        df_zs: Zero-shot runs data
        df_ft: Fine-tuned runs data
        metric: Metric to compare
        
    Returns:
        dict: Mean comparison results
    """
    zs_data = df_zs[metric].values
    ft_data = df_ft[metric].values
    
    # Welch's t-test (does not assume equal variances)
    stat, p_value = stats.ttest_ind(zs_data, ft_data, equal_var=False)
    
    # Effect size (Cohen's d)
    cohens_d = calculate_cohens_d(zs_data, ft_data)
    
    # 95% CI for mean difference
    mean_diff = np.mean(zs_data) - np.mean(ft_data)
    se_diff = np.sqrt(np.var(zs_data, ddof=1)/len(zs_data) + np.var(ft_data, ddof=1)/len(ft_data))
    
    # Degrees of freedom for Welch's t-test
    n1, n2 = len(zs_data), len(ft_data)
    s1, s2 = np.var(zs_data, ddof=1), np.var(ft_data, ddof=1)
    df = (s1/n1 + s2/n2)**2 / ((s1/n1)**2/(n1-1) + (s2/n2)**2/(n2-1))
    
    t_crit = stats.t.ppf(0.975, df)
    ci_lower = mean_diff - t_crit * se_diff
    ci_upper = mean_diff + t_crit * se_diff
    
    return {
        'metric': metric,
        'mean_zero_shot': np.mean(zs_data),
        'mean_fine_tuned': np.mean(ft_data),
        'mean_difference': mean_diff,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        't_statistic': stat,
        't_p_value': p_value,
        'degrees_of_freedom': df,
        'cohens_d': cohens_d,
        'effect_size_interpretation': interpret_cohens_d(cohens_d),
        'significant': p_value < 0.05,
    }


def create_comprehensive_comparison_table(df_zs_stats, df_ft_stats, var_results, mean_results):
    """
    Create a comprehensive comparison table for publication.
    
    Args:
        df_zs_stats: Zero-shot descriptive stats
        df_ft_stats: Fine-tuned descriptive stats
        var_results: Variance comparison results
        mean_results: Mean comparison results
        
    Returns:
        pd.DataFrame: Comprehensive comparison table
    """
    rows = []
    
    for metric in ['Move Accuracy', 'Step Accuracy', 'Move F1', 'Step F1']:
        zs_row = df_zs_stats[df_zs_stats['metric'] == metric].iloc[0]
        ft_row = df_ft_stats[df_ft_stats['metric'] == metric].iloc[0]
        
        # Find corresponding test results
        metric_key = metric.lower().replace(' ', '_')
        var_res = next((r for r in var_results if r['metric'] == metric_key), None)
        mean_res = next((r for r in mean_results if r['metric'] == metric_key), None)
        
        row = {
            'Metric': metric,
            'Zero-shot Mean': f"{zs_row['mean']:.4f}",
            'Zero-shot SD': f"{zs_row['sd']:.4f}",
            'Zero-shot CV (%)': f"{zs_row['cv']:.2f}",
            'Fine-tuned Mean': f"{ft_row['mean']:.4f}",
            'Fine-tuned SD': f"{ft_row['sd']:.4f}",
            'Fine-tuned CV (%)': f"{ft_row['cv']:.2f}",
        }
        
        if mean_res:
            row['Mean Diff'] = f"{mean_res['mean_difference']:.4f}"
            row['p-value (mean)'] = f"{mean_res['t_p_value']:.4f}"
            row['Cohen\'s d'] = f"{mean_res['cohens_d']:.3f}"
        
        if var_res:
            row['Var Ratio'] = f"{var_res['var_ratio']:.3f}"
            row['p-value (var)'] = f"{var_res['levene_p_value']:.4f}"
        
        rows.append(row)
    
    return pd.DataFrame(rows)


def create_summary_report(df_zs_stats, df_ft_stats, var_results, mean_results, output_file):
    """
    Create human-readable summary report.
    
    Args:
        df_zs_stats: Zero-shot stats
        df_ft_stats: Fine-tuned stats
        var_results: Variance comparison results
        mean_results: Mean comparison results
        output_file: Output file path
    """
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=" * 70 + "\n")
        f.write("CONSISTENCY COMPARISON: ZERO-SHOT VS FINE-TUNED\n")
        f.write("=" * 70 + "\n\n")
        
        f.write("Research Question 2 (RQ2): Consistency Analysis\n")
        f.write(f"Dataset: {DATASET}\n\n")
        
        f.write("-" * 70 + "\n")
        f.write("1. VARIANCE COMPARISON (Levene's Test)\n")
        f.write("-" * 70 + "\n\n")
        
        f.write("Research question: Do zero-shot and fine-tuned differ in variance?\n")
        f.write("H0: σ²(zero-shot) = σ²(fine-tuned)\n\n")
        
        for var_res in var_results:
            f.write(f"{var_res['metric'].upper()}:\n")
            f.write(f"  Zero-shot variance: {var_res['var_zero_shot']:.6f}\n")
            f.write(f"  Fine-tuned variance: {var_res['var_fine_tuned']:.6f}\n")
            f.write(f"  Variance ratio (ZS/FT): {var_res['var_ratio']:.3f}\n")
            f.write(f"  Levene's statistic: {var_res['levene_statistic']:.4f}\n")
            f.write(f"  p-value: {var_res['levene_p_value']:.4f}\n")
            
            if var_res['significant']:
                f.write(f"  ✓ SIGNIFICANT difference in variance (p < 0.05)\n")
            else:
                f.write(f"  ✗ No significant difference in variance (p ≥ 0.05)\n")
            f.write("\n")
        
        f.write("-" * 70 + "\n")
        f.write("2. MEAN COMPARISON (Welch's t-test)\n")
        f.write("-" * 70 + "\n\n")
        
        f.write("Research question: Do zero-shot and fine-tuned differ in mean accuracy?\n")
        f.write("H0: μ(zero-shot) = μ(fine-tuned)\n\n")
        
        for mean_res in mean_results:
            f.write(f"{mean_res['metric'].upper()}:\n")
            f.write(f"  Zero-shot mean: {mean_res['mean_zero_shot']:.4f}\n")
            f.write(f"  Fine-tuned mean: {mean_res['mean_fine_tuned']:.4f}\n")
            f.write(f"  Difference: {mean_res['mean_difference']:.4f}\n")
            f.write(f"  95% CI: [{mean_res['ci_lower']:.4f}, {mean_res['ci_upper']:.4f}]\n")
            f.write(f"  t-statistic: {mean_res['t_statistic']:.4f}\n")
            f.write(f"  p-value: {mean_res['t_p_value']:.4f}\n")
            f.write(f"  Cohen's d: {mean_res['cohens_d']:.3f} ({mean_res['effect_size_interpretation']})\n")
            
            if mean_res['significant']:
                f.write(f"  ✓ SIGNIFICANT difference in mean (p < 0.05)\n")
            else:
                f.write(f"  ✗ No significant difference in mean (p ≥ 0.05)\n")
            f.write("\n")
        
        f.write("-" * 70 + "\n")
        f.write("3. CONSISTENCY COMPARISON (Coefficient of Variation)\n")
        f.write("-" * 70 + "\n\n")
        
        zs_move = df_zs_stats[df_zs_stats['metric'] == 'Move Accuracy'].iloc[0]
        ft_move = df_ft_stats[df_ft_stats['metric'] == 'Move Accuracy'].iloc[0]
        
        f.write(f"Zero-shot CV: {zs_move['cv']:.2f}%\n")
        f.write(f"Fine-tuned CV: {ft_move['cv']:.2f}%\n")
        f.write(f"Difference: {abs(zs_move['cv'] - ft_move['cv']):.2f} percentage points\n\n")
        
        if zs_move['cv'] < ft_move['cv']:
            f.write("→ Zero-shot shows LOWER variability (more consistent)\n")
        else:
            f.write("→ Fine-tuned shows LOWER variability (more consistent)\n")
        
        f.write("\n")
        f.write("-" * 70 + "\n")
        f.write("4. INTERPRETATION GUIDELINES\n")
        f.write("-" * 70 + "\n\n")
        
        f.write("Effect Size (Cohen's d):\n")
        f.write("  < 0.2:   Negligible\n")
        f.write("  0.2-0.5: Small\n")
        f.write("  0.5-0.8: Medium\n")
        f.write("  > 0.8:   Large\n\n")
        
        f.write("Coefficient of Variation (CV):\n")
        f.write("  < 5%:    Excellent consistency\n")
        f.write("  5-10%:   Good consistency\n")
        f.write("  10-20%:  Moderate consistency\n")
        f.write("  > 20%:   Poor consistency\n")


def main():
    """Main execution."""
    
    print("=" * 70)
    print("CONSISTENCY COMPARISON - RQ2")
    print("Zero-Shot vs Fine-Tuned")
    print("=" * 70)
    print()
    
    # Create output directory
    output_dir = Path("evaluation_results") / "rq2_analysis"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Load data for both conditions
        print("Loading data...")
        df_zs_stats = load_condition_stats("zero_shot")
        df_ft_stats = load_condition_stats("fine_tuned")
        df_zs_runs = load_condition_runs("zero_shot")
        df_ft_runs = load_condition_runs("fine_tuned")
        print(f"  ✓ Zero-shot: {len(df_zs_runs)} runs")
        print(f"  ✓ Fine-tuned: {len(df_ft_runs)} runs")
        print()
        
        # Compare variances
        print("Comparing variances (Levene's test)...")
        var_results = []
        for metric in ['move_accuracy', 'step_accuracy', 'move_f1', 'step_f1']:
            var_res = compare_variances(df_zs_runs, df_ft_runs, metric)
            var_results.append(var_res)
            print(f"  {metric}: F={var_res['levene_statistic']:.3f}, p={var_res['levene_p_value']:.4f}")
        print()
        
        # Compare means
        print("Comparing means (Welch's t-test)...")
        mean_results = []
        for metric in ['move_accuracy', 'step_accuracy', 'move_f1', 'step_f1']:
            mean_res = compare_means(df_zs_runs, df_ft_runs, metric)
            mean_results.append(mean_res)
            print(f"  {metric}: t={mean_res['t_statistic']:.3f}, p={mean_res['t_p_value']:.4f}, d={mean_res['cohens_d']:.3f}")
        print()
        
        # Create outputs
        print("Creating output files...")
        
        # Comprehensive comparison table
        df_comparison = create_comprehensive_comparison_table(
            df_zs_stats, df_ft_stats, var_results, mean_results
        )
        df_comparison.to_csv(
            output_dir / "comparison_comprehensive.csv",
            index=False
        )
        print("  ✓ comparison_comprehensive.csv")
        
        # Variance comparison details
        pd.DataFrame(var_results).to_csv(
            output_dir / "comparison_variance_tests.csv",
            index=False
        )
        print("  ✓ comparison_variance_tests.csv")
        
        # Mean comparison details
        pd.DataFrame(mean_results).to_csv(
            output_dir / "comparison_mean_tests.csv",
            index=False
        )
        print("  ✓ comparison_mean_tests.csv")
        
        # Summary report
        create_summary_report(
            df_zs_stats, df_ft_stats, var_results, mean_results,
            output_dir / "comparison_summary.txt"
        )
        print("  ✓ comparison_summary.txt")
        
        print("\n" + "=" * 70)
        print("✅ COMPARISON COMPLETE")
        print("=" * 70)
        
        # Print key findings
        move_var = var_results[0]
        move_mean = mean_results[0]
        
        print("\nKey Findings (Move Accuracy):")
        print(f"  Variance test: p = {move_var['levene_p_value']:.4f} {'(significant)' if move_var['significant'] else '(not significant)'}")
        print(f"  Mean test: p = {move_mean['t_p_value']:.4f} {'(significant)' if move_mean['significant'] else '(not significant)'}")
        print(f"  Effect size: d = {move_mean['cohens_d']:.3f} ({move_mean['effect_size_interpretation']})")
        
        print(f"\nOutput directory: {output_dir}/")
        print("\nNext steps:")
        print("  1. Review comparison_summary.txt for interpretation")
        print("  2. Use comparison_comprehensive.csv for manuscript table")
        print("  3. Run 'analyze_sentences_rq2.py' for sentence-level analysis")
        print("  4. Run 'visualize_rq2.py' to create figures")
        print()
        
    except FileNotFoundError as e:
        print(f"\n❌ ERROR: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
