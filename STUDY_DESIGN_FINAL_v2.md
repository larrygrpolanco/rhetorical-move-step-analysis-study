# Study Design: LLM Consistency in Rhetorical Move-Step Annotation
## A Methodological Study Applying Kim & Lu's (2024) Framework to Biology

---

## Executive Summary

**Study Type:** Methodological application with novel consistency analysis  
**Primary Contribution:** First systematic evaluation of LLM annotation consistency  
**Model:** GPT-4 (gpt-4-0613)  
**Domain:** Biology research article introductions  
**Dataset:** CaRS-50 (50 annotated articles)  
**Total Runs:** 124 (4 conditions × 1 initial + 4 conditions × 30 consistency)

---

## Research Questions

**RQ1 (Performance):** How do zero-shot, few-shot (3-shot and 8-shot), and fine-tuned approaches perform on Biology research article move-step annotation?

**RQ2 (Consistency - PRIMARY):** How does annotation consistency vary across prompting conditions over 30 repeated runs?

**RQ3 (Few-shot Comparison):** Does increasing few-shot examples from 3 to 8 improve performance and/or consistency?

---

## Theoretical Framework

This study applies the methodological framework established by Kim & Lu (2024), who demonstrated that GPT-based models could perform rhetorical move-step annotation with high accuracy when fine-tuned. Their work established that:

1. Fine-tuning substantially outperforms few-shot learning
2. Few-shot learning provides moderate improvements over zero-shot
3. Prompt specificity matters for accuracy

**Our Extension:** While Kim & Lu focused on single-run accuracy, we systematically evaluate **annotation consistency** - a critical but unexplored dimension for practical deployment of LLM-based annotation tools.

---

## Dataset

**Source:** CaRS-50 (Omotola et al., 2025)  
**Total:** 50 Biology research article introductions  
**Annotation Framework:** CaRS model (3 moves, 11 steps)

### Data Split (Option A: Development-Focused)

```
Training Set:   30 articles (60%) - For fine-tuning
Validation Set: 10 articles (20%) - For prompt development  
Test Set:       10 articles (20%) - For final evaluation (HELD OUT)
```

**Justification for 30/10/10 Split:**

1. **Training (30 articles):** 
   - Sufficient for GPT-4 fine-tuning (Kim & Lu used 40-80)
   - Represents 60% of data - standard for small datasets
   - ~30 sentences per article = ~900 training examples

2. **Validation (10 articles):**
   - Used for prompt development and formatting validation
   - Allows parser testing without contaminating test set
   - 20% allocation standard for hyperparameter tuning

3. **Test (10 articles):**
   - True holdout set (~250-300 sentences)
   - Never seen during development
   - Sufficient for robust evaluation (Kim & Lu used 10)
   - Enables 30 repeated evaluations with adequate sample size

**Statistical Power:** With 10 test articles × 30 runs = 300 observations per condition, we have 80% power to detect moderate differences in variance (Cohen's f = 0.25) using Levene's test at α = 0.05.

---

## Phase 1: Methods Development and Validation

### Pilot Study (Already Completed)

**Purpose:** Validate automated pipeline infrastructure

**Activities:**
1. ✅ Built XML extraction pipeline (xml_extractor.py)
2. ✅ Developed deterministic parser (parse_llm_output.py)
3. ✅ Created automation scripts (1_run_pilot.py, 2_parse_pilot.py)
4. ✅ Validated workflow on subset of articles
5. ✅ Established gold standard format (prepare_gold_standard.py)

**Key Outcome:** Confirmed that automated pipeline can reliably extract, annotate, parse, and evaluate without manual intervention.

**Scope Limitation:** Pilot focused exclusively on infrastructure validation, not on accuracy optimization or hypothesis testing. No results from pilot testing influenced research questions or design decisions.

### Prompt Development

**Approach:** Single-pass development (not iterative refinement)

**Base Prompt:** Adapted from Kim & Lu (2024) with modifications for:
1. CaRS-50 framework (11 steps vs. their 23)
2. Biology domain examples
3. Explicit output formatting for deterministic parsing

**Development Process:**
1. Start with Kim & Lu's refined prompt structure
2. Replace Applied Linguistics moves/steps with CaRS-50 definitions
3. Add Biology-specific examples for each step
4. Add 4 lines specifying output format: `[tag] sentence text`
5. Test on 3-5 validation articles for parsing compatibility
6. **Lock the prompt** - no further changes

**Validation Criteria:**
- ✅ Parser successfully extracts all sentences
- ✅ Tags are formatted correctly (100% parseable)
- ✅ No systematic formatting errors

**Final Prompt Location:** `prompts/final_prompt.txt`

---

## Phase 2: Single-Run Evaluation (Baseline Performance)

### Experimental Conditions (4)

**A1: Zero-Shot**
- Prompt only, no examples
- Tests baseline performance
- 1 run on test set

**A2: Few-Shot (3 examples)**
- Prompt + 3 annotated examples
- Examples: Fixed set randomly selected from training set
- 1 run on test set

**A3: Few-Shot (8 examples)**  
- Prompt + 8 annotated examples
- Examples: Fixed set randomly selected from training set
- Tests if more examples help
- 1 run on test set

**A4: Fine-Tuned**
- GPT-4 fine-tuned on 30 training articles
- OpenAI API supervised fine-tuning
- Default hyperparameters (see Technical Details)
- 1 run on test set

**Total Phase 2 Runs:** 4

### Few-Shot Example Selection Strategy

**Fixed Examples:** Use the same example articles across all 30 runs within each condition

**Selection Method:**
1. Randomly sample 3 articles from training set → A2 examples
2. Randomly sample 8 articles from training set → A3 examples  
3. Document article IDs used
4. Use identical examples for all 30 runs in each condition

**Rationale:** Fixed examples isolate LLM stochasticity (our research question) from example-selection variance.

### Fine-Tuning Technical Details

**Model:** gpt-4-0613 (fine-tunable version)

**Training Data:** 30 articles from training set, formatted as:
```json
{
  "messages": [
    {"role": "system", "content": "[prompt]"},
    {"role": "user", "content": "[article text]"},
    {"role": "assistant", "content": "[gold annotations]"}
  ]
}
```

**Hyperparameters** (OpenAI defaults):
- Epochs: Auto (typically 3-5)
- Batch size: Auto
- Learning rate multiplier: Auto
- No custom hyperparameter tuning

**Validation:** Use OpenAI's built-in validation split from training data

**Strategy:** Fine-tune once, evaluate 30 times (tests inference consistency, not training consistency)

### Model Parameters (Fixed Across All Conditions)

```
temperature: 1.0  (matches Kim & Lu 2024)
max_tokens: 4096
top_p: 1.0
frequency_penalty: 0
presence_penalty: 0
```

**Note:** Temperature = 1.0 allows for natural variability, which is exactly what we want to measure in consistency analysis.

---

## Phase 3: Consistency Analysis (Novel Contribution)

### Design

**Objective:** Measure annotation consistency across repeated runs

**Method:** Run each condition 30 times on the same test set

**Total Runs:** 4 conditions × 30 runs = 120 evaluations

**Fixed Elements:**
- Test set: Same 10 articles across all runs
- Prompt: Identical for all runs
- Few-shot examples: Same examples for all runs within A2 and A3
- Model parameters: Temperature 1.0, all other settings constant
- Fine-tuned model: Same model checkpoint for all 30 fine-tuned runs

**Variable Element:** Random seed / stochastic sampling (inherent to LLM generation)

### Why 30 Runs?

**Statistical Justification:**

1. **Variance Comparison Power:**
   - Levene's test requires n ≥ 20 per group for adequate power (0.80)
   - 30 runs provides power > 0.80 to detect moderate variance differences
   - Allows detection of effect size f = 0.25 at α = 0.05

2. **Precision of Estimates:**
   - With 30 runs, 95% CI width for SD ≈ ±30% of true SD
   - Example: If true SD = 3%, CI ≈ [2.4%, 3.9%]
   - Sufficient precision for meaningful comparisons

3. **Practical Considerations:**
   - More runs = better estimates, but diminishing returns after ~30
   - Balances rigor with computational cost
   - Exceeds Kim & Lu's 4 runs, providing much stronger conclusions

**Precedent:** Similar consistency studies in NLP use 20-50 runs (though often for smaller tasks).

---

## Evaluation Metrics

### Performance Metrics (Standard)

**Move-Level (3 classes):**
- Accuracy (primary)
- Precision, Recall, F1 per move
- Weighted average P/R/F1
- Confusion matrix

**Step-Level (11 classes):**
- Accuracy (primary)
- Precision, Recall, F1 per step
- Weighted average P/R/F1
- Confusion matrix

**Statistical Comparison:**
- McNemar's test for paired accuracy comparisons
- Effect sizes (Cohen's h)
- 95% confidence intervals

### Consistency Metrics (Novel)

**Primary Metrics:**
1. **Mean Accuracy** (μ): Average across 30 runs
2. **Standard Deviation** (σ): Spread of accuracy values
3. **Coefficient of Variation** (CV): σ/μ × 100% (normalized consistency measure)
4. **95% Confidence Interval:** [μ - 1.96(σ/√30), μ + 1.96(σ/√30)]

**Secondary Metrics:**
5. **Range:** Maximum - Minimum accuracy
6. **Interquartile Range (IQR):** 75th percentile - 25th percentile
7. **Median:** Middle value across runs

**Reliability Metric:**
8. **Intraclass Correlation Coefficient (ICC):** Measures consistency of annotations across runs (adapted from psychometrics)

**Agreement Visualization:**
9. **Bland-Altman Plots:** Visual assessment of run-to-run agreement

### Example Results Format

```
Condition: A2 (Few-shot, 3 examples)
─────────────────────────────────────
Move-Level Accuracy:
  Mean:     54.2%
  SD:        2.8%
  CV:        5.2%
  95% CI:   [53.2%, 55.2%]
  Range:    [49.1%, 59.3%]
  Median:   54.5%

Step-Level Accuracy:
  Mean:     38.7%
  SD:        4.1%
  CV:       10.6%
  95% CI:   [37.2%, 40.2%]
  Range:    [31.2%, 46.8%]
  Median:   38.9%
```

---

## Statistical Analysis Plan

### 1. Within-Condition Analysis

**For each condition (A1, A2, A3, A4):**

a) **Descriptive Statistics:**
   - Mean, SD, CV, 95% CI, Range, IQR, Median
   - Reported for both move-level and step-level accuracy

b) **Distribution Assessment:**
   - Shapiro-Wilk test for normality
   - Q-Q plots
   - Histograms with kernel density estimates

c) **Reliability:**
   - ICC calculation (two-way random effects model)

### 2. Between-Condition Comparisons

**Research Question: Does consistency differ across conditions?**

a) **Variance Comparison:**
   - **Levene's test:** Tests H₀: σ₁² = σ₂² = σ₃² = σ₄²
   - If significant → at least one condition has different variance
   - Report F-statistic, p-value, effect size

b) **Post-Hoc Pairwise Comparisons:**
   - Brown-Forsythe test for each pair of conditions
   - Bonferroni correction for multiple comparisons (α = 0.05/6 = 0.0083)
   - Report variance ratios (e.g., "A4 variance is 0.12× that of A1")

c) **Effect Sizes:**
   - Cohen's d for mean differences
   - Variance ratios for consistency differences

### 3. Accuracy vs. Consistency Trade-off

**Analysis:**
- Scatter plot: Mean accuracy vs. CV
- Does higher accuracy come with higher consistency?
- Which condition optimizes both?

### 4. Visualization Plan

**Figure 1:** Pipeline architecture  
**Figure 2:** Single-run results (Phase 2) - bar charts with error bars  
**Figure 3:** Distribution of accuracies across 30 runs - violin plots or boxplots  
**Figure 4:** Consistency comparison - CV comparison across conditions  
**Figure 5:** Bland-Altman plots for run-to-run agreement  
**Figure 6:** Accuracy vs. Consistency trade-off scatter plot  

---

## Relationship to Kim & Lu (2024)

### What We Replicate

✅ **Methodological Framework:**
- Zero-shot, few-shot, fine-tuning comparison
- Evaluation metrics (P/R/F1, confusion matrices)
- Statistical tests (McNemar's)
- Target genre (RA introductions)

✅ **Design Philosophy:**
- Systematic comparison of prompting strategies
- Focus on practical applicability
- Transparent reporting

### What We Adapt

🔄 **Annotation Framework:** 23 categories → 11 categories (CaRS-50)  
🔄 **Domain:** Applied Linguistics → Biology  
🔄 **Model:** GPT-3.5-turbo → GPT-4  
🔄 **Dataset:** COSSRAI → CaRS-50  

### What We Extend (Novel Contributions)

✨ **Primary Extension:** Systematic consistency analysis (30 runs per condition)  
✨ **Secondary Extension:** 3-shot vs. 8-shot comparison  
✨ **Methodological Extension:** Fully automated, reproducible pipeline  

### Framing Statement (for Paper)

> Building on the methodological framework established by Kim & Lu (2024) for LLM-based rhetorical annotation, we extend their approach in two key ways: (1) we conduct the first systematic evaluation of annotation **consistency** across 30 repeated runs per condition, addressing a critical gap for practical tool deployment, and (2) we test generalization to a different domain (Biology) and annotation framework (CaRS-50), demonstrating the broader applicability of their prompting strategies.

**Key Point:** We cite Kim & Lu prominently but frame this as an **extension study** focused on consistency, not as a direct replication.

---

## Timeline (10 Weeks)

| Week | Phase | Activities | Outputs |
|------|-------|-----------|---------|
| 1 | Setup | Finalize prompt, prepare few-shot examples, prepare fine-tuning data | Locked prompt, example sets |
| 2 | Setup | Run fine-tuning, validate pipeline | Fine-tuned model |
| 3 | Phase 2 | Run A1, A2, A3, A4 (single runs) | Baseline results |
| 4 | Analysis | Evaluate Phase 2, document patterns | Tables, confusion matrices |
| 5 | Phase 3 | Consistency runs: A1 (30 runs) | A1 consistency data |
| 6 | Phase 3 | Consistency runs: A2, A3 (60 runs) | A2/A3 consistency data |
| 7 | Phase 3 | Consistency runs: A4 (30 runs) | A4 consistency data |
| 8 | Analysis | Statistical analysis, create visualizations | All figures, tables |
| 9 | Writing | Draft full manuscript | Draft |
| 10 | Writing | Revisions, formatting, submission prep | Final manuscript |

---

## Budget Estimates

### Cost per Annotation

**Input tokens per article:** ~1,000 (article text + prompt)  
**Output tokens per article:** ~500 (annotations)  
**Total tokens:** ~1,500 per article

**GPT-4 Pricing:**
- Input: $0.03 / 1K tokens
- Output: $0.06 / 1K tokens
- Total per article: ~$0.08

### Phase 2: Single Runs
- Zero-shot (A1): 10 articles × $0.08 = $0.80
- 3-shot (A2): 10 articles × $0.10 = $1.00
- 8-shot (A3): 10 articles × $0.15 = $1.50
- Fine-tuned (A4): 10 articles × $0.12 = $1.20
- Fine-tuning cost: $10.00
- **Phase 2 Total: ~$15**

### Phase 3: Consistency Runs (30× each)
- A1: 30 × $0.80 = $24
- A2: 30 × $1.00 = $30
- A3: 30 × $1.50 = $45
- A4: 30 × $1.20 = $36
- **Phase 3 Total: ~$135**

**Grand Total: ~$150**

*(Note: Actual costs may vary with API pricing changes)*

---

## Success Criteria

### Phase 2 (Performance Baseline)

**Minimum Success:**
- ✅ Move-level accuracy > 50% for fine-tuned model
- ✅ Clear ranking: Fine-tuned > Few-shot > Zero-shot
- ✅ Successful parsing of all outputs

**Strong Success:**
- ✅ Move-level accuracy > 85% for fine-tuned model
- ✅ Significant differences between conditions (McNemar's p < 0.05)
- ✅ Clear 3-shot vs. 8-shot comparison

### Phase 3 (Consistency Analysis - Primary)

**Minimum Success:**
- ✅ Measurable variance exists across runs (not all identical)
- ✅ Statistically significant difference in variance between at least 2 conditions
- ✅ Interpretable patterns (e.g., fine-tuned more consistent than zero-shot)

**Strong Success:**
- ✅ Clear consistency hierarchy across all 4 conditions
- ✅ CV differences > 2% between conditions
- ✅ Actionable insights for method selection (accuracy-consistency trade-off)

### Publication Viability

**Core Contribution:** First systematic consistency evaluation of LLM move-step annotation

**Secondary Contributions:**
1. Cross-domain validation (Biology)
2. Few-shot comparison (3 vs. 8)
3. Fully reproducible methodology

**Even if accuracy is lower than Kim & Lu:** The consistency analysis is novel and valuable regardless of absolute performance levels.

---

## Deliverables

### 1. Manuscript Sections

- **Abstract** (250 words)
- **Introduction** with clear positioning relative to Kim & Lu
- **Methods** with full transparency about adaptations
- **Results** with comprehensive tables and figures
- **Discussion** emphasizing consistency findings
- **Conclusion** with practical recommendations

### 2. Supplementary Materials

- Full prompt text
- Complete few-shot examples
- Gold standard annotations (test set)
- Complete result tables
- Statistical test outputs
- Code repository (GitHub)

### 3. Data Artifacts

- All raw LLM outputs (124 files)
- All parsed outputs (124 JSON files)
- All evaluation results (124 evaluation files)
- Aggregated statistics (CSV)

### 4. Reproducibility Package

- Complete Python codebase
- README with setup instructions
- Requirements.txt
- Example usage notebooks

---

## Limitations and Scope

### Acknowledged Limitations

1. **Dataset Size:** 50 articles (limited by availability of annotated Biology corpus)
2. **Single Domain:** Biology only (limits generalization claims)
3. **Single Model Family:** GPT-4 only (no cross-model comparison)
4. **Framework:** 11 categories (simpler than Kim & Lu's 23)
5. **Temperature:** Fixed at 1.0 (no temperature exploration)

### Scope Boundaries

**This study DOES:**
- ✅ Evaluate consistency across prompting conditions
- ✅ Compare performance on Biology RA introductions
- ✅ Demonstrate methodological transferability
- ✅ Provide practical guidance for method selection

**This study DOES NOT:**
- ❌ Replicate Kim & Lu's exact numerical results
- ❌ Test on multiple domains simultaneously
- ❌ Compare different LLM families
- ❌ Optimize prompts iteratively
- ❌ Test all possible hyperparameter combinations

### Future Work Directions

1. **Cross-Model Study:** Test consistency across GPT-4, Claude, Llama
2. **Temperature Exploration:** Optimal temperature for consistency
3. **Cross-Domain:** Test same model on multiple domains
4. **Larger Scale:** 100+ articles per domain
5. **Real-Time Deployment:** Test consistency in production settings

---

## Ethical Considerations

### Transparency

- ✅ Full disclosure of pilot work (methods validation)
- ✅ Clear statement of relationship to Kim & Lu
- ✅ Honest reporting of all limitations
- ✅ Complete data and code availability

### Reproducibility

- ✅ Fixed random seeds where possible
- ✅ Documented all design decisions
- ✅ Provided complete codebase
- ✅ Shared prompts and examples

### Researcher Positionality

**Statement for Methods Section:**
> This research was conducted by an independent researcher with limited annotated data resources. The choice to use the CaRS-50 dataset (50 articles) rather than larger datasets was dictated by data availability, not optimal design. We acknowledge this limitation and frame our findings accordingly.

---

## Key Decisions Summary

| Decision Point | Choice | Rationale |
|---------------|--------|-----------|
| Train/Val/Test Split | 30/10/10 | Validation set for prompt development, test set held out |
| Consistency Runs | 30 per condition | Adequate power for variance comparison |
| Few-Shot Examples | Fixed sets | Isolates LLM stochasticity |
| Fine-Tuning Strategy | Once + 30 tests | Tests inference, not training consistency |
| Prompt Development | Single-pass | Focus on consistency, not prompt optimization |
| Temperature | 1.0 (fixed) | Matches Kim & Lu, allows natural variability |
| Primary Framing | Consistency analysis | Novel contribution, less replication baggage |
| Pilot Work | Transparent disclosure | Methods validation, not hypothesis testing |

---

**This design prioritizes transparency, reproducibility, and methodological rigor while making a clear novel contribution to understanding LLM annotation consistency.**
