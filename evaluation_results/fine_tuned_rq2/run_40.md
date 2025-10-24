# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 40  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8352 (83.52%)  

**Weighted Precision:** 0.8451  
**Weighted Recall:** 0.8352  
**Weighted F1:** 0.8357  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9325 | 0.8588 | 0.8941 | 177 |
| 2 | 0.6111 | 0.5641 | 0.5867 | 39 |
| 3 | 0.7206 | 0.9608 | 0.8235 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5693 (56.93%)  

**Weighted Precision:** 0.5851  
**Weighted Recall:** 0.5693  
**Weighted F1:** 0.5607  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.6250 | 0.4762 | 0.5405 | 21 |
| 1b | 0.6190 | 0.2889 | 0.3939 | 45 |
| 1c | 0.7143 | 0.8108 | 0.7595 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.6500 | 0.5652 | 0.6047 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1739 | 0.4000 | 0.2424 | 10 |
| 3b | 0.5000 | 0.7083 | 0.5862 | 24 |
| 3c | 0.4545 | 0.3125 | 0.3704 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.6250 |
| text012 | 33 | 0.9091 | 0.6667 |
| text013 | 25 | 1.0000 | 0.4800 |
| text014 | 23 | 0.7391 | 0.3913 |
| text015 | 29 | 0.9310 | 0.6207 |
| text016 | 31 | 0.7419 | 0.5806 |
| text017 | 18 | 0.8333 | 0.6111 |
| text018 | 34 | 0.7353 | 0.6471 |
| text019 | 26 | 0.8077 | 0.6538 |
| text020 | 32 | 0.8125 | 0.4062 |
