# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 5  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8652 (86.52%)  

**Weighted Precision:** 0.8586  
**Weighted Recall:** 0.8652  
**Weighted F1:** 0.8590  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8967 | 0.9322 | 0.9141 | 177 |
| 2 | 0.7143 | 0.5128 | 0.5970 | 39 |
| 3 | 0.8364 | 0.9020 | 0.8679 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.6217 (62.17%)  

**Weighted Precision:** 0.6113  
**Weighted Recall:** 0.6217  
**Weighted F1:** 0.5967  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.7692 | 0.4762 | 0.5882 | 21 |
| 1b | 0.7200 | 0.4000 | 0.5143 | 45 |
| 1c | 0.6918 | 0.9099 | 0.7860 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5909 | 0.5652 | 0.5778 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.2941 | 0.5000 | 0.3704 | 10 |
| 3b | 0.5185 | 0.5833 | 0.5490 | 24 |
| 3c | 0.5556 | 0.3125 | 0.4000 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.6875 |
| text012 | 33 | 0.9394 | 0.6364 |
| text013 | 25 | 1.0000 | 0.5600 |
| text014 | 23 | 0.8696 | 0.5652 |
| text015 | 29 | 0.6897 | 0.4828 |
| text016 | 31 | 0.9677 | 0.7419 |
| text017 | 18 | 0.7778 | 0.5556 |
| text018 | 34 | 0.8235 | 0.7353 |
| text019 | 26 | 0.9231 | 0.6923 |
| text020 | 32 | 0.7812 | 0.5312 |
