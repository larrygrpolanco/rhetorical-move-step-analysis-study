# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 42  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8539 (85.39%)  

**Weighted Precision:** 0.8567  
**Weighted Recall:** 0.8539  
**Weighted F1:** 0.8511  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9176 | 0.8814 | 0.8991 | 177 |
| 2 | 0.7097 | 0.5641 | 0.6286 | 39 |
| 3 | 0.7576 | 0.9804 | 0.8547 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5169 (51.69%)  

**Weighted Precision:** 0.5160  
**Weighted Recall:** 0.5169  
**Weighted F1:** 0.5122  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.5000 | 0.4286 | 0.4615 | 21 |
| 1b | 0.4375 | 0.3111 | 0.3636 | 45 |
| 1c | 0.6917 | 0.7477 | 0.7186 | 111 |
| 2a | 0.2500 | 0.2000 | 0.2222 | 5 |
| 2b | 0.6500 | 0.5652 | 0.6047 | 23 |
| 2c | 0.2000 | 0.2500 | 0.2222 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1000 | 0.2000 | 0.1333 | 10 |
| 3b | 0.3438 | 0.4583 | 0.3929 | 24 |
| 3c | 0.2857 | 0.2500 | 0.2667 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.7500 |
| text012 | 33 | 0.9697 | 0.6364 |
| text013 | 25 | 1.0000 | 0.4400 |
| text014 | 23 | 0.7826 | 0.4783 |
| text015 | 29 | 0.8621 | 0.4828 |
| text016 | 31 | 0.8387 | 0.5161 |
| text017 | 18 | 0.8333 | 0.5556 |
| text018 | 34 | 0.7941 | 0.4706 |
| text019 | 26 | 0.8462 | 0.5385 |
| text020 | 32 | 0.7188 | 0.4062 |
