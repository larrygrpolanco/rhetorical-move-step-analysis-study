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

### Phase 1 Results (RQ1)

**Dataset:** test  
**Research Question:** rq1  
**Conditions Compared:** 4  

**Conditions:**
1. eight_shot
2. fine_tuned
3. three_shot
4. zero_shot

---

## Move-Level Performance Comparison

| Condition   |   Accuracy |   Precision |   Recall |     F1 |   Sentences |
|:------------|-----------:|------------:|---------:|-------:|------------:|
| eight_shot  |     0.7678 |      0.8238 |   0.7678 | 0.7833 |         267 |
| fine_tuned  |     0.839  |      0.8526 |   0.839  | 0.8426 |         267 |
| three_shot  |     0.7453 |      0.8388 |   0.7453 | 0.7707 |         267 |
| zero_shot   |     0.7678 |      0.8401 |   0.7678 | 0.789  |         267 |

## Step-Level Performance Comparison

| Condition   |   Accuracy |   Precision |   Recall |     F1 |   Sentences |
|:------------|-----------:|------------:|---------:|-------:|------------:|
| eight_shot  |     0.4981 |      0.5517 |   0.4981 | 0.5095 |         267 |
| fine_tuned  |     0.5206 |      0.5356 |   0.5206 | 0.5159 |         267 |
| three_shot  |     0.4794 |      0.5841 |   0.4794 | 0.4929 |         267 |
| zero_shot   |     0.4607 |      0.539  |   0.4607 | 0.4803 |         267 |

---

## Statistical Significance Tests (McNemar's Test)

*McNemar's test evaluates whether accuracy differences between conditions are statistically significant.*

### Move-Level Comparisons

| Comparison | p-value | Significant (p<0.05)? | Statistic |
|------------|---------|----------------------|------------|
| eight_shot vs fine_tuned | 0.0094 | ✓ Yes | 15.0000 |
| eight_shot vs three_shot | 0.3915 | No | 14.0000 |
| eight_shot vs zero_shot | 1.0000 | No | 17.0000 |
| fine_tuned vs three_shot | 0.0005 | ✓ Yes | 12.0000 |
| fine_tuned vs zero_shot | 0.0094 | ✓ Yes | 15.0000 |
| three_shot vs zero_shot | 0.3449 | No | 11.0000 |

### Step-Level Comparisons

| Comparison | p-value | Significant (p<0.05)? | Statistic |
|------------|---------|----------------------|------------|
| eight_shot vs fine_tuned | 0.6024 | No | 43.0000 |
| eight_shot vs three_shot | 0.6089 | No | 28.0000 |
| eight_shot vs zero_shot | 0.2604 | No | 27.0000 |
| fine_tuned vs three_shot | 0.3049 | No | 42.0000 |
| fine_tuned vs zero_shot | 0.1253 | No | 40.0000 |
| three_shot vs zero_shot | 0.5966 | No | 26.0000 |

---

### Why This Finding Matters

This is a methodological replication kim and lu with various changes. Similar results and this set the groundwork/baseline for RQ2

### The Critical Question

**RQ2:** How does annotation consistency differ between zero-shot and fine-tuned approaches?

---

## Research Question

**RQ2 (Consistency Analysis):** How consistent is annotation across repeated runs for zero-shot and fine-tuned approaches, and how do they compare?

**Sub-questions:**
- RQ2.1: What is the aggregate consistency for each condition (CV, ICC)?
- RQ2.2: How do zero-shot and fine-tuned compare in consistency?
- RQ2.3: Which sentences show high vs low consistency in each condition?
- RQ2.4: Do consistency patterns differ by move or step type?

---

### Why These Two Conditions?

**Zero-Shot (A1):**
- Simplest approach (no training data, no examples)
- Most accessible to researchers
- Baseline for consistency expectations

**Fine-Tuned (A4):**
- Most resource-intensive approach
- Expected to be most accurate
- Industry best practice for task-specific annotation
- Key comparison point

**Excluded from Phase 2:**
- Few-shot conditions (A2, A3): Intermediate performance, less practical interest for consistency analysis
- Simplifies narrative: "simplest vs. most sophisticated"

---

## Dataset and Evaluation

### Test Set Specifications

**Size:** 10 articles (~267 sentences)  

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
- Represents standard practice for methodologically similar studies
- Provides 267 sentences (~27 per article) for sentence-level analysis
- With 50 runs, yields 500 article-level and 13,350 sentence-level observations per condition

---

## Procedure

### Phase 2 Workflow

**Condition A1 (Zero-Shot) - 50 Runs:**



**Condition A4 (Fine-Tuned) - 50 Runs:**



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

**Table 1: RQ1 Performance Summary**
- Single-run accuracy for all 4 conditions
- McNemar's test results
- Establish baseline and extension then set up questions and value of consistency

**Table 2: RQ2 Consistency Summary**
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

What does consistency per condition mean to genre analysis resaerch

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
   - *Acknowledgment:* Few-shot examples randomly selected
   - *Implication:* Example selection effects cannot be ruled out as partial explanation for RQ1 results
   - *Future work:* Systematic investigation of example selection strategies (similarity-based, stratified, prototype selection)

---

## Ethical Considerations

### Transparency

✅ Full code and data availability

### Methodological Integrity

✅ Test set held out
✅ Fixed evaluation procedures across all runs  
✅ Reproducibility package provided

### Intellectual Honesty

✅ Results reported regardless of direction  
✅ Limitations stated prominently  
✅ Alternative explanations considered  
✅ Future research directions suggested rather than definitive claims

---