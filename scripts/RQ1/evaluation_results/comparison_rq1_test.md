# Condition Comparison Results

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

## Interpretation Guide

**p-value < 0.05:** Statistically significant difference  
**p-value ≥ 0.05:** No significant difference  

McNemar's test is specifically designed for paired comparisons (same sentences evaluated by different conditions), making it appropriate for this evaluation.
