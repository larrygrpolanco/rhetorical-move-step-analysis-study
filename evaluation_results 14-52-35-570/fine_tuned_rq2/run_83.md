# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 83  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8202 (82.02%)  

**Weighted Precision:** 0.8162  
**Weighted Recall:** 0.8202  
**Weighted F1:** 0.8138  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8674 | 0.8870 | 0.8771 | 177 |
| 2 | 0.6923 | 0.4615 | 0.5538 | 39 |
| 3 | 0.7333 | 0.8627 | 0.7928 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5393 (53.93%)  

**Weighted Precision:** 0.5143  
**Weighted Recall:** 0.5393  
**Weighted F1:** 0.5216  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.4545 | 0.4762 | 0.4651 | 21 |
| 1b | 0.4000 | 0.2667 | 0.3200 | 45 |
| 1c | 0.6667 | 0.7748 | 0.7167 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5789 | 0.4783 | 0.5238 | 23 |
| 2c | 0.2000 | 0.2500 | 0.2222 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1667 | 0.3000 | 0.2143 | 10 |
| 3b | 0.4800 | 0.5000 | 0.4898 | 24 |
| 3c | 0.5294 | 0.5625 | 0.5455 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.6875 |
| text012 | 33 | 0.9394 | 0.4545 |
| text013 | 25 | 1.0000 | 0.6400 |
| text014 | 23 | 0.7826 | 0.5217 |
| text015 | 29 | 0.7586 | 0.3448 |
| text016 | 31 | 0.7419 | 0.5484 |
| text017 | 18 | 0.6667 | 0.4444 |
| text018 | 34 | 0.8235 | 0.6176 |
| text019 | 26 | 0.9231 | 0.8077 |
| text020 | 32 | 0.6875 | 0.4062 |
