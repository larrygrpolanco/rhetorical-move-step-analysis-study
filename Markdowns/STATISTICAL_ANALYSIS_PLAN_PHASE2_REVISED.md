# Statistical Analysis Plan - Phase 2 (Revised)
## Zero-Shot vs Fine-Tuned Consistency Comparison

**Purpose:** Systematic comparison of annotation consistency between zero-shot and fine-tuned approaches  
**Design:** 50 runs per condition on test set (10 articles, ~267 sentences)  
**Conditions:** Zero-shot (A1) vs Fine-tuned (A4)  
**Total Runs:** 100

---

## Analysis Structure

```
Phase 2 Analysis
├── 1. Data Loading and Preparation
│   ├── Load 50 zero-shot runs (test set)
│   ├── Load 50 fine-tuned runs (test set)
│   └── Create consolidated dataset
├── 2. Within-Condition Analysis
│   ├── Zero-shot descriptive statistics
│   ├── Fine-tuned descriptive statistics
│   ├── Distribution assessment (both conditions)
│   └── ICC calculation (both conditions)
├── 3. Between-Condition Comparison
│   ├── Variance comparison (Levene's test)
│   ├── Accuracy comparison (Welch's t-test)
│   ├── ICC comparison
│   └── Effect sizes
├── 4. Sentence-Level Analysis
│   ├── Agreement rates per sentence (both conditions)
│   ├── Entropy analysis (both conditions)
│   ├── Modal predictions (both conditions)
│   └── Cross-condition comparison
├── 5. Stratified Analysis
│   ├── Consistency by move type (M1, M2, M3)
│   ├── Consistency by step type (11 categories)
│   └── ANOVA for category differences
└── 6. Visualization and Reporting
    ├── Distribution plots
    ├── Comparison visualizations
    ├── Sentence-level heatmaps
    └── Summary tables
```

---

## Required Python Packages

```python
# Core data manipulation
import pandas as pd
import numpy as np
from pathlib import Path
import json

# Statistical tests
from scipy import stats
from scipy.stats import (
    shapiro,          # Normality test
    levene,           # Variance equality test
    ttest_ind,        # Independent samples t-test (Welch's)
    f_oneway,         # One-way ANOVA
    entropy,          # Shannon entropy
)

# Effect sizes and reliability
from pingouin import (
    intraclass_corr,  # ICC calculation
    compute_effsize,  # Cohen's d
)

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 120)
plt.style.use('seaborn-v0_8-paper')
```

---

## Part 1: Data Loading and Preparation

### 1.1 Load Zero-Shot Results (50 Runs)

```python
def load_condition_results(condition='zero_shot', dataset='test', research_question='rq2'):
    """
    Load all 50 evaluation results for a specific condition.
    
    Args:
        condition: 'zero_shot' or 'fine_tuned'
        dataset: 'test' (always test for Phase 2)
        research_question: 'rq2'
    
    Returns:
        DataFrame with one row per run
    """
    results = []
    results_dir = Path('evaluation_results')
    
    # Pattern: {condition}_rq2_test_run_01.json through run_50.json
    for run_num in range(1, 51):
        json_file = results_dir / f"{condition}_{research_question}_{dataset}_run_{run_num:02d}.json"
        
        if not json_file.exists():
            print(f"⚠️  Warning: Missing {json_file}")
            continue
            
        with open(json_file) as f:
            data = json.load(f)
        
        result_row = {
            'condition': condition,
            'run_number': run_num,
            'move_accuracy': data['move_metrics']['accuracy'],
            'step_accuracy': data['step_metrics']['accuracy'],
            'move_f1': data['move_metrics']['weighted_f1'],
            'step_f1': data['step_metrics']['weighted_f1'],
            'move_precision': data['move_metrics']['weighted_precision'],
            'move_recall': data['move_metrics']['weighted_recall'],
            'step_precision': data['step_metrics']['weighted_precision'],
            'step_recall': data['step_metrics']['weighted_recall'],
            'total_sentences': data['total_sentences'],
            'total_articles': len(data.get('per_article_metrics', [])),
        }
        results.append(result_row)
    
    df = pd.DataFrame(results)
    print(f"✓ Loaded {len(df)} runs for {condition} ({dataset} set)")
    
    return df

# Load both conditions
print("=" * 70)
print("LOADING PHASE 2 DATA")
print("=" * 70)
print()

df_zero_shot = load_condition_results(condition='zero_shot', dataset='test', research_question='rq2')
df_fine_tuned = load_condition_results(condition='fine_tuned', dataset='test', research_question='rq2')

# Combine for some analyses
df_combined = pd.concat([df_zero_shot, df_fine_tuned], ignore_index=True)

# Save consolidated data
output_dir = Path('evaluation_results')
df_zero_shot.to_csv(output_dir / 'zero_shot_test_consolidated_rq2.csv', index=False)
df_fine_tuned.to_csv(output_dir / 'fine_tuned_test_consolidated_rq2.csv', index=False)
df_combined.to_csv(output_dir / 'combined_test_consolidated_rq2.csv', index=False)

print()
print("Dataset Summary:")
print(f"  Test set: {df_zero_shot['total_sentences'].iloc[0]} sentences")
print(f"  Zero-shot runs: {len(df_zero_shot)}")
print(f"  Fine-tuned runs: {len(df_fine_tuned)}")
print(f"  Total observations per condition: {df_zero_shot['total_sentences'].iloc[0] * 50}")
print()
```

---

## Part 2: Within-Condition Analysis

### 2.1 Descriptive Statistics

```python
def calculate_consistency_metrics(df, metric='move_accuracy', condition_name=''):
    """
    Calculate comprehensive consistency metrics for a single condition.
    
    Returns:
        Dictionary with all consistency metrics
    """
    data = df[metric].values
    
    metrics = {
        'condition': condition_name,
        'n_runs': len(data),
        'mean': np.mean(data),
        'sd': np.std(data, ddof=1),
        'median': np.median(data),
        'min': np.min(data),
        'max': np.max(data),
        'range': np.max(data) - np.min(data),
        'q25': np.percentile(data, 25),
        'q75': np.percentile(data, 75),
        'iqr': np.percentile(data, 75) - np.percentile(data, 25),
        'cv': (np.std(data, ddof=1) / np.mean(data)) * 100,  # Coefficient of variation (%)
    }
    
    # 95% Confidence interval for mean
    ci = stats.t.interval(
        0.95, 
        len(data)-1,
        loc=np.mean(data),
        scale=stats.sem(data)
    )
    metrics['ci_lower'] = ci[0]
    metrics['ci_upper'] = ci[1]
    metrics['ci_width'] = ci[1] - ci[0]
    
    return metrics

print("=" * 70)
print("WITHIN-CONDITION DESCRIPTIVE STATISTICS")
print("=" * 70)
print()

# Calculate for both conditions, both levels
zs_move = calculate_consistency_metrics(df_zero_shot, 'move_accuracy', 'Zero-shot')
ft_move = calculate_consistency_metrics(df_fine_tuned, 'move_accuracy', 'Fine-tuned')

zs_step = calculate_consistency_metrics(df_zero_shot, 'step_accuracy', 'Zero-shot')
ft_step = calculate_consistency_metrics(df_fine_tuned, 'step_accuracy', 'Fine-tuned')

# Print move-level results
print("MOVE-LEVEL ACCURACY")
print("-" * 70)
print()
print("Zero-Shot:")
print(f"  Mean: {zs_move['mean']:.1%} ± {zs_move['sd']:.2%}")
print(f"  95% CI: [{zs_move['ci_lower']:.1%}, {zs_move['ci_upper']:.1%}]")
print(f"  CV: {zs_move['cv']:.2f}%")
print(f"  Range: [{zs_move['min']:.1%}, {zs_move['max']:.1%}] (span: {zs_move['range']:.2%})")
print(f"  IQR: {zs_move['iqr']:.2%}")
print()
print("Fine-Tuned:")
print(f"  Mean: {ft_move['mean']:.1%} ± {ft_move['sd']:.2%}")
print(f"  95% CI: [{ft_move['ci_lower']:.1%}, {ft_move['ci_upper']:.1%}]")
print(f"  CV: {ft_move['cv']:.2f}%")
print(f"  Range: [{ft_move['min']:.1%}, {ft_move['max']:.1%}] (span: {ft_move['range']:.2%})")
print(f"  IQR: {ft_move['iqr']:.2%}")
print()

# Print step-level results
print("STEP-LEVEL ACCURACY")
print("-" * 70)
print()
print("Zero-Shot:")
print(f"  Mean: {zs_step['mean']:.1%} ± {zs_step['sd']:.2%}")
print(f"  CV: {zs_step['cv']:.2f}%")
print()
print("Fine-Tuned:")
print(f"  Mean: {ft_step['mean']:.1%} ± {ft_step['sd']:.2%}")
print(f"  CV: {ft_step['cv']:.2f}%")
print()

# Save summary table
summary_df = pd.DataFrame([zs_move, ft_move, zs_step, ft_step])
summary_df['level'] = ['move', 'move', 'step', 'step']
summary_df = summary_df[['condition', 'level', 'n_runs', 'mean', 'sd', 'cv', 'ci_lower', 'ci_upper', 
                          'min', 'max', 'range', 'median', 'iqr']]
summary_df.to_csv(output_dir / 'consistency_summary.csv', index=False)
print("✓ Saved: consistency_summary.csv")
print()
```

### 2.2 Distribution Assessment

```python
def assess_distribution(df, metric='move_accuracy', condition_name=''):
    """
    Test normality and visualize distribution.
    """
    data = df[metric].values
    
    # Shapiro-Wilk test for normality
    stat, p_value = shapiro(data)
    
    print(f"{condition_name} - {metric}:")
    print(f"  Shapiro-Wilk: W = {stat:.4f}, p = {p_value:.4f}")
    if p_value > 0.05:
        print(f"  ✓ Distribution is approximately normal (p > 0.05)")
    else:
        print(f"  ⚠️  Distribution deviates from normality (p < 0.05)")
    print()
    
    return {'condition': condition_name, 'metric': metric, 'W': stat, 'p_value': p_value}

print("=" * 70)
print("DISTRIBUTION ASSESSMENT (NORMALITY TESTS)")
print("=" * 70)
print()

normality_results = []
normality_results.append(assess_distribution(df_zero_shot, 'move_accuracy', 'Zero-shot'))
normality_results.append(assess_distribution(df_fine_tuned, 'move_accuracy', 'Fine-tuned'))
normality_results.append(assess_distribution(df_zero_shot, 'step_accuracy', 'Zero-shot'))
normality_results.append(assess_distribution(df_fine_tuned, 'step_accuracy', 'Fine-tuned'))

normality_df = pd.DataFrame(normality_results)
normality_df.to_csv(output_dir / 'normality_tests.csv', index=False)
print("✓ Saved: normality_tests.csv")
print()
```

### 2.3 Intraclass Correlation Coefficient (ICC)

```python
def calculate_icc(condition='zero_shot', dataset='test', level='move'):
    """
    Calculate ICC(2,1) for annotation consistency.
    
    ICC(2,1) = Two-way random effects, single rater, absolute agreement
    Measures: Consistency of annotations across runs
    """
    results_dir = Path('evaluation_results')
    
    # Load sentence-level predictions for all runs
    sentence_data = []
    
    for run_num in range(1, 51):
        json_file = results_dir / f"{condition}_rq2_{dataset}_run_{run_num:02d}.json"
        
        if not json_file.exists():
            continue
            
        with open(json_file) as f:
            data = json.load(f)
        
        # Extract sentence-level results
        for sent_idx, sent in enumerate(data['sentences']):
            if level == 'move':
                predicted = sent['predicted_move']
                gold = sent['gold_move']
            else:  # step
                predicted = sent['predicted_step']
                gold = sent['gold_step']
            
            sentence_data.append({
                'sentence_id': sent_idx,
                'run': run_num,
                'correct': 1 if predicted == gold else 0
            })
    
    df_sentences = pd.DataFrame(sentence_data)
    
    # Reshape for ICC: rows = sentences, columns = runs
    df_wide = df_sentences.pivot(index='sentence_id', columns='run', values='correct')
    
    # Calculate ICC using pingouin
    icc_result = intraclass_corr(
        data=df_sentences, 
        targets='sentence_id', 
        raters='run', 
        ratings='correct',
        nan_policy='omit'
    )
    
    # Extract ICC(2,1) - two-way random, single rater
    icc_2_1 = icc_result[icc_result['Type'] == 'ICC2']['ICC'].values[0]
    icc_ci_lower = icc_result[icc_result['Type'] == 'ICC2']['CI95%'].values[0][0]
    icc_ci_upper = icc_result[icc_result['Type'] == 'ICC2']['CI95%'].values[0][1]
    
    return {
        'condition': condition,
        'level': level,
        'icc': icc_2_1,
        'ci_lower': icc_ci_lower,
        'ci_upper': icc_ci_upper,
        'n_sentences': len(df_wide),
        'n_runs': 50
    }

print("=" * 70)
print("INTRACLASS CORRELATION COEFFICIENT (ICC)")
print("=" * 70)
print()

icc_results = []

print("Calculating ICC(2,1)...")
print()

# Move-level ICC
zs_icc_move = calculate_icc('zero_shot', 'test', 'move')
ft_icc_move = calculate_icc('fine_tuned', 'test', 'move')

print("Move-Level ICC:")
print(f"  Zero-shot: ICC(2,1) = {zs_icc_move['icc']:.3f} [95% CI: {zs_icc_move['ci_lower']:.3f}, {zs_icc_move['ci_upper']:.3f}]")
print(f"  Fine-tuned: ICC(2,1) = {ft_icc_move['icc']:.3f} [95% CI: {ft_icc_move['ci_lower']:.3f}, {ft_icc_move['ci_upper']:.3f}]")
print()

# Step-level ICC
zs_icc_step = calculate_icc('zero_shot', 'test', 'step')
ft_icc_step = calculate_icc('fine_tuned', 'test', 'step')

print("Step-Level ICC:")
print(f"  Zero-shot: ICC(2,1) = {zs_icc_step['icc']:.3f} [95% CI: {zs_icc_step['ci_lower']:.3f}, {zs_icc_step['ci_upper']:.3f}]")
print(f"  Fine-tuned: ICC(2,1) = {ft_icc_step['icc']:.3f} [95% CI: {ft_icc_step['ci_lower']:.3f}, {ft_icc_step['ci_upper']:.3f}]")
print()

# Interpretation guide
def interpret_icc(icc_value):
    if icc_value < 0.5:
        return "Poor"
    elif icc_value < 0.75:
        return "Moderate"
    elif icc_value < 0.9:
        return "Good"
    else:
        return "Excellent"

print("Interpretation (Koo & Li, 2016):")
print(f"  Zero-shot move: {interpret_icc(zs_icc_move['icc'])}")
print(f"  Fine-tuned move: {interpret_icc(ft_icc_move['icc'])}")
print(f"  Zero-shot step: {interpret_icc(zs_icc_step['icc'])}")
print(f"  Fine-tuned step: {interpret_icc(ft_icc_step['icc'])}")
print()

# Save ICC results
icc_df = pd.DataFrame([zs_icc_move, ft_icc_move, zs_icc_step, ft_icc_step])
icc_df.to_csv(output_dir / 'icc_results.csv', index=False)
print("✓ Saved: icc_results.csv")
print()
```

---

## Part 3: Between-Condition Comparison

### 3.1 Variance Comparison (Levene's Test)

```python
print("=" * 70)
print("BETWEEN-CONDITION COMPARISON")
print("=" * 70)
print()

print("3.1 VARIANCE COMPARISON (Levene's Test)")
print("-" * 70)
print()

def compare_variance(df1, df2, metric='move_accuracy', name1='Zero-shot', name2='Fine-tuned'):
    """
    Test if two conditions have equal variance using Levene's test.
    H₀: σ₁² = σ₂²
    """
    data1 = df1[metric].values
    data2 = df2[metric].values
    
    # Levene's test (center='median' is more robust)
    stat, p_value = levene(data1, data2, center='median')
    
    # Variance ratio
    var1 = np.var(data1, ddof=1)
    var2 = np.var(data2, ddof=1)
    var_ratio = var1 / var2
    
    print(f"{metric}:")
    print(f"  {name1} variance: {var1:.6f}")
    print(f"  {name2} variance: {var2:.6f}")
    print(f"  Variance ratio ({name1}/{name2}): {var_ratio:.3f}")
    print(f"  Levene's test: F = {stat:.3f}, p = {p_value:.4f}")
    
    if p_value < 0.05:
        print(f"  ✓ Significant difference in variance (p < 0.05)")
        if var_ratio > 1:
            print(f"    → {name1} has {var_ratio:.1f}× more variance")
        else:
            print(f"    → {name2} has {1/var_ratio:.1f}× more variance")
    else:
        print(f"  ✗ No significant difference in variance (p ≥ 0.05)")
    print()
    
    return {
        'metric': metric,
        'var1': var1,
        'var2': var2,
        'var_ratio': var_ratio,
        'levene_F': stat,
        'p_value': p_value,
        'significant': p_value < 0.05
    }

variance_results = []
variance_results.append(compare_variance(df_zero_shot, df_fine_tuned, 'move_accuracy'))
variance_results.append(compare_variance(df_zero_shot, df_fine_tuned, 'step_accuracy'))

variance_df = pd.DataFrame(variance_results)
variance_df.to_csv(output_dir / 'variance_comparison.csv', index=False)
print("✓ Saved: variance_comparison.csv")
print()
```

### 3.2 Accuracy Comparison (Welch's t-test)

```python
print("3.2 ACCURACY COMPARISON (Welch's t-test)")
print("-" * 70)
print()

def compare_means(df1, df2, metric='move_accuracy', name1='Zero-shot', name2='Fine-tuned'):
    """
    Test if two conditions have different mean accuracy using Welch's t-test.
    (Does not assume equal variances)
    """
    data1 = df1[metric].values
    data2 = df2[metric].values
    
    # Welch's t-test (unequal variances)
    t_stat, p_value = ttest_ind(data1, data2, equal_var=False)
    
    mean1 = np.mean(data1)
    mean2 = np.mean(data2)
    mean_diff = mean1 - mean2
    
    # Cohen's d effect size
    # Using pooled SD despite unequal variances for interpretability
    pooled_sd = np.sqrt((np.var(data1, ddof=1) + np.var(data2, ddof=1)) / 2)
    cohens_d = mean_diff / pooled_sd
    
    # 95% CI for mean difference
    se_diff = np.sqrt(stats.sem(data1)**2 + stats.sem(data2)**2)
    df_welch = len(data1) + len(data2) - 2  # Approximate
    ci_diff = stats.t.interval(0.95, df_welch, loc=mean_diff, scale=se_diff)
    
    print(f"{metric}:")
    print(f"  {name1} mean: {mean1:.1%}")
    print(f"  {name2} mean: {mean2:.1%}")
    print(f"  Mean difference: {mean_diff:.2%} ({name1} - {name2})")
    print(f"  95% CI: [{ci_diff[0]:.2%}, {ci_diff[1]:.2%}]")
    print(f"  Welch's t-test: t = {t_stat:.3f}, p = {p_value:.4f}")
    print(f"  Cohen's d: {cohens_d:.3f}")
    
    if p_value < 0.05:
        print(f"  ✓ Significant difference in mean accuracy (p < 0.05)")
        if mean_diff > 0:
            print(f"    → {name1} is {mean_diff*100:.1f} percentage points higher")
        else:
            print(f"    → {name2} is {abs(mean_diff)*100:.1f} percentage points higher")
    else:
        print(f"  ✗ No significant difference in mean accuracy (p ≥ 0.05)")
    
    # Effect size interpretation
    def interpret_cohens_d(d):
        abs_d = abs(d)
        if abs_d < 0.2:
            return "negligible"
        elif abs_d < 0.5:
            return "small"
        elif abs_d < 0.8:
            return "medium"
        else:
            return "large"
    
    print(f"  Effect size: {interpret_cohens_d(cohens_d)}")
    print()
    
    return {
        'metric': metric,
        'mean1': mean1,
        'mean2': mean2,
        'mean_diff': mean_diff,
        'ci_lower': ci_diff[0],
        'ci_upper': ci_diff[1],
        't_stat': t_stat,
        'p_value': p_value,
        'cohens_d': cohens_d,
        'significant': p_value < 0.05
    }

mean_results = []
mean_results.append(compare_means(df_zero_shot, df_fine_tuned, 'move_accuracy'))
mean_results.append(compare_means(df_zero_shot, df_fine_tuned, 'step_accuracy'))

mean_df = pd.DataFrame(mean_results)
mean_df.to_csv(output_dir / 'mean_comparison.csv', index=False)
print("✓ Saved: mean_comparison.csv")
print()
```

### 3.3 Summary Comparison Table

```python
print("3.3 COMPREHENSIVE COMPARISON SUMMARY")
print("-" * 70)
print()

# Create publication-ready comparison table
comparison_table = pd.DataFrame({
    'Metric': ['Move Accuracy', 'Step Accuracy'],
    'Zero-shot Mean (SD)': [
        f"{zs_move['mean']:.1%} ({zs_move['sd']:.2%})",
        f"{zs_step['mean']:.1%} ({zs_step['sd']:.2%})"
    ],
    'Fine-tuned Mean (SD)': [
        f"{ft_move['mean']:.1%} ({ft_move['sd']:.2%})",
        f"{ft_step['mean']:.1%} ({ft_step['sd']:.2%})"
    ],
    'Zero-shot CV': [
        f"{zs_move['cv']:.2f}%",
        f"{zs_step['cv']:.2f}%"
    ],
    'Fine-tuned CV': [
        f"{ft_move['cv']:.2f}%",
        f"{ft_step['cv']:.2f}%"
    ],
    'Zero-shot ICC': [
        f"{zs_icc_move['icc']:.3f}",
        f"{zs_icc_step['icc']:.3f}"
    ],
    'Fine-tuned ICC': [
        f"{ft_icc_move['icc']:.3f}",
        f"{ft_icc_step['icc']:.3f}"
    ],
    'Mean Diff (p)': [
        f"{mean_results[0]['mean_diff']:.2%} ({mean_results[0]['p_value']:.3f})",
        f"{mean_results[1]['mean_diff']:.2%} ({mean_results[1]['p_value']:.3f})"
    ],
    'Variance Ratio (p)': [
        f"{variance_results[0]['var_ratio']:.2f} ({variance_results[0]['p_value']:.3f})",
        f"{variance_results[1]['var_ratio']:.2f} ({variance_results[1]['p_value']:.3f})"
    ]
})

print(comparison_table.to_string(index=False))
print()

comparison_table.to_csv(output_dir / 'comprehensive_comparison.csv', index=False)
print("✓ Saved: comprehensive_comparison.csv")
print()
```

---

## Part 4: Sentence-Level Analysis

### 4.1 Agreement Rate Analysis

```python
print("=" * 70)
print("SENTENCE-LEVEL ANALYSIS")
print("=" * 70)
print()

def analyze_sentence_level_consistency(condition='zero_shot', dataset='test', level='move'):
    """
    Calculate agreement rate, entropy, and modal prediction for each sentence.
    """
    results_dir = Path('evaluation_results')
    
    # Collect all predictions for each sentence across 50 runs
    sentence_predictions = {}
    gold_labels = {}
    
    for run_num in range(1, 51):
        json_file = results_dir / f"{condition}_rq2_{dataset}_run_{run_num:02d}.json"
        
        if not json_file.exists():
            continue
            
        with open(json_file) as f:
            data = json.load(f)
        
        for sent_idx, sent in enumerate(data['sentences']):
            if sent_idx not in sentence_predictions:
                sentence_predictions[sent_idx] = []
                gold_labels[sent_idx] = sent[f'gold_{level}']
            
            sentence_predictions[sent_idx].append(sent[f'predicted_{level}'])
    
    # Calculate metrics for each sentence
    sentence_metrics = []
    
    for sent_idx in sorted(sentence_predictions.keys()):
        predictions = sentence_predictions[sent_idx]
        gold = gold_labels[sent_idx]
        
        # Agreement rate: % correct predictions
        correct_count = sum(1 for pred in predictions if pred == gold)
        agreement_rate = correct_count / len(predictions)
        
        # Modal prediction
        from collections import Counter
        pred_counts = Counter(predictions)
        modal_pred = pred_counts.most_common(1)[0][0]
        modal_freq = pred_counts.most_common(1)[0][1] / len(predictions)
        
        # Entropy: uncertainty in predictions
        label_probs = np.array([count / len(predictions) for count in pred_counts.values()])
        pred_entropy = entropy(label_probs, base=2)
        
        # Flip frequency: how often label changes between consecutive runs
        flips = sum(1 for i in range(1, len(predictions)) if predictions[i] != predictions[i-1])
        flip_rate = flips / (len(predictions) - 1)
        
        sentence_metrics.append({
            'sentence_id': sent_idx,
            'gold_label': gold,
            'agreement_rate': agreement_rate,
            'n_correct': correct_count,
            'n_runs': len(predictions),
            'modal_prediction': modal_pred,
            'modal_frequency': modal_freq,
            'entropy': pred_entropy,
            'flip_rate': flip_rate,
            'modal_is_correct': modal_pred == gold
        })
    
    df_sentences = pd.DataFrame(sentence_metrics)
    
    # Categorize sentences by agreement
    df_sentences['consistency_category'] = pd.cut(
        df_sentences['agreement_rate'],
        bins=[0, 0.3, 0.7, 0.9, 1.0],
        labels=['Problematic (<30%)', 'Uncertain (30-70%)', 'Moderate (70-90%)', 'High (>90%)'],
        include_lowest=True
    )
    
    return df_sentences

print("Analyzing sentence-level consistency...")
print()

# Analyze both conditions
df_sent_zs_move = analyze_sentence_level_consistency('zero_shot', 'test', 'move')
df_sent_ft_move = analyze_sentence_level_consistency('fine_tuned', 'test', 'move')

df_sent_zs_step = analyze_sentence_level_consistency('zero_shot', 'test', 'step')
df_sent_ft_step = analyze_sentence_level_consistency('fine_tuned', 'test', 'step')

# Save detailed results
df_sent_zs_move.to_csv(output_dir / 'sentence_consistency_zero_shot_move.csv', index=False)
df_sent_ft_move.to_csv(output_dir / 'sentence_consistency_fine_tuned_move.csv', index=False)
df_sent_zs_step.to_csv(output_dir / 'sentence_consistency_zero_shot_step.csv', index=False)
df_sent_ft_step.to_csv(output_dir / 'sentence_consistency_fine_tuned_step.csv', index=False)

print("✓ Saved: sentence_consistency_*.csv")
print()

# Summary statistics
print("MOVE-LEVEL SENTENCE CONSISTENCY SUMMARY")
print("-" * 70)
print()
print("Zero-Shot:")
print(df_sent_zs_move['consistency_category'].value_counts().sort_index())
print(f"  Mean agreement rate: {df_sent_zs_move['agreement_rate'].mean():.1%}")
print(f"  Median agreement rate: {df_sent_zs_move['agreement_rate'].median():.1%}")
print(f"  Mean entropy: {df_sent_zs_move['entropy'].mean():.3f} bits")
print()
print("Fine-Tuned:")
print(df_sent_ft_move['consistency_category'].value_counts().sort_index())
print(f"  Mean agreement rate: {df_sent_ft_move['agreement_rate'].mean():.1%}")
print(f"  Median agreement rate: {df_sent_ft_move['agreement_rate'].median():.1%}")
print(f"  Mean entropy: {df_sent_ft_move['entropy'].mean():.3f} bits")
print()
```

### 4.2 Cross-Condition Sentence Comparison

```python
print("4.2 CROSS-CONDITION SENTENCE COMPARISON")
print("-" * 70)
print()

# Merge sentence-level data
df_sent_comparison = df_sent_zs_move[['sentence_id', 'gold_label', 'agreement_rate', 'entropy']].copy()
df_sent_comparison.columns = ['sentence_id', 'gold_label', 'zs_agreement', 'zs_entropy']

df_sent_comparison = df_sent_comparison.merge(
    df_sent_ft_move[['sentence_id', 'agreement_rate', 'entropy']],
    on='sentence_id',
    suffixes=('', '_ft')
)
df_sent_comparison.columns = ['sentence_id', 'gold_label', 'zs_agreement', 'zs_entropy', 
                               'ft_agreement', 'ft_entropy']

# Calculate differences
df_sent_comparison['agreement_diff'] = df_sent_comparison['zs_agreement'] - df_sent_comparison['ft_agreement']
df_sent_comparison['entropy_diff'] = df_sent_comparison['zs_entropy'] - df_sent_comparison['ft_entropy']

# Identify sentence categories
df_sent_comparison['category'] = 'Both moderate'
df_sent_comparison.loc[
    (df_sent_comparison['zs_agreement'] > 0.9) & (df_sent_comparison['ft_agreement'] > 0.9),
    'category'
] = 'Both high'
df_sent_comparison.loc[
    (df_sent_comparison['zs_agreement'] < 0.7) & (df_sent_comparison['ft_agreement'] < 0.7),
    'category'
] = 'Both low'
df_sent_comparison.loc[
    (df_sent_comparison['zs_agreement'] > 0.9) & (df_sent_comparison['ft_agreement'] < 0.7),
    'category'
] = 'ZS better'
df_sent_comparison.loc[
    (df_sent_comparison['zs_agreement'] < 0.7) & (df_sent_comparison['ft_agreement'] > 0.9),
    'category'
] = 'FT better'

print("Sentence Category Distribution:")
print(df_sent_comparison['category'].value_counts())
print()

print("Summary Statistics:")
print(f"  Mean agreement difference (ZS - FT): {df_sent_comparison['agreement_diff'].mean():.2%}")
print(f"  Sentences where ZS > FT: {(df_sent_comparison['agreement_diff'] > 0).sum()}")
print(f"  Sentences where FT > ZS: {(df_sent_comparison['agreement_diff'] < 0).sum()}")
print()

df_sent_comparison.to_csv(output_dir / 'sentence_comparison_move.csv', index=False)
print("✓ Saved: sentence_comparison_move.csv")
print()
```

---

## Part 5: Stratified Analysis

### 5.1 Consistency by Move Type

```python
print("=" * 70)
print("STRATIFIED ANALYSIS BY MOVE TYPE")
print("=" * 70)
print()

def stratify_by_category(df_sentences, category_col='gold_label', condition_name=''):
    """
    Calculate consistency metrics stratified by category (move or step).
    """
    stratified = df_sentences.groupby(category_col).agg({
        'agreement_rate': ['mean', 'std', 'min', 'max', 'count'],
        'entropy': ['mean', 'std']
    }).reset_index()
    
    stratified.columns = [category_col, 'mean_agreement', 'sd_agreement', 'min_agreement', 
                         'max_agreement', 'n_sentences', 'mean_entropy', 'sd_entropy']
    
    stratified['cv_agreement'] = (stratified['sd_agreement'] / stratified['mean_agreement']) * 100
    stratified['condition'] = condition_name
    
    return stratified

# Stratify by move type
zs_by_move = stratify_by_category(df_sent_zs_move, 'gold_label', 'Zero-shot')
ft_by_move = stratify_by_category(df_sent_ft_move, 'gold_label', 'Fine-tuned')

print("ZERO-SHOT - Consistency by Move Type:")
print(zs_by_move[['gold_label', 'mean_agreement', 'cv_agreement', 'n_sentences']].to_string(index=False))
print()

print("FINE-TUNED - Consistency by Move Type:")
print(ft_by_move[['gold_label', 'mean_agreement', 'cv_agreement', 'n_sentences']].to_string(index=False))
print()

# Combine for comparison
move_comparison = zs_by_move.merge(
    ft_by_move[['gold_label', 'mean_agreement', 'cv_agreement']],
    on='gold_label',
    suffixes=('_zs', '_ft')
)

move_comparison.to_csv(output_dir / 'consistency_by_move.csv', index=False)
print("✓ Saved: consistency_by_move.csv")
print()
```

### 5.2 ANOVA: Do Moves Differ in Consistency?

```python
print("5.2 ANOVA: DO MOVES DIFFER IN CONSISTENCY?")
print("-" * 70)
print()

def test_category_differences(df_sentences, category_col='gold_label', condition_name=''):
    """
    Test if different categories (moves/steps) have different consistency using ANOVA.
    """
    # Group sentences by category
    groups = [group['agreement_rate'].values for name, group in df_sentences.groupby(category_col)]
    
    # One-way ANOVA
    f_stat, p_value = f_oneway(*groups)
    
    # Effect size (eta-squared)
    grand_mean = df_sentences['agreement_rate'].mean()
    ss_between = sum(len(group) * (group.mean() - grand_mean)**2 for group in groups)
    ss_total = sum((df_sentences['agreement_rate'] - grand_mean)**2)
    eta_squared = ss_between / ss_total
    
    print(f"{condition_name}:")
    print(f"  F({len(groups)-1}, {len(df_sentences)-len(groups)}) = {f_stat:.3f}, p = {p_value:.4f}")
    print(f"  η² = {eta_squared:.3f}")
    
    if p_value < 0.05:
        print(f"  ✓ Significant differences across {category_col}s (p < 0.05)")
    else:
        print(f"  ✗ No significant differences across {category_col}s (p ≥ 0.05)")
    print()
    
    return {
        'condition': condition_name,
        'category': category_col,
        'f_stat': f_stat,
        'p_value': p_value,
        'eta_squared': eta_squared,
        'df_between': len(groups) - 1,
        'df_within': len(df_sentences) - len(groups)
    }

anova_results = []
anova_results.append(test_category_differences(df_sent_zs_move, 'gold_label', 'Zero-shot'))
anova_results.append(test_category_differences(df_sent_ft_move, 'gold_label', 'Fine-tuned'))

anova_df = pd.DataFrame(anova_results)
anova_df.to_csv(output_dir / 'anova_by_move.csv', index=False)
print("✓ Saved: anova_by_move.csv")
print()
```

---

## Part 6: Visualization

### 6.1 Distribution Plots

```python
print("=" * 70)
print("CREATING VISUALIZATIONS")
print("=" * 70)
print()

import matplotlib.pyplot as plt
import seaborn as sns

figures_dir = Path('figures')
figures_dir.mkdir(exist_ok=True)

plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.size'] = 10

# Figure 1: Accuracy distribution across 50 runs
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Move-level
axes[0].violinplot([df_zero_shot['move_accuracy'], df_fine_tuned['move_accuracy']], 
                    positions=[1, 2], showmeans=True, showmedians=True)
axes[0].set_xticks([1, 2])
axes[0].set_xticklabels(['Zero-shot', 'Fine-tuned'])
axes[0].set_ylabel('Move-Level Accuracy')
axes[0].set_title('Move-Level Accuracy Distribution (50 Runs)')
axes[0].grid(axis='y', alpha=0.3)

# Step-level
axes[1].violinplot([df_zero_shot['step_accuracy'], df_fine_tuned['step_accuracy']], 
                    positions=[1, 2], showmeans=True, showmedians=True)
axes[1].set_xticks([1, 2])
axes[1].set_xticklabels(['Zero-shot', 'Fine-tuned'])
axes[1].set_ylabel('Step-Level Accuracy')
axes[1].set_title('Step-Level Accuracy Distribution (50 Runs)')
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig(figures_dir / 'accuracy_distributions.png')
plt.close()

print("✓ Saved: accuracy_distributions.png")
```

### 6.2 Coefficient of Variation Comparison

```python
# Figure 2: CV comparison
fig, ax = plt.subplots(figsize=(8, 6))

categories = ['Move', 'Step']
zs_cvs = [zs_move['cv'], zs_step['cv']]
ft_cvs = [ft_move['cv'], ft_step['cv']]

x = np.arange(len(categories))
width = 0.35

bars1 = ax.bar(x - width/2, zs_cvs, width, label='Zero-shot', alpha=0.8)
bars2 = ax.bar(x + width/2, ft_cvs, width, label='Fine-tuned', alpha=0.8)

ax.set_ylabel('Coefficient of Variation (%)')
ax.set_title('Consistency Comparison: Zero-shot vs Fine-tuned')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.grid(axis='y', alpha=0.3)

# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig(figures_dir / 'cv_comparison.png')
plt.close()

print("✓ Saved: cv_comparison.png")
```

### 6.3 Sentence-Level Heatmap

```python
# Figure 3: Sentence-level agreement heatmap
fig, axes = plt.subplots(1, 2, figsize=(14, 8))

# Zero-shot
sorted_zs = df_sent_zs_move.sort_values('agreement_rate', ascending=False)
axes[0].barh(range(len(sorted_zs)), sorted_zs['agreement_rate'], alpha=0.7)
axes[0].axvline(x=0.9, color='green', linestyle='--', alpha=0.5, label='High (>90%)')
axes[0].axvline(x=0.7, color='orange', linestyle='--', alpha=0.5, label='Moderate (>70%)')
axes[0].set_xlabel('Agreement Rate')
axes[0].set_ylabel('Sentence (sorted)')
axes[0].set_title('Zero-shot: Sentence-Level Consistency')
axes[0].legend()

# Fine-tuned
sorted_ft = df_sent_ft_move.sort_values('agreement_rate', ascending=False)
axes[1].barh(range(len(sorted_ft)), sorted_ft['agreement_rate'], alpha=0.7, color='coral')
axes[1].axvline(x=0.9, color='green', linestyle='--', alpha=0.5, label='High (>90%)')
axes[1].axvline(x=0.7, color='orange', linestyle='--', alpha=0.5, label='Moderate (>70%)')
axes[1].set_xlabel('Agreement Rate')
axes[1].set_ylabel('Sentence (sorted)')
axes[1].set_title('Fine-tuned: Sentence-Level Consistency')
axes[1].legend()

plt.tight_layout()
plt.savefig(figures_dir / 'sentence_consistency_heatmap.png')
plt.close()

print("✓ Saved: sentence_consistency_heatmap.png")
```

### 6.4 Accuracy vs Consistency Trade-off

```python
# Figure 4: Accuracy vs Consistency scatter plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot conditions
ax.scatter(zs_move['mean'] * 100, zs_move['cv'], s=200, alpha=0.7, label='Zero-shot', color='steelblue')
ax.scatter(ft_move['mean'] * 100, ft_move['cv'], s=200, alpha=0.7, label='Fine-tuned', color='coral')

# Annotate points
ax.annotate('Zero-shot', (zs_move['mean'] * 100, zs_move['cv']), 
            xytext=(5, 5), textcoords='offset points', fontsize=11)
ax.annotate('Fine-tuned', (ft_move['mean'] * 100, ft_move['cv']), 
            xytext=(5, 5), textcoords='offset points', fontsize=11)

# Ideal region
ax.axhspan(0, 5, alpha=0.1, color='green', label='Excellent consistency (CV<5%)')
ax.axvspan(85, 100, alpha=0.1, color='green')

ax.set_xlabel('Mean Accuracy (%)')
ax.set_ylabel('Coefficient of Variation (%)')
ax.set_title('Accuracy-Consistency Trade-off')
ax.legend()
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig(figures_dir / 'accuracy_consistency_tradeoff.png')
plt.close()

print("✓ Saved: accuracy_consistency_tradeoff.png")
```

### 6.5 Consistency by Move Type

```python
# Figure 5: Consistency by move type
fig, ax = plt.subplots(figsize=(10, 6))

move_types = sorted(zs_by_move['gold_label'].unique())
x = np.arange(len(move_types))
width = 0.35

zs_cvs_by_move = [zs_by_move[zs_by_move['gold_label'] == m]['cv_agreement'].values[0] for m in move_types]
ft_cvs_by_move = [ft_by_move[ft_by_move['gold_label'] == m]['cv_agreement'].values[0] for m in move_types]

bars1 = ax.bar(x - width/2, zs_cvs_by_move, width, label='Zero-shot', alpha=0.8)
bars2 = ax.bar(x + width/2, ft_cvs_by_move, width, label='Fine-tuned', alpha=0.8, color='coral')

ax.set_ylabel('Coefficient of Variation (%)')
ax.set_xlabel('Move Type')
ax.set_title('Consistency by Move Type')
ax.set_xticks(x)
ax.set_xticklabels(move_types)
ax.legend()
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig(figures_dir / 'consistency_by_move.png')
plt.close()

print("✓ Saved: consistency_by_move.png")
print()
```

---

## Main Execution Function

```python
def main():
    """
    Main execution function for Phase 2 analysis.
    """
    print()
    print("=" * 70)
    print("PHASE 2 STATISTICAL ANALYSIS: ZERO-SHOT VS FINE-TUNED CONSISTENCY")
    print("=" * 70)
    print()
    
    # Create output directories
    Path('evaluation_results').mkdir(exist_ok=True)
    Path('figures').mkdir(exist_ok=True)
    
    # Run all analyses
    # (All code blocks above would be executed here in sequence)
    
    print()
    print("=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)
    print()
    print("Outputs saved to:")
    print("  - CSV files: evaluation_results/")
    print("  - Figures: figures/")
    print()
    print("Key Files Generated:")
    print("  1. consistency_summary.csv - Aggregate metrics")
    print("  2. icc_results.csv - Reliability coefficients")
    print("  3. variance_comparison.csv - Levene's test results")
    print("  4. mean_comparison.csv - Welch's t-test results")
    print("  5. comprehensive_comparison.csv - Publication table")
    print("  6. sentence_consistency_*.csv - Sentence-level analyses")
    print("  7. consistency_by_move.csv - Stratified results")
    print("  8. All figures in figures/ directory")
    print()
    print("Next Steps:")
    print("  1. Review comprehensive_comparison.csv for manuscript table")
    print("  2. Examine figures for publication")
    print("  3. Interpret results using guidelines in study design document")
    print("  4. Draft results section using templates provided")
    print()

if __name__ == "__main__":
    main()
```

---

## Results Reporting Templates

### For Manuscript Results Section

**Template 1: Aggregate Consistency**

> To assess annotation consistency, we conducted 50 repeated evaluations of both zero-shot and fine-tuned approaches on the test set (10 articles, 267 sentences). Zero-shot annotation exhibited a mean move-level accuracy of X.X% (SD = X.X%, CV = X.X%), with a 95% confidence interval of [X.X%, X.X%]. Fine-tuned annotation achieved a mean accuracy of X.X% (SD = X.X%, CV = X.X%), with a 95% CI of [X.X%, X.X%]. The intraclass correlation coefficient for zero-shot was ICC(2,1) = 0.XXX [95% CI: 0.XXX, 0.XXX], indicating [poor/moderate/good/excellent] reliability, while fine-tuned achieved ICC(2,1) = 0.XXX [95% CI: 0.XXX, 0.XXX].

**Template 2: Variance Comparison**

> Levene's test revealed [a significant difference / no significant difference] in variance between conditions (F = X.XX, p = .XXX), with [zero-shot / fine-tuned] exhibiting X.XX× more variability. This suggests that [interpretation of practical significance].

**Template 3: Sentence-Level Patterns**

> Sentence-level analysis revealed distinct consistency patterns. For zero-shot, XX% of sentences were consistently annotated correctly (agreement > 90%), while XX% showed high uncertainty (agreement 30-70%). In comparison, fine-tuned annotation achieved high consistency on XX% of sentences, with XX% showing uncertainty. [Condition] demonstrated more stable predictions overall, with a mean sentence-level agreement rate of XX% compared to XX% for [other condition].

**Template 4: Stratified Analysis**

> Consistency varied significantly across move categories for [zero-shot / fine-tuned / both] conditions (Zero-shot: F(2, XXX) = X.XX, p = .XXX, η² = .XX; Fine-tuned: F(2, XXX) = X.XX, p = .XXX, η² = .XX). Move X demonstrated the highest consistency (Zero-shot: CV = X.X%; Fine-tuned: CV = X.X%), while Move X showed the greatest variability (Zero-shot: CV = XX.X%; Fine-tuned: CV = XX.X%).

---

## Interpretation Guidelines

### Coefficient of Variation (CV)

- **< 5%:** Excellent consistency - very stable performance
- **5-10%:** Good consistency - acceptable for research applications
- **10-20%:** Moderate consistency - interpret aggregate trends carefully
- **> 20%:** Poor consistency - individual predictions unreliable

### ICC(2,1) Interpretation (Koo & Li, 2016)

- **< 0.5:** Poor reliability - unacceptable for any application
- **0.5-0.75:** Moderate reliability - acceptable for exploratory research
- **0.75-0.9:** Good reliability - suitable for most research applications
- **> 0.9:** Excellent reliability - suitable for high-stakes applied use

### Effect Size (Cohen's d)

- **< 0.2:** Negligible effect
- **0.2-0.5:** Small effect
- **0.5-0.8:** Medium effect
- **> 0.8:** Large effect

---

## Checklist

### Data Preparation
- [ ] All 100 runs collected (50 zero-shot + 50 fine-tuned)
- [ ] All runs parsed successfully
- [ ] No missing data
- [ ] Consolidated CSV files created

### Analysis Completed
- [ ] Descriptive statistics calculated for both conditions
- [ ] Distribution assessment completed (normality tests)
- [ ] ICC calculated for both conditions
- [ ] Levene's test (variance comparison)
- [ ] Welch's t-test (mean comparison)
- [ ] Sentence-level analysis completed
- [ ] Stratified analysis by move type
- [ ] ANOVA for move differences

### Visualizations Created
- [ ] Accuracy distribution plots
- [ ] CV comparison bar chart
- [ ] Sentence-level agreement heatmaps
- [ ] Accuracy-consistency trade-off scatter plot
- [ ] Consistency by move type bar chart

### Outputs Generated
- [ ] All CSV files saved
- [ ] All figures saved (high resolution)
- [ ] Comprehensive comparison table formatted
- [ ] Results ready for manuscript

### Reporting
- [ ] Results section drafted using templates
- [ ] Tables formatted for publication
- [ ] Figures have clear captions
- [ ] Interpretations grounded in guidelines
- [ ] Limitations acknowledged

---

**This analysis plan provides a rigorous, focused approach to Phase 2 that will satisfy RMAL reviewers and produce high-quality methodological research.**
