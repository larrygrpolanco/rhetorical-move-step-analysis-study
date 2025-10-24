# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 38  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8652 (86.52%)  

**Weighted Precision:** 0.8590  
**Weighted Recall:** 0.8652  
**Weighted F1:** 0.8585  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8871 | 0.9322 | 0.9091 | 177 |
| 2 | 0.7407 | 0.5128 | 0.6061 | 39 |
| 3 | 0.8519 | 0.9020 | 0.8762 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.6067 (60.67%)  

**Weighted Precision:** 0.5690  
**Weighted Recall:** 0.6067  
**Weighted F1:** 0.5678  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.7500 | 0.4286 | 0.5455 | 21 |
| 1b | 0.6429 | 0.4000 | 0.4932 | 45 |
| 1c | 0.6712 | 0.8829 | 0.7626 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5833 | 0.6087 | 0.5957 | 23 |
| 2c | 1.0000 | 0.2500 | 0.4000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.3333 | 0.6000 | 0.4286 | 10 |
| 3b | 0.5000 | 0.6667 | 0.5714 | 24 |
| 3c | 0.0000 | 0.0000 | 0.0000 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.7500 |
| text012 | 33 | 0.9091 | 0.6061 |
| text013 | 25 | 1.0000 | 0.4400 |
| text014 | 23 | 0.8696 | 0.6087 |
| text015 | 29 | 0.6897 | 0.4138 |
| text016 | 31 | 0.9032 | 0.6774 |
| text017 | 18 | 0.7778 | 0.6111 |
| text018 | 34 | 0.7941 | 0.7059 |
| text019 | 26 | 0.9615 | 0.7692 |
| text020 | 32 | 0.8750 | 0.5312 |
