# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 25  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8427 (84.27%)  

**Weighted Precision:** 0.8445  
**Weighted Recall:** 0.8427  
**Weighted F1:** 0.8425  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9123 | 0.8814 | 0.8966 | 177 |
| 2 | 0.6216 | 0.5897 | 0.6053 | 39 |
| 3 | 0.7797 | 0.9020 | 0.8364 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5655 (56.55%)  

**Weighted Precision:** 0.5461  
**Weighted Recall:** 0.5655  
**Weighted F1:** 0.5399  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.5789 | 0.5238 | 0.5500 | 21 |
| 1b | 0.5789 | 0.2444 | 0.3438 | 45 |
| 1c | 0.6992 | 0.8378 | 0.7623 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5556 | 0.6522 | 0.6000 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.2667 | 0.4000 | 0.3200 | 10 |
| 3b | 0.4516 | 0.5833 | 0.5091 | 24 |
| 3c | 0.2308 | 0.1875 | 0.2069 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.7500 |
| text012 | 33 | 0.9697 | 0.6364 |
| text013 | 25 | 0.9200 | 0.4800 |
| text014 | 23 | 0.7391 | 0.4783 |
| text015 | 29 | 0.6552 | 0.3793 |
| text016 | 31 | 0.9032 | 0.6774 |
| text017 | 18 | 0.6667 | 0.4444 |
| text018 | 34 | 0.8529 | 0.6471 |
| text019 | 26 | 0.8846 | 0.6923 |
| text020 | 32 | 0.8750 | 0.4688 |
