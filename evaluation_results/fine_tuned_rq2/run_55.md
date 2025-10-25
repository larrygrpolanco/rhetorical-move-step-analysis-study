# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 55  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8689 (86.89%)  

**Weighted Precision:** 0.8645  
**Weighted Recall:** 0.8689  
**Weighted F1:** 0.8625  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9056 | 0.9209 | 0.9132 | 177 |
| 2 | 0.7407 | 0.5128 | 0.6061 | 39 |
| 3 | 0.8167 | 0.9608 | 0.8829 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5843 (58.43%)  

**Weighted Precision:** 0.5776  
**Weighted Recall:** 0.5843  
**Weighted F1:** 0.5608  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.4545 | 0.4762 | 0.4651 | 21 |
| 1b | 0.4800 | 0.2667 | 0.3429 | 45 |
| 1c | 0.7068 | 0.8468 | 0.7705 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.6471 | 0.4783 | 0.5500 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 1.0000 | 0.1429 | 0.2500 | 7 |
| 3a | 0.3846 | 0.5000 | 0.4348 | 10 |
| 3b | 0.4286 | 0.3750 | 0.4000 | 24 |
| 3c | 0.5385 | 0.8750 | 0.6667 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.5625 |
| text012 | 33 | 0.9697 | 0.6061 |
| text013 | 25 | 0.9600 | 0.6000 |
| text014 | 23 | 0.8261 | 0.5217 |
| text015 | 29 | 0.8276 | 0.5172 |
| text016 | 31 | 0.8710 | 0.6129 |
| text017 | 18 | 0.6667 | 0.5556 |
| text018 | 34 | 0.8529 | 0.6176 |
| text019 | 26 | 0.9615 | 0.7692 |
| text020 | 32 | 0.7812 | 0.4688 |
