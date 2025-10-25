# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 75  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.7865 (78.65%)  

**Weighted Precision:** 0.8035  
**Weighted Recall:** 0.7865  
**Weighted F1:** 0.7874  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8938 | 0.8079 | 0.8487 | 177 |
| 2 | 0.6250 | 0.5128 | 0.5634 | 39 |
| 3 | 0.6267 | 0.9216 | 0.7460 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5918 (59.18%)  

**Weighted Precision:** 0.6130  
**Weighted Recall:** 0.5918  
**Weighted F1:** 0.5745  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.6429 | 0.4286 | 0.5143 | 21 |
| 1b | 0.7895 | 0.3333 | 0.4688 | 45 |
| 1c | 0.7087 | 0.8108 | 0.7563 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.4615 | 0.5217 | 0.4898 | 23 |
| 2c | 0.2000 | 0.2500 | 0.2222 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.2222 | 0.6000 | 0.3243 | 10 |
| 3b | 0.4872 | 0.7917 | 0.6032 | 24 |
| 3c | 0.6667 | 0.3750 | 0.4800 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.6875 |
| text012 | 33 | 0.9394 | 0.6667 |
| text013 | 25 | 1.0000 | 0.5200 |
| text014 | 23 | 0.8261 | 0.6087 |
| text015 | 29 | 0.6897 | 0.5517 |
| text016 | 31 | 0.8387 | 0.6774 |
| text017 | 18 | 0.7778 | 0.6111 |
| text018 | 34 | 0.5294 | 0.5000 |
| text019 | 26 | 0.7308 | 0.6923 |
| text020 | 32 | 0.7500 | 0.4688 |
