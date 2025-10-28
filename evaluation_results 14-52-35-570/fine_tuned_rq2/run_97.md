# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 97  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.7828 (78.28%)  

**Weighted Precision:** 0.7998  
**Weighted Recall:** 0.7828  
**Weighted F1:** 0.7838  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9057 | 0.8136 | 0.8571 | 177 |
| 2 | 0.5455 | 0.4615 | 0.5000 | 39 |
| 3 | 0.6267 | 0.9216 | 0.7460 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5131 (51.31%)  

**Weighted Precision:** 0.5087  
**Weighted Recall:** 0.5131  
**Weighted F1:** 0.5033  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.6111 | 0.5238 | 0.5641 | 21 |
| 1b | 0.4848 | 0.3556 | 0.4103 | 45 |
| 1c | 0.6667 | 0.6486 | 0.6575 | 111 |
| 2a | 0.3333 | 0.4000 | 0.3636 | 5 |
| 2b | 0.4800 | 0.5217 | 0.5000 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1304 | 0.3000 | 0.1818 | 10 |
| 3b | 0.4878 | 0.8333 | 0.6154 | 24 |
| 3c | 0.0909 | 0.0625 | 0.0741 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.6875 |
| text012 | 33 | 0.9091 | 0.6364 |
| text013 | 25 | 0.9600 | 0.4800 |
| text014 | 23 | 0.7391 | 0.5652 |
| text015 | 29 | 0.7586 | 0.4828 |
| text016 | 31 | 0.5806 | 0.3548 |
| text017 | 18 | 0.7778 | 0.6111 |
| text018 | 34 | 0.7059 | 0.5000 |
| text019 | 26 | 0.8077 | 0.5000 |
| text020 | 32 | 0.7500 | 0.4375 |
