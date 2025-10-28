# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 67  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8577 (85.77%)  

**Weighted Precision:** 0.8518  
**Weighted Recall:** 0.8577  
**Weighted F1:** 0.8504  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8913 | 0.9266 | 0.9086 | 177 |
| 2 | 0.7308 | 0.4872 | 0.5846 | 39 |
| 3 | 0.8070 | 0.9020 | 0.8519 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5918 (59.18%)  

**Weighted Precision:** 0.5828  
**Weighted Recall:** 0.5918  
**Weighted F1:** 0.5652  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.7143 | 0.4762 | 0.5714 | 21 |
| 1b | 0.5385 | 0.3111 | 0.3944 | 45 |
| 1c | 0.6806 | 0.8829 | 0.7686 | 111 |
| 2a | 1.0000 | 0.2000 | 0.3333 | 5 |
| 2b | 0.5455 | 0.5217 | 0.5333 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1667 | 0.3000 | 0.2143 | 10 |
| 3b | 0.4839 | 0.6250 | 0.5455 | 24 |
| 3c | 0.6250 | 0.3125 | 0.4167 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.5625 |
| text012 | 33 | 0.9697 | 0.6061 |
| text013 | 25 | 0.9600 | 0.5200 |
| text014 | 23 | 0.7826 | 0.6087 |
| text015 | 29 | 0.7241 | 0.4828 |
| text016 | 31 | 0.9355 | 0.6774 |
| text017 | 18 | 0.7222 | 0.6111 |
| text018 | 34 | 0.7941 | 0.6471 |
| text019 | 26 | 0.9231 | 0.6538 |
| text020 | 32 | 0.8125 | 0.5312 |
