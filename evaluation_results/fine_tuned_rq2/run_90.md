# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 90  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8315 (83.15%)  

**Weighted Precision:** 0.8345  
**Weighted Recall:** 0.8315  
**Weighted F1:** 0.8298  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9070 | 0.8814 | 0.8940 | 177 |
| 2 | 0.6774 | 0.5385 | 0.6000 | 39 |
| 3 | 0.7031 | 0.8824 | 0.7826 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.6180 (61.80%)  

**Weighted Precision:** 0.6034  
**Weighted Recall:** 0.6180  
**Weighted F1:** 0.5975  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.6667 | 0.4762 | 0.5556 | 21 |
| 1b | 0.6667 | 0.3556 | 0.4638 | 45 |
| 1c | 0.7068 | 0.8468 | 0.7705 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5000 | 0.5652 | 0.5306 | 23 |
| 2c | 0.5000 | 0.5000 | 0.5000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1667 | 0.3000 | 0.2143 | 10 |
| 3b | 0.5714 | 0.6667 | 0.6154 | 24 |
| 3c | 0.6111 | 0.6875 | 0.6471 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.6875 |
| text012 | 33 | 0.9091 | 0.6364 |
| text013 | 25 | 1.0000 | 0.6800 |
| text014 | 23 | 0.8261 | 0.6522 |
| text015 | 29 | 0.6897 | 0.4138 |
| text016 | 31 | 0.8710 | 0.7097 |
| text017 | 18 | 0.7222 | 0.6111 |
| text018 | 34 | 0.7941 | 0.6765 |
| text019 | 26 | 0.8846 | 0.7308 |
| text020 | 32 | 0.7188 | 0.4375 |
