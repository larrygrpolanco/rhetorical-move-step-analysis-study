# Evaluation Results

**Condition:** three_shot  
**Dataset:** validation  
**Research Question:** rq1  
**Articles Evaluated:** 10  
**Total Sentences:** 204  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8431 (84.31%)  

**Weighted Precision:** 0.8807  
**Weighted Recall:** 0.8431  
**Weighted F1:** 0.8536  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9533 | 0.8293 | 0.8870 | 123 |
| 2 | 0.5217 | 0.8571 | 0.6486 | 28 |
| 3 | 0.9020 | 0.8679 | 0.8846 | 53 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.4706 (47.06%)  

**Weighted Precision:** 0.5085  
**Weighted Recall:** 0.4706  
**Weighted F1:** 0.4796  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.4286 | 0.4000 | 0.4138 | 15 |
| 1b | 0.5000 | 0.4524 | 0.4750 | 42 |
| 1c | 0.6909 | 0.5758 | 0.6281 | 66 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 13 |
| 2b | 0.1714 | 0.7500 | 0.2791 | 8 |
| 2c | 0.1111 | 0.1667 | 0.1333 | 6 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 1 |
| 3a | 0.2857 | 0.3333 | 0.3077 | 12 |
| 3b | 0.4737 | 0.4286 | 0.4500 | 21 |
| 3c | 0.7647 | 0.6500 | 0.7027 | 20 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 0 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text001 | 26 | 0.8077 | 0.5385 |
| text002 | 14 | 0.9286 | 0.5000 |
| text003 | 15 | 0.8000 | 0.7333 |
| text004 | 16 | 0.8750 | 0.3750 |
| text005 | 23 | 0.9130 | 0.5217 |
| text006 | 19 | 0.7895 | 0.3684 |
| text007 | 16 | 0.7500 | 0.1875 |
| text008 | 27 | 0.8889 | 0.3333 |
| text009 | 22 | 0.9091 | 0.4545 |
| text010 | 26 | 0.7692 | 0.6538 |
