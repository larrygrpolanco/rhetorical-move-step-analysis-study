# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 24  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8502 (85.02%)  

**Weighted Precision:** 0.8495  
**Weighted Recall:** 0.8502  
**Weighted F1:** 0.8463  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9034 | 0.8983 | 0.9008 | 177 |
| 2 | 0.7241 | 0.5385 | 0.6176 | 39 |
| 3 | 0.7581 | 0.9216 | 0.8319 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5993 (59.93%)  

**Weighted Precision:** 0.5968  
**Weighted Recall:** 0.5993  
**Weighted F1:** 0.5785  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.6000 | 0.4286 | 0.5000 | 21 |
| 1b | 0.6957 | 0.3556 | 0.4706 | 45 |
| 1c | 0.6957 | 0.8649 | 0.7711 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.6316 | 0.5217 | 0.5714 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.2105 | 0.4000 | 0.2759 | 10 |
| 3b | 0.5294 | 0.7500 | 0.6207 | 24 |
| 3c | 0.5556 | 0.3125 | 0.4000 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.6250 |
| text012 | 33 | 0.9394 | 0.6364 |
| text013 | 25 | 1.0000 | 0.6400 |
| text014 | 23 | 0.8261 | 0.5217 |
| text015 | 29 | 0.7586 | 0.4483 |
| text016 | 31 | 0.8387 | 0.6774 |
| text017 | 18 | 0.7222 | 0.4444 |
| text018 | 34 | 0.7353 | 0.6471 |
| text019 | 26 | 0.9615 | 0.8462 |
| text020 | 32 | 0.8125 | 0.4688 |
