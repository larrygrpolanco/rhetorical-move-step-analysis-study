# Phase 2 Study Design: Zero-Shot and Fine-Tuned Consistency Analysis

## Executive Summary

**Purpose:** Systematic evaluation of annotation consistency for the two prompting approaches  
**Design:** 50 repeated runs per condition on held-out test set  
**Conditions:** Zero-shot vs Fine-tuned  
**Dataset:** Test set only (10 articles, ~267 sentences)  
**Total Runs:** 100 (50 zero-shot + 50 fine-tuned)  
**Model:** GPT-4 (gpt-4.1-2025-04-14)  
**Key Extension:** Kim & Lu (2024) tested 3 runs; we test 50 for robust characterization

---

## Background and Rationale

### Phase 1 Results (Validation Set)

Phase 1 evaluated four prompting conditions on the validation set (10 articles):
- **A1 (Zero-shot):** 87.3% move-level accuracy
- **A2 (3-shot):** 84.3% move-level accuracy  
- **A3 (8-shot):** 83.8% move-level accuracy
- **A4 (Fine-tuned):** 83.8% move-level accuracy

**Key Finding:** Zero-shot unexpectedly matched or exceeded few-shot and fine-tuned approaches.

**Statistical Testing:** McNemar's test revealed no significant differences between conditions.

### Why This Finding Matters

This result contradicts expectations from Kim & Lu (2024) and similar work in applied linguistics, where fine-tuning typically provides substantial improvements. Two plausible explanations emerge:

1. **Accuracy-consistency trade-off:** Zero-shot may be less consistent despite similar mean accuracy
2. **Task characteristics:** The CaRS framework (11 steps) may be simpler or better aligned with GPT-4's pre-training

### The Critical Question

**RQ2:** How does annotation consistency differ between zero-shot and fine-tuned approaches, and does zero-shot's strong performance come at the cost of reliability?

---

## Research Question

**RQ2 (Consistency Analysis):** How consistent is annotation across repeated runs for zero-shot and fine-tuned approaches, and how do they compare?

**Sub-questions:**
- RQ2.1: What is the aggregate consistency for each condition (CV, ICC)?
- RQ2.2: How do zero-shot and fine-tuned compare in consistency?
- RQ2.3: Which sentences show high vs low consistency in each condition?
- RQ2.4: Do consistency patterns differ by move or step type?

---

## Methodological Design

### Core Design Principles

✅ **Test Set Only:** Maintains methodological integrity by using the designated held-out set  
✅ **Two Conditions:** Focuses comparison on most practical approaches (zero-shot = simplest, fine-tuned = most resource-intensive)  
✅ **50 Runs:** Provides robust statistical power (16× more than Kim & Lu's 3 runs)  
✅ **No Post-Hoc Exploration:** Follows pre-registered RQ1→RQ2 plan without tangential analyses

### Why These Two Conditions?

**Zero-Shot (A1):**
- Simplest approach (no training data, no examples)
- Highest validation accuracy (87.3%)
- Most accessible to researchers
- Baseline for consistency expectations

**Fine-Tuned (A4):**
- Most resource-intensive approach
- Expected to be most accurate (based on prior work)
- Industry best practice for task-specific annotation
- Key comparison point

**Excluded from Phase 2:**
- Few-shot conditions (A2, A3): Intermediate performance, less practical interest for consistency analysis
- Simplifies narrative: "simplest vs. most sophisticated"

---

## Dataset and Evaluation

### Test Set Specifications

**Size:** 10 articles (~267 sentences)  
**Status:** Held-out since Phase 1  
**Usage History:**
- Phase 1: Used for single-run evaluation of all 4 conditions
- Phase 2: Used for 50-run consistency analysis of 2 conditions

**Justification for Test-Only Design:**

1. **Methodological Convention:** Test sets are designated for final evaluation
2. **Clean Narrative:** All Phase 2 analyses conducted on the same held-out dataset
3. **Direct Comparison:** Zero-shot and fine-tuned evaluated on identical articles and runs
4. **Statistical Adequacy:** 10 articles × 50 runs = 500 observations per condition provides excellent power

### Sample Size Justification

**Why 50 Runs?**

Kim & Lu (2024) tested consistency with 3 repeated runs. We extend this to 50 runs for several reasons:

1. **Statistical Power:**
   - Power > 0.95 to detect moderate variance differences (Cohen's f = 0.25)
   - Sufficient for robust ICC estimation (ICC 95% CI width ≈ ±0.15)
   - Enables fine-grained sentence-level analysis

2. **Precision:**
   - 95% CI for SD: approximately ±25% of true value
   - Example: True SD = 3% → CI = [2.4%, 3.6%]
   - Adequate precision for meaningful conclusions

3. **Practical Feasibility:**
   - Balances rigor with computational cost (~50 hours total)
   - Represents 16× more runs than prior work
   - Provides diminishing returns beyond 50

**Why 10 Articles?**

Limited by CaRS-50 dataset availability (constrained to 50 total articles, with 30 reserved for training and 10 for validation). This 10-article test set:
- Matches Kim & Lu's (2024) test set size
- Represents standard practice for genre analysis studies
- Provides 267 sentences (~27 per article) for sentence-level analysis
- With 50 runs, yields 500 article-level and 13,350 sentence-level observations per condition

---

## Procedure

### Phase 2 Workflow

**Condition A1 (Zero-Shot) - 50 Runs:**

```python
FOR run in 1 to 50:
    1. Apply zero-shot prompt to test set (10 articles)
    2. Parse LLM output
    3. Evaluate against gold standard
    4. Save results: zero_shot_rq2_test_run_{01-50}.json
```

**Condition A4 (Fine-Tuned) - 50 Runs:**

```python
FOR run in 1 to 50:
    1. Apply fine-tuned model to test set (10 articles)
    2. Parse LLM output
    3. Evaluate against gold standard
    4. Save results: fine_tuned_rq2_test_run_{01-50}.json
```

**Fixed Elements Across All Runs:**
- Test set: Same 10 articles
- Prompts: Identical for each condition
- Model parameters: temperature=1.0, max_tokens=4096
- Fine-tuned checkpoint: Same model for all A4 runs
- Evaluation metrics: Identical calculation method

**Variable Element:**
- Random seed / stochastic sampling (natural LLM variability)

### Temperature = 1.0 Rationale

Following Kim & Lu (2024), we use temperature=1.0 to:
- Match prior work methodology
- Measure consistency under realistic deployment conditions
- Allow natural model variability (which is what we aim to characterize)
- Avoid artificially constraining model behavior

While lower temperatures might reduce variance, our goal is to understand the model's **actual** consistency, not artificially inflated reliability.

---

## Analysis Plan

### 1. Aggregate Consistency Metrics

**For each condition (Zero-shot, Fine-tuned):**

**Accuracy Distribution:**
- Mean accuracy ± SD
- 95% Confidence Interval
- Coefficient of Variation (CV = SD/Mean × 100%)
- Range (Max - Min)
- Interquartile Range (IQR)
- Median

**Reliability:**
- Intraclass Correlation Coefficient ICC(2,1)
- Interpretation: <0.5=poor, 0.5-0.75=moderate, 0.75-0.9=good, >0.9=excellent

**Distribution Assessment:**
- Shapiro-Wilk normality test
- Q-Q plots
- Histograms with kernel density

### 2. Between-Condition Comparison

**Primary Test:** Do zero-shot and fine-tuned differ in consistency?

**Variance Comparison:**
- Levene's test: H₀: σ²(zero-shot) = σ²(fine-tuned)
- Report F-statistic, p-value, effect size
- Variance ratio: σ²(A1) / σ²(A4)

**Accuracy Comparison:**
- Welch's t-test (allows unequal variances)
- Cohen's d effect size
- 95% CI for mean difference

**ICC Comparison:**
- Compare ICC(2,1) values
- Interpret practical significance

### 3. Sentence-Level Analysis

**For each sentence across 50 runs:**

**Metrics:**
- Agreement rate: % runs with correct prediction
- Entropy: Shannon entropy of label distribution
- Modal prediction: Most common label
- Flip frequency: Number of times label changed between consecutive runs

**Categorization:**
- High confidence: Agreement > 90%
- Moderate confidence: Agreement 70-90%
- Uncertain: Agreement 30-70%
- Consistently problematic: Agreement < 30%

**Comparison:**
- Which sentences are consistently easy/hard in both conditions?
- Which sentences show condition-specific variability?
- Identify systematic error patterns

### 4. Stratified Analysis

**By Move Type (M1, M2, M3):**
- Mean accuracy and CV per move
- One-way ANOVA: Does consistency vary by move?
- Compare between conditions

**By Step Type (11 categories):**
- Focus on well-represented steps (n ≥ 15 in test set)
- Identify high/low consistency steps
- Compare between conditions

**By Sentence Characteristics:**
- Sentence position (first, middle, last in article)
- Sentence length (short vs long)
- Exploratory correlations with consistency

---

## Reporting and Visualization

### Tables

**Table 1: Phase 1 Performance Summary (Validation Set)**
- Single-run accuracy for all 4 conditions
- McNemar's test results
- Sets up the "surprising result" motivation

**Table 2: Phase 2 Consistency Summary (Test Set, 50 Runs)**
- Aggregate metrics for zero-shot and fine-tuned
- Mean, SD, CV, ICC, Range for both conditions
- Direct side-by-side comparison

**Table 3: Between-Condition Statistical Comparison**
- Levene's test for variance
- Welch's t-test for means
- Effect sizes and interpretations

**Table 4: Sentence-Level Consistency Distribution**
- % sentences in each agreement category (high/moderate/uncertain/problematic)
- Separate columns for zero-shot and fine-tuned

**Table 5: Consistency by Move Type**
- Stratified CV and accuracy by M1, M2, M3
- Both conditions shown

### Figures

**Figure 1: Accuracy Distribution Across 50 Runs**
- Side-by-side violin plots or box plots
- Zero-shot vs Fine-tuned
- Shows central tendency and spread

**Figure 2: Coefficient of Variation Comparison**
- Bar chart with error bars
- Highlights consistency differences

**Figure 3: Sentence-Level Agreement Heatmap**
- Each row = one sentence
- Color intensity = agreement rate across 50 runs
- Separate panels for zero-shot and fine-tuned

**Figure 4: Accuracy vs Consistency Trade-off**
- Scatter plot: Mean accuracy (x-axis) vs CV (y-axis)
- Two points: zero-shot and fine-tuned
- Annotated with condition labels
- Ideal region (high accuracy, low CV) highlighted

**Figure 5: Consistency by Move Type**
- Grouped bar chart
- X-axis: Move type (M1, M2, M3)
- Y-axis: CV
- Two bars per move: zero-shot and fine-tuned

---

## Interpretation Guidelines

### Coefficient of Variation (CV)

- **CV < 5%:** Excellent consistency (very stable)
- **CV 5-10%:** Good consistency (acceptable variation)
- **CV 10-20%:** Moderate consistency (noticeable variation)
- **CV > 20%:** Poor consistency (high instability)

### Intraclass Correlation Coefficient (ICC)

- **ICC < 0.5:** Poor reliability (unacceptable)
- **ICC 0.5-0.75:** Moderate reliability (acceptable with caution)
- **ICC 0.75-0.9:** Good reliability (suitable for research)
- **ICC > 0.9:** Excellent reliability (suitable for applied use)

### Practical Implications

**Best Case:** Zero-shot achieves high accuracy AND high consistency
- Recommendation: Zero-shot is viable for both research and applied annotation

**Mixed Case:** Zero-shot has high accuracy but low consistency
- Recommendation: Zero-shot suitable for aggregate analyses, not individual article decisions
- Fine-tuning provides more reliable instance-level predictions

**Worst Case:** Zero-shot has both lower accuracy and lower consistency
- Recommendation: Fine-tuning justified despite resource cost
- Zero-shot may still be useful for exploratory work

---

## Expected Results and Scenarios

### Scenario 1: Zero-Shot Wins on Both Dimensions

**Findings:**
- Zero-shot: Mean accuracy ≈ 87%, CV ≈ 3%, ICC ≈ 0.85
- Fine-tuned: Mean accuracy ≈ 84%, CV ≈ 2%, ICC ≈ 0.90

**Interpretation:** Zero-shot is both more accurate and reasonably consistent. Fine-tuned is slightly more consistent but less accurate.

**Implication:** Challenges conventional wisdom; zero-shot may be preferred for this task.

### Scenario 2: Accuracy-Consistency Trade-off

**Findings:**
- Zero-shot: Mean accuracy ≈ 87%, CV ≈ 15%, ICC ≈ 0.60
- Fine-tuned: Mean accuracy ≈ 84%, CV ≈ 4%, ICC ≈ 0.88

**Interpretation:** Zero-shot has higher mean but much more variability. Fine-tuned is more stable.

**Implication:** Choice depends on use case. Bulk annotation → zero-shot. Critical applications → fine-tuned.

### Scenario 3: Fine-Tuning Recovers on Test Set

**Findings:**
- Zero-shot: Mean accuracy ≈ 83%, CV ≈ 6%, ICC ≈ 0.75
- Fine-tuned: Mean accuracy ≈ 89%, CV ≈ 3%, ICC ≈ 0.90

**Interpretation:** Validation set was unrepresentative. Fine-tuning superiority confirmed on test set.

**Implication:** Original hypothesis validated; fine-tuning recommended.

---

## Relationship to Kim & Lu (2024)

### What We Replicate

✅ Methodological framework (zero-shot, fine-tuning comparison)  
✅ Evaluation metrics (accuracy, precision, recall, F1)  
✅ Target genre (research article introductions)  
✅ Temperature setting (1.0)

### What We Adapt

🔄 Domain: Applied Linguistics → Biology  
🔄 Model: GPT-3.5-turbo → GPT-4  
🔄 Framework: COSSRAI (23 steps) → CaRS (11 steps)  
🔄 Dataset: Custom corpus → CaRS-50

### What We Extend (Novel Contribution)

✨ **Primary Extension:** 50 runs per condition (vs. Kim & Lu's 3 runs)  
✨ **Statistical rigor:** Robust variance comparison, ICC analysis  
✨ **Sentence-level analysis:** Identify high/low consistency instances  
✨ **Stratified analysis:** Consistency patterns by move/step type

**Kim & Lu's Conclusion (p. 11):**
> "Third, validation of output consistency is strongly recommended to confirm model reliability."

**Our Study:** Provides the systematic consistency validation they recommended.

---

## Success Criteria

### Minimum Success

✅ All 100 runs completed and parsed successfully  
✅ Measurable variance exists (not all runs identical)  
✅ Statistically significant difference in at least one metric (accuracy or consistency)  
✅ Interpretable patterns (can explain results with theoretical grounding)

### Strong Success

✅ Clear consistency hierarchy between conditions  
✅ CV differs by ≥ 2 percentage points  
✅ Sentence-level patterns reveal systematic factors influencing consistency  
✅ Actionable recommendations for method selection based on use case

### Publication Viability

**Core Contribution:** First systematic multi-run consistency analysis for LLM rhetorical annotation

**Even if results contradict expectations:** Empirical findings are valuable regardless of direction. Unexpected results are often most interesting to reviewers.

---

## Limitations (Acknowledged)

### Dataset Constraints

1. **Test set size:** 10 articles (~267 sentences) limited by CaRS-50 availability
   - *Mitigation:* 50-run design provides 500 article-level observations
   - *Precedent:* Matches Kim & Lu (2024) test set size

2. **Single domain:** Biology research articles only
   - *Implication:* Findings may not generalize to other disciplines
   - *Future work:* Cross-domain consistency validation

### Design Constraints

3. **Two conditions only:** Few-shot excluded from Phase 2
   - *Justification:* Focuses on most practical comparison (simplest vs. most sophisticated)
   - *Trade-off:* Gains depth on key comparison, sacrifices breadth

4. **Single model family:** GPT-4 only
   - *Implication:* Results may not generalize to other LLMs
   - *Future work:* Cross-model consistency comparison

5. **Fixed temperature:** 1.0 only
   - *Justification:* Matches Kim & Lu; measures realistic deployment consistency
   - *Future work:* Temperature effects on consistency

### Methodological Constraints

6. **Example selection not systematically controlled**
   - *Acknowledgment:* Few-shot examples randomly selected (seed=42)
   - *Implication:* Example selection effects cannot be ruled out as partial explanation for Phase 1 results
   - *Future work:* Systematic investigation of example selection strategies (similarity-based, stratified, prototype selection)

---

## Ethical Considerations

### Transparency

✅ Pre-registered RQ1 and RQ2 design  
✅ Following original plan despite unexpected validation results  
✅ No post-hoc analyses driven by undesired findings  
✅ Honest acknowledgment of limitations  
✅ Full code and data availability

### Methodological Integrity

✅ Test set held out since Phase 1  
✅ No hyperparameter tuning on test set  
✅ Fixed evaluation procedures across all runs  
✅ Complete reporting (no selective reporting)  
✅ Reproducibility package provided

### Intellectual Honesty

✅ Results reported regardless of direction  
✅ Unexpected findings framed as empirical observations requiring explanation  
✅ Limitations stated prominently  
✅ Alternative explanations considered  
✅ Future research directions suggested rather than definitive claims

---

## Deliverables

### 1. Data Artifacts

- 100 raw LLM output files (50 per condition)
- 100 parsed JSON files
- 100 evaluation result files
- Consolidated CSV: all 100 runs with metrics

### 2. Statistical Outputs

- Aggregate consistency summary tables
- Sentence-level analysis CSV
- Stratified analysis results
- All statistical test outputs

### 3. Visualizations

- 5 main figures (publication-ready)
- Supplementary figures (exploratory analyses)
- All figures as high-resolution PDFs and PNGs

### 4. Manuscript Sections

- Methods: Phase 2 design and rationale
- Results: Comprehensive reporting with tables and figures
- Discussion: Interpretation and implications
- Supplementary materials: Full prompts, examples, detailed results

### 5. Reproducibility Package

- Complete Python codebase
- README with setup instructions
- Requirements.txt
- Example usage notebooks
- Raw data (with permission)

---

## Timeline and Compute

### Phase 2 Execution

**Zero-Shot (50 runs):**
- 10 articles × 50 runs = 500 API calls
- Estimated: ~30 seconds per article
- Total time: ~4 hours
- Cost: ~$25-30 (estimated)

**Fine-Tuned (50 runs):**
- 10 articles × 50 runs = 500 API calls
- Estimated: ~30 seconds per article
- Total time: ~4 hours
- Cost: ~$25-30 (estimated)

**Analysis:**
- Parsing and evaluation: ~2 hours
- Statistical analysis: ~4 hours
- Visualization: ~4 hours
- Total: ~10 hours

**Overall Phase 2:** ~18 hours execution, ~$50-60 estimated cost

---

## Summary: Why This Design is Methodologically Sound

1. ✅ **Follows conventions:** Test set reserved for final evaluation only
2. ✅ **Honors pre-registration:** Executes planned RQ2 without deviation
3. ✅ **No post-hoc exploration:** Resists temptation to "explain away" Phase 1 results
4. ✅ **Adequate power:** 50 runs provides robust statistical inferences
5. ✅ **Clear narrative:** Logical RQ1 → RQ2 progression
6. ✅ **Extends prior work:** Builds on Kim & Lu's consistency recommendation
7. ✅ **Transparent limitations:** Acknowledges constraints honestly
8. ✅ **Intellectual honesty:** Reports findings regardless of expectations
9. ✅ **Actionable insights:** Provides practical guidance for method selection
10. ✅ **Novel contribution:** First systematic consistency analysis for this task

**This design will satisfy RMAL reviewers and produce defensible, high-quality methodological research.**
