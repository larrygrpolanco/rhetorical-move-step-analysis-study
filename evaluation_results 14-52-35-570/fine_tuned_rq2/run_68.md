# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 68  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8052 (80.52%)  

**Weighted Precision:** 0.8091  
**Weighted Recall:** 0.8052  
**Weighted F1:** 0.8030  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8876 | 0.8475 | 0.8671 | 177 |
| 2 | 0.6129 | 0.4872 | 0.5429 | 39 |
| 3 | 0.6866 | 0.9020 | 0.7797 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5805 (58.05%)  

**Weighted Precision:** 0.6032  
**Weighted Recall:** 0.5805  
**Weighted F1:** 0.5765  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.8462 | 0.5238 | 0.6471 | 21 |
| 1b | 0.5517 | 0.3556 | 0.4324 | 45 |
| 1c | 0.6772 | 0.7748 | 0.7227 | 111 |
| 2a | 1.0000 | 0.2000 | 0.3333 | 5 |
| 2b | 0.4583 | 0.4783 | 0.4681 | 23 |
| 2c | 0.1667 | 0.2500 | 0.2000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1429 | 0.4000 | 0.2105 | 10 |
| 3b | 0.6250 | 0.6250 | 0.6250 | 24 |
| 3c | 0.6667 | 0.6250 | 0.6452 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.7500 |
| text012 | 33 | 0.9091 | 0.6667 |
| text013 | 25 | 1.0000 | 0.6800 |
| text014 | 23 | 0.7391 | 0.5217 |
| text015 | 29 | 0.7931 | 0.4483 |
| text016 | 31 | 0.9032 | 0.4516 |
| text017 | 18 | 0.7778 | 0.6111 |
| text018 | 34 | 0.6471 | 0.5294 |
| text019 | 26 | 0.6923 | 0.6923 |
| text020 | 32 | 0.7188 | 0.5625 |
