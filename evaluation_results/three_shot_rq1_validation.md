# Evaluation Results

**Condition:** three_shot  
**Dataset:** validation  
**Research Question:** rq1  
**Articles Evaluated:** 10  
**Total Sentences:** 204  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8137 (81.37%)  

**Weighted Precision:** 0.8563  
**Weighted Recall:** 0.8137  
**Weighted F1:** 0.8251  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9417 | 0.7886 | 0.8584 | 123 |
| 2 | 0.4894 | 0.8214 | 0.6133 | 28 |
| 3 | 0.8519 | 0.8679 | 0.8598 | 53 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.4706 (47.06%)  

**Weighted Precision:** 0.5269  
**Weighted Recall:** 0.4706  
**Weighted F1:** 0.4893  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.4000 | 0.2667 | 0.3200 | 15 |
| 1b | 0.5556 | 0.4762 | 0.5128 | 42 |
| 1c | 0.7368 | 0.6364 | 0.6829 | 66 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 13 |
| 2b | 0.1481 | 0.5000 | 0.2286 | 8 |
| 2c | 0.1429 | 0.3333 | 0.2000 | 6 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 1 |
| 3a | 0.1579 | 0.2500 | 0.1935 | 12 |
| 3b | 0.4444 | 0.3810 | 0.4103 | 21 |
| 3c | 0.8125 | 0.6500 | 0.7222 | 20 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 0 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text001 | 26 | 0.6923 | 0.4615 |
| text002 | 14 | 0.9286 | 0.4286 |
| text003 | 15 | 0.8000 | 0.6667 |
| text004 | 16 | 0.9375 | 0.5000 |
| text005 | 23 | 0.6957 | 0.4783 |
| text006 | 19 | 0.7895 | 0.3158 |
| text007 | 16 | 0.7500 | 0.0625 |
| text008 | 27 | 0.8889 | 0.4815 |
| text009 | 22 | 0.8636 | 0.4091 |
| text010 | 26 | 0.8462 | 0.7692 |
