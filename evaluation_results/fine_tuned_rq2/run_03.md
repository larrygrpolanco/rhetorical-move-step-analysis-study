# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 3  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8539 (85.39%)  

**Weighted Precision:** 0.8503  
**Weighted Recall:** 0.8539  
**Weighted F1:** 0.8492  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9306 | 0.9096 | 0.9200 | 177 |
| 2 | 0.5806 | 0.4615 | 0.5143 | 39 |
| 3 | 0.7778 | 0.9608 | 0.8596 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5618 (56.18%)  

**Weighted Precision:** 0.5441  
**Weighted Recall:** 0.5618  
**Weighted F1:** 0.5365  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.5882 | 0.4762 | 0.5263 | 21 |
| 1b | 0.6190 | 0.2889 | 0.3939 | 45 |
| 1c | 0.6963 | 0.8468 | 0.7642 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5217 | 0.5217 | 0.5217 | 23 |
| 2c | 0.1250 | 0.2500 | 0.1667 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.3077 | 0.4000 | 0.3478 | 10 |
| 3b | 0.3421 | 0.5417 | 0.4194 | 24 |
| 3c | 0.2500 | 0.1875 | 0.2143 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.6875 |
| text012 | 33 | 0.9697 | 0.6667 |
| text013 | 25 | 1.0000 | 0.4800 |
| text014 | 23 | 0.8696 | 0.6087 |
| text015 | 29 | 0.8276 | 0.4138 |
| text016 | 31 | 0.8065 | 0.5806 |
| text017 | 18 | 0.7222 | 0.6111 |
| text018 | 34 | 0.7353 | 0.5588 |
| text019 | 26 | 0.9615 | 0.7308 |
| text020 | 32 | 0.7812 | 0.3750 |
