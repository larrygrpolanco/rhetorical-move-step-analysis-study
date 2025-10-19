# Evaluation Results: a1_zero_shot / gpt-5mini
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

**Overall Accuracy**: 85.8%
- *Percentage of sentences where predicted move matches gold standard move*

### Weighted Averages
*Weighted by the number of instances of each move (accounts for class imbalance)*

- **Precision**: 87.4%
  - *Of all sentences predicted as a given move, what % were correct?*
- **Recall**: 85.8%
  - *Of all sentences that actually belong to a given move, what % were found?*
- **F1 Score**: 86.3%
  - *Harmonic mean of precision and recall (balances both metrics)*

### Macro Averages
*Unweighted average across all moves (treats each move equally)*

- **Precision**: 80.7%
- **Recall**: 82.8%
- **F1 Score**: 81.3%

### Per-Move Breakdown

| Move | Precision | Recall | F1 Score | Support |
|------|-----------|--------|----------|----------|
| 1 | 91.6% | 88.6% | 90.1% | 123 |
| 2 | 56.8% | 75.0% | 64.6% | 28 |
| 3 | 93.8% | 84.9% | 89.1% | 53 |

*Support = number of sentences with this move in the gold standard*

## Step-Level Performance
*Step classification evaluates fine-grained rhetorical functions (1a, 1b, 2a, etc.)*

**Overall Accuracy**: 53.4%
- *Percentage of sentences where predicted step matches gold standard primary step*

### Weighted Averages
*Weighted by the number of instances of each step*

- **Precision**: 62.5%
- **Recall**: 53.4%
- **F1 Score**: 54.0%

### Macro Averages
*Unweighted average across all steps*

- **Precision**: 47.0%
- **Recall**: 39.8%
- **F1 Score**: 37.2%

### Per-Step Breakdown

| Step | Precision | Recall | F1 Score | Support |
|------|-----------|--------|----------|----------|
| 1a | 42.1% | 53.3% | 47.1% | 15 |
| 1b | 63.6% | 50.0% | 56.0% | 42 |
| 1c | 70.1% | 71.2% | 70.7% | 66 |
| 2a | 100.0% | 7.7% | 14.3% | 13 |
| 2b | 16.1% | 62.5% | 25.6% | 8 |
| 2c | 0.0% | 0.0% | 0.0% | 6 |
| 2d | 0.0% | 0.0% | 0.0% | 1 |
| 3a | 30.0% | 50.0% | 37.5% | 12 |
| 3b | 66.7% | 38.1% | 48.5% | 21 |
| 3c | 81.2% | 65.0% | 72.2% | 20 |

## Per-Article Results

| Article | Sentences | Move Acc. | Step Acc. | Issues |
|---------|-----------|-----------|-----------|--------|
| text001 | 26 | 84.6% | 61.5% | 0 |
| text002 | 14 | 92.9% | 50.0% | 0 |
| text003 | 15 | 73.3% | 66.7% | 0 |
| text004 | 16 | 93.8% | 43.8% | 0 |
| text005 | 23 | 87.0% | 52.2% | 0 |
| text006 | 19 | 84.2% | 52.6% | 0 |
| text007 | 16 | 75.0% | 31.2% | 0 |
| text008 | 27 | 92.6% | 51.9% | 0 |
| text009 | 22 | 90.9% | 45.5% | 0 |
| text010 | 26 | 80.8% | 69.2% | 0 |

