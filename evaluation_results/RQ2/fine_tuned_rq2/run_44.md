# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 44  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8315 (83.15%)  

**Weighted Precision:** 0.8243  
**Weighted Recall:** 0.8315  
**Weighted F1:** 0.8236  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8785 | 0.8983 | 0.8883 | 177 |
| 2 | 0.6538 | 0.4359 | 0.5231 | 39 |
| 3 | 0.7667 | 0.9020 | 0.8288 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5993 (59.93%)  

**Weighted Precision:** 0.5956  
**Weighted Recall:** 0.5993  
**Weighted F1:** 0.5711  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.7692 | 0.4762 | 0.5882 | 21 |
| 1b | 0.6842 | 0.2889 | 0.4062 | 45 |
| 1c | 0.6510 | 0.8739 | 0.7462 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.6500 | 0.5652 | 0.6047 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.3158 | 0.6000 | 0.4138 | 10 |
| 3b | 0.6316 | 0.5000 | 0.5581 | 24 |
| 3c | 0.4091 | 0.5625 | 0.4737 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.6875 |
| text012 | 33 | 0.9091 | 0.7273 |
| text013 | 25 | 1.0000 | 0.6800 |
| text014 | 23 | 0.7826 | 0.6522 |
| text015 | 29 | 0.6897 | 0.3448 |
| text016 | 31 | 0.8710 | 0.6452 |
| text017 | 18 | 0.7222 | 0.5556 |
| text018 | 34 | 0.7941 | 0.5882 |
| text019 | 26 | 0.8846 | 0.6538 |
| text020 | 32 | 0.7812 | 0.5000 |
