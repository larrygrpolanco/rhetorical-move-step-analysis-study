# Study Design: LLM Consistency in Rhetorical Move-Step Annotation

## A Methodological Study Applying Kim & Lu's (2024) Framework to Biology

---

## Executive Summary

**Study Type:** Methodological application with consistency analysis  
**Primary Contribution:** Systematic evaluation of LLM annotation consistency  
**Model:** GPT-4 (gpt-4.1-2025-04-14)  
**Domain:** AI Genre Analysis on annotated Biology article introductions Dataset
**Dataset:** CaRS-50 (50 annotated articles)  
**Total Runs:** 104 on test set (10 articles, ~267 sentences)(4 conditions × 1 initial + 2 conditions × 50 consistency)

---

## Research Questions

**RQ1 (Performance):** How do zero-shot, few-shot (3-shot and 8-shot), and fine-tuned approaches perform on CaRS-50 Biology research article move-step annotation?

**RQ2 (Consistency - PRIMARY):** How consistent is annotation across repeated runs for zero-shot and fine-tuned approaches, and how do they compare?

---

## Theoretical Framework

This study is inspired by the methodological framework established by Kim & Lu (2024), who demonstrated that GPT-based models could perform rhetorical move-step annotation with high accuracy when fine-tuned. Their work established that:

1. Fine-tuning substantially outperforms few-shot learning
2. Few-shot learning provides moderate improvements over zero-shot
3. Prompt specificity matters for accuracy

**Extension:** While Kim & Lu focused on single-run accuracy, I systematically evaluate **annotation consistency** - a critical but unexplored dimension for practical deployment of LLM as annotation tools in genre analysis.

---

## Dataset

**Source:** CaRS-50 (Omotola et al., 2025)  
**Total:** 50 Biology research article introductions  
**Annotation Framework:** CaRS model (3 moves, 11 steps)

### Data Split

```
Training Set:   30 articles (60%) - For fine-tuning
Validation Set: 10 articles (20%) - For prompt development and pipeline testing
Test Set:       10 articles (20%) - For final evaluation (HELD OUT)
```

**Justification for 30/10/10 Split:**

1. **Training (30 articles):**

   - limitation of dataset, but good for testing fine-tuning limitations (Kim & Lu used 40-80)
   - Represents 60% of data
   - ~30 sentences per article, 826 sentences total

2. **Validation (10 articles):**

   - Used for prompt development and formatting validation
   - Allows parser testing without contaminating test set

3. **Test (10 articles):**
   - True holdout set (~250-300 sentences)
   - Never seen during development
   - Sufficient for robust evaluation (Kim & Lu used 10)
   - Enables 50 repeated evaluations with adequate sample size

**Statistical Power:** With 10 test articles × 50 runs = 500 observations per condition

---

## Phase 1: Methods Development and Validation

### Pilot Study

**Purpose:** Validate automated pipeline infrastructure

**Activities:**

1. Built XML extractor to get CaRS-50 dataset into an easier to work with format
2. Established gold standard format (prepare_gold_standard.py)
3. Developed deterministic parser (parse_llm_output.py)
4. Created automation scripts (run_condition.py)
5. Validated workflow on subset of articles
6. Created evaluation scripts for calculating and reporting various metrics

**Key Outcome:** Confirmed that automated pipeline can reliably extract, annotate, parse, and evaluate with checkpoints for manual inspection and code reports on errors

**Scope Limitation:** Pilot focused exclusively on infrastructure validation, not on accuracy optimization or hypothesis testing. No results from pilot testing influenced research questions or design decisions.

### Prompt Development

**Approach:** Single-pass development (not iterative refinement)

**Base Prompt:** Adapted from Kim & Lu (2024) with modifications for:

1. CaRS-50 framework (11 steps vs. their 23)
2. Biology domain examples
3. Explicit output formatting for deterministic parsing

**Modifications (system_prompt.txt):**
We added explicit formatting instructions:

```diff
Output format:
- Use EXACTLY this format: [tag] sentence text
- ONE tag and sentence per line
- Do NOT add commentary, numbering, or explanation
- Begin each line with the tag in square brackets
- Question marks typically signal sentence boundaries

CRITICAL: You must annotate ALL sentences in the input text, in order, without skipping or truncating any.
```

### Justification:

1. **Scientific**: Kim & Lu likely parsed outputs manually or semi-manually. For reproducible automation, explicit format specification is necessary.
2. **Conservative**: We added constraints on OUTPUT FORMAT, not on annotation decisions. The semantic instructions remain identical.
3. **Transparent**: We document this change clearly in methods section.

**Development Process:**

1. Start with Kim & Lu's refined prompt structure
2. Replace Applied Linguistics moves/steps with CaRS-50 definitions
3. Add instructions specifying output format rules: `[tag] sentence text`
4. Test on 3-5 validation articles for parsing compatibility
5. **Lock the prompt** - no further changes

**Validation Criteria:**

- ✅ Parser successfully extracts all sentences
- ✅ Tags are formatted correctly (100% parseable)
- ✅ No systematic formatting errors

---

## RQ1: Single-Run Evaluation

### Experimental Conditions (4)

**A1: Zero-Shot**

-System prompt + article text only

- Tests baseline performance
- 1 run on test set

**A1: Three-Shot**

- System prompt + 3 example pairs + article text.
- Example Selection Protocol below

**A1: Eight-Shot**

- System prompt + 8 example pairs + article text.
- Example Selection Protocol below

**A4: Fine-Tuned**

- System prompt + article text.
- Examples are baked into the model weights during fine-tuning.
- OpenAI API supervised fine-tuning
- Same hyperparameters as Kim and Lu (see Technical Details)
- 1 run on test set

**Few-Shot Example Selection Protocol:**

For the 3-shot and 8-shot conditions, training examples were selected using
stratified random sampling from the training set (articles 21-50, n=30).
We used a fixed random seed (seed=42) to ensure reproducibility.

Selection process:

1. Set random seed to 42
2. Randomly sample 3 articles from training set → 3-shot examples
3. Reset random seed to 42
4. Randomly sample 8 articles from training set → 8-shot examples

The same example sets were used for all 30 repeated runs within each
condition to isolate model stochasticity from example-selection variance
(following Kim & Lu, 2024). All selected article IDs and the random seed
are documented in few_shot_examples.json for full transparency and
reproducibility.

This design choice reflects our research focus: measuring inherent LLM
consistency rather than example-set effects. By fixing examples across
runs, we ensure that any observed variance reflects model behavior rather
than input variation.

### Fine-Tuning Technical Details

**Model:** gpt-4.1-2025-04-14 (fine-tunable version)

**Training Data:** 30 articles from training set, formatted as:

```json
{
  "messages": [
    { "role": "system", "content": "[prompt]" },
    { "role": "user", "content": "[article text]" },
    { "role": "assistant", "content": "[gold annotations]" }
  ]
}
```

**Hyperparameters** (Same as Kim & Lu):

- Epochs: 4
- Batch size: 1
- Learning rate multiplier: 2

**Strategy:** Fine-tune once, evaluate 50 times (tests inference consistency, not training consistency)

### Model Parameters (Fixed Across All Conditions)

```
temperature: 1.0  (matches Kim & Lu 2024)
max_tokens: 4096
```

**Note:** Temperature = 1.0 allows for natural variability, which is exactly what we want to measure in consistency analysis.

---

# RQ2 Study Design: Zero-Shot and Fine-Tuned Consistency Analysis

## Executive Summary

**Purpose:** Systematic evaluation of annotation consistency for the two prompting approaches  
**Design:** 50 repeated runs per condition on held-out test set  
**Conditions:** Zero-shot vs Fine-tuned  
**Dataset:** Test set only (10 articles, ~267 sentences)  
**Total Runs:** 100 (50 zero-shot + 50 fine-tuned)  
**Model:** GPT-4 (gpt-4.1-2025-04-14)  
**Key Extension:** Kim & Lu (2024) tested 3 runs; we test 50 for robust characterization

---

## Research Question

**RQ2 (Consistency Analysis):** How consistent is annotation across repeated runs for zero-shot and fine-tuned approaches, and how do they compare?

**Possible Sub-questions to address:**

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

**Few-Shot Excluded from RQ2:**

- Few-shot conditions (A2, A3): Intermediate performance, less practical interest for consistency analysis
- Few-shot is methodologically interesting but practically awkward (which examples? how many?)
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

- Stochastic sampling (natural LLM variability)

### Temperature = 1.0 Rationale

Following Kim & Lu (2024), we use temperature=1.0 to:

- Match prior work methodology
- Measure consistency under realistic deployment conditions
- Allow natural model variability (which is what we aim to characterize)
- Avoid artificially constraining model behavior

While lower temperatures might reduce variance, our goal is to understand the model's **actual** consistency, not artificially inflated reliability. Future research should explore this

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

A lot of data here so, decide later what is most helpful and informative for the narrative.
Not all of these statistics tell something important.
Collecting a lot of data and stats alone does not make for good research, making them clear and focused does.

### Possible Visualization Directions

**Figure 1:** Pipeline architecture  
**Figure 2:** Single-run results (Phase 2) - bar charts with error bars  
**Figure 3:** Distribution of accuracies across 30 runs - violin plots or boxplots  
**Figure 4:** Consistency comparison - CV comparison across conditions  
**Figure 5:** Bland-Altman plots for run-to-run agreement  
**Figure 6:** Accuracy vs. Consistency trade-off scatter plot

---

### Practical Implications

What does consistency per condition mean to genre analysis resaerch?

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

Think more about this

**Primary Extension:** 50 runs per condition (vs. Kim & Lu's 3 runs)  
**Statistical rigor:** Robust variance comparison, ICC analysis  
**Sentence-level analysis:** Identify high/low consistency instances  
**Stratified analysis:** Consistency patterns by move/step type

**Kim & Lu's Conclusion (p. 11):**

> "Third, validation of output consistency is strongly recommended to confirm model reliability."

**Our Study:** Provides the systematic consistency validation they recommended.

---

## Limitations (Acknowledged)

### Dataset Constraints

1. **Test set size:** 10 articles (~267 sentences) limited by CaRS-50 availability

   - _Mitigation:_ 50-run design provides 500 article-level observations
   - _Precedent:_ Matches Kim & Lu (2024) test set size

2. **Single domain:** Biology research articles only
   - _Implication:_ Findings may not generalize to other disciplines
   - _Future work:_ Cross-domain consistency validation

### Design Constraints

3. **Two conditions only:** Few-shot excluded from RQ2

   - _Justification:_ Focuses on most practical comparison (simplest vs. most sophisticated)
   - _Trade-off:_ Gains depth on key comparison, sacrifices breadth

4. **Single model family:** GPT-4 only

   - _Implication:_ Results may not generalize to other LLMs
   - _Future work:_ Cross-model consistency comparison

5. **Fixed temperature:** 1.0 only
   - _Justification:_ Matches Kim & Lu; measures realistic deployment consistency
   - _Future work:_ Temperature effects on consistency

### Methodological Constraints

6. **Example selection not systematically controlled**
   - _Acknowledgment:_ Few-shot examples randomly selected
   - _Implication:_ Example selection effects cannot be ruled out as partial explanation for RQ1 results
   - _Future work:_ Systematic investigation of example selection strategies (similarity-based, stratified, prototype selection)

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

### Framing Statement (for Paper)

> Building on the methodological framework established by Kim & Lu (2024) for LLM-based rhetorical annotation, we extend their approach in two key ways: (1) we conduct the a systematic evaluation of annotation **consistency** across 30 repeated runs per condition, addressing a critical gap for practical tool deployment, and (2) we test generalization to a different domain (Biology) and annotation framework (CaRS-50), demonstrating the broader applicability of their prompting strategies.

**Key Point:** We cite Kim & Lu prominently but frame this as an **extension study** focused on consistency, not as a direct replication.

---

### Publication Viability

**Core Contribution:** Systematic consistency evaluation of LLM move-step annotation

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

- "We set temperature to 1.0 to match Kim & Lu (2024) and to measure consistency under realistic deployment conditions with natural model variability. While lower temperatures (e.g., 0.3-0.7) might reduce variance, we prioritize measuring consistency of the model's intended behavior rather than artificially constraining it. This allows our findings to generalize to typical use cases where researchers employ default or recommended temperature settings."
- "Future research should systematically investigate the temperature-consistency trade-off. While lower temperatures may reduce output variability, they may also reduce output quality for complex reasoning tasks. Identifying optimal temperature settings for move-step annotation across different conditions represents an important avenue for practical tool development."

6. **10-article test set:**: This is my biggest statistical limitation. With ~250-300 sentences, you have adequate power for condition-level comparisons, but limited power for fine-grained analysis (e.g., specific move/step performance). Acknowledge this clearly.

- "Few-shot examples were randomly selected from the training set rather than strategically curated (cf. Yu et al., 2024). This choice prioritizes ecological validity over maximal performance—practitioners deploying these methods will typically use random or convenience samples of training data rather than carefully optimized example sets. Our design thus tests the robustness of few-shot learning under realistic deployment conditions."

6. **Single-Pass Prompt Development:**: You lock the prompt after validation. This is methodologically sound for your goals, but you might get reviewer pushback. Be ready to defend this as "testing consistency of a fixed method" vs. "optimizing performance."

- Unlike Kim & Lu (2024), who iteratively refined their prompt on a validation set to maximize accuracy, we adopted a single-pass prompt development approach. Our base prompt was adapted from Kim & Lu's refined prompt with minimal modifications for the CaRS-50 framework (11 steps vs. 23) and Biology domain. After confirming successful parsing on 3-5 validation articles, the prompt was locked for all subsequent evaluations.
  This design choice reflects our research goals: we evaluate consistency of a fixed method rather than optimize performance through iterative refinement. Consistency analysis requires a stable prompt across all runs—iterative refinement would conflate prompt variability with model stochasticity. Our approach thus tests: "Given a reasonable prompt adapted from established methods, how consistent are different annotation approaches?" This question has greater practical relevance than "What is the maximum achievable accuracy with optimal prompt engineering?"

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
- ✅ Honest reporting of all limitations
- ✅ Complete data and code availability

### Reproducibility

- ✅ Fixed random seeds where possible
- ✅ Documented all design decisions
- ✅ Provided complete codebase
- ✅ Shared prompts and examples

---

## Key Decisions Summary

| Decision Point       | Choice                 | Rationale                                                |
| -------------------- | ---------------------- | -------------------------------------------------------- |
| Train/Val/Test Split | 30/10/10               | Validation set for prompt development, test set held out |
| Consistency Runs     | 30 per condition       | Adequate power for variance comparison                   |
| Few-Shot Examples    | Fixed sets             | Isolates LLM stochasticity                               |
| Fine-Tuning Strategy | Once + 30 tests        | Tests inference, not training consistency                |
| Prompt Development   | Single-pass            | Focus on consistency, not prompt optimization            |
| Temperature          | 1.0 (fixed)            | Matches Kim & Lu, allows natural variability             |
| Primary Framing      | Consistency analysis   | Novel contribution, less replication baggage             |
| Pilot Work           | Transparent disclosure | Methods validation, not hypothesis testing               |

---

**More information:**

1. **Dataset Description**:

```
"We used the CaRS-50 dataset (Omotola et al., 2025), consisting of
50 Biology research article introductions with 1,297 annotated sentences.
The dataset exhibits significant class imbalance, with step frequencies
ranging from 1 (step 3d) to 567 (step 1c) sentences. Inter-annotator
reliability was moderate (κ=0.426, α=0.424) based on 3% of the corpus."
```

2. **Limitation Statement**:

```
"Due to severe class imbalance in the CaRS-50 corpus, our evaluation
focuses primarily on move-level classification and well-represented steps
(≥50 examples). Rare steps (2a, 2c, 2d, 3d) are included in training but
may not be adequately represented in our 10-article test set for reliable
evaluation. This represents an inherent constraint of the available
annotated Biology corpus."
```

3. **Comparison to Kim & Lu**:

"Direct numerical comparison to Kim & Lu (2024) is limited by: (1) domain
differences (Biology vs. Applied Linguistics), (2) framework granularity
(11 vs. 23 categories), (3) dataset size (50 vs. 100 articles), and (4)
annotation reliability differences. Our contribution lies in demonstrating
methodological transferability and systematic consistency analysis rather
than achieving superior accuracy."

**Handling Class Imbalance in Reporting:**

- Primary focus: Move-level (3 classes, balanced representation)
- Secondary focus: Well-represented steps (n ≥ 50 in training set)
- Excluded from detailed analysis: Rare steps (2a, 2c, 2d, 3d) due to insufficient examples
- Metrics: Report weighted averages to account for class distribution

### **Primary Focus (Main Results Section):**

1. **Move-level classification** (3 classes) - your main story
2. **Consistency analysis at move level** - your novel contribution
3. **Comparison to Kim & Lu at move level** - fair comparison

### **Secondary Analysis (Supplementary or Brief Results):**

1. **Aggregate step-level performance** - report overall step accuracy
2. **Analysis of well-represented steps only** - acknowledge which ones
3. **Qualitative error analysis** - what types of steps are confused

### **Explicitly Out of Scope:**

1. ❌ Individual accuracy for rare steps (2a, 2c, 2d, 3d)
2. ❌ Claims about step-level consistency (too underpowered)
3. ❌ Step-level comparison to Kim & Lu (different frameworks anyway)

**Read this paper!:**
The Impact of Example Selection in Few-Shot Prompting on Automated Essay Scoring Using GPT Models
https://link.springer.com/chapter/10.1007/978-3-031-64315-6_5

**This design prioritizes transparency, reproducibility, and methodological rigor while making a clear novel contribution to understanding LLM annotation consistency.**
