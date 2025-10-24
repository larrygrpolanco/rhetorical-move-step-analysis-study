# Condition Comparison Results

**Dataset:** test  
**Research Question:** rq1  
**Conditions Compared:** 4  

**Conditions:**
1. fine_tuned
2. eight_shot
3. three_shot
4. zero_shot

---

## Move-Level Performance Comparison

| Condition   |   Accuracy |   Precision |   Recall |     F1 |   Sentences |
|:------------|-----------:|------------:|---------:|-------:|------------:|
| fine_tuned  |     0.8165 |      0.8118 |   0.8165 | 0.8109 |         267 |
| eight_shot  |     0.7715 |      0.8402 |   0.7715 | 0.791  |         267 |
| three_shot  |     0.7266 |      0.8216 |   0.7266 | 0.7506 |         267 |
| zero_shot   |     0.8277 |      0.86   |   0.8277 | 0.8385 |         267 |

## Step-Level Performance Comparison

| Condition   |   Accuracy |   Precision |   Recall |     F1 |   Sentences |
|:------------|-----------:|------------:|---------:|-------:|------------:|
| fine_tuned  |     0.5506 |      0.5234 |   0.5506 | 0.522  |         267 |
| eight_shot  |     0.5056 |      0.5826 |   0.5056 | 0.5311 |         267 |
| three_shot  |     0.4494 |      0.5343 |   0.4494 | 0.4642 |         267 |
| zero_shot   |     0.4981 |      0.5783 |   0.4981 | 0.5102 |         267 |

---

## Statistical Significance Tests (McNemar's Test)

*McNemar's test evaluates whether accuracy differences between conditions are statistically significant.*

### Move-Level Comparisons

| Comparison | p-value | Significant (p<0.05)? | Statistic |
|------------|---------|----------------------|------------|
| eight_shot vs fine_tuned | 0.1263 | No | 20.0000 |
| eight_shot vs three_shot | 0.0428 | ✓ Yes | 9.0000 |
| eight_shot vs zero_shot | 0.0107 | ✓ Yes | 8.0000 |
| fine_tuned vs three_shot | 0.0037 | ✓ Yes | 20.0000 |
| fine_tuned vs zero_shot | 0.7428 | No | 17.0000 |
| three_shot vs zero_shot | 0.0000 | ✓ Yes | 2.0000 |

### Step-Level Comparisons

| Comparison | p-value | Significant (p<0.05)? | Statistic |
|------------|---------|----------------------|------------|
| eight_shot vs fine_tuned | 0.2461 | No | 39.0000 |
| eight_shot vs three_shot | 0.0627 | No | 21.0000 |
| eight_shot vs zero_shot | 0.9088 | No | 37.0000 |
| fine_tuned vs three_shot | 0.0093 | ✓ Yes | 37.0000 |
| fine_tuned vs zero_shot | 0.1933 | No | 43.0000 |
| three_shot vs zero_shot | 0.1048 | No | 21.0000 |

---

## Interpretation Guide

**p-value < 0.05:** Statistically significant difference  
**p-value ≥ 0.05:** No significant difference  

McNemar's test is specifically designed for paired comparisons (same sentences evaluated by different conditions), making it appropriate for this evaluation.
