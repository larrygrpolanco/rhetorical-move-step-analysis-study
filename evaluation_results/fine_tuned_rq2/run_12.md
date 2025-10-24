# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 12  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8015 (80.15%)  

**Weighted Precision:** 0.8053  
**Weighted Recall:** 0.8015  
**Weighted F1:** 0.8021  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8876 | 0.8475 | 0.8671 | 177 |
| 2 | 0.5263 | 0.5128 | 0.5195 | 39 |
| 3 | 0.7333 | 0.8627 | 0.7928 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5506 (55.06%)  

**Weighted Precision:** 0.5475  
**Weighted Recall:** 0.5506  
**Weighted F1:** 0.5379  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.5882 | 0.4762 | 0.5263 | 21 |
| 1b | 0.6923 | 0.4000 | 0.5070 | 45 |
| 1c | 0.6746 | 0.7658 | 0.7173 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.3600 | 0.3913 | 0.3750 | 23 |
| 2c | 0.0833 | 0.2500 | 0.1250 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1000 | 0.1000 | 0.1000 | 10 |
| 3b | 0.4722 | 0.7083 | 0.5667 | 24 |
| 3c | 0.4286 | 0.3750 | 0.4000 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.5625 |
| text012 | 33 | 0.9394 | 0.5758 |
| text013 | 25 | 1.0000 | 0.5200 |
| text014 | 23 | 0.8261 | 0.6957 |
| text015 | 29 | 0.6552 | 0.4138 |
| text016 | 31 | 0.6774 | 0.5484 |
| text017 | 18 | 0.7222 | 0.5556 |
| text018 | 34 | 0.7647 | 0.6176 |
| text019 | 26 | 0.8846 | 0.7692 |
| text020 | 32 | 0.6875 | 0.3125 |
