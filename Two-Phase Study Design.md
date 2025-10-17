# Two-Phase Study Design: Complete Overview

## The Big Picture

**Phase 1 (Pilot):** Exploratory - Test many methods, find what works  
**Phase 2 (Main Study):** Confirmatory - Rigorously test the promising methods

---

## Phase 1: Pilot Study (Weeks 1-3)

### Purpose
"Which prompting methods are worth investigating rigorously?"

### Sample
- 10 articles (~260 sentences)
- These are "burned" for exploration

### Conditions Tested
1. ✅ **A1:** Zero-shot baseline (Kim & Lu replication)
2. ✅ **A2:** Few-shot (Kim & Lu replication)
3. ❓ **B1:** Chain-of-thought (simple)
4. ❓ **B2:** Chain-of-thought (detailed)
5. ❓ **B3:** Self-reflection
6. ❓ **C1:** Sentence-level context
7. ❓ **C2:** Explicit justification

### Budget
~$15 for all conditions

### Deliverable
**Decision:** Which 1-2 methods from ❓ to pursue in Phase 2?

---

## Phase 2: Main Study (Weeks 4-10)

### Purpose
"Rigorous evaluation of promising methods + Kim & Lu replication"

### Sample
- Remaining 40 articles (~1,037 sentences)
- Plus fine-tuning experiment (30 train, 10 test)

### Conditions (Example - Depends on Pilot)

**Scenario A: If CoT Wins in Pilot**
1. **Baseline:** Zero-shot (Kim & Lu replication)
2. **Few-shot:** 3 examples (Kim & Lu replication)
3. **CoT:** Best-performing CoT variant from pilot
4. **Fine-tuned:** Train on 30, test on 10 (Kim & Lu replication)

**Scenario B: If Context Wins in Pilot**
1. **Baseline:** Zero-shot
2. **Few-shot:** 3 examples
3. **Context-Aware:** Sentence-level context prompting
4. **Fine-tuned:** Train on 30, test on 10

**Scenario C: If Nothing Wins**
1. **Baseline:** Zero-shot (full dataset)
2. **Few-shot:** 3 examples (full dataset)
3. **Fine-tuned:** Train/test split
- Paper becomes pure Kim & Lu replication on Biology domain

### Budget
- Zero-shot: ~$2
- Few-shot: ~$5
- Best method from pilot: ~$5-15 (depends which)
- Fine-tuning: ~$60-80

**Total:** ~$70-100

### Deliverable
**Manuscript:** Following McManus (2024) standards

---

## Phase 2 Evaluation (Rigorous)

### Statistical Analysis

**For Zero-Shot Conditions (Baseline, Few-shot, Novel Method):**
- Test on all 40 articles (~1,037 sentences)
- **McNemar's test:** Paired comparisons
- **Bonferroni correction:** α = 0.05 / 3 = 0.0167
- **Effect sizes:** Odds ratios
- **No cross-validation needed** (not training anything)

**For Fine-Tuning:**
- Train on 30 articles
- Test on held-out 10 articles
- **McNemar's test** vs. zero-shot methods (on same 10 articles)

### Success Criteria
1. **Novel method beats baseline by ≥5%** (practical significance)
2. **p < 0.0167** (statistical significance, corrected)
3. **Results within ±10% of Kim & Lu** (generalizability check)

### Comparison Table in Paper

| Condition | Kim & Lu (AL) | This Study (Bio) | Difference |
|-----------|---------------|------------------|------------|
| Zero-shot (move) | 42.9% | X.X% | ±X.X% |
| Zero-shot (step) | 17.0% | X.X% | ±X.X% |
| Few-shot (move) | 52.7% | X.X% | ±X.X% |
| Few-shot (step) | 25.3% | X.X% | ±X.X% |
| Fine-tuned (move) | 92.3% | X.X% | ±X.X% |
| Fine-tuned (step) | 80.2% | X.X% | ±X.X% |
| **[Novel Method] (move)** | N/A | X.X% | NEW |
| **[Novel Method] (step)** | N/A | X.X% | NEW |

---

## Paper Structure (Following McManus 2024)

### Title
"Validating Kim & Lu (2024) with [Method Name]: Cross-Domain Evaluation of LLM-Assisted CaRS Annotation"

*Example:* "Validating Kim & Lu (2024) with Chain-of-Thought Reasoning: Cross-Domain Evaluation..."

---

### Abstract (250 words)
**Background:** Kim & Lu (2024) showed ChatGPT can annotate CaRS with 92% accuracy via fine-tuning on Applied Linguistics. However, no cross-domain validation exists, and alternative prompting methods remain unexplored.

**Purpose:** We validate Kim & Lu's findings on Biology articles and test whether [novel method] improves zero-shot performance.

**Method:** Using the CaRS-50 dataset (50 Biology articles, 1,297 sentences), we compared four conditions: zero-shot baseline, few-shot (3 examples), [novel method], and fine-tuned GPT-3.5-turbo. A pilot study (10 articles) informed method selection.

**Results:** [Novel method] achieved X.X% move-level accuracy, outperforming zero-shot baseline (X.X%, p < .01, OR = X.X) but remaining below fine-tuned performance (X.X%). Kim & Lu's findings partially replicated, with [similar/lower] accuracy on Biology (±X.X%).

**Conclusions:** [Novel method] offers a cost-effective improvement over baseline prompting without requiring training data. However, fine-tuning remains superior for production use. Results suggest CaRS annotation performance varies by domain, with implications for cross-disciplinary corpus studies.

---

### Introduction
1. **Genre analysis & CaRS framework** (2-3 paragraphs)
2. **LLMs for annotation tasks** (2-3 paragraphs)
3. **Kim & Lu (2024) study** (2-3 paragraphs)
   - Their methods and results
   - Limitations: single domain, unexplored methods
4. **Rationale for current study** (2 paragraphs)
   - Need for cross-domain validation
   - Testing alternative prompting methods
5. **Research questions** (1 paragraph)
   - RQ1: Do Kim & Lu's findings generalize to Biology?
   - RQ2: Does [novel method] improve zero-shot accuracy?

---

### Method (Following McManus Standards)

**2.1 Initial Study**
- Full description of Kim & Lu (2024)
- Their dataset, methods, results

**2.2 Rationale for Replication**
- High-impact study needing validation
- Single-domain limitation
- Unexplored prompting methods

**2.3 Modifications from Initial Study**

**Major Modifications:**
1. **Dataset:** Applied Linguistics (100 articles) → Biology (50 articles, CaRS-50)
2. **Novel condition:** Added [method name] based on pilot

**Minor Modifications:**
1. API version: gpt-3.5-turbo-1106 → gpt-3.5-turbo-0125
2. Smaller sample size (constraint)

**2.4 Pilot Study**
- Tested 7 prompting strategies on 10 articles
- Pre-specified decision criteria (3% improvement threshold)
- Selected [method] based on performance
- Full pilot results in Appendix A

**2.5 Main Study Design**
- 4 conditions on 40 articles (1,037 sentences)
- Plus fine-tuning on 30 articles, test on 10

**2.6 Materials**
- CaRS-50 dataset description
- Prompt templates for each condition (Appendix B)
- All materials on OSF: [link]

**2.7 Procedure**
- API calls, parameters, parsing methods

**2.8 Analysis Plan**
- McNemar's tests with Bonferroni correction
- Success criteria pre-specified

---

### Results

**3.1 Descriptive Statistics**
- Table 1: Performance across all conditions
- Figure 1: Bar chart (move vs. step by condition)

**3.2 Kim & Lu Replication**
- Table 2: Side-by-side comparison
- Narrative: Similar/different patterns

**3.3 Novel Method Evaluation**
- McNemar's test results
- Effect sizes and CIs
- Figure 2: Confusion matrices

**3.4 Fine-Tuning Results**
- Performance on Biology domain
- Comparison with Kim & Lu's fine-tuned results

**3.5 Error Analysis**
- Which moves/steps are hardest?
- Where does novel method help most?

---

### Discussion

**4.1 Key Findings**
- Kim & Lu findings [do/don't fully] generalize
- [Novel method] offers [X%] improvement
- Fine-tuning remains necessary for high accuracy

**4.2 Domain Differences**
- Why Biology may be easier/harder
- Linguistic differences in Biology vs. AL discourse

**4.3 Practical Implications**
- When to use which method
- Cost-benefit analysis

**4.4 Theoretical Implications**
- What does this tell us about LLM reasoning?
- What does this tell us about CaRS complexity?

**4.5 Limitations**
- Smaller dataset than Kim & Lu
- Single domain tested
- [Other honest limitations]

**4.6 Future Directions**
- Test on more domains
- Test other LLM architectures
- Combine methods (e.g., CoT + few-shot)

---

### References
- Kim & Lu (2024)
- McManus (2024)
- Omotola et al. (2025) - CaRS-50
- Wei et al. (2022) - CoT (if relevant)
- All other cited works

---

### Supplementary Materials (OSF)

**Appendix A: Pilot Study**
- Full results table
- All 7 prompt templates
- Decision rationale

**Appendix B: Main Study Prompts**
- Exact text for all conditions
- Examples used in few-shot

**Appendix C: Data & Code**
- CaRS-50 article IDs used
- Train/test split for fine-tuning
- Python scripts for API calls
- Analysis code (McNemar's, confusion matrices)

**Appendix D: Additional Results**
- Per-class performance (all 11 steps)
- Token usage and costs
- [If CoT:] Sample reasoning traces

---

## Timeline Summary

| Week | Phase | Task | Output |
|------|-------|------|--------|
| 1 | Pilot Setup | Extract prompts, write variants, sample data | Locked prompts |
| 2 | Pilot Run | Test 7 conditions on 10 articles | Pilot results |
| 3 | Pilot Analysis | Calculate metrics, make decision | Decision + rationale |
| 4 | Main Setup | Prepare remaining 40 articles | Ready to run |
| 5 | Main Run | Zero-shot, few-shot, novel method | Results files |
| 6 | Fine-tune | Prepare data, train model, test | Fine-tuned results |
| 7-8 | Analysis | McNemar's tests, confusion matrices | Full results |
| 9-10 | Writing | Draft manuscript per McManus (2024) | Draft paper |

**Total:** 10 weeks, ~$85-115

---

## Budget Breakdown

| Item | Cost |
|------|------|
| **Phase 1: Pilot** | |
| 7 conditions × 260 sentences × $0.008 avg | $15 |
| **Phase 2: Main Study** | |
| Zero-shot (1,037 sentences) | $2 |
| Few-shot (1,037 sentences) | $5 |
| Novel method (1,037 sentences) | $5-15* |
| Fine-tuning training | $60 |
| Fine-tuning testing (259 sentences) | $1 |
| **Total** | **$88-98** |

*Depends which method wins pilot

---

## Success Scenarios

### Best Case
- ✅ Novel method beats baseline by 10%+
- ✅ Kim & Lu results fully replicate
- ✅ Clear practical implications

**Contribution:** "We validate Kim & Lu (2024) and show [method] improves performance"

---

### Good Case
- ✅ Novel method beats baseline by 5-8%
- ⚠️ Kim & Lu results partially replicate (±5%)
- ✅ Interesting domain differences

**Contribution:** "We extend Kim & Lu (2024) and identify domain-specific challenges"

---

### Acceptable Case
- ⚠️ Novel method marginally better (3-4%)
- ✅ Kim & Lu replication is main story
- ✅ Valuable cross-domain validation

**Contribution:** "We provide first independent validation of Kim & Lu (2024) on Biology"

---

### Worst Case
- ❌ Nothing works better than baseline
- ❌ Kim & Lu results don't replicate well

**Pivot:** "We identify challenges in cross-domain CaRS annotation and discuss why Biology differs"

**Still publishable:** Negative results are valuable, especially if documented rigorously

---

## Key Principles (Review Before Each Phase)

### ✅ Pre-Commit
- Decide everything BEFORE seeing results
- No changing rules mid-stream

### ✅ Document Everything
- Save all prompts, code, decisions
- Timestamp everything

### ✅ Be Transparent
- Report pilot honestly
- Report failures honestly
- Report limitations honestly

### ✅ Follow McManus (2024)
- Justify study selection
- Describe all modifications
- Compare systematically with initial study

### ✅ Stay Flexible
- If pilot shows nothing works, that's OK
- Pivot to pure replication
- Still a contribution

---

## Your Next Immediate Actions

**This Week (Week 1):**

1. **Day 1-2:** Find Kim & Lu appendix, extract prompts
2. **Day 3-4:** Write your 5 prompt variants
3. **Day 5:** Sample 10 pilot articles
4. **Day 6-7:** Review and finalize all prompts

**Then:** Share with me for feedback before running pilot

**Questions to Ask Yourself:**
- Do I have Kim & Lu's exact prompts?
- Are my variants clear and different from baseline?
- Have I committed to not changing these?
- Do I understand what each variant is testing?

**Ready to start?** Go find those Kim & Lu prompts first, then we'll build your variants together.
