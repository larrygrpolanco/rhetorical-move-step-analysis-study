# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 22  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.7865 (78.65%)  

**Weighted Precision:** 0.8121  
**Weighted Recall:** 0.7865  
**Weighted F1:** 0.7907  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9103 | 0.8023 | 0.8529 | 177 |
| 2 | 0.6471 | 0.5641 | 0.6027 | 39 |
| 3 | 0.5974 | 0.9020 | 0.7188 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5581 (55.81%)  

**Weighted Precision:** 0.5794  
**Weighted Recall:** 0.5581  
**Weighted F1:** 0.5541  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.6875 | 0.5238 | 0.5946 | 21 |
| 1b | 0.6522 | 0.3333 | 0.4412 | 45 |
| 1c | 0.7094 | 0.7477 | 0.7281 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5600 | 0.6087 | 0.5833 | 23 |
| 2c | 0.2000 | 0.2500 | 0.2222 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.0952 | 0.2000 | 0.1290 | 10 |
| 3b | 0.3721 | 0.6667 | 0.4776 | 24 |
| 3c | 0.5385 | 0.4375 | 0.4828 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.6875 |
| text012 | 33 | 0.9091 | 0.5758 |
| text013 | 25 | 0.9200 | 0.5600 |
| text014 | 23 | 0.7826 | 0.5652 |
| text015 | 29 | 0.7931 | 0.4483 |
| text016 | 31 | 0.4839 | 0.3548 |
| text017 | 18 | 0.7778 | 0.6111 |
| text018 | 34 | 0.7941 | 0.7059 |
| text019 | 26 | 0.7692 | 0.6154 |
| text020 | 32 | 0.8125 | 0.5312 |
