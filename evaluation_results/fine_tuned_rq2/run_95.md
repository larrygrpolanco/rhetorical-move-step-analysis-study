# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 95  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8352 (83.52%)  

**Weighted Precision:** 0.8431  
**Weighted Recall:** 0.8352  
**Weighted F1:** 0.8369  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9212 | 0.8588 | 0.8889 | 177 |
| 2 | 0.6000 | 0.6154 | 0.6076 | 39 |
| 3 | 0.7581 | 0.9216 | 0.8319 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5805 (58.05%)  

**Weighted Precision:** 0.5651  
**Weighted Recall:** 0.5805  
**Weighted F1:** 0.5581  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.6250 | 0.4762 | 0.5405 | 21 |
| 1b | 0.5455 | 0.2667 | 0.3582 | 45 |
| 1c | 0.7165 | 0.8198 | 0.7647 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.6087 | 0.6087 | 0.6087 | 23 |
| 2c | 0.1818 | 0.5000 | 0.2667 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.4375 | 0.7000 | 0.5385 | 10 |
| 3b | 0.4857 | 0.7083 | 0.5763 | 24 |
| 3c | 0.1818 | 0.1250 | 0.1481 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.7500 |
| text012 | 33 | 0.9697 | 0.7273 |
| text013 | 25 | 0.9600 | 0.5200 |
| text014 | 23 | 0.7391 | 0.5217 |
| text015 | 29 | 0.7241 | 0.4138 |
| text016 | 31 | 0.9677 | 0.7419 |
| text017 | 18 | 0.7222 | 0.5556 |
| text018 | 34 | 0.7647 | 0.6471 |
| text019 | 26 | 0.8077 | 0.6154 |
| text020 | 32 | 0.7500 | 0.3438 |
