# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 85  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8202 (82.02%)  

**Weighted Precision:** 0.8300  
**Weighted Recall:** 0.8202  
**Weighted F1:** 0.8187  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9053 | 0.8644 | 0.8844 | 177 |
| 2 | 0.7143 | 0.5128 | 0.5970 | 39 |
| 3 | 0.6571 | 0.9020 | 0.7603 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5506 (55.06%)  

**Weighted Precision:** 0.5753  
**Weighted Recall:** 0.5506  
**Weighted F1:** 0.5352  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.6875 | 0.5238 | 0.5946 | 21 |
| 1b | 0.6500 | 0.2889 | 0.4000 | 45 |
| 1c | 0.6767 | 0.8108 | 0.7377 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5500 | 0.4783 | 0.5116 | 23 |
| 2c | 0.2000 | 0.2500 | 0.2222 | 4 |
| 2d | 1.0000 | 0.1429 | 0.2500 | 7 |
| 3a | 0.2000 | 0.4000 | 0.2667 | 10 |
| 3b | 0.3333 | 0.5417 | 0.4127 | 24 |
| 3c | 0.2727 | 0.1875 | 0.2222 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.6250 |
| text012 | 33 | 0.7576 | 0.4848 |
| text013 | 25 | 0.9600 | 0.4400 |
| text014 | 23 | 0.7826 | 0.5217 |
| text015 | 29 | 0.7931 | 0.4483 |
| text016 | 31 | 0.9032 | 0.6774 |
| text017 | 18 | 0.7222 | 0.6111 |
| text018 | 34 | 0.8235 | 0.7059 |
| text019 | 26 | 0.8846 | 0.6923 |
| text020 | 32 | 0.7188 | 0.3438 |
