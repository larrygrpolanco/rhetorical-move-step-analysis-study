# Evaluation Results: a1_zero_shot / claude-sonnet-4-5
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

**Overall Accuracy**: 86.3%
- *Percentage of sentences where predicted move matches gold standard move*

### Weighted Averages
*Weighted by the number of instances of each move (accounts for class imbalance)*

- **Precision**: 86.7%
  - *Of all sentences predicted as a given move, what % were correct?*
- **Recall**: 86.3%
  - *Of all sentences that actually belong to a given move, what % were found?*
- **F1 Score**: 86.3%
  - *Harmonic mean of precision and recall (balances both metrics)*

### Macro Averages
*Unweighted average across all moves (treats each move equally)*

- **Precision**: 82.9%
- **Recall**: 80.6%
- **F1 Score**: 81.5%

### Per-Move Breakdown

| Move | Precision | Recall | F1 Score | Support |
|------|-----------|--------|----------|----------|
| 1 | 87.7% | 92.7% | 90.1% | 123 |
| 2 | 65.5% | 67.9% | 66.7% | 28 |
| 3 | 95.6% | 81.1% | 87.8% | 53 |

*Support = number of sentences with this move in the gold standard*

## Step-Level Performance
*Step classification evaluates fine-grained rhetorical functions (1a, 1b, 2a, etc.)*

**Overall Accuracy**: 51.5%
- *Percentage of sentences where predicted step matches gold standard primary step*

### Weighted Averages
*Weighted by the number of instances of each step*

- **Precision**: 58.8%
- **Recall**: 51.5%
- **F1 Score**: 51.5%

### Macro Averages
*Unweighted average across all steps*

- **Precision**: 44.7%
- **Recall**: 37.2%
- **F1 Score**: 35.9%

### Per-Step Breakdown

| Step | Precision | Recall | F1 Score | Support |
|------|-----------|--------|----------|----------|
| 1a | 38.5% | 33.3% | 35.7% | 15 |
| 1b | 47.5% | 69.0% | 56.3% | 42 |
| 1c | 71.4% | 60.6% | 65.6% | 66 |
| 2a | 100.0% | 15.4% | 26.7% | 13 |
| 2b | 16.7% | 50.0% | 25.0% | 8 |
| 2c | 0.0% | 0.0% | 0.0% | 6 |
| 2d | 0.0% | 0.0% | 0.0% | 1 |
| 3a | 31.6% | 50.0% | 38.7% | 12 |
| 3b | 60.0% | 28.6% | 38.7% | 21 |
| 3c | 81.2% | 65.0% | 72.2% | 20 |

## Per-Article Results

| Article | Sentences | Move Acc. | Step Acc. | Issues |
|---------|-----------|-----------|-----------|--------|
| text001 | 26 | 84.6% | 57.7% | 0 |
| text002 | 14 | 92.9% | 42.9% | 0 |
| text003 | 15 | 73.3% | 53.3% | 0 |
| text004 | 16 | 93.8% | 43.8% | 0 |
| text005 | 23 | 91.3% | 52.2% | 0 |
| text006 | 19 | 84.2% | 52.6% | 0 |
| text007 | 16 | 75.0% | 31.2% | 0 |
| text008 | 27 | 88.9% | 55.6% | 0 |
| text009 | 22 | 86.4% | 36.4% | 0 |
| text010 | 26 | 88.5% | 73.1% | 0 |

