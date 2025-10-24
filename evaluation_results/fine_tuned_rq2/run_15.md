# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 15  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8502 (85.02%)  

**Weighted Precision:** 0.8475  
**Weighted Recall:** 0.8502  
**Weighted F1:** 0.8467  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8944 | 0.9096 | 0.9020 | 177 |
| 2 | 0.7333 | 0.5641 | 0.6377 | 39 |
| 3 | 0.7719 | 0.8627 | 0.8148 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.6030 (60.30%)  

**Weighted Precision:** 0.6243  
**Weighted Recall:** 0.6030  
**Weighted F1:** 0.5731  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.7692 | 0.4762 | 0.5882 | 21 |
| 1b | 0.7647 | 0.2889 | 0.4194 | 45 |
| 1c | 0.6733 | 0.9099 | 0.7739 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5600 | 0.6087 | 0.5833 | 23 |
| 2c | 0.5000 | 0.2500 | 0.3333 | 4 |
| 2d | 1.0000 | 0.1429 | 0.2500 | 7 |
| 3a | 0.1111 | 0.2000 | 0.1429 | 10 |
| 3b | 0.5161 | 0.6667 | 0.5818 | 24 |
| 3c | 0.3750 | 0.1875 | 0.2500 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.7500 |
| text012 | 33 | 0.9091 | 0.6364 |
| text013 | 25 | 1.0000 | 0.4400 |
| text014 | 23 | 0.8261 | 0.5652 |
| text015 | 29 | 0.6207 | 0.4138 |
| text016 | 31 | 0.9677 | 0.7419 |
| text017 | 18 | 0.7778 | 0.5000 |
| text018 | 34 | 0.7941 | 0.7353 |
| text019 | 26 | 1.0000 | 0.8077 |
| text020 | 32 | 0.7500 | 0.4375 |
