# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 60  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8427 (84.27%)  

**Weighted Precision:** 0.8440  
**Weighted Recall:** 0.8427  
**Weighted F1:** 0.8395  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9172 | 0.8757 | 0.8960 | 177 |
| 2 | 0.6250 | 0.5128 | 0.5634 | 39 |
| 3 | 0.7576 | 0.9804 | 0.8547 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.6030 (60.30%)  

**Weighted Precision:** 0.6073  
**Weighted Recall:** 0.6030  
**Weighted F1:** 0.5836  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.7857 | 0.5238 | 0.6286 | 21 |
| 1b | 0.6667 | 0.4000 | 0.5000 | 45 |
| 1c | 0.7109 | 0.8198 | 0.7615 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5652 | 0.5652 | 0.5652 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.3000 | 0.6000 | 0.4000 | 10 |
| 3b | 0.4634 | 0.7917 | 0.5846 | 24 |
| 3c | 0.6000 | 0.1875 | 0.2857 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.6250 |
| text012 | 33 | 0.9697 | 0.6667 |
| text013 | 25 | 0.9600 | 0.4400 |
| text014 | 23 | 0.8261 | 0.6522 |
| text015 | 29 | 0.7931 | 0.3793 |
| text016 | 31 | 0.8710 | 0.6452 |
| text017 | 18 | 0.6667 | 0.6111 |
| text018 | 34 | 0.7647 | 0.7059 |
| text019 | 26 | 0.8462 | 0.7308 |
| text020 | 32 | 0.8125 | 0.5625 |
