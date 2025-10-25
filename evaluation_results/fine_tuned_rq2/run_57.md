# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 57  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8464 (84.64%)  

**Weighted Precision:** 0.8638  
**Weighted Recall:** 0.8464  
**Weighted F1:** 0.8462  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9273 | 0.8644 | 0.8947 | 177 |
| 2 | 0.8214 | 0.5897 | 0.6866 | 39 |
| 3 | 0.6757 | 0.9804 | 0.8000 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5993 (59.93%)  

**Weighted Precision:** 0.6016  
**Weighted Recall:** 0.5993  
**Weighted F1:** 0.5777  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.5263 | 0.4762 | 0.5000 | 21 |
| 1b | 0.6364 | 0.3111 | 0.4179 | 45 |
| 1c | 0.7177 | 0.8018 | 0.7574 | 111 |
| 2a | 0.3333 | 0.2000 | 0.2500 | 5 |
| 2b | 0.6667 | 0.6957 | 0.6809 | 23 |
| 2c | 1.0000 | 0.2500 | 0.4000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.2500 | 0.5000 | 0.3333 | 10 |
| 3b | 0.4444 | 0.8333 | 0.5797 | 24 |
| 3c | 0.4444 | 0.2500 | 0.3200 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.7500 |
| text012 | 33 | 0.9091 | 0.6364 |
| text013 | 25 | 0.9600 | 0.4800 |
| text014 | 23 | 0.8261 | 0.5217 |
| text015 | 29 | 0.7931 | 0.5172 |
| text016 | 31 | 0.7097 | 0.5161 |
| text017 | 18 | 0.7778 | 0.6667 |
| text018 | 34 | 0.8529 | 0.6471 |
| text019 | 26 | 0.8462 | 0.8462 |
| text020 | 32 | 0.8750 | 0.5000 |
