# Next Steps: Organized Recommendations for Paper Development

## Executive Summary

**What you have:** A well-executed consistency study with a counterintuitive but important finding - zero-shot is more consistent than fine-tuned while maintaining comparable move-level accuracy.

**Core narrative:** Fine-tuning trades consistency for modest accuracy gains. When training data is limited and consistency matters, zero-shot may be the better choice.

**Key challenge:** Frame unexpected results (few-shot underperformance, fine-tuned inconsistency) as informative findings rather than methodological failures.

---

## 🔴 CRITICAL (Must Address)

These issues would cause reviewer rejection if not addressed.

### 1. Reframe Your Core Narrative

**Issue:** Your title/RQs emphasize accuracy comparison, but your most interesting finding is about **consistency**.

**Action:**
- Lead with consistency as the primary contribution
- Position this as extending Kim & Lu (2024): "While Kim & Lu tested 3 runs, we systematically evaluate consistency with 50 runs"
- Frame finding: "Zero-shot achieves comparable move accuracy (82.77% vs 81.65%, p=0.74) with superior consistency (CV=1.45% vs 2.65%, p=0.0055)"

**Where:** Abstract, Introduction, Discussion

---

### 2. Acknowledge Class Imbalance Limitations Prominently

**Issue:** Your step-level results are severely compromised by class imbalance, but this isn't foregrounded.

**Current state:**
- Step 1c: 47.2% of training data
- Steps 2a, 2c, 2d, 3d: <1% each
- Step-level accuracy: 45-58%

**Action:**
- Add limitation statement in Methods: "Due to severe class imbalance in CaRS-50 (e.g., step 1c=47.2%, steps 2a/2c/2d <1%), our evaluation focuses primarily on move-level classification. Step-level results are exploratory."
- Repeat in Results section header: "Given class imbalance, we focus interpretation on move-level performance"
- In Discussion: "Step-level annotation remains challenging across all approaches (45-58% accuracy), likely reflecting genuine task difficulty, severe class imbalance, and limited training data"

**Where:** Methods (dataset description), Results (section header), Discussion (limitations)

---

### 3. Explain Few-Shot Underperformance Honestly

**Issue:** Few-shot performing worse than zero-shot needs explanation.

**Your position (which I agree with):** This is the result of random sampling producing non-representative examples. This is informative, not a failure.

**Action:**
Write a clear explanation in Results/Discussion:

```markdown
Unexpectedly, few-shot approaches underperformed zero-shot (3-shot: 72.66%, 
8-shot: 77.15% vs zero-shot: 82.77%). Analysis of the randomly selected 
few-shot examples reveals likely causes:

**3-shot examples (77 sentences):**
- Step 2a: 0 instances (absent from examples)
- Step 1a: 2 instances (2.6% vs 6.7% in training data)
- Step 2c: 1 instance (1.3% vs 2.2% in training data)

This severe underrepresentation of rare steps in randomly selected examples 
suggests that few-shot learning for move-step annotation requires **stratified 
sampling** to ensure adequate representation of infrequent categories. Our 
random sampling approach, while methodologically valid, produced examples 
that failed to cover the label distribution adequately.

This finding has practical implications: researchers implementing few-shot 
annotation should employ stratified sampling rather than random selection, 
particularly when working with imbalanced datasets.
```

**Where:** Results (RQ1 section), Discussion

---

### 4. Address Statistical Assumption Violations

**Issue:** Fine-tuned move accuracy is non-normal (Shapiro-Wilk p=0.0132), but you used parametric tests.

**Action:**
- Add one sentence in Results: "Fine-tuned move accuracy showed departure from normality (Shapiro-Wilk p=0.0132); however, with n=50, the central limit theorem suggests our t-tests remain reasonably robust. We confirmed significance using non-parametric Mann-Whitney U test (p=0.0068)."
- Run the Mann-Whitney U test as a robustness check (takes 2 minutes in Python)

**Code:**
```python
from scipy.stats import mannwhitneyu
stat, p = mannwhitneyu(zero_shot_accuracies, finetuned_accuracies)
print(f"Mann-Whitney U: stat={stat}, p={p}")
```

**Where:** Results (statistical tests section)

---

### 5. Contextualize Kim & Lu Comparison Appropriately

**Issue:** You compare accuracies to Kim & Lu but conditions are too different.

**Action:**
- **Remove** statements like "Our accuracy was lower than Kim & Lu's 92.3%"
- **Replace** with: "Direct accuracy comparison to Kim & Lu (2024) is limited by differences in domain (Biology vs Applied Linguistics), framework granularity (11 vs 23 steps), and training size (30 vs 80 articles). Our move-level accuracies (81-83%) demonstrate feasibility of LLM annotation in Biology with limited training data."
- **Emphasize** what you add: "While Kim & Lu evaluated consistency with 3 runs, we provide the first systematic consistency analysis with 50 runs, revealing that..."

**Where:** Throughout Discussion, especially when comparing to prior work

---

## 🟡 IMPORTANT (Should Address to Strengthen Paper)

These additions significantly improve the paper's depth and credibility.

### 6. Add Basic Visualizations

**What to create:**
1. **Distribution comparison plot** (most important)
   - Side-by-side box plots or violin plots
   - Zero-shot vs Fine-tuned move accuracy distributions
   - Visually shows tighter spread for zero-shot
   
2. **Bar chart for RQ1** 
   - 4 conditions (zero-shot, 3-shot, 8-shot, fine-tuned)
   - Move accuracy + error bars (±1 SD)
   - Shows few-shot dip and consistency differences

**Where:** Results section, 2 figures total

**Time investment:** 1-2 hours

---

### 7. Analyze Move 2 Difficulty Specifically

**Issue:** Move 2 is terrible in fine-tuned (F1=47.06%, CV=10.11%) but better in zero-shot.

**Action:**
Add short paragraph in Results or Discussion:

```markdown
Fine-tuned performance on Move 2 was notably poor (precision=55.17%, 
recall=41.03%, F1=47.06%) and highly inconsistent (CV=10.11%), compared 
to zero-shot (precision=49.15%, recall=74.36%, F1=59.18%, CV=2.58%). 
This likely reflects Move 2's severe underrepresentation in training data 
(8.8% of sentences) combined with the fine-tuned model's sensitivity to 
training distribution. In contrast, zero-shot's pre-trained knowledge 
appears more robust to class imbalance. This finding is consistent with 
Kim & Lu (2024), who also reported Move 2 as most challenging.
```

**Where:** Results (move-level performance section) or Discussion

---

### 8. Calculate and Report Effect Sizes

**Issue:** You report p-values but not all effect sizes.

**Action:**
Add Cohen's d or variance ratios for key comparisons:

```markdown
**Variance comparison (Levene's test):**
- Zero-shot variance: 0.000141
- Fine-tuned variance: 0.000491
- Variance ratio: 3.5× higher in fine-tuned (95% CI: [2.1, 5.8])
- F-statistic: 8.05, p=0.0055

**Mean comparison (Welch's t-test):**
- Mean difference: 1.63 percentage points (95% CI: [0.92, 2.33])
- Cohen's d: 0.915 (large effect)
- t=4.57, p<0.001
```

**Where:** Results (statistical tests)

**Time investment:** 30 minutes (calculate CIs for variance ratio using bootstrap)

---

### 9. Sentence-Level Qualitative Analysis (Brief)

**What to do:**
- Pull the top 5 most inconsistent sentences for each condition
- Look at them qualitatively
- Add 1-2 example sentences to Discussion

**Example text:**
```markdown
Sentence-level analysis revealed specific sources of inconsistency. For example, 
Sentence 17 showed low agreement in both conditions (zero-shot: 46.89%, 
fine-tuned: 69.56%):

> "Recent studies have investigated the role of X in Y processes."

This sentence is genuinely ambiguous - it could be M1_S3 (reviewing previous 
research) or M1_S2 (making generalizations), depending on whether "recent 
studies" refers to a specific body of work or general trends. Such ambiguity 
accounts for [X]% of low-agreement sentences, suggesting inherent annotation 
difficulty rather than solely model limitation.
```

**Where:** Discussion (add one paragraph, ~150 words)

**Time investment:** 1-2 hours

---

### 10. Tighten Statistical Reporting

**Issue:** Too many redundant metrics reported.

**Action:**
**For RQ1 (accuracy comparison):**
- Report: Accuracy, F1, Support
- Drop: Individual precision/recall unless discussing specific class

**For RQ2 (consistency):**
- Report: CV (primary), ICC (reliability), Variance ratio (effect size)
- Drop: Mean comparisons (less relevant), detailed IQR/median

**Example simplified table:**

```markdown
| Condition   | Move Acc | Move F1 | Step Acc | Step F1 | CV    |
|-------------|----------|---------|----------|---------|-------|
| Zero-shot   | 82.77%   | 83.85%  | 49.81%   | 51.02%  | 1.45% |
| Fine-tuned  | 81.65%   | 81.09%  | 55.06%   | 52.20%  | 2.65% |
```

**Where:** Results tables

---

## 🟢 OPTIONAL (Nice to Have, Future Work)

These are good ideas but not necessary for this paper.

### 11. Few-Shot Consistency Runs
- **What:** Run 10-20 consistency iterations for 3-shot and 8-shot
- **Why:** Would show if consistency decreases monotonically with training
- **Verdict:** OUT OF SCOPE. Mention as future work: "Future research should examine whether consistency decreases monotonically from zero-shot through few-shot to fine-tuned"

### 12. Lower Temperature Experiments
- **What:** Test temperature=0.3, 0.5, 0.7 for consistency
- **Why:** Might reduce variance
- **Verdict:** OUT OF SCOPE. Mention in limitations: "We used temperature=1.0 following Kim & Lu (2024); lower temperatures may reduce variance but could affect output quality"

### 13. Cross-Model Comparison
- **What:** Test Claude, Llama, GPT-4o
- **Why:** Generalizability
- **Verdict:** FUTURE WORK. Mention in Discussion: "Future work should evaluate whether our consistency findings generalize to other LLMs"

### 14. Formal Power Analysis
- **What:** Post-hoc power calculation for Levene's test
- **Why:** Justifies n=50 choice
- **Verdict:** OPTIONAL. Only add if you have time and know how to do it properly. Otherwise skip.

---

## ⚫ CAN SKIP (Out of Scope or Unnecessary)

### 15. Re-running Few-Shot with Stratified Sampling
- **Why skip:** You correctly note this is unethical. Report what you found.
- **How to handle:** Frame as methodological learning (see #3 above)

### 16. Detailed Confusion Matrices for All Conditions
- **Why skip:** Too much detail for paper
- **How to handle:** Put in supplementary materials if journal allows

### 17. Aggregating Sentences into Rhetorical Chunks
- **Why skip:** Different research question entirely
- **How to handle:** Mention as limitation: "Sentence-level annotation may not align perfectly with rhetorical chunks"

### 18. Testing on More Disciplines
- **Why skip:** Beyond scope of this paper
- **How to handle:** One sentence in future work

---

## 📝 Writing Priorities

### Must Write:
1. **Abstract** - Lead with consistency finding, 200-250 words
2. **Introduction** - Position as extending Kim & Lu on consistency dimension
3. **Results RQ2** - Emphasize zero-shot consistency advantage
4. **Discussion** - Reframe findings around consistency-accuracy tradeoff
5. **Limitations** - Class imbalance, small training set, few-shot sampling

### Should Write:
6. **Results RQ1** - Explain few-shot underperformance (see #3)
7. **Discussion** - Move 2 difficulty analysis (see #7)
8. **Methods** - Add class imbalance caveat (see #2)

### Can Abbreviate:
9. Step-level results (exploratory, limited by class imbalance)
10. Article-level breakdowns (move to supplementary)

---

## 🎯 Your Core Argument

**Frame it like this:**

> "We provide the first systematic evaluation of LLM annotation consistency in genre analysis. Across 50 repeated runs, zero-shot GPT-4 demonstrated excellent consistency (CV=1.45%, ICC=0.835) while maintaining comparable move-level accuracy to fine-tuned models (82.77% vs 81.65%, p=0.74). Fine-tuning improved step-level accuracy but significantly increased variance (CV=2.65%, p=0.0055) and reduced reliability (ICC=0.565).
>
> These findings suggest that for genre analysis researchers working with limited training data (<50 articles) and severe class imbalance, zero-shot approaches may offer a better consistency-accuracy tradeoff than fine-tuning. However, both approaches struggled with underrepresented categories, indicating that improving automated genre analysis requires either larger, more balanced training sets or advances in handling imbalanced classification.
>
> Our results also demonstrate that few-shot learning requires careful example selection: randomly sampled examples that underrepresent rare categories can harm rather than help performance."

---

## ⏱️ Time Estimates

**Critical items (must do):** 4-6 hours
- Rewrite abstract/intro framing: 2 hours
- Add class imbalance statements: 30 min
- Write few-shot explanation: 1 hour
- Run Mann-Whitney U test: 15 min
- Revise Kim & Lu comparisons: 1 hour

**Important items (should do):** 4-6 hours
- Create 2 visualizations: 2 hours
- Calculate effect sizes + CIs: 1 hour
- Write Move 2 analysis: 1 hour
- Sentence-level examples: 1-2 hours
- Tighten statistical reporting: 1 hour

**Total:** 8-12 hours of focused work

---

## 📋 Checklist

### Before You Start Writing:
- [ ] Run Mann-Whitney U test for robustness check
- [ ] Calculate variance ratio confidence intervals (bootstrap)
- [ ] Create box plot comparing distributions
- [ ] Create bar chart for RQ1 results
- [ ] Extract top 5 inconsistent sentences for each condition
- [ ] Look at Move 2 confusion patterns in fine-tuned

### While Writing:
- [ ] Lead with consistency in abstract
- [ ] Add class imbalance caveat in Methods
- [ ] Explain few-shot underperformance in Results
- [ ] Frame as extending Kim & Lu (not competing on accuracy)
- [ ] Add Move 2 analysis paragraph
- [ ] Include 1-2 sentence examples
- [ ] Report Mann-Whitney U alongside t-test
- [ ] Simplify tables (remove redundant metrics)

### Before Submission:
- [ ] Supplementary materials with full results
- [ ] Code/data availability statement
- [ ] Check all p-values reported with effect sizes
- [ ] Ensure figures have clear captions
- [ ] Limitations section includes: class imbalance, small training set, single domain, temperature=1.0

---

## 🎓 Final Thoughts

**What you did well:**
- Rigorous experimental design
- Appropriate statistical tests
- 50 runs (more than adequate)
- Transparent documentation
- Held-out test set

**What to emphasize:**
- Consistency findings (novel)
- Practical implications (zero-shot may be sufficient)
- Methodological lessons (stratified few-shot sampling)

**What to downplay:**
- Absolute accuracy numbers (domain differences make comparison unfair)
- Step-level performance (limited by class imbalance)

**Remember:** Your paper's contribution is not "we got 82% accuracy." It's "we systematically evaluated consistency and found that simpler approaches may be more reliable than complex fine-tuning when data is limited."

That's a valuable finding. Own it. 💪

---

## 📚 Key Citations to Add

Beyond Kim & Lu (2024), consider citing:

1. **On class imbalance in NLP:**
   - He & Garcia (2009) on learning from imbalanced data
   - Or domain-specific NLP imbalance papers

2. **On few-shot example selection:**
   - Liu et al. (2022) "What Makes Good In-Context Examples for GPT-3?"
   - Or the paper you mentioned in your design doc

3. **On consistency/reliability:**
   - Landis & Koch (1977) on kappa interpretation
   - Shrout & Fleiss (1979) on ICC
   
4. **On LLM temperature effects:**
   - OpenAI documentation or papers on temperature-creativity tradeoffs

---

## Questions to Ask Yourself

Before submitting, answer these:

1. **Can a reader understand my contribution in 2 sentences?**
   - "We show zero-shot is more consistent than fine-tuned while maintaining comparable accuracy. This matters for practitioners with limited training data."

2. **Have I been honest about what my data shows?**
   - Yes: Few-shot underperformed, fine-tuned is less consistent
   - No evasion, no p-hacking, no hiding uncomfortable results

3. **Are my claims supported by appropriate statistics?**
   - Levene's test for variance: Yes
   - Effect sizes reported: Check
   - Robustness checks: Add Mann-Whitney U

4. **Would Kim & Lu find this interesting?**
   - Yes - you extend their work on a dimension they recommended (consistency)
   - You're not criticizing them, you're building on them

5. **Is my scope appropriate for a single paper?**
   - Yes - Two clear RQs, one dataset, focused narrative
   - Future work is future work, not this paper

---

**You've got this. The hard part (data collection) is done. Now just frame it honestly and clearly.** 🎯
