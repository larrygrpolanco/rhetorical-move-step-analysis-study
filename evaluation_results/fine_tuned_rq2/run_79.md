# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 79  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8577 (85.77%)  

**Weighted Precision:** 0.8575  
**Weighted Recall:** 0.8577  
**Weighted F1:** 0.8553  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9091 | 0.9040 | 0.9065 | 177 |
| 2 | 0.7419 | 0.5897 | 0.6571 | 39 |
| 3 | 0.7667 | 0.9020 | 0.8288 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5805 (58.05%)  

**Weighted Precision:** 0.5601  
**Weighted Recall:** 0.5805  
**Weighted F1:** 0.5528  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.6667 | 0.4762 | 0.5556 | 21 |
| 1b | 0.6957 | 0.3556 | 0.4706 | 45 |
| 1c | 0.6957 | 0.8649 | 0.7711 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.4815 | 0.5652 | 0.5200 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.2222 | 0.4000 | 0.2857 | 10 |
| 3b | 0.4242 | 0.5833 | 0.4912 | 24 |
| 3c | 0.2222 | 0.1250 | 0.1600 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.7500 |
| text012 | 33 | 0.9091 | 0.6364 |
| text013 | 25 | 1.0000 | 0.5200 |
| text014 | 23 | 0.8261 | 0.5217 |
| text015 | 29 | 0.6897 | 0.4483 |
| text016 | 31 | 0.8387 | 0.6129 |
| text017 | 18 | 0.8889 | 0.6667 |
| text018 | 34 | 0.8235 | 0.7353 |
| text019 | 26 | 0.9231 | 0.6923 |
| text020 | 32 | 0.8125 | 0.3125 |
