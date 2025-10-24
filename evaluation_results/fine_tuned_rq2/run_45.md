# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 45  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8352 (83.52%)  

**Weighted Precision:** 0.8331  
**Weighted Recall:** 0.8352  
**Weighted F1:** 0.8325  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9023 | 0.8870 | 0.8946 | 177 |
| 2 | 0.6061 | 0.5128 | 0.5556 | 39 |
| 3 | 0.7667 | 0.9020 | 0.8288 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5880 (58.80%)  

**Weighted Precision:** 0.5730  
**Weighted Recall:** 0.5880  
**Weighted F1:** 0.5673  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.5625 | 0.4286 | 0.4865 | 21 |
| 1b | 0.5833 | 0.3111 | 0.4058 | 45 |
| 1c | 0.6940 | 0.8378 | 0.7592 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.4828 | 0.6087 | 0.5385 | 23 |
| 2c | 0.5000 | 0.2500 | 0.3333 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1500 | 0.3000 | 0.2000 | 10 |
| 3b | 0.6190 | 0.5417 | 0.5778 | 24 |
| 3c | 0.5263 | 0.6250 | 0.5714 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.6875 |
| text012 | 33 | 0.9697 | 0.6364 |
| text013 | 25 | 0.9200 | 0.6000 |
| text014 | 23 | 0.8261 | 0.5652 |
| text015 | 29 | 0.7241 | 0.4138 |
| text016 | 31 | 0.8387 | 0.6129 |
| text017 | 18 | 0.7778 | 0.7222 |
| text018 | 34 | 0.8235 | 0.7353 |
| text019 | 26 | 0.8462 | 0.5000 |
| text020 | 32 | 0.7500 | 0.4688 |
