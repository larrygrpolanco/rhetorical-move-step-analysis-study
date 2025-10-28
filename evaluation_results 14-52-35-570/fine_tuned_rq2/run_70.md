# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 70  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8464 (84.64%)  

**Weighted Precision:** 0.8502  
**Weighted Recall:** 0.8464  
**Weighted F1:** 0.8466  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9167 | 0.8701 | 0.8928 | 177 |
| 2 | 0.6316 | 0.6154 | 0.6234 | 39 |
| 3 | 0.7869 | 0.9412 | 0.8571 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5993 (59.93%)  

**Weighted Precision:** 0.5997  
**Weighted Recall:** 0.5993  
**Weighted F1:** 0.5927  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.5455 | 0.5714 | 0.5581 | 21 |
| 1b | 0.5862 | 0.3778 | 0.4595 | 45 |
| 1c | 0.7350 | 0.7748 | 0.7544 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.6522 | 0.6522 | 0.6522 | 23 |
| 2c | 0.0833 | 0.2500 | 0.1250 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.2353 | 0.4000 | 0.2963 | 10 |
| 3b | 0.5484 | 0.7083 | 0.6182 | 24 |
| 3c | 0.6154 | 0.5000 | 0.5517 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.7500 |
| text012 | 33 | 0.9697 | 0.6061 |
| text013 | 25 | 1.0000 | 0.6400 |
| text014 | 23 | 0.8261 | 0.6957 |
| text015 | 29 | 0.7586 | 0.4483 |
| text016 | 31 | 0.7419 | 0.5806 |
| text017 | 18 | 0.8333 | 0.7222 |
| text018 | 34 | 0.7647 | 0.6471 |
| text019 | 26 | 0.8462 | 0.5000 |
| text020 | 32 | 0.8750 | 0.5312 |
