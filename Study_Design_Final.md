# Study Design: LLM Consistency in CaRS Annotation Across Prompting Conditions

## Overview

**Core Design:** Replicate Kim & Lu (2024) methodology on Biology domain + add consistency analysis

**Model:** GPT-4 (fine-tunable version)

**Domain:** Biology research articles (CaRS-50 dataset)

**Novel Contribution:** First systematic evaluation of LLM annotation consistency across prompting conditions

---

## Research Questions

**RQ1:** Do Kim & Lu's (2024) findings generalize to Biology research articles?

**RQ2:** How does annotation consistency vary across zero-shot, few-shot, and fine-tuned conditions?

**RQ3:** Does the number of few-shot examples (3 vs. 8) affect performance and consistency?

---

## Phase 1: Kim & Lu Replication (Biology Domain)

### Dataset
- **Source:** CaRS-50 (Omotola et al., 2025)
- **Total:** 50 Biology research article introductions
- **Split:** 
  - Training: 30 articles
  - Validation: 10 articles  
  - Test: 10 articles

### Conditions (4)

**A1: Zero-shot**
- Kim & Lu's prompt adapted for CaRS-50 framework
- No examples provided
- Single run on test set

**A2: Few-shot (3 examples)**
- Same prompt + 3 annotated examples
- Examples randomly selected from training set
- Single run on test set

**A3: Few-shot (8 examples)**
- Same prompt + 8 annotated examples
- Examples randomly selected from training set
- Single run on test set

**A4: Fine-tuned**
- Supervised fine-tuning on 30 training articles
- GPT-4 base model
- Test on held-out 10 articles

### Evaluation Metrics (Following Kim & Lu)
- Move-level accuracy (3 classes)
- Step-level accuracy (11 classes)
- Precision, Recall, F1 per class
- McNemar's test for paired comparisons
- Confusion matrices

---

## Phase 2: Consistency Analysis (Novel Contribution)

### Design
Run each condition **30 times** on the same test set to measure variance

**Fixed parameters:**
- Test set: Same 10 articles across all runs
- Temperature: 1.0 (default, matches Kim & Lu)
- All other parameters constant

### Consistency Metrics

**Primary:**
- Mean accuracy (move and step level)
- Standard deviation
- Coefficient of variation (CV)
- 95% confidence intervals

**Secondary:**
- Intraclass correlation coefficient (ICC)
- Range (max - min accuracy)
- Bland-Altman plots for agreement

### Analysis Plan

**Compare consistency across conditions:**
- Is fine-tuning more consistent than zero-shot?
- Does few-shot reduce variance?
- Does 8-shot provide better consistency than 3-shot?

**Statistical tests:**
- F-test or Levene's test for variance comparison
- Mixed-effects model: `Accuracy ~ Condition + (1|Run)`
- Post-hoc pairwise comparisons

---

## Budget Estimates

### Phase 1: Single Runs
- Zero-shot: $0.05
- Few-shot (3 examples): $0.05
- Few-shot (8 examples): $0.05
- Fine-tuning training: $0.50
- Fine-tuning inference: $0.05
- **Phase 1 Total:** ~$0.70

### Phase 2: Consistency Runs (30 runs per condition)
- Zero-shot (30 runs): $1.50
- Few-shot 3-shot (30 runs): $1.50
- Few-shot 8-shot (30 runs): $1.50
- Fine-tuned (30 runs): $1.50
- **Phase 2 Total:** ~$6.00

**Total Budget:** ~$6.70

---

## Key Citations

**Primary replication target:**
- Kim, M., & Lu, X. (2024). Exploring the potential of using ChatGPT for rhetorical move-step analysis: The impact of prompt refinement, few-shot learning, and fine-tuning. *Journal of English for Academic Purposes*, 71, 101422.

**Dataset:**
- Omotola, B., et al. (2025). CaRS-50 dataset [Details TBD]

**Replication methodology:**
- McManus, C. (2024). [Replication standards - get full citation]

**Few-shot learning:**
- Brown, T., et al. (2020). Language models are few-shot learners. *NeurIPS*.

**Chain-of-thought background** (for lit review if needed):
- Wei, J., et al. (2022). Chain-of-thought prompting elicits reasoning in large language models. *NeurIPS*.
- Wang, B., et al. (2023). Towards understanding chain-of-thought prompting: An empirical study of what matters. *ACL*.

**Self-reflection background** (for lit review if needed):
- Shinn, N., et al. (2023). Reflexion: Language agents with verbal reinforcement learning.
- Renze, M., & Schubmehl, G. (2024). Self-reflection in LLM agents: Effects on problem-solving performance. *arXiv preprint*.

---

## Modifications from Kim & Lu (2024)

**Major:**
1. Domain: Applied Linguistics → Biology
2. Framework: 23 categories → 11 categories (CaRS-50)
3. Added consistency analysis (novel contribution)
4. Added 8-shot condition to test example count effects

**Minor:**
1. API version: gpt-3.5-turbo-1106 → gpt-4-[current version]
2. Explicit output formatting (for automated parsing)

---

## Timeline

| Week | Phase | Task |
|------|-------|------|
| 1-2  | Setup | Prepare dataset splits, prompts, code |
| 3    | Phase 1 | Run A1, A2, A3, A4 (single runs) |
| 4    | Analysis | Evaluate Phase 1, compare to Kim & Lu |
| 5-6  | Phase 2 | Consistency runs (30 runs × 4 conditions) |
| 7-8  | Analysis | Statistical analysis, visualizations |
| 9-10 | Writing | Draft manuscript |

**Total:** 10 weeks

---

## Success Criteria

**Phase 1 (Replication):**
- Move-level accuracy within ±10% of Kim & Lu results
- Same ranking: Fine-tuned > Few-shot > Zero-shot
- Statistical significance patterns replicate
- Clear comparison of 3-shot vs. 8-shot performance

**Phase 2 (Consistency):**
- Measurable variance across runs (not all identical)
- Clear differences in consistency across conditions
- Interpretable patterns (e.g., fine-tuned more consistent than zero-shot)

**Publication viability:**
- Even if findings differ from Kim & Lu, systematic documentation of cross-domain behavior is valuable
- Consistency analysis fills gap in existing literature
- Few-shot comparison (3 vs. 8) adds methodological insight

---

## Deliverables

1. **Full replication on Biology domain** (compare to Kim & Lu Table 2)
2. **Few-shot comparison** (3-shot vs. 8-shot)
3. **Consistency analysis** with descriptive statistics for all conditions
4. **Statistical comparison** of variance across conditions
5. **Manuscript** following McManus (2024) replication standards

---

## Next Immediate Steps

1. ✅ Confirm dataset access (CaRS-50 Biology articles)
2. ✅ Set up GPT-4 API access with fine-tuning capability
3. ✅ Adapt Kim & Lu prompts for CaRS-50 framework
4. ✅ Create training/validation/test splits
5. ✅ Prepare 3-shot and 8-shot example sets
6. ✅ Run Phase 1 baseline conditions (A1, A2, A3, A4)
7. ✅ Evaluate Phase 1 results
8. ✅ Launch Phase 2 consistency runs (30 × 4 = 120 total runs)

---

**This design is:** Clean, focused, replicable, and makes a clear novel contribution while building on established methodology. The addition of 3-shot vs. 8-shot comparison addresses methodological questions about optimal few-shot example count.
