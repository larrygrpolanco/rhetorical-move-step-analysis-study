# LLM Consistency in Rhetorical Move-Step Annotation

**A methodological study evaluating the reliability of GPT-4 for automated rhetorical analysis of scientific writing**

---

## What This Project Is About

This repository contains the complete analysis pipeline for a research study that asks a fundamental question about using AI for rhetorical analysis: **When we ask an AI to analyze the same text multiple times, how consistent are its answers?**

### The Big Picture

Large Language Models (LLMs) like GPT-4 are increasingly used to automate rhetorical move-step annotation—the task of identifying the communicative functions of sentences in academic writing (e.g., "establishing a research territory" or "indicating a gap"). While researchers have shown these models can be *accurate*, we don't know if they're *consistent*.

This study fills that gap by running the same annotation task **50 times per condition** and systematically measuring variability.

### Why This Matters

Imagine a researcher uses GPT-4 to annotate 100 research articles. If the model gives different answers each time it sees the same text, those results aren't trustworthy—even if the average accuracy is high. This study quantifies that reliability problem and identifies which approaches (zero-shot prompting vs. fine-tuning) produce more consistent annotations.

---

## Research Questions

**RQ1 (Phase 1):** How do zero-shot, few-shot (3-shot and 8-shot), and fine-tuned GPT-4 perform on Biology research article move-step annotation?

**RQ2 (Phase 2 ):** How consistent is annotation across repeated runs for zero-shot and fine-tuned approaches? Does higher accuracy come with higher consistency?

---

## Theoretical Foundation

This work builds directly on **Kim & Lu (2024)**, who demonstrated that fine-tuned GPT models could perform rhetorical annotation with high accuracy on Applied Linguistics texts. They noted:

> "Validation of output consistency is strongly recommended to confirm model reliability." (p. 11)

**Our Contribution:** We provide that systematic consistency validation—running 50 evaluations per condition (16× more than Kim & Lu's 3 runs) to characterize variability.

### What We Extend

- **Domain:** Applied Linguistics → **Biology** research articles
- **Framework:** COSSRAI (23 steps) → **CaRS** (11 steps)
- **Model:** GPT-3.5-turbo → **GPT-4** (gpt-4.1-2025-04-14)
- **Scale:** 3 consistency runs → **50 consistency runs**
- **Analysis:** Single-run accuracy → **Systematic consistency characterization**

---

## Dataset & Experimental Design

### Dataset: CaRS-50

- **Source:** Biology research article introductions annotated with the Creating a Research Space (CaRS) framework
- **Size:** 50 articles total
- **Framework:** 3 moves, 11 steps (simplified from Kim & Lu's 23-step scheme)
- **Split:** 
  - Training: 30 articles (60%) - for fine-tuning
  - Validation: 10 articles (20%) - for prompt development
  - Test: 10 articles (20%) - for evaluation (~267 sentences)

### Study Design: Two Phases

#### Phase 1: Initial Performance Evaluation (Validation Set)

Evaluated **4 conditions** with **1 run each** on the validation set:

1. **A1: Zero-Shot** - Prompt only, no examples
2. **A2: Few-Shot (3 examples)** - Prompt + 3 annotated articles
3. **A3: Few-Shot (8 examples)** - Prompt + 8 annotated articles
4. **A4: Fine-Tuned** - GPT-4 fine-tuned on 30 training articles

**Key Finding:** Zero-shot achieved 87.3% move-level accuracy—matching or exceeding few-shot (84.3%, 83.8%) and fine-tuned (83.8%). McNemar's test showed no significant differences.

**The Surprise:** This contradicted expectations. Fine-tuning typically provides substantial improvements. Either zero-shot is genuinely as good, or there's an accuracy-consistency trade-off we can't see from single runs.

#### Phase 2: Consistency Analysis (Test Set)

Focused on **2 conditions** with **50 runs each** on the held-out test set:

1. **Zero-Shot** - Simplest approach (no training data needed)
2. **Fine-Tuned** - Most resource-intensive approach

**Why 50 runs?**
- Provides >95% statistical power to detect moderate variance differences
- Enables 13,350 sentence-run observations per condition
- 16× more robust than prior work's 3-run approach

**Why only 2 conditions?**
- Focus depth over breadth: test extremes of the complexity spectrum
- Simplifies narrative: "simplest vs. most sophisticated"
- Practical relevance: these are the approaches researchers actually choose between

---


### Statistical Sophistication

- **Variance comparison** (Levene's test) - not just mean accuracy
- **Intraclass Correlation Coefficient (ICC)** - standard reliability metric
- **Coefficient of Variation (CV)** - enables consistency comparison across different scales
- **Sentence-level analysis** - identifies which specific sentences are problematic
- **Stratified analysis** - consistency patterns by move type and step type

### Practical Impact

Regardless of results, this study provides actionable guidance:
- When is zero-shot "good enough" vs. when is fine-tuning worth the cost?
- How much annotation variability should researchers expect?
- Which sentences/categories are inherently more difficult?
- What consistency benchmarks should practitioners aim for?

---

## Repository Structure

```
rhetorical-move-step-analysis-study/
│
├── data/
│   ├── gold_standard/          # Ground truth annotations
│   ├── training/                # Fine-tuning data (30 articles)
│   ├── validation/              # Prompt development data (10 articles)
│   └── test/                    # Evaluation data (10 articles)
│
├── prompts/
│   ├── system_prompt.txt          # Core annotation instructions
│   └── fine_tuning_format.jsonl # A4 training format
│
├── outputs/
│   ├── zero_shot/               # Raw LLM outputs + parsed results
│   │   ├── phase1_validation/
│   │   └── rq2_run_01/ ... rq2_run_50/
│   └── fine_tuned/
│       ├── phase1_validation/
│       └── rq2_run_01/ ... rq2_run_50/
│
├── evaluation_results/
│   ├── zero_shot_rq2/           # Evaluation metrics for 50 runs
│   ├── fine_tuned_rq2/          # Evaluation metrics for 50 runs
│   └── rq2_analysis/            # Aggregated statistics and comparisons
│       ├── *_all_runs.csv           # Complete run-level data
│       ├── *_descriptive_stats.csv  # Summary statistics
│       ├── *_consistency_summary.txt # Human-readable summaries
│       ├── comparison_*.csv          # Between-condition tests
│       └── sentences_*.csv           # Sentence-level consistency
│
├── figures/
│   └── rq2/                     # Publication-ready visualizations
│       ├── figure1_distributions.png
│       ├── figure2_cv_comparison.png
│       ├── figure3_sentence_consistency.png
│       ├── figure4_tradeoff.png
│       └── figure5_boxplots.png
│
├── scripts/
│   ├── run_condition.py             # Execute annotation runs
│   ├── parse_llm_output.py          # Extract structured data
│   ├── evaluate_run.py              # Compare to gold standard
│   ├── evaluate_rq2_runs.py         # Batch evaluate all 50 runs
│   ├── analyze_consistency_rq2.py   # Within-condition statistics
│   ├── compare_consistency_rq2.py   # Between-condition comparisons
│   ├── analyze_sentences_rq2.py     # Sentence-level patterns
│   └── visualize_rq2.py             # Generate all figures
│
└── docs/
    ├── STUDY_DESIGN_FINAL.md            # Complete methodology
    ├── STATISTICAL_ANALYSIS_PLAN.md     # Analysis procedures
    ├── PHASE_2_STUDY_DESIGN_REVISED.md  # RQ2 detailed design
    └── RQ2_ANALYSIS_README.md           # Pipeline execution guide
```

---

## Key Outputs & Results

### Data Products

**100 Complete Evaluations:**
- 50 zero-shot runs on test set
- 50 fine-tuned runs on test set
- Each includes: raw output, parsed JSON, evaluation metrics, sentence-level results

**Aggregated Statistics:**
- Descriptive statistics per condition (mean, SD, CV, ICC, CI)
- Normality tests (Shapiro-Wilk, Q-Q plots)
- Variance comparison (Levene's test)
- Mean comparison (Welch's t-test)
- Effect sizes (Cohen's d, variance ratios)

**Sentence-Level Analysis:**
- Agreement rate: % runs where model was correct for each sentence
- Shannon entropy: uncertainty in label distribution
- Modal prediction: most common prediction across runs
- Consistency categories: high/moderate/uncertain/consistently-problematic

### Statistical Tests Performed

1. **Variance Comparison** (Levene's test)
   - Null hypothesis: Zero-shot and fine-tuned have equal variance
   - Directly tests RQ2's core question about consistency

2. **Mean Comparison** (Welch's t-test)
   - Accounts for unequal variances
   - Determines if accuracy differs between conditions

3. **Reliability Assessment** (ICC)
   - ICC(2,1): consistency of annotations across runs
   - Interpretation: <0.5=poor, 0.5-0.75=moderate, 0.75-0.9=good, >0.9=excellent

4. **Normality Assessment** (Shapiro-Wilk)
   - Validates parametric test assumptions
   - Q-Q plots provide visual confirmation

### Visualizations

**Figure 1: Accuracy Distributions**
- Histograms + density curves for both conditions
- Shows central tendency and spread
- Reveals distribution shape (normal, skewed, bimodal)

**Figure 2: Coefficient of Variation Comparison**
- Bar chart directly comparing consistency
- Lower CV = more consistent
- Primary visual for RQ2

**Figure 3: Sentence Consistency Heatmaps**
- Each row = one test sentence
- Color intensity = agreement rate across 50 runs
- Identifies problematic sentences

**Figure 4: Accuracy-Consistency Trade-off**
- Scatter plot: mean accuracy vs. CV
- Shows whether high accuracy comes with high consistency
- Ideal quadrant: high accuracy, low CV

**Figure 5: Boxplot Comparisons**
- Distribution comparison between conditions
- Shows median, quartiles, outliers
- Alternative view to histograms

---

## Key Metrics Explained

### For Researchers New to Consistency Analysis

**Accuracy** - What percentage of sentences did the model label correctly? (averaged across runs)

**Standard Deviation (SD)** - How much do individual run accuracies vary from the mean?

**Coefficient of Variation (CV)** - SD as a percentage of the mean. Allows comparing variability across different scales.
- CV < 5%: Excellent consistency
- CV 5-10%: Good consistency
- CV 10-20%: Moderate consistency
- CV > 20%: Poor consistency

**Intraclass Correlation Coefficient (ICC)** - What proportion of total variance is due to true differences (between sentences) vs. measurement error (between runs)?
- Higher ICC = more reliable measurement
- Used in fields like psychology, medicine, education

**Variance Ratio** - How much bigger is one condition's variance compared to another?
- Ratio = 2.0 means Condition A is twice as variable as Condition B

**Cohen's d** - Standardized mean difference. Effect size independent of sample size.
- 0.2 = small, 0.5 = medium, 0.8 = large effect

---

## Technical Details

### Model & Parameters

- **Model:** GPT-4 (`gpt-4.1-2025-04-14`) - fine-tunable version
- **Temperature:** 1.0 (matches Kim & Lu; allows natural variability)
- **Max Tokens:** 4096
- **Fine-Tuning:** OpenAI API supervised fine-tuning with default hyperparameters

### Temperature Rationale

We use temperature=1.0 (not 0) to:
- Match prior work methodology for comparability
- Measure consistency under realistic deployment conditions
- Allow the model's natural variability to manifest (which is what we aim to characterize)

While lower temperatures might reduce variance, our goal is to understand the model's **actual** consistency, not artificially constrain it. This allows findings to generalize to typical use cases where researchers employ default temperature settings.

### Fine-Tuning Specifications

- **Training data:** 30 articles formatted as system-user-assistant message triplets
- **Validation split:** 20% held out during training
- **Epochs:** Determined automatically by OpenAI API (early stopping based on validation performance)
- **Checkpoint:** Single fine-tuned model used for all 50 test runs

### Parsing & Evaluation

**Deterministic Parser:**
- Extracts sentence-level predictions from LLM free-text output
- Regex-based pattern matching: `[MOVE-STEP] sentence text`
- Handles common formatting variations
- Logs unparseable outputs for manual review

**Evaluation Metrics:**
- **Move-level:** Accuracy, Precision, Recall, F1 (for each of 3 moves)
- **Step-level:** Accuracy, Precision, Recall, F1 (for each of 11 steps)
- **Aggregate:** Weighted F1 (accounts for class imbalance)
- **Per-sentence:** Binary correct/incorrect for downstream analysis

---

## Interpretation Scenarios

We identified three plausible outcome patterns before data collection:

### Scenario 1: Zero-Shot Wins on Both Dimensions

**Findings:** Zero-shot has both higher mean accuracy AND lower variance than fine-tuned

**Interpretation:** Challenges conventional wisdom. For this task/framework, zero-shot may be genuinely superior.

**Implication:** Simpler is better. Fine-tuning may not be justified.

### Scenario 2: Accuracy-Consistency Trade-off

**Findings:** Zero-shot has higher mean accuracy but much higher variance. Fine-tuned is more stable.

**Interpretation:** Zero-shot is "right on average" but unreliable for individual instances.

**Implication:** Method choice depends on use case:
- Bulk annotation / corpus studies → zero-shot acceptable
- Critical applications / individual decisions → fine-tuned required

### Scenario 3: Fine-Tuning Superiority

**Findings:** Fine-tuned has both higher accuracy and lower variance on test set.

**Interpretation:** Validation set results were anomalous or unrepresentative. Expected pattern confirmed.

**Implication:** Fine-tuning justified despite resource cost. Original hypothesis validated.

---

## Limitations & Scope

### What This Study Does

✅ Systematically evaluates consistency across prompting conditions  
✅ Compares performance on Biology research articles  
✅ Demonstrates methodological transferability of Kim & Lu's framework  
✅ Provides practical guidance for method selection  
✅ Establishes consistency benchmarks for the field

### What This Study Does Not Do

❌ Test multiple domains simultaneously (Biology only)  
❌ Compare different LLM families (GPT-4 only)  
❌ Explore temperature effects (fixed at 1.0)  
❌ Optimize prompts iteratively (single-pass development)  
❌ Test all possible hyperparameter combinations

### Acknowledged Constraints

**Dataset Size:** 10-article test set limited by CaRS-50 availability
- *Mitigation:* 50-run design provides 500 article-level observations per condition
- *Precedent:* Matches Kim & Lu's test set size
- *Trade-off:* Adequate power for condition-level comparisons, limited power for fine-grained move/step analysis

**Single Domain:** Biology only
- *Implication:* Findings may not generalize to other disciplines
- *Future work:* Cross-domain consistency validation

**Single Model:** GPT-4 only
- *Implication:* Results may not generalize to Claude, Llama, etc.
- *Future work:* Cross-model consistency comparison

**Few-Shot Examples:** Randomly selected, not optimized
- *Rationale:* Tests ecological validity—practitioners typically use convenience samples
- *Limitation:* Cannot rule out effects of strategic example selection

---

## Dependencies

### Required Python Packages

```bash
# Core analysis
pip install pandas numpy scipy scikit-learn

# Visualization
pip install matplotlib seaborn

# Optional (for ICC and advanced stats)
pip install pingouin statsmodels

# OpenAI API
pip install openai
```

All scripts are designed to run without `pingouin` (gracefully skip ICC calculation if not available).

---

## Expected Run Times

**Data Collection (Phase 2):**
- Zero-shot: 50 runs × ~30 sec/article × 10 articles ≈ 4 hours
- Fine-tuned: 50 runs × ~30 sec/article × 10 articles ≈ 4 hours
- **Total:** ~8 hours + API costs (~$50-60)

**Analysis Pipeline:**
- Parsing & evaluation: ~2 hours
- Statistical analysis: ~4 hours
- Visualization: ~4 hours
- **Total:** ~10 hours

---

## Ethical Considerations

### Transparency

✅ Pre-registered research questions before data collection  
✅ Following original plan despite unexpected validation results  
✅ No post-hoc analyses driven by undesired findings  
✅ Honest acknowledgment of all limitations  
✅ Complete code, data, and prompts available

### Methodological Integrity

✅ Test set held out since Phase 1 (never used for development)  
✅ Fixed evaluation procedures across all runs  
✅ Complete reporting (no selective reporting)  
✅ Results reported regardless of direction  
✅ Alternative explanations considered

### Reproducibility

✅ Fixed random seeds where possible  
✅ Documented all design decisions  
✅ Provided complete reproducibility package  
✅ Shared prompts, examples, and gold standard (with appropriate permissions)

---

## Citation

If you use this code or methodology, please cite:

```bibtex
[Citation information to be added upon publication]
```

**Primary Reference:**
Kim, Y., & Lu, X. (2024). Automated rhetorical analysis using GPT-based large language models: Methods and validation. *Research Methods in Applied Linguistics*, *100618*. https://doi.org/10.1016/j.rmal.2024.100618

---

## Future Directions

This study opens several avenues for future research:

1. **Cross-Model Comparison:** Test consistency across GPT-4, Claude, Llama, and other LLMs
2. **Temperature Exploration:** Optimal temperature for balancing accuracy and consistency
3. **Cross-Domain Validation:** Apply same methodology to other disciplines
4. **Larger Scale:** 50+ test articles for finer-grained analysis
5. **Strategic Example Selection:** Compare random vs. similarity-based few-shot examples
6. **Real-Time Deployment:** Consistency in production annotation tools

---

## Contact & Support

For questions about methodology, please refer to:
- `docs/STUDY_DESIGN_FINAL.md` - Complete study design
- `docs/STATISTICAL_ANALYSIS_PLAN.md` - Analysis procedures
- `docs/RQ2_ANALYSIS_README.md` - Pipeline execution guide

For questions about the CaRS framework or CaRS-50 dataset, please consult:
- Omotola, B., et al. (2025). CaRS-50: Corpus of Biology research article introductions

---

## Acknowledgments

This work builds on the methodological foundations established by Kim & Lu (2024) and applies them to the CaRS annotation framework developed by Omotola et al. (2025). We thank the authors for making their work available and inspiring this consistency-focused extension.

---

## License

[License information to be added]

---

**Last Updated:** October 2024  
**Study Status:** Phase 2 Data Collection Complete, Analysis In Progress