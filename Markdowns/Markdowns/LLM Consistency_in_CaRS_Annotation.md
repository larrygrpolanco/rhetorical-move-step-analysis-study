Models: GPT-3.5, GPT-4, Claude, Llama (4 models)
Conditions per model: Zero-shot, Few-shot, Fine-tuned (3 conditions)
Runs per condition: 30
Temperature settings: 0.0, 0.5, 1.0 (3 temps)
Test sets: Apply Ling, Biology, Psychology (3 domains)

Total runs: 4 × 3 × 30 × 3 × 3 = 3,240 runs
```

**What to measure:**

1. **Within-model consistency:**
   - Variance across runs for same model/condition
   - CV for each model
   - Distribution shape

2. **Between-model consistency:**
   - Which models are most stable?
   - Does fine-tuning reduce variance equally across models?
   - Model × temperature interaction

3. **Temperature effects:**
   - How much does temperature matter?
   - Optimal temperature for consistency vs. accuracy trade-off

4. **Cross-domain consistency:**
   - Is consistency domain-dependent?
   - Which models generalize consistency better?

**Statistical Framework:**
```
Mixed-effects model:
Accuracy ~ Model + Condition + Temperature + Domain + (1|Run)

With variance components:
σ²_between-models
σ²_within-model
σ²_residual
```

**Report:**
- Intraclass correlation coefficients (ICC)
- Variance partition coefficients
- Reliability coefficients (Cronbach's alpha analogue)
- Bland-Altman plots for agreement

---

## Practical Recommendation for YOUR Study

Given your constraints, here's what I'd do:

### **Phase 1 Pilot - No Consistency Testing**
- Too expensive to test consistency for exploratory conditions
- Just run each once
- Pick your winner

### **Phase 2 Main Study - Strategic Consistency Testing**

**Option A: Minimal but Defensible**
```
What: 10 runs of your best method on a SUBSET
How: Test on 5 articles (130 sentences) instead of full test set
Runs: 10
Cost: 10 × 130 × $0.008 = $10.40

Report:
- "To assess consistency, we ran the best-performing 
  method 10 times on a random subset of 5 test articles.
  Accuracy ranged from X% to Y% (M = Z%, SD = W%, 95% CI [L, U])."
```

**Option B: Better but Pricey**
```
What: 10 runs of your top 2 methods on full test set
Runs: 10 × 2 = 20 total
Cost: 20 × 1,037 × $0.008 = $166

Report:
- Full descriptive statistics
- Comparison of variance between methods
- "Method A was more consistent (SD=X%) than Method B (SD=Y%), 
  F(9,9) = Z, p = .XX"
```

**Option C: My Actual Recommendation**
```
What: 5 runs on subset + temperature exploration
How: 
- 5 runs at temp=1.0 on 10 articles
- 5 runs at temp=0.7 on same 10 articles  
- 5 runs at temp=0.5 on same 10 articles

Cost: 15 × 260 × $0.008 = $31.20

Report:
- Consistency at different temperatures
- Optimal temperature for your task
- This is NOVEL - Kim & Lu didn't do this!
```

---

## For an Extension Study Design

**Title:** *"Consistency and Reliability of Large Language Models in Rhetorical Move-Step Annotation: A Multi-Model, Multi-Temperature Comparison"*

### Research Questions:
1. How consistent are different LLMs at CaRS annotation across repeated runs?
2. Does model consistency improve with fine-tuning?
3. What temperature setting optimizes the accuracy-consistency trade-off?
4. Do consistency patterns generalize across domains?

### Design:

**Models (4):** GPT-3.5-turbo, GPT-4, Claude-3, Llama-3-70B

**Conditions per model (3):**
- Zero-shot (refined prompt)
- Few-shot (3 examples)
- Fine-tuned (80 articles)

**Temperature settings (3):** 0.3, 0.7, 1.0

**Runs per combination:** 30

**Test sets (3 domains):**
- Applied Linguistics (10 articles)
- Biology (10 articles)  
- Psychology (10 articles)

**Total:** 4 models × 3 conditions × 3 temps × 30 runs × 3 domains = **3,240 runs**

### Key Metrics:

1. **Accuracy metrics** (standard)
   - Mean accuracy
   - Precision, recall, F1

2. **Consistency metrics** (novel focus)
   - **Coefficient of variation (CV)**
   - **Intraclass correlation coefficient (ICC)**
   - **95% confidence interval width**
   - **Range (max-min)**
   - **Reliability coefficient** (adapted from psychometrics)

3. **Stability metrics**
   - **Accuracy-consistency trade-off curve**
   - **Temperature sensitivity**

### Statistical Analysis:
```
Linear mixed model:
Accuracy ~ Model * Condition * Temperature * Domain + (1|Run)

Variance model:
SD ~ Model + Condition + Temperature + Domain + Model:Condition
```

**Key comparisons:**
- Which model is most consistent overall?
- Does fine-tuning reduce variance equally across models?
- Optimal temperature per model
- Domain effects on consistency

### Expected Findings:

**Hypotheses:**
1. Fine-tuned models will be more consistent (lower CV)
2. Lower temperature → higher consistency, possibly lower accuracy
3. GPT-4 will be more consistent than GPT-3.5
4. Consistency will be domain-dependent
5. Optimal temperature will vary by model

### Sample Results Table:
```
| Model      | Condition  | Temp | Mean Acc | SD   | CV    | 95% CI      |
|------------|-----------|------|----------|------|-------|-------------|
| GPT-3.5    | Zero-shot | 1.0  | 52.7%    | 3.2% | 6.1%  | [51.1,54.3] |
| GPT-3.5    | Zero-shot | 0.7  | 51.8%    | 1.8% | 3.5%  | [51.1,52.5] |
| GPT-3.5    | Fine-tune | 1.0  | 92.3%    | 0.9% | 1.0%  | [91.9,92.7] |
| GPT-4      | Zero-shot | 1.0  | 67.2%    | 2.1% | 3.1%  | [66.4,68.0] |
| GPT-4      | Fine-tune | 1.0  | 95.1%    | 0.5% | 0.5%  | [94.9,95.3] |