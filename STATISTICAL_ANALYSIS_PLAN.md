# Statistical Analysis Plan
## LLM Consistency in Rhetorical Move-Step Annotation

**Purpose:** Comprehensive, step-by-step guide for analyzing consistency data  
**Audience:** Researchers with Python skills but limited statistical background  
**Approach:** Cookbook style - clear instructions, code examples, interpretation guidance

---

## Analysis Software & Packages

### Required Python Packages

```python
# Core data manipulation
import pandas as pd
import numpy as np

# Statistical tests
from scipy import stats
from scipy.stats import (
    shapiro,           # Normality test
    levene,            # Variance homogeneity test  
    f_oneway,          # One-way ANOVA
    mannwhitneyu,      # Non-parametric alternative
)

# Effect sizes
from pingouin import (
    compute_effsize,   # Cohen's d
    intraclass_corr,   # ICC calculation
)

# Mixed models (optional, for advanced analysis)
import statsmodels.api as sm
from statsmodels.formula.api import mixedlm

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Multiple testing correction
from statsmodels.stats.multitest import multipletests
```

### Installation Commands

```bash
pip install pandas numpy scipy pingouin statsmodels matplotlib seaborn
```

---

## Phase 1: Data Preparation

### 1.1 Load Results Data

**Expected Data Structure:**

You'll have 124 evaluation JSON files (4 conditions × 31 runs each):
- 1 baseline run per condition (Phase 2)
- 30 consistency runs per condition (Phase 3)

**Create Summary DataFrame:**

```python
import json
import pandas as pd
from pathlib import Path

def load_all_results():
    """Load all evaluation results into a single DataFrame."""
    results = []
    
    # Conditions
    conditions = ['a1_zero_shot', 'a2_few_shot_3', 'a3_few_shot_8', 'a4_fine_tuned']
    
    for condition in conditions:
        results_dir = Path(f'results/{condition}/')
        
        # Load all JSON files for this condition
        for json_file in sorted(results_dir.glob('run_*.json')):
            with open(json_file) as f:
                data = json.load(f)
            
            # Extract key metrics
            result_row = {
                'condition': condition,
                'run_number': int(json_file.stem.split('_')[1]),
                'move_accuracy': data['move_level']['accuracy'],
                'step_accuracy': data['step_level']['accuracy'],
                'move_f1': data['move_level']['weighted_f1'],
                'step_f1': data['step_level']['weighted_f1'],
                # Add other metrics as needed
            }
            results.append(result_row)
    
    df = pd.DataFrame(results)
    return df

# Load data
df = load_all_results()

# Save for later use
df.to_csv('results/consolidated_results.csv', index=False)
```

### 1.2 Inspect Data

```python
# Check data structure
print(df.head())
print(f"\nShape: {df.shape}")
print(f"\nConditions: {df['condition'].unique()}")
print(f"\nRuns per condition: {df.groupby('condition').size()}")

# Check for missing values
print(f"\nMissing values:\n{df.isnull().sum()}")

# Basic statistics
print(f"\nBasic statistics:\n{df.describe()}")
```

---

## Phase 2: Descriptive Statistics

### 2.1 Calculate Summary Statistics Per Condition

```python
def calculate_summary_stats(df, metric='move_accuracy'):
    """Calculate comprehensive summary statistics for each condition."""
    
    summary = df.groupby('condition')[metric].agg([
        ('mean', 'mean'),
        ('sd', 'std'),
        ('median', 'median'),
        ('min', 'min'),
        ('max', 'max'),
        ('q25', lambda x: x.quantile(0.25)),
        ('q75', lambda x: x.quantile(0.75)),
    ]).reset_index()
    
    # Calculate additional metrics
    summary['cv'] = (summary['sd'] / summary['mean']) * 100  # Coefficient of variation
    summary['range'] = summary['max'] - summary['min']
    summary['iqr'] = summary['q75'] - summary['q25']
    
    # Calculate 95% CI for mean
    n = df.groupby('condition').size().values
    summary['ci_lower'] = summary['mean'] - 1.96 * (summary['sd'] / np.sqrt(n))
    summary['ci_upper'] = summary['mean'] + 1.96 * (summary['sd'] / np.sqrt(n))
    
    return summary

# Calculate for move accuracy
move_summary = calculate_summary_stats(df, 'move_accuracy')
print("Move-Level Accuracy Summary:")
print(move_summary.to_string(index=False))

# Calculate for step accuracy  
step_summary = calculate_summary_stats(df, 'step_accuracy')
print("\nStep-Level Accuracy Summary:")
print(step_summary.to_string(index=False))

# Save to CSV
move_summary.to_csv('results/move_accuracy_summary.csv', index=False)
step_summary.to_csv('results/step_accuracy_summary.csv', index=False)
```

### 2.2 Create Summary Table for Paper

```python
def create_results_table(move_summary, step_summary):
    """Create publication-ready table."""
    
    # Format for LaTeX or Markdown
    table_rows = []
    
    for _, row in move_summary.iterrows():
        condition = row['condition'].replace('_', ' ').title()
        
        # Move-level results
        move_text = f"{row['mean']:.1f}% (SD={row['sd']:.2f}%, CV={row['cv']:.1f}%)"
        
        # Get step-level results
        step_row = step_summary[step_summary['condition'] == row['condition']].iloc[0]
        step_text = f"{step_row['mean']:.1f}% (SD={step_row['sd']:.2f}%, CV={step_row['cv']:.1f}%)"
        
        table_rows.append({
            'Condition': condition,
            'Move Accuracy': move_text,
            'Step Accuracy': step_text,
            'Move 95% CI': f"[{row['ci_lower']:.1f}%, {row['ci_upper']:.1f}%]",
            'Step 95% CI': f"[{step_row['ci_lower']:.1f}%, {step_row['ci_upper']:.1f}%]",
        })
    
    results_table = pd.DataFrame(table_rows)
    print(results_table.to_string(index=False))
    
    # Save as CSV for easy import to Word/LaTeX
    results_table.to_csv('results/TABLE_1_summary_statistics.csv', index=False)
    
    return results_table

table1 = create_results_table(move_summary, step_summary)
```

---

## Phase 3: Normality Assessment

**Why:** Many statistical tests assume normal distribution. We need to check this assumption.

```python
def test_normality(df, metric='move_accuracy'):
    """Test if data in each condition follows normal distribution."""
    
    results = []
    
    for condition in df['condition'].unique():
        data = df[df['condition'] == condition][metric]
        
        # Shapiro-Wilk test
        statistic, p_value = shapiro(data)
        
        results.append({
            'condition': condition,
            'statistic': statistic,
            'p_value': p_value,
            'is_normal': p_value > 0.05  # Conventional threshold
        })
    
    normality_df = pd.DataFrame(results)
    print(f"Normality Test Results ({metric}):")
    print(normality_df.to_string(index=False))
    print("\nInterpretation: p > 0.05 suggests data is normally distributed")
    
    return normality_df

# Test normality
norm_move = test_normality(df, 'move_accuracy')
norm_step = test_normality(df, 'step_accuracy')

# Save results
norm_move.to_csv('results/normality_test_move.csv', index=False)
norm_step.to_csv('results/normality_test_step.csv', index=False)
```

### 3.2 Visual Inspection of Distribution

```python
def plot_distributions(df, metric='move_accuracy', save_path='figures/'):
    """Create Q-Q plots and histograms to assess normality visually."""
    
    Path(save_path).mkdir(parents=True, exist_ok=True)
    
    conditions = df['condition'].unique()
    n_conditions = len(conditions)
    
    # Create figure with subplots
    fig, axes = plt.subplots(2, n_conditions, figsize=(4*n_conditions, 8))
    
    for i, condition in enumerate(conditions):
        data = df[df['condition'] == condition][metric]
        
        # Histogram (top row)
        axes[0, i].hist(data, bins=10, edgecolor='black', alpha=0.7)
        axes[0, i].axvline(data.mean(), color='red', linestyle='--', label='Mean')
        axes[0, i].axvline(data.median(), color='blue', linestyle='--', label='Median')
        axes[0, i].set_title(condition)
        axes[0, i].set_xlabel(metric)
        axes[0, i].set_ylabel('Frequency')
        axes[0, i].legend()
        
        # Q-Q plot (bottom row)
        stats.probplot(data, dist="norm", plot=axes[1, i])
        axes[1, i].set_title(f'Q-Q Plot: {condition}')
    
    plt.tight_layout()
    plt.savefig(f'{save_path}distribution_assessment_{metric}.png', dpi=300)
    plt.close()
    
    print(f"Saved distribution plots to {save_path}")

# Create plots
plot_distributions(df, 'move_accuracy')
plot_distributions(df, 'step_accuracy')
```

**Interpretation Guide:**
- **Histogram:** Should look roughly bell-shaped for normal distribution
- **Q-Q Plot:** Points should fall roughly on the diagonal line
- **If not normal:** Consider using non-parametric tests (see Section 6)

---

## Phase 4: Variance Comparison (PRIMARY ANALYSIS)

**Research Question:** Does consistency (variance) differ across conditions?

### 4.1 Levene's Test (Omnibus Test)

**What it does:** Tests if variances are equal across all conditions  
**Null hypothesis:** σ₁² = σ₂² = σ₃² = σ₄² (all variances are equal)

```python
def levenes_test(df, metric='move_accuracy'):
    """Perform Levene's test for variance homogeneity."""
    
    # Split data by condition
    groups = [df[df['condition'] == cond][metric].values 
              for cond in df['condition'].unique()]
    
    # Perform test
    statistic, p_value = levene(*groups)
    
    print(f"\nLevene's Test for {metric}:")
    print(f"Test Statistic: {statistic:.4f}")
    print(f"P-value: {p_value:.4f}")
    
    if p_value < 0.05:
        print("✓ Significant difference in variance detected (p < 0.05)")
        print("  → At least one condition has different consistency")
    else:
        print("✗ No significant difference in variance (p ≥ 0.05)")
        print("  → Consistency is similar across conditions")
    
    return {'statistic': statistic, 'p_value': p_value}

# Run Levene's test
levene_move = levenes_test(df, 'move_accuracy')
levene_step = levenes_test(df, 'step_accuracy')

# Save results
pd.DataFrame([levene_move, levene_step], 
             index=['move_accuracy', 'step_accuracy']).to_csv(
    'results/levenes_test_results.csv'
)
```

### 4.2 Pairwise Variance Comparisons

**Why:** If Levene's test is significant, we want to know WHICH conditions differ.

```python
from itertools import combinations

def pairwise_variance_tests(df, metric='move_accuracy', alpha=0.05):
    """Compare variance between all pairs of conditions."""
    
    conditions = sorted(df['condition'].unique())
    pairs = list(combinations(conditions, 2))
    
    results = []
    
    for cond1, cond2 in pairs:
        data1 = df[df['condition'] == cond1][metric].values
        data2 = df[df['condition'] == cond2][metric].values
        
        # Levene's test for this pair
        statistic, p_value = levene(data1, data2)
        
        # Calculate variance ratio
        var1 = np.var(data1, ddof=1)
        var2 = np.var(data2, ddof=1)
        var_ratio = var1 / var2  # How many times bigger is var1?
        
        results.append({
            'condition_1': cond1,
            'condition_2': cond2,
            'var_1': var1,
            'var_2': var2,
            'var_ratio': var_ratio,
            'p_value': p_value,
        })
    
    results_df = pd.DataFrame(results)
    
    # Apply Bonferroni correction
    n_tests = len(pairs)
    corrected_alpha = alpha / n_tests
    results_df['significant'] = results_df['p_value'] < corrected_alpha
    results_df['corrected_alpha'] = corrected_alpha
    
    print(f"\nPairwise Variance Comparisons ({metric}):")
    print(f"Bonferroni-corrected α = {corrected_alpha:.4f}")
    print(results_df.to_string(index=False))
    
    # Save results
    results_df.to_csv(f'results/pairwise_variance_{metric}.csv', index=False)
    
    return results_df

# Run pairwise tests
pairwise_move = pairwise_variance_tests(df, 'move_accuracy')
pairwise_step = pairwise_variance_tests(df, 'step_accuracy')
```

**Interpretation:**
- **var_ratio = 2.0:** Condition 1 has 2× the variance of Condition 2
- **var_ratio = 0.5:** Condition 1 has half the variance of Condition 2
- **p < corrected_alpha:** This difference is statistically significant

---

## Phase 5: Mean Accuracy Comparisons

**Research Question:** Does mean accuracy differ across conditions?

### 5.1 One-Way ANOVA (if data is normal)

```python
def anova_test(df, metric='move_accuracy'):
    """Perform one-way ANOVA to compare means across conditions."""
    
    # Split data by condition
    groups = [df[df['condition'] == cond][metric].values 
              for cond in df['condition'].unique()]
    
    # Perform ANOVA
    f_stat, p_value = f_oneway(*groups)
    
    print(f"\nOne-Way ANOVA for {metric}:")
    print(f"F-statistic: {f_stat:.4f}")
    print(f"P-value: {p_value:.4f}")
    
    if p_value < 0.05:
        print("✓ Significant difference in means detected (p < 0.05)")
    else:
        print("✗ No significant difference in means (p ≥ 0.05)")
    
    return {'f_statistic': f_stat, 'p_value': p_value}

# Run ANOVA
anova_move = anova_test(df, 'move_accuracy')
anova_step = anova_test(df, 'step_accuracy')
```

### 5.2 Pairwise Mean Comparisons (Post-Hoc)

```python
def pairwise_mean_tests(df, metric='move_accuracy', alpha=0.05):
    """Compare means between all pairs of conditions."""
    
    from scipy.stats import ttest_ind
    
    conditions = sorted(df['condition'].unique())
    pairs = list(combinations(conditions, 2))
    
    results = []
    
    for cond1, cond2 in pairs:
        data1 = df[df['condition'] == cond1][metric].values
        data2 = df[df['condition'] == cond2][metric].values
        
        # T-test
        t_stat, p_value = ttest_ind(data1, data2)
        
        # Calculate effect size (Cohen's d)
        mean1, mean2 = np.mean(data1), np.mean(data2)
        std1, std2 = np.std(data1, ddof=1), np.std(data2, ddof=1)
        pooled_std = np.sqrt((std1**2 + std2**2) / 2)
        cohens_d = (mean1 - mean2) / pooled_std
        
        results.append({
            'condition_1': cond1,
            'condition_2': cond2,
            'mean_1': mean1,
            'mean_2': mean2,
            'mean_diff': mean1 - mean2,
            'cohens_d': cohens_d,
            't_statistic': t_stat,
            'p_value': p_value,
        })
    
    results_df = pd.DataFrame(results)
    
    # Bonferroni correction
    n_tests = len(pairs)
    corrected_alpha = alpha / n_tests
    results_df['significant'] = results_df['p_value'] < corrected_alpha
    results_df['corrected_alpha'] = corrected_alpha
    
    print(f"\nPairwise Mean Comparisons ({metric}):")
    print(f"Bonferroni-corrected α = {corrected_alpha:.4f}")
    print(results_df.to_string(index=False))
    
    results_df.to_csv(f'results/pairwise_means_{metric}.csv', index=False)
    
    return results_df

# Run pairwise tests
pairwise_means_move = pairwise_mean_tests(df, 'move_accuracy')
pairwise_means_step = pairwise_mean_tests(df, 'step_accuracy')
```

**Cohen's d Interpretation:**
- |d| < 0.2: Small effect
- 0.2 ≤ |d| < 0.5: Small to medium effect
- 0.5 ≤ |d| < 0.8: Medium to large effect
- |d| ≥ 0.8: Large effect

---

## Phase 6: Reliability Analysis (ICC)

**What is ICC?** Intraclass Correlation Coefficient measures how consistent annotations are across runs.

```python
def calculate_icc(df, metric='move_accuracy'):
    """Calculate ICC for each condition."""
    
    import pingouin as pg
    
    results = []
    
    for condition in df['condition'].unique():
        # Prepare data: need long format with 'targets' and 'raters'
        condition_data = df[df['condition'] == condition].copy()
        condition_data['article'] = condition_data.index % 10  # Assuming 10 test articles
        
        # ICC calculation
        # ICC(2,1) = two-way random effects, single measurement
        icc_result = pg.intraclass_corr(
            data=condition_data,
            targets='article',
            raters='run_number',
            ratings=metric
        )
        
        # Get ICC(2,1) value
        icc_value = icc_result[icc_result['Type'] == 'ICC2']['ICC'].values[0]
        
        results.append({
            'condition': condition,
            'icc': icc_value,
            'interpretation': interpret_icc(icc_value)
        })
        
        print(f"\n{condition}:")
        print(f"  ICC: {icc_value:.3f}")
        print(f"  {interpret_icc(icc_value)}")
    
    icc_df = pd.DataFrame(results)
    icc_df.to_csv(f'results/icc_{metric}.csv', index=False)
    
    return icc_df

def interpret_icc(icc):
    """Interpret ICC value."""
    if icc < 0.5:
        return "Poor reliability"
    elif icc < 0.75:
        return "Moderate reliability"
    elif icc < 0.9:
        return "Good reliability"
    else:
        return "Excellent reliability"

# Calculate ICC
icc_move = calculate_icc(df, 'move_accuracy')
icc_step = calculate_icc(df, 'step_accuracy')
```

**ICC Interpretation:**
- ICC < 0.5: Poor consistency
- 0.5 ≤ ICC < 0.75: Moderate consistency
- 0.75 ≤ ICC < 0.9: Good consistency
- ICC ≥ 0.9: Excellent consistency

---

## Phase 7: Visualization

### 7.1 Distribution Plots (Violin + Box)

```python
def create_distribution_plot(df, metric='move_accuracy', save_path='figures/'):
    """Create violin plot with overlaid boxplot."""
    
    Path(save_path).mkdir(parents=True, exist_ok=True)
    
    plt.figure(figsize=(12, 6))
    
    # Violin plot
    sns.violinplot(data=df, x='condition', y=metric, inner=None, color='lightblue')
    
    # Overlay boxplot
    sns.boxplot(data=df, x='condition', y=metric, width=0.3, 
                boxprops=dict(alpha=0.7), showfliers=False)
    
    # Add individual points
    sns.stripplot(data=df, x='condition', y=metric, 
                  size=3, alpha=0.3, color='black')
    
    # Formatting
    plt.xlabel('Condition', fontsize=12)
    plt.ylabel(metric.replace('_', ' ').title(), fontsize=12)
    plt.title(f'Distribution of {metric.replace("_", " ").title()} Across Conditions', 
              fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Save
    plt.savefig(f'{save_path}FIGURE_distribution_{metric}.png', dpi=300)
    plt.close()
    
    print(f"Saved distribution plot: {save_path}FIGURE_distribution_{metric}.png")

# Create plots
create_distribution_plot(df, 'move_accuracy')
create_distribution_plot(df, 'step_accuracy')
```

### 7.2 Consistency Comparison (CV Bar Chart)

```python
def create_consistency_plot(move_summary, step_summary, save_path='figures/'):
    """Create bar chart comparing CV across conditions."""
    
    Path(save_path).mkdir(parents=True, exist_ok=True)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Move-level CV
    ax1.bar(range(len(move_summary)), move_summary['cv'], 
            color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    ax1.set_xticks(range(len(move_summary)))
    ax1.set_xticklabels(move_summary['condition'], rotation=45, ha='right')
    ax1.set_ylabel('Coefficient of Variation (%)', fontsize=12)
    ax1.set_title('Move-Level Consistency', fontsize=14, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for i, v in enumerate(move_summary['cv']):
        ax1.text(i, v + 0.2, f'{v:.1f}%', ha='center', fontsize=10)
    
    # Step-level CV
    ax2.bar(range(len(step_summary)), step_summary['cv'],
            color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    ax2.set_xticks(range(len(step_summary)))
    ax2.set_xticklabels(step_summary['condition'], rotation=45, ha='right')
    ax2.set_ylabel('Coefficient of Variation (%)', fontsize=12)
    ax2.set_title('Step-Level Consistency', fontsize=14, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for i, v in enumerate(step_summary['cv']):
        ax2.text(i, v + 0.2, f'{v:.1f}%', ha='center', fontsize=10)
    
    plt.tight_layout()
    plt.savefig(f'{save_path}FIGURE_consistency_comparison.png', dpi=300)
    plt.close()
    
    print(f"Saved consistency plot: {save_path}FIGURE_consistency_comparison.png")

# Create plot
create_consistency_plot(move_summary, step_summary)
```

### 7.3 Accuracy vs. Consistency Trade-off

```python
def create_tradeoff_plot(move_summary, save_path='figures/'):
    """Create scatter plot showing accuracy-consistency trade-off."""
    
    Path(save_path).mkdir(parents=True, exist_ok=True)
    
    plt.figure(figsize=(10, 8))
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    
    for i, row in move_summary.iterrows():
        plt.scatter(row['mean'], row['cv'], s=200, c=colors[i], 
                   alpha=0.7, edgecolors='black', linewidth=2)
        plt.text(row['mean'] + 0.5, row['cv'], row['condition'], 
                fontsize=10, va='center')
    
    plt.xlabel('Mean Accuracy (%)', fontsize=13, fontweight='bold')
    plt.ylabel('Coefficient of Variation (%) - Lower is Better', 
              fontsize=13, fontweight='bold')
    plt.title('Accuracy vs. Consistency Trade-off', 
             fontsize=15, fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    # Add ideal region annotation
    plt.axhline(y=5, color='gray', linestyle='--', alpha=0.5, label='Good consistency (CV < 5%)')
    plt.axvline(x=80, color='gray', linestyle='--', alpha=0.5, label='Good accuracy (> 80%)')
    plt.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig(f'{save_path}FIGURE_accuracy_consistency_tradeoff.png', dpi=300)
    plt.close()
    
    print(f"Saved trade-off plot: {save_path}FIGURE_accuracy_consistency_tradeoff.png")

# Create plot
create_tradeoff_plot(move_summary)
```

### 7.4 Bland-Altman Plot (Run-to-Run Agreement)

```python
def create_bland_altman_plot(df, metric='move_accuracy', save_path='figures/'):
    """Create Bland-Altman plot for agreement analysis."""
    
    Path(save_path).mkdir(parents=True, exist_ok=True)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    axes = axes.flatten()
    
    for idx, condition in enumerate(df['condition'].unique()):
        ax = axes[idx]
        
        # Get data for this condition
        cond_data = df[df['condition'] == condition][metric].values
        
        # Calculate differences and means for consecutive runs
        differences = []
        means = []
        
        for i in range(len(cond_data) - 1):
            diff = cond_data[i+1] - cond_data[i]
            mean = (cond_data[i+1] + cond_data[i]) / 2
            differences.append(diff)
            means.append(mean)
        
        # Plot
        ax.scatter(means, differences, alpha=0.5, s=30)
        
        # Add mean difference line
        mean_diff = np.mean(differences)
        ax.axhline(mean_diff, color='red', linestyle='-', linewidth=2, label=f'Mean diff: {mean_diff:.2f}')
        
        # Add limits of agreement (±1.96 SD)
        std_diff = np.std(differences)
        upper_loa = mean_diff + 1.96 * std_diff
        lower_loa = mean_diff - 1.96 * std_diff
        ax.axhline(upper_loa, color='gray', linestyle='--', linewidth=1, label='95% LOA')
        ax.axhline(lower_loa, color='gray', linestyle='--', linewidth=1)
        
        # Formatting
        ax.set_xlabel('Mean of Two Runs', fontsize=10)
        ax.set_ylabel('Difference Between Runs', fontsize=10)
        ax.set_title(condition, fontsize=11, fontweight='bold')
        ax.legend(loc='upper right', fontsize=8)
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{save_path}FIGURE_bland_altman_{metric}.png', dpi=300)
    plt.close()
    
    print(f"Saved Bland-Altman plot: {save_path}FIGURE_bland_altman_{metric}.png")

# Create plot
create_bland_altman_plot(df, 'move_accuracy')
```

---

## Phase 8: Results Reporting

### 8.1 Generate Summary Report

```python
def generate_summary_report(df, move_summary, step_summary, 
                           levene_move, pairwise_move,
                           output_file='results/SUMMARY_REPORT.txt'):
    """Generate comprehensive text summary of all analyses."""
    
    with open(output_file, 'w') as f:
        f.write("="*70 + "\n")
        f.write("STATISTICAL ANALYSIS SUMMARY REPORT\n")
        f.write("LLM Consistency in Rhetorical Move-Step Annotation\n")
        f.write("="*70 + "\n\n")
        
        # Sample size
        f.write("SAMPLE SIZE\n")
        f.write("-"*70 + "\n")
        for condition in df['condition'].unique():
            n = len(df[df['condition'] == condition])
            f.write(f"{condition}: {n} runs\n")
        f.write(f"\nTotal observations: {len(df)}\n\n")
        
        # Descriptive statistics
        f.write("DESCRIPTIVE STATISTICS - MOVE ACCURACY\n")
        f.write("-"*70 + "\n")
        f.write(move_summary.to_string(index=False))
        f.write("\n\n")
        
        f.write("DESCRIPTIVE STATISTICS - STEP ACCURACY\n")
        f.write("-"*70 + "\n")
        f.write(step_summary.to_string(index=False))
        f.write("\n\n")
        
        # Variance comparison
        f.write("VARIANCE COMPARISON (Levene's Test)\n")
        f.write("-"*70 + "\n")
        f.write(f"Move Accuracy: F = {levene_move['statistic']:.4f}, p = {levene_move['p_value']:.4f}\n")
        if levene_move['p_value'] < 0.05:
            f.write("  → SIGNIFICANT difference in consistency detected\n")
        else:
            f.write("  → No significant difference in consistency\n")
        f.write("\n")
        
        # Pairwise comparisons
        f.write("PAIRWISE VARIANCE COMPARISONS\n")
        f.write("-"*70 + "\n")
        f.write(pairwise_move[['condition_1', 'condition_2', 'var_ratio', 'p_value', 'significant']].to_string(index=False))
        f.write("\n\n")
        
        # Key findings
        f.write("KEY FINDINGS\n")
        f.write("-"*70 + "\n")
        
        # Most accurate
        best_accuracy = move_summary.loc[move_summary['mean'].idxmax()]
        f.write(f"1. Highest mean accuracy: {best_accuracy['condition']} ({best_accuracy['mean']:.1f}%)\n")
        
        # Most consistent
        best_consistency = move_summary.loc[move_summary['cv'].idxmin()]
        f.write(f"2. Best consistency (lowest CV): {best_consistency['condition']} (CV = {best_consistency['cv']:.1f}%)\n")
        
        # Worst consistency
        worst_consistency = move_summary.loc[move_summary['cv'].idxmax()]
        f.write(f"3. Worst consistency (highest CV): {worst_consistency['condition']} (CV = {worst_consistency['cv']:.1f}%)\n")
        
        f.write("\n" + "="*70 + "\n")
    
    print(f"Summary report saved to: {output_file}")

# Generate report
generate_summary_report(df, move_summary, step_summary, 
                       levene_move, pairwise_move)
```

---

## Phase 9: Complete Analysis Pipeline

### Master Script: `run_statistical_analysis.py`

```python
"""
Master Statistical Analysis Script
Run this after collecting all 124 evaluation results.
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Import all analysis functions defined above
# (or copy them into this file)

def main():
    """Run complete statistical analysis pipeline."""
    
    print("="*70)
    print("STARTING STATISTICAL ANALYSIS PIPELINE")
    print("="*70)
    
    # Create output directories
    Path('results').mkdir(exist_ok=True)
    Path('figures').mkdir(exist_ok=True)
    
    # 1. Load data
    print("\n[1/9] Loading data...")
    df = load_all_results()
    print(f"  Loaded {len(df)} observations")
    
    # 2. Descriptive statistics
    print("\n[2/9] Calculating descriptive statistics...")
    move_summary = calculate_summary_stats(df, 'move_accuracy')
    step_summary = calculate_summary_stats(df, 'step_accuracy')
    
    # 3. Normality tests
    print("\n[3/9] Testing normality assumptions...")
    norm_move = test_normality(df, 'move_accuracy')
    norm_step = test_normality(df, 'step_accuracy')
    plot_distributions(df, 'move_accuracy')
    plot_distributions(df, 'step_accuracy')
    
    # 4. Variance comparison
    print("\n[4/9] Comparing variance across conditions...")
    levene_move = levenes_test(df, 'move_accuracy')
    levene_step = levenes_test(df, 'step_accuracy')
    
    # 5. Pairwise variance tests
    print("\n[5/9] Running pairwise variance comparisons...")
    pairwise_var_move = pairwise_variance_tests(df, 'move_accuracy')
    pairwise_var_step = pairwise_variance_tests(df, 'step_accuracy')
    
    # 6. Mean comparisons
    print("\n[6/9] Comparing mean accuracy...")
    anova_move = anova_test(df, 'move_accuracy')
    anova_step = anova_test(df, 'step_accuracy')
    pairwise_means_move = pairwise_mean_tests(df, 'move_accuracy')
    pairwise_means_step = pairwise_mean_tests(df, 'step_accuracy')
    
    # 7. Reliability analysis
    print("\n[7/9] Calculating ICC...")
    icc_move = calculate_icc(df, 'move_accuracy')
    icc_step = calculate_icc(df, 'step_accuracy')
    
    # 8. Visualizations
    print("\n[8/9] Creating visualizations...")
    create_distribution_plot(df, 'move_accuracy')
    create_distribution_plot(df, 'step_accuracy')
    create_consistency_plot(move_summary, step_summary)
    create_tradeoff_plot(move_summary)
    create_bland_altman_plot(df, 'move_accuracy')
    
    # 9. Summary report
    print("\n[9/9] Generating summary report...")
    generate_summary_report(df, move_summary, step_summary,
                           levene_move, pairwise_var_move)
    
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE")
    print("="*70)
    print(f"\nResults saved to:")
    print(f"  - CSV files: results/")
    print(f"  - Figures: figures/")
    print(f"  - Summary: results/SUMMARY_REPORT.txt")

if __name__ == "__main__":
    main()
```

---

## Phase 10: Interpretation Guide for Paper

### How to Report Results

**For Descriptive Statistics:**
```
Move-level accuracy ranged from M = 52.7% (SD = 3.2%, CV = 6.1%) 
in the zero-shot condition to M = 92.3% (SD = 0.9%, CV = 1.0%) 
in the fine-tuned condition (see Table 1).
```

**For Variance Comparison:**
```
Levene's test revealed significant differences in consistency across 
conditions, F(3, 116) = 15.43, p < .001. Pairwise comparisons with 
Bonferroni correction (α = .0083) showed that the fine-tuned model 
exhibited significantly lower variance than all other conditions 
(all ps < .001), with variance ratios ranging from 0.08 to 0.12 
(i.e., fine-tuned variance was 88-92% lower than other conditions).
```

**For ICC:**
```
Intraclass correlation coefficients indicated excellent consistency 
for the fine-tuned model (ICC = .94) and moderate consistency for 
zero-shot (ICC = .68) and few-shot conditions (ICC = .72-.75).
```

**For Key Finding:**
```
While fine-tuning achieved the highest mean accuracy (92.3%), it also 
demonstrated the best consistency (CV = 1.0%), suggesting that fine-
tuning improves both accuracy and reliability. In contrast, zero-shot 
annotation showed high variability (CV = 6.1%), making it less suitable 
for practical deployment despite reasonable mean accuracy (52.7%).
```

---

## Troubleshooting Common Issues

### Issue 1: Data Not Normally Distributed

**Solution:** Use non-parametric alternatives
```python
# Instead of ANOVA, use Kruskal-Wallis
from scipy.stats import kruskal
h_stat, p_value = kruskal(*groups)

# Instead of t-test, use Mann-Whitney U
from scipy.stats import mannwhitneyu
u_stat, p_value = mannwhitneyu(data1, data2)
```

### Issue 2: Unequal Sample Sizes

**Solution:** This shouldn't happen in your design (30 runs per condition), but if it does:
```python
# Use Welch's t-test instead of standard t-test
from scipy.stats import ttest_ind
t_stat, p_value = ttest_ind(data1, data2, equal_var=False)  # Welch's t-test
```

### Issue 3: Missing Data

**Solution:**
```python
# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values (only if minimal)
df_clean = df.dropna()

# Or impute with mean (not recommended for accuracy data)
df['move_accuracy'].fillna(df['move_accuracy'].mean(), inplace=True)
```

---

## Checklist Before Submission

- [ ] All 124 evaluation files collected
- [ ] Consolidated CSV created
- [ ] Descriptive statistics calculated for all conditions
- [ ] Normality assumptions checked
- [ ] Levene's test completed
- [ ] Pairwise variance tests with Bonferroni correction
- [ ] Mean comparisons (ANOVA + post-hoc)
- [ ] ICC calculated
- [ ] All visualizations created (5+ figures)
- [ ] Summary report generated
- [ ] Results tables formatted for paper
- [ ] Statistical notation checked (italicized p, F, t, etc.)
- [ ] Effect sizes reported
- [ ] 95% CIs reported
- [ ] All analyses reproducible from saved code

---

## Key Statistical Concepts Explained

### Coefficient of Variation (CV)
- **What:** SD / Mean × 100%
- **Why:** Allows comparison of variability across different scales
- **Interpretation:** Lower CV = more consistent

### Levene's Test
- **What:** Tests if variances are equal
- **Why:** Tells us if consistency differs across conditions
- **Interpretation:** p < .05 means at least one condition has different variance

### Bonferroni Correction
- **What:** Adjusts α for multiple comparisons (α / n_tests)
- **Why:** Prevents inflated Type I error from multiple tests
- **Interpretation:** Use corrected α as threshold for significance

### ICC (Intraclass Correlation)
- **What:** Measures reliability/agreement across repeated measures
- **Why:** Standard metric for consistency assessment
- **Interpretation:** 
  - < 0.5 = poor
  - 0.5-0.75 = moderate
  - 0.75-0.9 = good
  - > 0.9 = excellent

### Cohen's d
- **What:** Standardized mean difference
- **Why:** Effect size independent of sample size
- **Interpretation:**
  - 0.2 = small
  - 0.5 = medium
  - 0.8 = large

---

**This plan provides everything you need to conduct rigorous statistical analysis. Work through each phase sequentially, and save all outputs for your paper.**
