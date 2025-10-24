# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 4  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8464 (84.64%)  

**Weighted Precision:** 0.8433  
**Weighted Recall:** 0.8464  
**Weighted F1:** 0.8378  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8989 | 0.9040 | 0.9014 | 177 |
| 2 | 0.7083 | 0.4359 | 0.5397 | 39 |
| 3 | 0.7538 | 0.9608 | 0.8448 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5805 (58.05%)  

**Weighted Precision:** 0.5789  
**Weighted Recall:** 0.5805  
**Weighted F1:** 0.5549  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.8462 | 0.5238 | 0.6471 | 21 |
| 1b | 0.7500 | 0.3333 | 0.4615 | 45 |
| 1c | 0.6897 | 0.9009 | 0.7812 | 111 |
| 2a | 0.2500 | 0.2000 | 0.2222 | 5 |
| 2b | 0.5263 | 0.4348 | 0.4762 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1765 | 0.3000 | 0.2222 | 10 |
| 3b | 0.3714 | 0.5417 | 0.4407 | 24 |
| 3c | 0.1538 | 0.1250 | 0.1379 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.7500 |
| text012 | 33 | 0.9091 | 0.6061 |
| text013 | 25 | 0.9600 | 0.4400 |
| text014 | 23 | 0.6957 | 0.5217 |
| text015 | 29 | 0.8276 | 0.4138 |
| text016 | 31 | 0.8710 | 0.6774 |
| text017 | 18 | 0.8333 | 0.7222 |
| text018 | 34 | 0.7059 | 0.5588 |
| text019 | 26 | 0.9615 | 0.6923 |
| text020 | 32 | 0.8125 | 0.5312 |
