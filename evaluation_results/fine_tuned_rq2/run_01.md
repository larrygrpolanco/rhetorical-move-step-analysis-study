# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 1  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8464 (84.64%)  

**Weighted Precision:** 0.8482  
**Weighted Recall:** 0.8464  
**Weighted F1:** 0.8415  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9181 | 0.8870 | 0.9023 | 177 |
| 2 | 0.6786 | 0.4872 | 0.5672 | 39 |
| 3 | 0.7353 | 0.9804 | 0.8403 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5693 (56.93%)  

**Weighted Precision:** 0.5566  
**Weighted Recall:** 0.5693  
**Weighted F1:** 0.5510  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.6000 | 0.4286 | 0.5000 | 21 |
| 1b | 0.6552 | 0.4222 | 0.5135 | 45 |
| 1c | 0.7323 | 0.8378 | 0.7815 | 111 |
| 2a | 0.2000 | 0.2000 | 0.2000 | 5 |
| 2b | 0.6316 | 0.5217 | 0.5714 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1000 | 0.2000 | 0.1333 | 10 |
| 3b | 0.3636 | 0.6667 | 0.4706 | 24 |
| 3c | 0.0000 | 0.0000 | 0.0000 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.7500 |
| text012 | 33 | 0.9394 | 0.6364 |
| text013 | 25 | 1.0000 | 0.4800 |
| text014 | 23 | 0.7826 | 0.5652 |
| text015 | 29 | 0.8276 | 0.5862 |
| text016 | 31 | 0.8065 | 0.6452 |
| text017 | 18 | 0.8333 | 0.5000 |
| text018 | 34 | 0.7941 | 0.7059 |
| text019 | 26 | 0.8077 | 0.5769 |
| text020 | 32 | 0.7812 | 0.2812 |
