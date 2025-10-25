# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 99  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8764 (87.64%)  

**Weighted Precision:** 0.8765  
**Weighted Recall:** 0.8764  
**Weighted F1:** 0.8749  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9257 | 0.9153 | 0.9205 | 177 |
| 2 | 0.7576 | 0.6410 | 0.6944 | 39 |
| 3 | 0.7966 | 0.9216 | 0.8545 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.6330 (63.30%)  

**Weighted Precision:** 0.6219  
**Weighted Recall:** 0.6330  
**Weighted F1:** 0.6133  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.7059 | 0.5714 | 0.6316 | 21 |
| 1b | 0.7692 | 0.4444 | 0.5634 | 45 |
| 1c | 0.7424 | 0.8829 | 0.8066 | 111 |
| 2a | 0.2500 | 0.2000 | 0.2222 | 5 |
| 2b | 0.7083 | 0.7391 | 0.7234 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.2000 | 0.3000 | 0.2400 | 10 |
| 3b | 0.4444 | 0.6667 | 0.5333 | 24 |
| 3c | 0.2500 | 0.1250 | 0.1667 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.7500 |
| text012 | 33 | 0.9394 | 0.6364 |
| text013 | 25 | 1.0000 | 0.5200 |
| text014 | 23 | 0.7391 | 0.5217 |
| text015 | 29 | 0.8276 | 0.5517 |
| text016 | 31 | 0.9032 | 0.7097 |
| text017 | 18 | 0.7222 | 0.5556 |
| text018 | 34 | 0.7941 | 0.7353 |
| text019 | 26 | 1.0000 | 0.8846 |
| text020 | 32 | 0.8750 | 0.4688 |
