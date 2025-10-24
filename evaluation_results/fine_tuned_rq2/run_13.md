# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 13  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8577 (85.77%)  

**Weighted Precision:** 0.8608  
**Weighted Recall:** 0.8577  
**Weighted F1:** 0.8561  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9240 | 0.8927 | 0.9080 | 177 |
| 2 | 0.7188 | 0.5897 | 0.6479 | 39 |
| 3 | 0.7500 | 0.9412 | 0.8348 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5918 (59.18%)  

**Weighted Precision:** 0.5985  
**Weighted Recall:** 0.5918  
**Weighted F1:** 0.5644  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.4762 | 0.4762 | 0.4762 | 21 |
| 1b | 0.6667 | 0.2222 | 0.3333 | 45 |
| 1c | 0.7037 | 0.8559 | 0.7724 | 111 |
| 2a | 0.3333 | 0.2000 | 0.2500 | 5 |
| 2b | 0.6087 | 0.6087 | 0.6087 | 23 |
| 2c | 0.1667 | 0.2500 | 0.2000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.2273 | 0.5000 | 0.3125 | 10 |
| 3b | 0.4857 | 0.7083 | 0.5763 | 24 |
| 3c | 0.7143 | 0.3125 | 0.4348 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.7500 |
| text012 | 33 | 0.9394 | 0.6364 |
| text013 | 25 | 0.9600 | 0.6400 |
| text014 | 23 | 0.8261 | 0.4783 |
| text015 | 29 | 0.8276 | 0.5517 |
| text016 | 31 | 0.9032 | 0.6774 |
| text017 | 18 | 0.7778 | 0.6667 |
| text018 | 34 | 0.8235 | 0.7353 |
| text019 | 26 | 0.8846 | 0.5385 |
| text020 | 32 | 0.7188 | 0.3125 |
