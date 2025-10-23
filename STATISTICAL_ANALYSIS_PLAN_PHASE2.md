# Statistical Analysis Plan - Phase 2 (Revised)
## Zero-Shot Consistency and Example Selection Effects

**Purpose:** Analysis plan for Phase 2 following unexpected validation results  
**Primary:** Zero-shot consistency characterization (50 runs × 2 datasets = 100 runs)  
**Secondary:** Example selection exploration (5 alternative sets, test set only, descriptive)

---

## Analysis Structure

```
Phase 2 Analysis
├── Primary: Zero-Shot Consistency (RQ2)
│   ├── Training Set Analysis (Primary - 30 articles, 826 sentences)
│   │   ├── Aggregate Consistency Metrics
│   │   ├── Sentence-Level Analysis
│   │   ├── Stratified Analysis (by move/step)
│   │   └── Visualizations
│   ├── Test Set Analysis (Replication - 10 articles, 267 sentences)
│   │   ├── Aggregate Consistency Metrics
│   │   ├── Sentence-Level Analysis
│   │   ├── Stratified Analysis (by move/step)
│   │   └── Visualizations
│   └── Cross-Dataset Comparison
│       ├── Variance Comparison (Training vs Test)
│       ├── ICC Comparison
│       └── Generalization Analysis
└── Secondary: Example Selection (RQ2b) 
    ├── Descriptive Statistics Only (Test Set)
    └── Visual Comparison
```

---

## Required Python Packages

```python
# Core data manipulation
import pandas as pd
import numpy as np

# Statistical tests
from scipy import stats
from scipy.stats import (
    shapiro,           # Normality test
    ttest_1samp,       # One-sample t-test
    f_oneway,          # One-way ANOVA
)

# Effect sizes and reliability
from pingouin import (
    intraclass_corr,   # ICC calculation
)

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Entropy calculation
from scipy.stats import entropy
```

---

## Part 1: Primary Analysis - Zero-Shot Consistency

### 1.1 Load Zero-Shot Results (50 Runs × 2 Datasets)

```python
import json
import pandas as pd
from pathlib import Path

def load_zero_shot_results(dataset='train', research_question='rq2'):
    """
    Load all 50 zero-shot evaluation results for a specific dataset.
    
    Args:
        dataset: 'train' (30 articles) or 'test' (10 articles)
        research_question: 'rq2'
    
    Returns:
        DataFrame with one row per run
    """
    results = []
    results_dir = Path('evaluation_results')
    
    # Pattern: zero_shot_rq2_{dataset}_run_01.json through run_50.json
    for run_num in range(1, 51):
        json_file = results_dir / f"zero_shot_{research_question}_{dataset}_run_{run_num:02d}.json"
        
        if not json_file.exists():
            print(f"Warning: Missing {json_file}")
            continue
            
        with open(json_file) as f:
            data = json.load(f)
        
        result_row = {
            'dataset': dataset,
            'run_number': run_num,
            'move_accuracy': data['move_metrics']['accuracy'],
            'step_accuracy': data['step_metrics']['accuracy'],
            'move_f1': data['move_metrics']['weighted_f1'],
            'step_f1': data['step_metrics']['weighted_f1'],
            'move_precision': data['move_metrics']['weighted_precision'],
            'move_recall': data['move_metrics']['weighted_recall'],
            'total_sentences': data['total_sentences'],
        }
        results.append(result_row)
    
    df = pd.DataFrame(results)
    print(f"Loaded {len(df)} runs for {dataset} dataset")
    
    return df

# Load both datasets
df_train = load_zero_shot_results(dataset='train', research_question='rq2')
df_test = load_zero_shot_results(dataset='test', research_question='rq2')

# Combine for some analyses
df_combined = pd.concat([df_train, df_test], ignore_index=True)

# Save consolidated data
df_train.to_csv('evaluation_results/zero_shot_train_consolidated_rq2.csv', index=False)
df_test.to_csv('evaluation_results/zero_shot_test_consolidated_rq2.csv', index=False)
df_combined.to_csv('evaluation_results/zero_shot_combined_consolidated_rq2.csv', index=False)

print("\nDataset Summary:")
print(f"  Training set: {df_train['total_sentences'].iloc[0]} sentences × 50 runs = {df_train['total_sentences'].iloc[0] * 50} observations")
print(f"  Test set: {df_test['total_sentences'].iloc[0]} sentences × 50 runs = {df_test['total_sentences'].iloc[0] * 50} observations")
```
```

### 1.2 Aggregate Consistency Metrics

```python
def calculate_zero_shot_consistency(df, metric='move_accuracy'):
    """
    Calculate comprehensive consistency metrics.
    
    Returns:
        Dictionary with all consistency metrics
    """
    data = df[metric].values
    
    metrics = {
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
        'cv': (np.std(data, ddof=1) / np.mean(data)) * 100,  # Coefficient of variation
    }
    
    # 95% Confidence interval for mean
    from scipy import stats
    ci = stats.t.interval(
        0.95, 
        len(data)-1,
        loc=np.mean(data),
        scale=stats.sem(data)
    )
    metrics['ci_lower'] = ci[0]
    metrics['ci_upper'] = ci[1]
    
    return metrics

# Calculate for move and step
move_consistency = calculate_zero_shot_consistency(df_zero_shot, 'move_accuracy')
step_consistency = calculate_zero_shot_consistency(df_zero_shot, 'step_accuracy')

print("=" * 70)
print("ZERO-SHOT CONSISTENCY METRICS")
print("=" * 70)
print("\nMove-Level Accuracy:")
print(f"  Mean: {move_consistency['mean']:.1%} ± {move_consistency['sd']:.2%}")
print(f"  95% CI: [{move_consistency['ci_lower']:.1%}, {move_consistency['ci_upper']:.1%}]")
print(f"  CV: {move_consistency['cv']:.2f}%")
print(f"  Range: {move_consistency['min']:.1%} - {move_consistency['max']:.1%}")
print(f"  IQR: {move_consistency['iqr']:.2%}")

print("\nStep-Level Accuracy:")
print(f"  Mean: {step_consistency['mean']:.1%} ± {step_consistency['sd']:.2%}")
print(f"  95% CI: [{step_consistency['ci_lower']:.1%}, {step_consistency['ci_upper']:.1%}]")
print(f"  CV: {step_consistency['cv']:.2f}%")
print(f"  Range: {step_consistency['min']:.1%} - {step_consistency['max']:.1%}")

# Save summary
summary_df = pd.DataFrame([
    {'level': 'move', **move_consistency},
    {'level': 'step', **step_consistency}
])
summary_df.to_csv('evaluation_results/zero_shot_consistency_summary.csv', index=False)
```

### 1.3 Intraclass Correlation Coefficient (ICC)

**ICC measures:** What proportion of total variance is between-sentences vs within-sentence (across runs)?

```python
def calculate_icc_zero_shot(dataset='test', research_question='rq2', level='move'):
    """
    Calculate ICC for zero-shot consistency.
    
    Requires sentence-level data from all runs.
    """
    from pingouin import intraclass_corr
    
    # Load sentence-level details from all runs
    results_dir = Path('evaluation_results')
    all_sentences = []
    
    for run_num in range(1, 51):
        csv_file = results_dir / f"zero_shot_{research_question}_{dataset}_run_{run_num:02d}.csv"
        
        if not csv_file.exists():
            continue
            
        df = pd.read_csv(csv_file)
        df['run'] = run_num
        all_sentences.append(df)
    
    # Combine all runs
    combined = pd.concat(all_sentences, ignore_index=True)
    
    # Calculate ICC
    # Ratings are correctness (0 or 1), judges are runs, targets are sentences
    if level == 'move':
        correctness_col = 'move_correct'
    else:
        correctness_col = 'step_correct'
    
    # Prepare data for ICC
    icc_data = combined[['sentence_id', 'run', correctness_col]].copy()
    icc_data.columns = ['target', 'rater', 'rating']
    
    # Calculate ICC(2,1) - two-way random effects, single rater
    icc_result = intraclass_corr(
        data=icc_data,
        targets='target',
        raters='rater',
        ratings='rating',
        nan_policy='omit'
    )
    
    # Extract ICC(2,1)
    icc_21 = icc_result[icc_result['Type'] == 'ICC2']['ICC'].values[0]
    
    print(f"\n{level.upper()}-LEVEL ICC:")
    print(f"  ICC(2,1) = {icc_21:.3f}")
    print("\n  Interpretation:")
    if icc_21 < 0.5:
        print("    Poor consistency")
    elif icc_21 < 0.75:
        print("    Moderate consistency")
    elif icc_21 < 0.9:
        print("    Good consistency")
    else:
        print("    Excellent consistency")
    
    return icc_21

# Calculate ICC
icc_move = calculate_icc_zero_shot(level='move')
icc_step = calculate_icc_zero_shot(level='step')

# Save ICC results
icc_results = pd.DataFrame([
    {'level': 'move', 'icc_21': icc_move},
    {'level': 'step', 'icc_21': icc_step}
])
icc_results.to_csv('evaluation_results/zero_shot_icc.csv', index=False)
```

### 1.4 Sentence-Level Consistency Analysis

**Goal:** Identify which sentences are consistently correct vs uncertain

```python
def analyze_sentence_consistency(dataset='test', research_question='rq2', level='move'):
    """
    Analyze consistency for each sentence across 50 runs.
    """
    from scipy.stats import entropy
    
    # Load all runs
    results_dir = Path('evaluation_results')
    all_sentences = []
    
    for run_num in range(1, 51):
        csv_file = results_dir / f"zero_shot_{research_question}_{dataset}_run_{run_num:02d}.csv"
        if not csv_file.exists():
            continue
        df = pd.read_csv(csv_file)
        df['run'] = run_num
        all_sentences.append(df)
    
    combined = pd.concat(all_sentences, ignore_index=True)
    
    # Group by sentence
    if level == 'move':
        pred_col = 'move_pred'
        true_col = 'move_true'
        correct_col = 'move_correct'
    else:
        pred_col = 'step_pred'
        true_col = 'step_true'
        correct_col = 'step_correct'
    
    sentence_stats = []
    
    for sentence_id in combined['sentence_id'].unique():
        sentence_data = combined[combined['sentence_id'] == sentence_id]
        
        # Get ground truth (should be same across all runs)
        true_label = sentence_data[true_col].iloc[0]
        
        # Calculate statistics
        predictions = sentence_data[pred_col].values
        correctness = sentence_data[correct_col].values
        
        # Agreement rate
        agreement_rate = np.mean(correctness)
        
        # Modal prediction
        from collections import Counter
        pred_counts = Counter(predictions)
        modal_pred = pred_counts.most_common(1)[0][0]
        modal_freq = pred_counts.most_common(1)[0][1] / len(predictions)
        
        # Entropy (uncertainty)
        label_probs = np.array([count for label, count in pred_counts.items()]) / len(predictions)
        sent_entropy = entropy(label_probs, base=2)
        
        # Flip count
        flips = np.sum(np.diff(correctness) != 0)
        
        sentence_stats.append({
            'sentence_id': sentence_id,
            'true_label': true_label,
            'agreement_rate': agreement_rate,
            'modal_prediction': modal_pred,
            'modal_frequency': modal_freq,
            'entropy': sent_entropy,
            'num_flips': flips,
            'n_runs': len(predictions),
            'consistent_correct': agreement_rate == 1.0,
            'consistent_incorrect': agreement_rate == 0.0,
            'uncertain': 0.3 < agreement_rate < 0.7,  # Define uncertainty threshold
        })
    
    sentence_df = pd.DataFrame(sentence_stats)
    
    # Summary statistics
    print(f"\n{level.upper()}-LEVEL SENTENCE CONSISTENCY:")
    print(f"  Total sentences: {len(sentence_df)}")
    print(f"  Consistently correct (100%): {sentence_df['consistent_correct'].sum()}")
    print(f"  Consistently incorrect (0%): {sentence_df['consistent_incorrect'].sum()}")
    print(f"  Uncertain (30-70%): {sentence_df['uncertain'].sum()}")
    print(f"  Mean agreement rate: {sentence_df['agreement_rate'].mean():.1%}")
    print(f"  Mean entropy: {sentence_df['entropy'].mean():.3f}")
    
    # Save detailed results
    sentence_df.to_csv(
        f'evaluation_results/sentence_consistency_{level}_rq2.csv',
        index=False
    )
    
    return sentence_df

# Analyze both levels
sentence_move = analyze_sentence_consistency(level='move')
sentence_step = analyze_sentence_consistency(level='step')
```

### 1.5 Stratified Analysis (by Move/Step Type)

```python
def analyze_consistency_by_category(sentence_df, level='move'):
    """
    Analyze consistency patterns by move or step category.
    """
    # Group by true label
    category_stats = sentence_df.groupby('true_label').agg({
        'agreement_rate': ['mean', 'std', 'min', 'max'],
        'entropy': ['mean', 'std'],
        'sentence_id': 'count'
    }).round(3)
    
    category_stats.columns = ['_'.join(col).strip() for col in category_stats.columns.values]
    category_stats = category_stats.reset_index()
    
    print(f"\n{level.upper()}-LEVEL CONSISTENCY BY CATEGORY:")
    print(category_stats.to_string(index=False))
    
    # ANOVA: Does consistency differ across categories?
    from scipy.stats import f_oneway
    
    groups = [
        sentence_df[sentence_df['true_label'] == label]['agreement_rate'].values
        for label in sentence_df['true_label'].unique()
    ]
    
    f_stat, p_value = f_oneway(*groups)
    
    print(f"\nANOVA Test:")
    print(f"  F({len(groups)-1}, {len(sentence_df)-len(groups)}) = {f_stat:.2f}, p = {p_value:.4f}")
    if p_value < 0.05:
        print("  → Significant differences in consistency across categories")
    else:
        print("  → No significant differences in consistency across categories")
    
    # Save results
    category_stats.to_csv(
        f'evaluation_results/consistency_by_category_{level}_rq2.csv',
        index=False
    )
    
    return category_stats

# Analyze by category
move_by_category = analyze_consistency_by_category(sentence_move, level='move')
step_by_category = analyze_consistency_by_category(sentence_step, level='step')
```

### 1.6 Visualizations

```python
def create_zero_shot_visualizations(df_zero_shot, sentence_df, level='move', dataset='train'):
    """
    Create comprehensive visualization suite.
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. Distribution of accuracy across runs
    ax1 = axes[0, 0]
    ax1.hist(df_zero_shot[f'{level}_accuracy'], bins=20, edgecolor='black', alpha=0.7)
    ax1.axvline(df_zero_shot[f'{level}_accuracy'].mean(), color='red', 
                linestyle='--', label=f'Mean = {df_zero_shot[f"{level}_accuracy"].mean():.1%}')
    ax1.set_xlabel('Accuracy')
    ax1.set_ylabel('Frequency')
    ax1.set_title(f'{level.title()}-Level Accuracy Distribution (50 Runs, {dataset.upper()})')
    ax1.legend()
    
    # 2. Sentence-level agreement rates
    ax2 = axes[0, 1]
    ax2.hist(sentence_df['agreement_rate'], bins=20, edgecolor='black', alpha=0.7)
    ax2.set_xlabel('Agreement Rate (% Correct)')
    ax2.set_ylabel('Number of Sentences')
    ax2.set_title(f'Sentence-Level Agreement Rates ({dataset.upper()})')
    
    # 3. Entropy distribution
    ax3 = axes[1, 0]
    ax3.hist(sentence_df['entropy'], bins=20, edgecolor='black', alpha=0.7, color='orange')
    ax3.set_xlabel('Entropy (bits)')
    ax3.set_ylabel('Number of Sentences')
    ax3.set_title(f'Prediction Uncertainty (Entropy, {dataset.upper()})')
    
    # 4. Agreement rate by category
    ax4 = axes[1, 1]
    category_means = sentence_df.groupby('true_label')['agreement_rate'].mean().sort_values()
    ax4.barh(range(len(category_means)), category_means.values)
    ax4.set_yticks(range(len(category_means)))
    ax4.set_yticklabels(category_means.index)
    ax4.set_xlabel('Mean Agreement Rate')
    ax4.set_title(f'Consistency by {level.title()} Category ({dataset.upper()})')
    ax4.axvline(0.5, color='red', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig(f'figures/zero_shot_consistency_{level}_{dataset}_rq2.png', dpi=300, bbox_inches='tight')
    print(f"Saved: figures/zero_shot_consistency_{level}_{dataset}_rq2.png")
    plt.close()

# Create visualizations for both datasets
Path('figures').mkdir(exist_ok=True)
create_zero_shot_visualizations(df_train, sentence_move_train, level='move', dataset='train')
create_zero_shot_visualizations(df_train, sentence_step_train, level='step', dataset='train')
create_zero_shot_visualizations(df_test, sentence_move_test, level='move', dataset='test')
create_zero_shot_visualizations(df_test, sentence_step_test, level='step', dataset='test')
```

---

## Part 1B: Cross-Dataset Comparison

### 1.7 Compare Consistency Across Datasets

```python
def compare_datasets(df_train, df_test, metric='move_accuracy'):
    """
    Compare consistency metrics between training and test sets.
    
    Args:
        df_train: Training set results
        df_test: Test set results
        metric: Metric to compare
    
    Returns:
        Comparison summary
    """
    from scipy.stats import levene, f_oneway
    
    train_data = df_train[metric].values
    test_data = df_test[metric].values
    
    # Calculate metrics for both
    train_metrics = {
        'dataset': 'Training',
        'n_articles': 30,
        'n_sentences': df_train['total_sentences'].iloc[0],
        'n_runs': len(train_data),
        'mean': np.mean(train_data),
        'sd': np.std(train_data, ddof=1),
        'cv': (np.std(train_data, ddof=1) / np.mean(train_data)) * 100,
        'median': np.median(train_data),
        'min': np.min(train_data),
        'max': np.max(train_data),
        'range': np.max(train_data) - np.min(train_data),
    }
    
    test_metrics = {
        'dataset': 'Test',
        'n_articles': 10,
        'n_sentences': df_test['total_sentences'].iloc[0],
        'n_runs': len(test_data),
        'mean': np.mean(test_data),
        'sd': np.std(test_data, ddof=1),
        'cv': (np.std(test_data, ddof=1) / np.mean(test_data)) * 100,
        'median': np.median(test_data),
        'min': np.min(test_data),
        'max': np.max(test_data),
        'range': np.max(test_data) - np.min(test_data),
    }
    
    # Statistical comparison
    # Levene's test for variance homogeneity
    levene_stat, levene_p = levene(train_data, test_data)
    
    # F-test for mean difference (probably not different, but check)
    f_stat, f_p = f_oneway(train_data, test_data)
    
    print("=" * 70)
    print(f"CROSS-DATASET COMPARISON: {metric.upper()}")
    print("=" * 70)
    print("\nTraining Set:")
    print(f"  Mean: {train_metrics['mean']:.1%} ± {train_metrics['sd']:.2%}")
    print(f"  CV: {train_metrics['cv']:.2f}%")
    print(f"  Range: {train_metrics['min']:.1%} - {train_metrics['max']:.1%}")
    
    print("\nTest Set:")
    print(f"  Mean: {test_metrics['mean']:.1%} ± {test_metrics['sd']:.2%}")
    print(f"  CV: {test_metrics['cv']:.2f}%")
    print(f"  Range: {test_metrics['min']:.1%} - {test_metrics['max']:.1%}")
    
    print("\nStatistical Tests:")
    print(f"  Levene's test (variance): F = {levene_stat:.2f}, p = {levene_p:.4f}")
    if levene_p < 0.05:
        print("    → Variances differ significantly")
    else:
        print("    → No significant difference in variances")
    
    print(f"  ANOVA (means): F = {f_stat:.2f}, p = {f_p:.4f}")
    if f_p < 0.05:
        print("    → Means differ significantly")
    else:
        print("    → No significant difference in means")
    
    # Save comparison
    comparison_df = pd.DataFrame([train_metrics, test_metrics])
    comparison_df.to_csv(
        f'evaluation_results/cross_dataset_comparison_{metric}_rq2.csv',
        index=False
    )
    
    return comparison_df

# Compare both levels
move_comparison = compare_datasets(df_train, df_test, metric='move_accuracy')
step_comparison = compare_datasets(df_train, df_test, metric='step_accuracy')
```

### 1.8 Compare ICC Across Datasets

```python
def compare_icc_across_datasets(icc_train_move, icc_test_move, icc_train_step, icc_test_step):
    """
    Compare ICC values across datasets.
    """
    print("\n" + "=" * 70)
    print("ICC COMPARISON: TRAINING VS TEST")
    print("=" * 70)
    
    print("\nMove-Level ICC:")
    print(f"  Training: {icc_train_move:.3f}")
    print(f"  Test: {icc_test_move:.3f}")
    print(f"  Difference: {abs(icc_train_move - icc_test_move):.3f}")
    
    print("\nStep-Level ICC:")
    print(f"  Training: {icc_train_step:.3f}")
    print(f"  Test: {icc_test_step:.3f}")
    print(f"  Difference: {abs(icc_train_step - icc_test_step):.3f}")
    
    # Save comparison
    icc_comparison = pd.DataFrame([
        {'level': 'move', 'dataset': 'train', 'icc': icc_train_move},
        {'level': 'move', 'dataset': 'test', 'icc': icc_test_move},
        {'level': 'step', 'dataset': 'train', 'icc': icc_train_step},
        {'level': 'step', 'dataset': 'test', 'icc': icc_test_step},
    ])
    
    icc_comparison.to_csv('evaluation_results/icc_cross_dataset_comparison_rq2.csv', index=False)
    
    print("\nInterpretation:")
    if abs(icc_train_move - icc_test_move) < 0.1:
        print("  ICC values are similar across datasets, suggesting")
        print("  consistency patterns are stable and generalizable.")
    else:
        print("  ICC values differ substantially across datasets, suggesting")
        print("  consistency may depend on article characteristics.")

# Compare ICCs (after calculating them for both datasets)
compare_icc_across_datasets(icc_train_move, icc_test_move, icc_train_step, icc_test_step)
```

### 1.9 Cross-Dataset Visualization

```python
def create_cross_dataset_comparison_plot(df_train, df_test, move_comparison):
    """
    Create side-by-side comparison of training and test datasets.
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # 1. Accuracy distributions
    ax1 = axes[0]
    ax1.hist(df_train['move_accuracy'], bins=15, alpha=0.6, label='Training', edgecolor='black')
    ax1.hist(df_test['move_accuracy'], bins=15, alpha=0.6, label='Test', edgecolor='black')
    ax1.set_xlabel('Move-Level Accuracy')
    ax1.set_ylabel('Frequency')
    ax1.set_title('Accuracy Distribution Comparison')
    ax1.legend()
    
    # 2. Box plots
    ax2 = axes[1]
    data_for_box = pd.DataFrame({
        'Training': df_train['move_accuracy'],
        'Test': df_test['move_accuracy']
    })
    data_for_box.boxplot(ax=ax2)
    ax2.set_ylabel('Move-Level Accuracy')
    ax2.set_title('Accuracy Variability Comparison')
    ax2.grid(axis='y', alpha=0.3)
    
    # 3. CV comparison
    ax3 = axes[2]
    datasets = ['Training\n(30 articles)', 'Test\n(10 articles)']
    cvs = [move_comparison.iloc[0]['cv'], move_comparison.iloc[1]['cv']]
    bars = ax3.bar(datasets, cvs, color=['steelblue', 'coral'], edgecolor='black')
    ax3.set_ylabel('Coefficient of Variation (%)')
    ax3.set_title('Consistency Comparison (CV)')
    ax3.set_ylim(0, max(cvs) * 1.2)
    
    # Add value labels on bars
    for bar, cv in zip(bars, cvs):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{cv:.2f}%', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('figures/cross_dataset_comparison_rq2.png', dpi=300, bbox_inches='tight')
    print("Saved: figures/cross_dataset_comparison_rq2.png")
    plt.close()

# Create cross-dataset visualization
create_cross_dataset_comparison_plot(df_train, df_test, move_comparison)
```

---

## Part 2: Secondary Analysis - Example Selection Effects

### 2.1 Load Alternative Example Set Results

```python
def load_alternative_example_results(dataset='test', research_question='rq2'):
    """
    Load results from 5 alternative 3-shot example sets.
    
    Expected files:
    - three_shot_alt_set_b_rq2_test.json
    - three_shot_alt_set_c_rq2_test.json
    - three_shot_alt_set_d_rq2_test.json
    - three_shot_alt_set_e_rq2_test.json
    - three_shot_rq1_validation.json (original for comparison)
    """
    results = []
    results_dir = Path('evaluation_results')
    
    # Original set (from RQ1 validation - as baseline)
    original_file = results_dir / f'three_shot_rq1_validation.json'
    if original_file.exists():
        with open(original_file) as f:
            data = json.load(f)
        results.append({
            'set_id': 'A (Original)',
            'seed': 42,
            'move_accuracy': data['move_metrics']['accuracy'],
            'step_accuracy': data['step_metrics']['accuracy'],
            'move_f1': data['move_metrics']['weighted_f1'],
        })
    
    # Alternative sets B-E
    for set_letter, seed in [('b', 100), ('c', 200), ('d', 300), ('e', 400)]:
        json_file = results_dir / f'three_shot_alt_set_{set_letter}_{research_question}_{dataset}.json'
        
        if not json_file.exists():
            print(f"Warning: Missing {json_file}")
            continue
            
        with open(json_file) as f:
            data = json.load(f)
        
        results.append({
            'set_id': f'{set_letter.upper()}',
            'seed': seed,
            'move_accuracy': data['move_metrics']['accuracy'],
            'step_accuracy': data['step_metrics']['accuracy'],
            'move_f1': data['move_metrics']['weighted_f1'],
        })
    
    df = pd.DataFrame(results)
    print(f"Loaded {len(df)} example sets")
    
    return df

# Load alternative results
df_alt_examples = load_alternative_example_results()

# Save consolidated
df_alt_examples.to_csv('evaluation_results/alternative_examples_rq2.csv', index=False)
```

### 2.2 Descriptive Statistics (No Significance Testing)

```python
def analyze_example_selection_effects(df_alt, zero_shot_mean):
    """
    Descriptive analysis of example selection effects.
    
    Args:
        df_alt: DataFrame with alternative example set results
        zero_shot_mean: Mean accuracy from 50 zero-shot runs (for comparison)
    """
    print("=" * 70)
    print("EXAMPLE SELECTION EFFECTS (EXPLORATORY)")
    print("=" * 70)
    print(f"\nN = {len(df_alt)} example sets (too small for significance testing)")
    print("Results are descriptive only and generate hypotheses for future work.")
    print()
    
    # Move-level analysis
    print("MOVE-LEVEL ACCURACY:")
    print(f"  Mean: {df_alt['move_accuracy'].mean():.1%}")
    print(f"  SD: {df_alt['move_accuracy'].std():.2%}")
    print(f"  Min: {df_alt['move_accuracy'].min():.1%}")
    print(f"  Max: {df_alt['move_accuracy'].max():.1%}")
    print(f"  Range: {df_alt['move_accuracy'].max() - df_alt['move_accuracy'].min():.2%}")
    print()
    
    # Comparison to zero-shot
    print("COMPARISON TO ZERO-SHOT:")
    print(f"  Zero-shot mean: {zero_shot_mean:.1%}")
    print(f"  Few-shot mean: {df_alt['move_accuracy'].mean():.1%}")
    print(f"  Difference: {df_alt['move_accuracy'].mean() - zero_shot_mean:+.2%}")
    print(f"  Sets exceeding zero-shot: {(df_alt['move_accuracy'] > zero_shot_mean).sum()}/{len(df_alt)}")
    print()
    
    # Individual set comparison
    print("INDIVIDUAL EXAMPLE SETS:")
    for _, row in df_alt.iterrows():
        diff = row['move_accuracy'] - zero_shot_mean
        symbol = "↑" if diff > 0 else "↓" if diff < 0 else "="
        print(f"  Set {row['set_id']:12} (seed {row['seed']}): {row['move_accuracy']:.1%}  ({diff:+.2%} vs zero-shot) {symbol}")
    print()
    
    # Interpretation
    range_pct = (df_alt['move_accuracy'].max() - df_alt['move_accuracy'].min()) * 100
    print("INTERPRETATION:")
    if range_pct > 5:
        print(f"  Range of {range_pct:.1f} percentage points suggests example selection")
        print(f"  has SUBSTANTIAL impact on few-shot performance.")
    elif range_pct > 2:
        print(f"  Range of {range_pct:.1f} percentage points suggests example selection")
        print(f"  has MODERATE impact on few-shot performance.")
    else:
        print(f"  Range of {range_pct:.1f} percentage points suggests example selection")
        print(f"  has MINIMAL impact; underperformance may be fundamental.")
    print()
    
    if df_alt['move_accuracy'].max() > zero_shot_mean:
        print("  At least one example set exceeds zero-shot performance,")
        print("  suggesting example selection can improve few-shot results.")
    else:
        print("  NO example sets exceed zero-shot performance,")
        print("  suggesting few-shot underperformance is robust across random selections.")
    print()
    
    # Save summary
    summary = {
        'n_sets': len(df_alt),
        'mean': df_alt['move_accuracy'].mean(),
        'sd': df_alt['move_accuracy'].std(),
        'min': df_alt['move_accuracy'].min(),
        'max': df_alt['move_accuracy'].max(),
        'range': df_alt['move_accuracy'].max() - df_alt['move_accuracy'].min(),
        'zero_shot_mean': zero_shot_mean,
        'n_exceed_zero_shot': (df_alt['move_accuracy'] > zero_shot_mean).sum(),
    }
    
    pd.DataFrame([summary]).to_csv(
        'evaluation_results/example_selection_summary_rq2.csv',
        index=False
    )

# Run analysis
zero_shot_mean_acc = df_zero_shot['move_accuracy'].mean()
analyze_example_selection_effects(df_alt_examples, zero_shot_mean_acc)
```

### 2.3 Visual Comparison

```python
def plot_example_selection_comparison(df_alt, zero_shot_mean, zero_shot_ci):
    """
    Create visual comparison of example sets vs zero-shot.
    """
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot alternative example sets
    x = range(len(df_alt))
    ax.bar(x, df_alt['move_accuracy'], alpha=0.7, label='Few-shot (alternative sets)')
    
    # Add zero-shot reference line
    ax.axhline(zero_shot_mean, color='red', linestyle='--', linewidth=2, 
               label=f'Zero-shot mean ({zero_shot_mean:.1%})')
    
    # Add zero-shot confidence interval
    ax.axhspan(zero_shot_ci[0], zero_shot_ci[1], alpha=0.2, color='red',
               label='Zero-shot 95% CI')
    
    # Labels
    ax.set_xticks(x)
    ax.set_xticklabels(df_alt['set_id'])
    ax.set_xlabel('Example Set')
    ax.set_ylabel('Move-Level Accuracy')
    ax.set_title('Few-Shot Example Selection Effects (N=5 Sets, Exploratory)')
    ax.legend()
    ax.set_ylim(0, 1)
    
    # Add value labels on bars
    for i, (_, row) in enumerate(df_alt.iterrows()):
        ax.text(i, row['move_accuracy'] + 0.01, f"{row['move_accuracy']:.1%}",
                ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('figures/example_selection_comparison_rq2.png', dpi=300, bbox_inches='tight')
    print("Saved: figures/example_selection_comparison_rq2.png")
    plt.close()

# Create visualization
zero_shot_ci = (move_consistency['ci_lower'], move_consistency['ci_upper'])
plot_example_selection_comparison(df_alt_examples, zero_shot_mean_acc, zero_shot_ci)
```

---

## Complete Analysis Pipeline

### Master Script: `run_phase2_analysis.py`

```python
"""
Phase 2 Statistical Analysis
Run after collecting:
- 50 zero-shot runs on training set (30 articles)
- 50 zero-shot runs on test set (10 articles)
- 5 alternative few-shot example sets on test set
Total: 105 runs
"""

from pathlib import Path
import pandas as pd
import numpy as np

# Import all functions defined above
# (or include them in this file)

def main():
    """Run complete Phase 2 analysis."""
    
    print("=" * 70)
    print("PHASE 2 STATISTICAL ANALYSIS")
    print("RQ2: Zero-Shot Consistency + Example Selection")
    print("=" * 70)
    
    # Create output directories
    Path('evaluation_results').mkdir(exist_ok=True)
    Path('figures').mkdir(exist_ok=True)
    
    # ========================================================================
    # PRIMARY ANALYSIS: ZERO-SHOT CONSISTENCY (TRAINING SET)
    # ========================================================================
    
    print("\n" + "=" * 70)
    print("PRIMARY ANALYSIS: ZERO-SHOT CONSISTENCY - TRAINING SET (50 RUNS)")
    print("=" * 70)
    
    # 1. Load training set results
    print("\n[1/12] Loading training set zero-shot results...")
    df_train = load_zero_shot_results(dataset='train', research_question='rq2')
    
    # 2. Aggregate consistency metrics (training)
    print("\n[2/12] Calculating aggregate consistency (training)...")
    move_consistency_train = calculate_zero_shot_consistency(df_train, 'move_accuracy')
    step_consistency_train = calculate_zero_shot_consistency(df_train, 'step_accuracy')
    
    # 3. ICC calculation (training)
    print("\n[3/12] Calculating ICC (training)...")
    icc_train_move = calculate_icc_zero_shot(dataset='train', level='move')
    icc_train_step = calculate_icc_zero_shot(dataset='train', level='step')
    
    # 4. Sentence-level analysis (training)
    print("\n[4/12] Analyzing sentence-level consistency (training)...")
    sentence_move_train = analyze_sentence_consistency(dataset='train', level='move')
    sentence_step_train = analyze_sentence_consistency(dataset='train', level='step')
    
    # 5. Stratified analysis (training)
    print("\n[5/12] Analyzing consistency by category (training)...")
    move_by_category_train = analyze_consistency_by_category(sentence_move_train, level='move')
    step_by_category_train = analyze_consistency_by_category(sentence_step_train, level='step')
    
    # 6. Visualizations (training)
    print("\n[6/12] Creating visualizations (training)...")
    create_zero_shot_visualizations(df_train, sentence_move_train, level='move', dataset='train')
    create_zero_shot_visualizations(df_train, sentence_step_train, level='step', dataset='train')
    
    # ========================================================================
    # REPLICATION ANALYSIS: ZERO-SHOT CONSISTENCY (TEST SET)
    # ========================================================================
    
    print("\n" + "=" * 70)
    print("REPLICATION ANALYSIS: ZERO-SHOT CONSISTENCY - TEST SET (50 RUNS)")
    print("=" * 70)
    
    # 7. Load test set results
    print("\n[7/12] Loading test set zero-shot results...")
    df_test = load_zero_shot_results(dataset='test', research_question='rq2')
    
    # 8. Aggregate consistency metrics (test)
    print("\n[8/12] Calculating aggregate consistency (test)...")
    move_consistency_test = calculate_zero_shot_consistency(df_test, 'move_accuracy')
    step_consistency_test = calculate_zero_shot_consistency(df_test, 'step_accuracy')
    
    # 9. ICC calculation (test)
    print("\n[9/12] Calculating ICC (test)...")
    icc_test_move = calculate_icc_zero_shot(dataset='test', level='move')
    icc_test_step = calculate_icc_zero_shot(dataset='test', level='step')
    
    # 10. Sentence-level analysis (test)
    print("\n[10/12] Analyzing sentence-level consistency (test)...")
    sentence_move_test = analyze_sentence_consistency(dataset='test', level='move')
    sentence_step_test = analyze_sentence_consistency(dataset='test', level='step')
    
    # Visualizations (test)
    create_zero_shot_visualizations(df_test, sentence_move_test, level='move', dataset='test')
    create_zero_shot_visualizations(df_test, sentence_step_test, level='step', dataset='test')
    
    # ========================================================================
    # CROSS-DATASET COMPARISON
    # ========================================================================
    
    print("\n" + "=" * 70)
    print("CROSS-DATASET COMPARISON: TRAINING VS TEST")
    print("=" * 70)
    
    # 11. Compare consistency across datasets
    print("\n[11/12] Comparing consistency across datasets...")
    move_comparison = compare_datasets(df_train, df_test, metric='move_accuracy')
    step_comparison = compare_datasets(df_train, df_test, metric='step_accuracy')
    
    # Compare ICCs
    compare_icc_across_datasets(icc_train_move, icc_test_move, icc_train_step, icc_test_step)
    
    # Create cross-dataset visualizations
    create_cross_dataset_comparison_plot(df_train, df_test, move_comparison)
    
    # ========================================================================
    # SECONDARY ANALYSIS: EXAMPLE SELECTION (EXPLORATORY)
    # ========================================================================
    
    print("\n" + "=" * 70)
    print("SECONDARY ANALYSIS: EXAMPLE SELECTION (EXPLORATORY)")
    print("=" * 70)
    
    # 12. Alternative example sets
    print("\n[12/12] Analyzing example selection effects...")
    df_alt_examples = load_alternative_example_results()
    
    # Use test set zero-shot mean for comparison
    zero_shot_mean_test = df_test['move_accuracy'].mean()
    analyze_example_selection_effects(df_alt_examples, zero_shot_mean_test)
    
    zero_shot_ci_test = (move_consistency_test['ci_lower'], move_consistency_test['ci_upper'])
    plot_example_selection_comparison(df_alt_examples, zero_shot_mean_test, zero_shot_ci_test)
    
    # ========================================================================
    # SUMMARY REPORT
    # ========================================================================
    
    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)
    print("\nOutputs saved to:")
    print("  - CSV files: evaluation_results/")
    print("  - Figures: figures/")
    print("\nKey Findings:")
    print("\nTRAINING SET (Primary, 30 articles):")
    print(f"  Mean accuracy: {move_consistency_train['mean']:.1%} (CV = {move_consistency_train['cv']:.2f}%)")
    print(f"  ICC(2,1): {icc_train_move:.3f}")
    print("\nTEST SET (Replication, 10 articles):")
    print(f"  Mean accuracy: {move_consistency_test['mean']:.1%} (CV = {move_consistency_test['cv']:.2f}%)")
    print(f"  ICC(2,1): {icc_test_move:.3f}")
    print("\nCROSS-DATASET:")
    print(f"  CV difference: {abs(move_consistency_train['cv'] - move_consistency_test['cv']):.2f} pp")
    print(f"  ICC difference: {abs(icc_train_move - icc_test_move):.3f}")
    print("\nALTERNATIVE EXAMPLES (Exploratory, 5 sets):")
    print(f"  Mean (5 sets): {df_alt_examples['move_accuracy'].mean():.1%}")
    print(f"  Range: {(df_alt_examples['move_accuracy'].max() - df_alt_examples['move_accuracy'].min())*100:.1f} pp")
    print(f"  vs Zero-shot (test): {zero_shot_mean_test:.1%}")
    
if __name__ == "__main__":
    main()
```

---

## How to Report Results

### Primary Analysis (Zero-Shot Consistency)

**Template for Results Section:**

> Zero-shot annotation demonstrated [excellent/good/moderate/poor] consistency across 50 repeated runs on the test set. Move-level accuracy exhibited a mean of XX.X% (SD = X.X%, CV = X.X%), with a 95% confidence interval of [XX.X%, XX.X%]. The intraclass correlation coefficient was ICC(2,1) = 0.XXX, indicating [excellent/good/moderate/poor] reliability.
>
> Sentence-level analysis revealed that XX% of sentences were consistently annotated correctly across all 50 runs, while XX% showed high uncertainty (agreement rate 30-70%). Mean prediction entropy was X.XX bits (range: X.XX - X.XX), suggesting [low/moderate/high] variability in model predictions at the sentence level.
>
> Consistency varied significantly across move categories (F(2, XXX) = X.XX, p < .001), with Move X showing the highest agreement rate (M = XX%) and Move X the lowest (M = XX%).

### Secondary Analysis (Example Selection)

**Template for Results Section:**

> As an exploratory follow-up to the unexpected zero-shot superiority, we evaluated 5 alternative randomly selected 3-shot example sets (seeds: 100, 200, 300, 400, in addition to the original seed 42). Move-level accuracy ranged from XX.X% to XX.X% (M = XX.X%, SD = X.X%), representing a span of XX.X percentage points. [None/X] of the 5 sets exceeded the zero-shot mean accuracy of XX.X%.
>
> This preliminary evidence suggests that [example selection has substantial impact on few-shot performance / few-shot underperformance is robust to example selection]. However, given the small sample size (N = 5 sets, each evaluated once), these results should be interpreted as hypothesis-generating rather than conclusive. Systematic investigation of example selection strategies is warranted in future research.

---

## Interpretation Guide

### Coefficient of Variation (CV)
- **< 5%:** Excellent consistency
- **5-10%:** Good consistency
- **10-20%:** Moderate consistency
- **> 20%:** Poor consistency

### ICC(2,1)
- **< 0.5:** Poor reliability
- **0.5-0.75:** Moderate reliability
- **0.75-0.9:** Good reliability
- **> 0.9:** Excellent reliability

### Agreement Rate (Sentence-Level)
- **> 90%:** High confidence sentence
- **70-90%:** Moderate confidence
- **30-70%:** Uncertain sentence
- **< 30%:** Consistently problematic

### Example Selection Range
- **< 2 pp:** Minimal impact
- **2-5 pp:** Moderate impact
- **> 5 pp:** Substantial impact

---

## Checklist

### Primary Analysis
- [ ] All 50 zero-shot runs collected and parsed
- [ ] Aggregate consistency metrics calculated (mean, SD, CV, ICC)
- [ ] Sentence-level analysis completed
- [ ] Stratified analysis by move/step
- [ ] All visualizations created
- [ ] Results tables formatted for paper

### Secondary Analysis
- [ ] 5 alternative example sets generated
- [ ] Each set evaluated once on test set
- [ ] Descriptive statistics calculated
- [ ] Comparison to zero-shot completed
- [ ] Visualization created
- [ ] Limitations clearly stated

### Reporting
- [ ] Distinguish primary (inferential) from secondary (exploratory)
- [ ] Acknowledge small N for example selection
- [ ] Frame example selection as hypothesis-generating
- [ ] Recommend future systematic investigation

---

**This analysis plan provides a focused, rigorous approach to Phase 2 that maintains scientific integrity while honestly addressing the unexpected finding.**
