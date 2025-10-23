# Phase 2 Study Design: Consistency Analysis and Example Selection Effects

## Executive Summary

**Context:** Phase 1 (RQ1) revealed an unexpected pattern on the validation set: zero-shot prompting outperformed both few-shot and fine-tuned conditions. This contradicts findings from Kim & Lu (2024) and similar studies in applied linguistics.

**Response:** Phase 2 shifts focus to (a) robustly characterizing zero-shot consistency as the primary analysis, and (b) conducting an exploratory investigation into few-shot example selection effects as a secondary analysis.

**Total Runs:** 55 runs on test set
- 50 runs: Zero-shot consistency analysis (primary)
- 5 runs: Alternative few-shot example sets (exploratory)

---

## Revised Research Questions

**RQ1 (Performance - COMPLETED):** How do zero-shot, few-shot (3-shot and 8-shot), and fine-tuned approaches perform on Biology research article move-step annotation?

**Finding:** Validation set showed zero-shot achieving highest accuracy (87.3% move-level) compared to 3-shot (84.3%), 8-shot (83.8%), and fine-tuned (83.8%). No significant differences detected via McNemar's test.

**RQ2 (Consistency - PRIMARY):** How consistent is zero-shot annotation across repeated runs, and what characterizes sentence-level variability?

**RQ2b (Example Selection - EXPLORATORY):** To what extent does few-shot example selection contribute to the observed underperformance?

---

## Rationale for Design Modification

### Why We Changed Course

**Expected Pattern (based on Kim & Lu 2024):**
- Fine-tuned > Few-shot > Zero-shot
- More examples and task-specific training should improve accuracy

**Observed Pattern (validation set):**
- Zero-shot ≥ Few-shot ≥ Fine-tuned (reversed or flat)
- Statistical tests show no significant differences

**Possible Explanations:**
1. **Task simplicity:** CaRS framework (11 steps) may be simpler than Kim & Lu's 23-step system
2. **Domain familiarity:** GPT-4's pre-training may already cover Biology RA conventions
3. **Example quality:** Current few-shot examples may be unrepresentative or misleading
4. **Overfitting:** Fine-tuning on 30 articles may overfit to training set quirks
5. **Dataset noise:** CaRS-50's moderate IAA (κ=0.426) introduces gold standard uncertainty

### Why This Matters

If zero-shot annotation achieves comparable or superior accuracy, understanding its **consistency** becomes critical for practical deployment. Researchers need to know:
- How reliable are repeated zero-shot runs?
- Which sentences/moves/steps show high vs low consistency?
- When can practitioners trust zero-shot annotation?

**This represents a methodological contribution:** Characterizing the reliability boundary of the simplest prompting approach.

---

## Phase 2: Primary Analysis (Zero-Shot Consistency)

### Design Overview

**Condition:** Zero-shot only  
**Datasets:** 
- **Training set** (30 articles, ~826 sentences) - PRIMARY analysis
- **Test set** (10 articles, ~267 sentences) - REPLICATION analysis
**Runs:** 50 repeated evaluations on EACH dataset (100 total)  
**Model:** GPT-4 (gpt-4.1-2025-04-14)  
**Temperature:** 1.0 (fixed)  
**Random Seed:** None (natural stochasticity)

### Dual-Dataset Rationale

Since zero-shot prompting does not depend on training data, we conduct our primary consistency analysis on the training set, which provides 3× more data (826 vs 267 sentences) for robust sentence-level analysis. We replicate the analysis on the held-out test set to verify that consistency patterns generalize across independent article samples.

**Key justification:** Zero-shot has never "seen" any articles in either dataset, making both equally valid for consistency evaluation. The training set was used only for fine-tuning a separate model in Phase 1, but zero-shot by definition does not utilize task-specific training data.

### Research Questions

**RQ2.1:** What is the aggregate consistency of zero-shot annotation?
- Coefficient of variation (CV)
- 95% confidence intervals for mean accuracy
- Intraclass correlation coefficient (ICC)
- Calculated for both training and test sets

**RQ2.2:** Which sentences show high vs low consistency?
- Sentence-level variance analysis
- Identification of "stable" vs "uncertain" instances
- Error pattern analysis
- Primary analysis on training set (better power)

**RQ2.3:** Do consistency patterns differ by move or step type?
- Move-level consistency (M1, M2, M3)
- Step-level consistency for well-represented categories
- Stratified analysis on both datasets

**RQ2.4:** Do consistency patterns generalize across article sets?
- Compare training vs test set consistency
- Cross-dataset ICC comparison
- Test data-dependence of reliability

### Metrics and Analysis

#### Aggregate Metrics (50 runs per dataset)

**Training Set (Primary):**
- 50 runs × 30 articles = 1,500 article evaluations
- ~826 sentences × 50 runs = 41,300 sentence-level observations
- **Better statistical power** for sentence-level analysis

**Test Set (Replication):**
- 50 runs × 10 articles = 500 article evaluations
- ~267 sentences × 50 runs = 13,350 sentence-level observations
- **Generalization verification**

**Metrics for Each Dataset:**
1. **Mean accuracy** with 95% CI
2. **Standard deviation** and CV
3. **Min/Max range** across runs
4. **ICC(2,1)** - consistency across runs

#### Cross-Dataset Comparison
1. **CV comparison:** Is consistency similar across datasets?
2. **ICC comparison:** Do reliability coefficients differ?
3. **Sentence-level patterns:** Are stable/uncertain sentences similar?
4. **Statistical test:** Compare variances across datasets

#### Sentence-Level Metrics (per sentence across 50 runs)

**Primary Analysis (Training Set):**
1. **Agreement rate:** % of runs producing correct label
2. **Entropy:** Uncertainty in predictions (Shannon entropy)
3. **Modal prediction:** Most common label across runs
4. **Flip frequency:** How often label changes between runs

**Replication (Test Set):**
- Same metrics calculated
- Compare patterns to training set

#### Stratified Analysis
- Consistency by move type (M1, M2, M3) - both datasets
- Consistency by step type (well-represented steps) - training set primary
- Consistency by sentence position (first, middle, last)
- Consistency by sentence length (short vs long)

### Expected Outputs

**Tables:**
- Table 2a: Zero-shot consistency summary - Training set (50 runs, 30 articles)
- Table 2b: Zero-shot consistency summary - Test set (50 runs, 10 articles)
- Table 2c: Cross-dataset comparison (training vs test)
- Table 3: Sentence-level consistency patterns (training set primary)
- Table 4: Consistency by move/step type (both datasets)

**Figures:**
- Figure 1a: Distribution of accuracy across 50 runs (training set)
- Figure 1b: Distribution of accuracy across 50 runs (test set)
- Figure 2: Sentence-level agreement rates (training set, heatmap)
- Figure 3: Consistency by move type (both datasets, comparison)
- Figure 4: Cross-dataset ICC comparison

**Statistical Tests:**
- One-sample t-test: Is mean accuracy stable? (both datasets)
- ICC: What proportion of variance is between vs within runs? (both datasets)
- ANOVA: Do moves/steps differ in consistency? (both datasets)
- Levene's test: Do training and test sets differ in variance?

---

## Phase 2: Secondary Analysis (Example Selection Effects)

### Design Overview

**Purpose:** Exploratory investigation into whether current few-shot underperformance is due to poor example selection or a fundamental limitation.

**Scope:** Limited analysis to explore plausibility, not exhaustive study

### Approach

**Generate 5 alternative 3-shot example sets:**
1. **Set A (Original):** Random seed 42 (from Phase 1)
2. **Set B:** Random seed 100 (pure random alternative)
3. **Set C:** Random seed 200 (pure random alternative)
4. **Set D:** Random seed 300 (pure random alternative)
5. **Set E:** Random seed 400 (pure random alternative)

**Note:** We use purely random selection to test generalizability. Stratified/optimized selection is left for future work.

**Evaluation:** Run each set ONCE on test set (5 total runs)

### Research Question

**RQ2b:** Does few-shot accuracy vary substantially across different randomly selected example sets?

**If YES:** Current underperformance may be due to unlucky example selection  
**If NO:** Few-shot may be fundamentally limited for this task/domain

### Metrics

1. **Mean accuracy** across 5 alternative sets
2. **Range** of accuracy (max - min)
3. **Comparison to original:** Is Set A an outlier?
4. **Comparison to zero-shot:** Do ANY sets exceed zero-shot mean?

### Analysis Plan

**Descriptive Only:**
- Report mean, SD, min, max across 5 sets
- Visual comparison (bar chart with error bars)
- Note: N=5 is insufficient for significance testing

**Interpretation:**
- If range > 5%: "Example selection has substantial impact"
- If all sets < zero-shot: "Few-shot underperformance is robust"
- If some sets > zero-shot: "Example selection matters; further research needed"

### Limitations (Acknowledged in Paper)

1. **Small N:** 5 example sets insufficient for strong conclusions
2. **Random only:** Did not test stratified or optimized selection
3. **Single run per set:** Cannot assess consistency of each set
4. **Exploratory:** Results generate hypotheses, not definitive answers

**Framing in Paper:**
> "Given the unexpected zero-shot superiority, we conducted a preliminary exploration of whether example selection contributed to few-shot underperformance. We generated 5 alternative randomly selected example sets and evaluated each once on the test set. This analysis is exploratory and intended to guide future research rather than provide definitive conclusions."

---

## Data Collection Timeline

### Phase 2a: Zero-Shot Consistency (Primary)

**Training Set (Primary Analysis):**
1. Run zero-shot 50 times on training set (30 articles)
2. Expected time: ~50 runs × 90 min = ~75 hours
3. Parse and evaluate all runs
4. Conduct statistical analysis

**Test Set (Replication):**
1. Run zero-shot 50 times on test set (10 articles)
2. Expected time: ~50 runs × 30 min = ~25 hours
3. Parse and evaluate all runs
4. Compare to training set patterns

**Total Zero-Shot Runs:** 100 (50 per dataset)
**Total Compute Time:** ~100 hours (can batch over 2 weeks)

### Phase 2b: Example Selection (Secondary)
1. Generate 5 alternative example sets (script provided)
2. Run each set once on test set ONLY (maintains independence)
3. Expected time: ~5 runs × 30 min = ~2.5 hours
4. Parse and evaluate
5. Descriptive comparison

**Total Phase 2 Compute:** ~102 hours of API calls
**Total Phase 2 Runs:** 105 (100 zero-shot + 5 few-shot)

---

## Statistical Analysis Plan Summary

### Primary Analysis (Zero-Shot Consistency)

**Descriptive Statistics:**
```python
# Aggregate consistency
- Mean accuracy ± SD
- 95% CI for mean
- Coefficient of variation (CV)
- Min, max, range
- Interquartile range (IQR)

# ICC calculation
- ICC(2,1): Single rater consistency
- Interpretation: <0.5 poor, 0.5-0.75 moderate, 0.75-0.9 good, >0.9 excellent
```

**Sentence-Level Analysis:**
```python
# For each sentence across 50 runs:
- Agreement rate: % correct predictions
- Entropy: -Σ p(label) × log2(p(label))
- Modal prediction stability
- Identify high-variance sentences (agreement < 70%)
```

**Stratified Analysis:**
```python
# Consistency by subgroup:
- One-way ANOVA: Do moves differ in consistency?
- Effect size: η² (proportion of variance explained)
- Post-hoc: Tukey HSD if significant
```

### Secondary Analysis (Example Selection)

**Descriptive Only:**
```python
# Across 5 example sets:
- Mean ± SD
- Min, max, range
- Visual comparison to zero-shot
- Identify if original set is outlier
```

**No significance testing** (underpowered with N=5)

---

## Updated Methods Section Text

### For the Paper

**Phase 2 Design Rationale**

> Following Phase 1 evaluation on the validation set, we observed an unexpected pattern: zero-shot prompting achieved the highest move-level accuracy (87.3%), outperforming both few-shot (3-shot: 84.3%, 8-shot: 83.8%) and fine-tuned (83.8%) conditions. This finding contradicted our expectations based on Kim & Lu (2024), who reported substantial benefits from few-shot examples and fine-tuning in applied linguistics.
>
> This surprising result prompted a reorientation of Phase 2. Rather than comparing consistency across all four conditions as originally planned, we prioritized characterizing zero-shot consistency (RQ2) while conducting an exploratory investigation into few-shot example selection effects (RQ2b). This design modification reflects our commitment to following empirical evidence rather than predetermined hypotheses.

**Zero-Shot Consistency Study (RQ2)**

> To assess the reliability of zero-shot annotation, we conducted 50 repeated evaluations on two independent datasets: the training set (30 articles, 826 sentences) and the held-out test set (10 articles, 267 sentences). 
>
> Since zero-shot prompting does not depend on training data, both datasets are equally valid for consistency evaluation—zero-shot has not "seen" any articles in either set. We designated the training set as our primary analysis dataset due to its substantially larger sample size, which provides greater statistical power for sentence-level variability analysis (3× more sentences). The test set serves as an independent replication to verify that consistency patterns generalize across different article samples.
>
> This dual-dataset approach allows us to: (1) characterize zero-shot reliability with adequate statistical power, (2) test generalization of consistency patterns, and (3) investigate whether article characteristics influence annotation reliability.
>
> All runs used identical prompts and model parameters (temperature=1.0), allowing natural model stochasticity to produce variation across runs. We calculated aggregate consistency metrics (coefficient of variation, ICC) and performed sentence-level analysis to identify which instances showed stable versus uncertain predictions.

**Example Selection Exploration (RQ2b)**

> To investigate whether few-shot underperformance was due to poor example selection, we generated 5 alternative 3-shot example sets using different random seeds (100, 200, 300, 400, in addition to the original seed 42). Each set was evaluated once on the test set only (not the training set) to maintain complete independence between evaluation articles and the example pool. This prevents contamination from articles that appear in the example sets.
>
> This exploratory analysis (N=5 sets, each evaluated once) provides preliminary evidence regarding the role of example selection but is not powered for inferential statistics. Results inform hypotheses for future systematic investigation of optimal example selection strategies.

---

## Modified Success Criteria

**Phase 2 will be successful if we can answer:**

1. ✓ **Consistency characterization:** Is zero-shot annotation reliable enough for practical use?
2. ✓ **Practical guidance:** When should researchers trust zero-shot vs few-shot?
3. ✓ **Preliminary evidence:** Does example selection plausibly explain few-shot underperformance?
4. ✓ **Future directions:** What questions remain for systematic investigation?

**We acknowledge:**
- Phase 2b is exploratory, not confirmatory
- Small N limits conclusions about example selection
- Primary contribution is zero-shot consistency characterization
- Example selection effects deserve dedicated future study

---

## Key Decisions Summary

| Decision Point           | Choice                          | Rationale                                               |
| ------------------------ | ------------------------------- | ------------------------------------------------------- |
| Primary focus            | Zero-shot consistency           | Best performing condition; practical value              |
| Datasets for zero-shot   | Training (primary) + Test (replication) | Training set: better power; Test set: generalization |
| Number of zero-shot runs | 50 per dataset (100 total)      | Adequate power for ICC, CV; cross-dataset comparison    |
| Example selection study  | 5 alternative sets, 1 run each  | Exploratory; balance between evidence and feasibility   |
| Example selection dataset | Test set only                  | Avoids contamination from example articles              |
| Selection strategy       | Random (multiple seeds)         | Tests generalizability; stratified left for future work |
| Statistical approach     | Inferential for zero-shot; Descriptive for examples | Powered for primary; N=5 insufficient for significance |
| Framing                  | Transparent, exploratory        | Honest about scope and limitations                      |

---

## Implications for Publication

**Main Story:**
"Zero-shot prompting achieves competitive accuracy and demonstrates [high/moderate/low - TBD] consistency, making it a viable option for rhetorical move annotation in Biology research articles."

**Secondary Story:**
"Preliminary evidence suggests few-shot example selection may contribute to performance variability, warranting systematic investigation in future work."

**Contribution:**
1. First consistency analysis of zero-shot rhetorical move annotation
2. Evidence of task conditions where zero-shot suffices
3. Methodological guidance for resource-constrained researchers
4. Identification of example selection as research gap

**Limitations (Transparent):**
- 10-article test set limits fine-grained analysis
- Single domain (Biology) limits generalizability
- Exploratory example selection analysis (N=5)
- Single model family (GPT-4)

**Future Work:**
- Systematic example selection optimization
- Cross-domain validation
- Comparison to other LLM families
- Larger-scale consistency studies (100+ articles)

---

## Ethical Considerations

**Transparency:**
- Clearly label Phase 2b as exploratory
- Report all 5 alternative sets (no cherry-picking)
- Acknowledge when results are suggestive vs conclusive
- State limitations prominently

**Methodological Integrity:**
- Test set remains held out (never used in Phase 1)
- No hyperparameter tuning based on test set
- Random seeds documented for reproducibility
- Full code and data availability

**Intellectual Honesty:**
- Acknowledge that design was modified in response to data
- Frame as adaptive rather than confirmatory research
- Do not overstate conclusions from N=5 analysis
- Suggest rather than claim regarding example selection effects

---

**This revised design maintains scientific rigor while acknowledging and investigating an unexpected but meaningful finding. The primary focus on zero-shot consistency provides a robust contribution, while the exploratory example selection analysis addresses an obvious question without overreaching.**
