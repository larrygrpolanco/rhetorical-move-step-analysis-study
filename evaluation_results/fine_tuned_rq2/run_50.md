# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 50  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8577 (85.77%)  

**Weighted Precision:** 0.8510  
**Weighted Recall:** 0.8577  
**Weighted F1:** 0.8525  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9011 | 0.9266 | 0.9136 | 177 |
| 2 | 0.6667 | 0.5128 | 0.5797 | 39 |
| 3 | 0.8182 | 0.8824 | 0.8491 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.6292 (62.92%)  

**Weighted Precision:** 0.6025  
**Weighted Recall:** 0.6292  
**Weighted F1:** 0.6067  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.5556 | 0.4762 | 0.5128 | 21 |
| 1b | 0.6667 | 0.4889 | 0.5641 | 45 |
| 1c | 0.7328 | 0.8649 | 0.7934 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5455 | 0.5217 | 0.5333 | 23 |
| 2c | 0.1667 | 0.2500 | 0.2000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.2727 | 0.3000 | 0.2857 | 10 |
| 3b | 0.5429 | 0.7917 | 0.6441 | 24 |
| 3c | 0.5556 | 0.3125 | 0.4000 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.6250 |
| text012 | 33 | 0.9697 | 0.6667 |
| text013 | 25 | 0.9600 | 0.7200 |
| text014 | 23 | 0.8261 | 0.5652 |
| text015 | 29 | 0.7931 | 0.5172 |
| text016 | 31 | 0.9032 | 0.7097 |
| text017 | 18 | 0.7222 | 0.6667 |
| text018 | 34 | 0.8235 | 0.6765 |
| text019 | 26 | 0.8462 | 0.5769 |
| text020 | 32 | 0.7812 | 0.5625 |
