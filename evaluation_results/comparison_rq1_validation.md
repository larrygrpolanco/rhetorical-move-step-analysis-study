# Condition Comparison Results

**Dataset:** validation  
**Research Question:** rq1  
**Conditions Compared:** 3  

**Conditions:**
1. eight_shot
2. three_shot
3. zero_shot

---

## Move-Level Performance Comparison

| Condition   |   Accuracy |   Precision |   Recall |     F1 |   Sentences |
|:------------|-----------:|------------:|---------:|-------:|------------:|
| eight_shot  |     0.8382 |      0.8593 |   0.8382 | 0.845  |         204 |
| three_shot  |     0.8431 |      0.8807 |   0.8431 | 0.8536 |         204 |
| zero_shot   |     0.8725 |      0.8881 |   0.8725 | 0.8776 |         204 |

## Step-Level Performance Comparison

| Condition   |   Accuracy |   Precision |   Recall |     F1 |   Sentences |
|:------------|-----------:|------------:|---------:|-------:|------------:|
| eight_shot  |     0.4853 |      0.5337 |   0.4853 | 0.4912 |         204 |
| three_shot  |     0.4706 |      0.5085 |   0.4706 | 0.4796 |         204 |
| zero_shot   |     0.5196 |      0.5503 |   0.5196 | 0.5229 |         204 |

---

## Statistical Significance Tests (McNemar's Test)

*McNemar's test evaluates whether accuracy differences between conditions are statistically significant.*

### Move-Level Comparisons

| Comparison | p-value | Significant (p<0.05)? | Statistic |
|------------|---------|----------------------|------------|
| eight_shot vs three_shot | 1.0000 | No | 10.0000 |
| eight_shot vs zero_shot | 0.1185 | No | 4.0000 |
| three_shot vs zero_shot | 0.1796 | No | 4.0000 |

### Step-Level Comparisons

| Comparison | p-value | Significant (p<0.05)? | Statistic |
|------------|---------|----------------------|------------|
| eight_shot vs three_shot | 0.7754 | No | 23.0000 |
| eight_shot vs zero_shot | 0.3489 | No | 17.0000 |
| three_shot vs zero_shot | 0.0872 | No | 9.0000 |

---

## Interpretation Guide

**p-value < 0.05:** Statistically significant difference  
**p-value ≥ 0.05:** No significant difference  

McNemar's test is specifically designed for paired comparisons (same sentences evaluated by different conditions), making it appropriate for this evaluation.
