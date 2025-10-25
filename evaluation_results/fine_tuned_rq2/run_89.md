# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 89  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8427 (84.27%)  

**Weighted Precision:** 0.8492  
**Weighted Recall:** 0.8427  
**Weighted F1:** 0.8365  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9128 | 0.8870 | 0.8997 | 177 |
| 2 | 0.7500 | 0.4615 | 0.5714 | 39 |
| 3 | 0.7042 | 0.9804 | 0.8197 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5955 (59.55%)  

**Weighted Precision:** 0.5967  
**Weighted Recall:** 0.5955  
**Weighted F1:** 0.5759  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.5882 | 0.4762 | 0.5263 | 21 |
| 1b | 0.6522 | 0.3333 | 0.4412 | 45 |
| 1c | 0.7197 | 0.8559 | 0.7819 | 111 |
| 2a | 0.5000 | 0.2000 | 0.2857 | 5 |
| 2b | 0.6111 | 0.4783 | 0.5366 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1765 | 0.3000 | 0.2222 | 10 |
| 3b | 0.4091 | 0.7500 | 0.5294 | 24 |
| 3c | 0.6000 | 0.3750 | 0.4615 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.6250 |
| text012 | 33 | 0.9697 | 0.6364 |
| text013 | 25 | 0.9600 | 0.4800 |
| text014 | 23 | 0.8261 | 0.6522 |
| text015 | 29 | 0.7586 | 0.4483 |
| text016 | 31 | 0.9355 | 0.7419 |
| text017 | 18 | 0.6667 | 0.5000 |
| text018 | 34 | 0.7941 | 0.7059 |
| text019 | 26 | 0.8077 | 0.6923 |
| text020 | 32 | 0.7500 | 0.4375 |
