# Statistical Analysis Plan - Phase 2 (Revised)

## Zero-Shot vs Fine-Tuned Consistency Comparison

**Purpose:** Systematic comparison of annotation consistency between zero-shot and fine-tuned approaches  
**Design:** 50 runs per condition on test set (10 articles, ~267 sentences)  
**Conditions:** Zero-shot (A1) vs Fine-tuned (A4)

## Results Reporting Templates

### For Manuscript Results Section

**Template 1: Aggregate Consistency**

> To assess annotation consistency, we conducted 50 repeated evaluations of both zero-shot and fine-tuned approaches on the test set (10 articles, 267 sentences). Zero-shot annotation exhibited a mean move-level accuracy of X.X% (SD = X.X%, CV = X.X%), with a 95% confidence interval of [X.X%, X.X%]. Fine-tuned annotation achieved a mean accuracy of X.X% (SD = X.X%, CV = X.X%), with a 95% CI of [X.X%, X.X%]. The intraclass correlation coefficient for zero-shot was ICC(2,1) = 0.XXX [95% CI: 0.XXX, 0.XXX], indicating [poor/moderate/good/excellent] reliability, while fine-tuned achieved ICC(2,1) = 0.XXX [95% CI: 0.XXX, 0.XXX].

**Template 2: Variance Comparison**

> Levene's test revealed [a significant difference / no significant difference] in variance between conditions (F = X.XX, p = .XXX), with [zero-shot / fine-tuned] exhibiting X.XX× more variability. This suggests that [interpretation of practical significance].

**Template 3: Sentence-Level Patterns**

> Sentence-level analysis revealed distinct consistency patterns. For zero-shot, XX% of sentences were consistently annotated correctly (agreement > 90%), while XX% showed high uncertainty (agreement 30-70%). In comparison, fine-tuned annotation achieved high consistency on XX% of sentences, with XX% showing uncertainty. [Condition] demonstrated more stable predictions overall, with a mean sentence-level agreement rate of XX% compared to XX% for [other condition].

**Template 4: Stratified Analysis**

> Consistency varied significantly across move categories for [zero-shot / fine-tuned / both] conditions (Zero-shot: F(2, XXX) = X.XX, p = .XXX, η² = .XX; Fine-tuned: F(2, XXX) = X.XX, p = .XXX, η² = .XX). Move X demonstrated the highest consistency (Zero-shot: CV = X.X%; Fine-tuned: CV = X.X%), while Move X showed the greatest variability (Zero-shot: CV = XX.X%; Fine-tuned: CV = XX.X%).

---

## Interpretation Guidelines

### Coefficient of Variation (CV)

- **< 5%:** Excellent consistency - very stable performance
- **5-10%:** Good consistency - acceptable for research applications
- **10-20%:** Moderate consistency - interpret aggregate trends carefully
- **> 20%:** Poor consistency - individual predictions unreliable

### ICC(2,1) Interpretation (Koo & Li, 2016)

- **< 0.5:** Poor reliability - unacceptable for any application
- **0.5-0.75:** Moderate reliability - acceptable for exploratory research
- **0.75-0.9:** Good reliability - suitable for most research applications
- **> 0.9:** Excellent reliability - suitable for high-stakes applied use

### Effect Size (Cohen's d)

- **< 0.2:** Negligible effect
- **0.2-0.5:** Small effect
- **0.5-0.8:** Medium effect
- **> 0.8:** Large effect

---

**This analysis plan provides a rigorous, focused approach to RQ2 that will satisfy RMAL reviewers and produce high-quality methodological research.**
