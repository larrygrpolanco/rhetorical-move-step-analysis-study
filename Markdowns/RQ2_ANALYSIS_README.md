# RQ2 Analysis Pipeline - README

## Overview
This folder contains the complete analysis pipeline for Research Question 2 (RQ2): Consistency analysis comparing zero-shot and fine-tuned approaches across 50 runs each.

## Folder Structure

```
evaluation_results/
├── zero_shot_rq2/          # Zero-shot run evaluations (50 runs)
│   ├── run_01.json/csv/md
│   ├── run_02.json/csv/md
│   └── ... (runs 01-50)
├── fine_tuned_rq2/         # Fine-tuned run evaluations (50 runs)
│   ├── run_01.json/csv/md
│   └── ... (runs 01-50)
└── rq2_analysis/           # Aggregated analysis results
    ├── zero_shot_all_runs.csv
    ├── zero_shot_descriptive_stats.csv
    ├── zero_shot_consistency_summary.txt
    ├── fine_tuned_all_runs.csv
    ├── fine_tuned_descriptive_stats.csv
    ├── fine_tuned_consistency_summary.txt
    ├── comparison_comprehensive.csv
    ├── comparison_variance_tests.csv
    ├── comparison_mean_tests.csv
    ├── comparison_summary.txt
    ├── sentences_*.csv (6 files)
    └── sentences_summary.txt

figures/
└── rq2/                    # Publication-ready figures
    ├── figure1_distributions.png
    ├── figure2_cv_comparison.png
    ├── figure3_sentence_consistency.png
    ├── figure4_tradeoff.png
    ├── figure5_boxplots.png
    └── supplementary_qqplots.png
```

## Scripts (Run in Order)

### 1. evaluate_rq2_runs.py
**Purpose:** Batch evaluate all 50 runs for one condition

**Configuration:**
```python
CONDITION = "zero_shot"  # or "fine_tuned"
DATASET = "test"
```

**What it does:**
- Auto-discovers completed runs in `outputs/{condition}/rq2_run_XX/`
- Evaluates each run against gold standard
- Creates 3 files per run: JSON (metrics), CSV (sentence details), MD (summary)

**Outputs:** 
- `evaluation_results/{condition}_rq2/run_01.json` through `run_50.json` (+ csv, md)

**Run twice:** Once for zero_shot, once for fine_tuned

---

### 2. analyze_consistency_rq2.py
**Purpose:** Calculate within-condition consistency metrics

**Configuration:**
```python
CONDITION = "zero_shot"  # or "fine_tuned"
DATASET = "test"
```

**What it does:**
- Loads all 50 runs for one condition
- Calculates descriptive stats (mean, SD, CV, CI, range, IQR)
- Tests for normality (Shapiro-Wilk)
- Creates consolidated CSVs and summary report

**Outputs:**
- `evaluation_results/rq2_analysis/{condition}_all_runs.csv`
- `evaluation_results/rq2_analysis/{condition}_descriptive_stats.csv`
- `evaluation_results/rq2_analysis/{condition}_consistency_summary.txt`

**Run twice:** Once for zero_shot, once for fine_tuned

---

### 3. compare_consistency_rq2.py
**Purpose:** Compare zero-shot vs fine-tuned conditions

**Configuration:** None needed (automatically compares both)

**What it does:**
- Variance comparison (Levene's test)
- Mean comparison (Welch's t-test)
- Effect size calculation (Cohen's d)
- Creates comprehensive comparison table for manuscript

**Outputs:**
- `evaluation_results/rq2_analysis/comparison_comprehensive.csv`
- `evaluation_results/rq2_analysis/comparison_variance_tests.csv`
- `evaluation_results/rq2_analysis/comparison_mean_tests.csv`
- `evaluation_results/rq2_analysis/comparison_summary.txt`

**Run once:** After both conditions analyzed

---

### 4. analyze_sentences_rq2.py
**Purpose:** Track sentence-level consistency across all runs

**Configuration:** None needed (analyzes both conditions)

**What it does:**
- Calculates agreement rate for each sentence (% runs correct)
- Shannon entropy (label distribution uncertainty)
- Modal prediction (most common label)
- Categorizes sentences (high/moderate/uncertain/problematic)
- Compares conditions sentence-by-sentence

**Outputs:**
- `evaluation_results/rq2_analysis/sentences_zero_shot_move.csv`
- `evaluation_results/rq2_analysis/sentences_fine_tuned_move.csv`
- `evaluation_results/rq2_analysis/sentences_zero_shot_step.csv`
- `evaluation_results/rq2_analysis/sentences_fine_tuned_step.csv`
- `evaluation_results/rq2_analysis/sentences_comparison_move.csv`
- `evaluation_results/rq2_analysis/sentences_comparison_step.csv`
- `evaluation_results/rq2_analysis/sentences_summary_stats.csv`
- `evaluation_results/rq2_analysis/sentences_summary.txt`

**Run once:** After both conditions analyzed

---

### 5. visualize_rq2.py
**Purpose:** Create all publication-ready figures

**Configuration:** None needed

**What it does:**
- Creates 5 main figures + supplementary
- High resolution (300 DPI) for publication
- Professional styling with clear labels

**Main Figures:**
1. Accuracy distributions (histograms + density curves)
2. CV comparison (bar chart)
3. Sentence consistency heatmaps
4. Accuracy-consistency trade-off (scatter plot)
5. Distribution comparisons (boxplots)

**Supplementary:**
- Q-Q plots for normality assessment

**Outputs:**
- `figures/rq2/figure1_distributions.png`
- `figures/rq2/figure2_cv_comparison.png`
- `figures/rq2/figure3_sentence_consistency.png`
- `figures/rq2/figure4_tradeoff.png`
- `figures/rq2/figure5_boxplots.png`
- `figures/rq2/supplementary_qqplots.png`

**Run once:** After all analyses complete

---

## Complete Workflow

```bash
# Step 1: Evaluate zero-shot runs (after running run_condition.py 50 times)
python evaluate_rq2_runs.py  # Set CONDITION = "zero_shot"

# Step 2: Evaluate fine-tuned runs (after running run_condition.py 50 times)
python evaluate_rq2_runs.py  # Set CONDITION = "fine_tuned"

# Step 3: Analyze zero-shot consistency
python analyze_consistency_rq2.py  # Set CONDITION = "zero_shot"

# Step 4: Analyze fine-tuned consistency
python analyze_consistency_rq2.py  # Set CONDITION = "fine_tuned"

# Step 5: Compare conditions
python compare_consistency_rq2.py

# Step 6: Analyze sentence-level consistency
python analyze_sentences_rq2.py

# Step 7: Create visualizations
python visualize_rq2.py
```

## Key Outputs for Manuscript

1. **Table 1 (Descriptive Statistics):**
   - Use: `comparison_comprehensive.csv`

2. **Statistical Test Results:**
   - Use: `comparison_summary.txt` or individual test CSVs

3. **Figures:**
   - All figures in `figures/rq2/` ready for publication

4. **Sentence-Level Analysis:**
   - Use: `sentences_summary.txt` and comparison CSVs

## Dependencies

```bash
pip install pandas numpy scipy scikit-learn matplotlib seaborn pingouin
```

- `pingouin` is optional (for ICC and effect sizes), will skip if not available
- All core functionality works without it

## Notes

- Scripts are designed to be run independently (no chaining required)
- Each script has clear error messages if prerequisites aren't met
- All outputs are both machine-readable (CSV/JSON) and human-readable (TXT/MD)
- Scripts auto-detect available data and skip missing files gracefully

## Expected Run Times

- `evaluate_rq2_runs.py`: ~1-2 minutes (50 runs)
- `analyze_consistency_rq2.py`: ~5-10 seconds
- `compare_consistency_rq2.py`: ~5 seconds
- `analyze_sentences_rq2.py`: ~30-60 seconds (processes ~13,350 sentence-run pairs)
- `visualize_rq2.py`: ~10-20 seconds

**Total analysis time:** ~2-5 minutes after data collection complete

---

## Troubleshooting

**Error: "No completed runs found"**
- Make sure you've run `run_condition.py` to generate outputs
- Check that parsed JSON files exist in `outputs/{condition}/rq2_run_XX/parsed/`

**Error: "Statistics not found for {condition}"**
- Run `analyze_consistency_rq2.py` for that condition first

**Error: "No sentence data found"**
- Check that CSV files exist in `evaluation_results/{condition}_rq2/`
- Re-run `evaluate_rq2_runs.py` if needed

**Import errors (pingouin)**
- Script will run without pingouin, just skips ICC calculation
- Install with: `pip install pingouin` if needed
