# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 29  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8165 (81.65%)  

**Weighted Precision:** 0.8197  
**Weighted Recall:** 0.8165  
**Weighted F1:** 0.8118  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9017 | 0.8814 | 0.8914 | 177 |
| 2 | 0.6538 | 0.4359 | 0.5231 | 39 |
| 3 | 0.6618 | 0.8824 | 0.7563 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.6030 (60.30%)  

**Weighted Precision:** 0.6148  
**Weighted Recall:** 0.6030  
**Weighted F1:** 0.5762  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.5556 | 0.4762 | 0.5128 | 21 |
| 1b | 0.6842 | 0.2889 | 0.4062 | 45 |
| 1c | 0.6985 | 0.8559 | 0.7692 | 111 |
| 2a | 1.0000 | 0.2000 | 0.3333 | 5 |
| 2b | 0.4583 | 0.4783 | 0.4681 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1364 | 0.3000 | 0.1875 | 10 |
| 3b | 0.5641 | 0.9167 | 0.6984 | 24 |
| 3c | 0.8571 | 0.3750 | 0.5217 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.8125 |
| text012 | 33 | 0.9394 | 0.6061 |
| text013 | 25 | 1.0000 | 0.6400 |
| text014 | 23 | 0.6957 | 0.4348 |
| text015 | 29 | 0.7586 | 0.5172 |
| text016 | 31 | 0.9032 | 0.7419 |
| text017 | 18 | 0.6111 | 0.5000 |
| text018 | 34 | 0.6471 | 0.5588 |
| text019 | 26 | 0.9231 | 0.8462 |
| text020 | 32 | 0.7500 | 0.4375 |
