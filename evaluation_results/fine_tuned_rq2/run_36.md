# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 36  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.7903 (79.03%)  

**Weighted Precision:** 0.7935  
**Weighted Recall:** 0.7903  
**Weighted F1:** 0.7888  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8824 | 0.8475 | 0.8646 | 177 |
| 2 | 0.5625 | 0.4615 | 0.5070 | 39 |
| 3 | 0.6615 | 0.8431 | 0.7414 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5693 (56.93%)  

**Weighted Precision:** 0.6062  
**Weighted Recall:** 0.5693  
**Weighted F1:** 0.5587  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.6000 | 0.4286 | 0.5000 | 21 |
| 1b | 0.7391 | 0.3778 | 0.5000 | 45 |
| 1c | 0.6667 | 0.7928 | 0.7243 | 111 |
| 2a | 1.0000 | 0.2000 | 0.3333 | 5 |
| 2b | 0.6000 | 0.5217 | 0.5581 | 23 |
| 2c | 0.2500 | 0.5000 | 0.3333 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1250 | 0.3000 | 0.1765 | 10 |
| 3b | 0.4722 | 0.7083 | 0.5667 | 24 |
| 3c | 0.6000 | 0.1875 | 0.2857 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.7500 |
| text012 | 33 | 0.9091 | 0.7273 |
| text013 | 25 | 0.9200 | 0.4400 |
| text014 | 23 | 0.7391 | 0.6087 |
| text015 | 29 | 0.6552 | 0.4483 |
| text016 | 31 | 0.6774 | 0.3871 |
| text017 | 18 | 0.7778 | 0.5000 |
| text018 | 34 | 0.6765 | 0.5882 |
| text019 | 26 | 0.9615 | 0.9231 |
| text020 | 32 | 0.7500 | 0.4062 |
