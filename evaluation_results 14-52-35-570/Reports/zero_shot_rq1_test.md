# Evaluation Results

**Condition:** zero_shot  
**Dataset:** test  
**Research Question:** rq1  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8277 (82.77%)  

**Weighted Precision:** 0.8600  
**Weighted Recall:** 0.8277  
**Weighted F1:** 0.8385  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9193 | 0.8362 | 0.8757 | 177 |
| 2 | 0.4915 | 0.7436 | 0.5918 | 39 |
| 3 | 0.9362 | 0.8627 | 0.8980 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.4981 (49.81%)  

**Weighted Precision:** 0.5783  
**Weighted Recall:** 0.4981  
**Weighted F1:** 0.5102  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.4545 | 0.4762 | 0.4651 | 21 |
| 1b | 0.3846 | 0.5556 | 0.4545 | 45 |
| 1c | 0.7973 | 0.5315 | 0.6378 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.3659 | 0.6522 | 0.4688 | 23 |
| 2c | 0.1333 | 0.5000 | 0.2105 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.2381 | 0.5000 | 0.3226 | 10 |
| 3b | 0.6000 | 0.5000 | 0.5455 | 24 |
| 3c | 0.8333 | 0.3125 | 0.4545 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.6250 |
| text012 | 33 | 1.0000 | 0.6970 |
| text013 | 25 | 1.0000 | 0.5600 |
| text014 | 23 | 0.6957 | 0.3913 |
| text015 | 29 | 0.7586 | 0.3448 |
| text016 | 31 | 0.7742 | 0.4839 |
| text017 | 18 | 0.7222 | 0.4444 |
| text018 | 34 | 0.7353 | 0.4118 |
| text019 | 26 | 0.7692 | 0.3846 |
| text020 | 32 | 0.8750 | 0.6250 |
