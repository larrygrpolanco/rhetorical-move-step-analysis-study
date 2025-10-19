# Evaluation Results: a1_zero_shot / gpt-5
*Generated: /Users/larrygrpolanco/Documents/GitHub/rhetorical-move-step-analysis-study*
---
## Summary Statistics
- **Articles Evaluated**: 10
- **Total Sentences**: 204
- **Alignment Issues**: 0
- **Multi-tag Sentences (Gold)**: 0 (0.0%)
- **Multi-tag Sentences (Predicted)**: 0 (0.0%)

## Move-Level Performance
*Move classification evaluates broad rhetorical functions (Move 1, 2, 3)*

**Overall Accuracy**: 85.3%
- *Percentage of sentences where predicted move matches gold standard move*

### Weighted Averages
*Weighted by the number of instances of each move (accounts for class imbalance)*

- **Precision**: 85.7%
  - *Of all sentences predicted as a given move, what % were correct?*
- **Recall**: 85.3%
  - *Of all sentences that actually belong to a given move, what % were found?*
- **F1 Score**: 85.4%
  - *Harmonic mean of precision and recall (balances both metrics)*

### Macro Averages
*Unweighted average across all moves (treats each move equally)*

- **Precision**: 80.6%
- **Recall**: 78.5%
- **F1 Score**: 79.4%

### Per-Move Breakdown

| Move | Precision | Recall | F1 Score | Support |
|------|-----------|--------|----------|----------|
| 1 | 87.6% | 91.9% | 89.7% | 123 |
| 2 | 58.6% | 60.7% | 59.6% | 28 |
| 3 | 95.7% | 83.0% | 88.9% | 53 |

*Support = number of sentences with this move in the gold standard*

## Step-Level Performance
*Step classification evaluates fine-grained rhetorical functions (1a, 1b, 2a, etc.)*

**Overall Accuracy**: 52.5%
- *Percentage of sentences where predicted step matches gold standard primary step*

### Weighted Averages
*Weighted by the number of instances of each step*

- **Precision**: 55.6%
- **Recall**: 52.5%
- **F1 Score**: 52.4%

### Macro Averages
*Unweighted average across all steps*

- **Precision**: 39.9%
- **Recall**: 39.0%
- **F1 Score**: 37.2%

### Per-Step Breakdown

| Step | Precision | Recall | F1 Score | Support |
|------|-----------|--------|----------|----------|
| 1a | 50.0% | 53.3% | 51.6% | 15 |
| 1b | 49.1% | 66.7% | 56.6% | 42 |
| 1c | 69.6% | 59.1% | 63.9% | 66 |
| 2a | 33.3% | 7.7% | 12.5% | 13 |
| 2b | 17.4% | 50.0% | 25.8% | 8 |
| 2c | 0.0% | 0.0% | 0.0% | 6 |
| 2d | 0.0% | 0.0% | 0.0% | 1 |
| 3a | 35.3% | 50.0% | 41.4% | 12 |
| 3b | 57.1% | 38.1% | 45.7% | 21 |
| 3c | 86.7% | 65.0% | 74.3% | 20 |

## Per-Article Results

| Article | Sentences | Move Acc. | Step Acc. | Issues |
|---------|-----------|-----------|-----------|--------|
| text001 | 26 | 88.5% | 65.4% | 0 |
| text002 | 14 | 92.9% | 50.0% | 0 |
| text003 | 15 | 66.7% | 53.3% | 0 |
| text004 | 16 | 93.8% | 43.8% | 0 |
| text005 | 23 | 91.3% | 65.2% | 0 |
| text006 | 19 | 84.2% | 42.1% | 0 |
| text007 | 16 | 68.8% | 31.2% | 0 |
| text008 | 27 | 88.9% | 51.9% | 0 |
| text009 | 22 | 81.8% | 45.5% | 0 |
| text010 | 26 | 88.5% | 61.5% | 0 |

