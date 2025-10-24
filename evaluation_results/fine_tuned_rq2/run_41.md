# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 41  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8464 (84.64%)  

**Weighted Precision:** 0.8450  
**Weighted Recall:** 0.8464  
**Weighted F1:** 0.8429  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9128 | 0.8870 | 0.8997 | 177 |
| 2 | 0.6250 | 0.5128 | 0.5634 | 39 |
| 3 | 0.7778 | 0.9608 | 0.8596 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5918 (59.18%)  

**Weighted Precision:** 0.5975  
**Weighted Recall:** 0.5918  
**Weighted F1:** 0.5712  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.6429 | 0.4286 | 0.5143 | 21 |
| 1b | 0.6500 | 0.2889 | 0.4000 | 45 |
| 1c | 0.7101 | 0.8829 | 0.7871 | 111 |
| 2a | 1.0000 | 0.2000 | 0.3333 | 5 |
| 2b | 0.5217 | 0.5217 | 0.5217 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1765 | 0.3000 | 0.2222 | 10 |
| 3b | 0.4667 | 0.5833 | 0.5185 | 24 |
| 3c | 0.5000 | 0.5000 | 0.5000 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.6875 |
| text012 | 33 | 0.9394 | 0.6667 |
| text013 | 25 | 0.9200 | 0.6000 |
| text014 | 23 | 0.8261 | 0.5217 |
| text015 | 29 | 0.7931 | 0.3793 |
| text016 | 31 | 0.8387 | 0.5806 |
| text017 | 18 | 0.6667 | 0.5556 |
| text018 | 34 | 0.7941 | 0.6765 |
| text019 | 26 | 0.8846 | 0.7692 |
| text020 | 32 | 0.8438 | 0.5000 |
