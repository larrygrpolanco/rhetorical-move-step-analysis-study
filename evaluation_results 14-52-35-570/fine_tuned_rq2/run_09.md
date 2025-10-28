# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 9  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8315 (83.15%)  

**Weighted Precision:** 0.8265  
**Weighted Recall:** 0.8315  
**Weighted F1:** 0.8217  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8785 | 0.8983 | 0.8883 | 177 |
| 2 | 0.6957 | 0.4103 | 0.5161 | 39 |
| 3 | 0.7460 | 0.9216 | 0.8246 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5768 (57.68%)  

**Weighted Precision:** 0.5786  
**Weighted Recall:** 0.5768  
**Weighted F1:** 0.5533  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.6667 | 0.4762 | 0.5556 | 21 |
| 1b | 0.6818 | 0.3333 | 0.4478 | 45 |
| 1c | 0.6667 | 0.8649 | 0.7529 | 111 |
| 2a | 1.0000 | 0.2000 | 0.3333 | 5 |
| 2b | 0.6000 | 0.5217 | 0.5581 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.0952 | 0.2000 | 0.1290 | 10 |
| 3b | 0.4688 | 0.6250 | 0.5357 | 24 |
| 3c | 0.3000 | 0.1875 | 0.2308 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.6875 |
| text012 | 33 | 0.9394 | 0.6364 |
| text013 | 25 | 1.0000 | 0.4400 |
| text014 | 23 | 0.7391 | 0.5652 |
| text015 | 29 | 0.6897 | 0.4483 |
| text016 | 31 | 0.9355 | 0.7419 |
| text017 | 18 | 0.6667 | 0.5556 |
| text018 | 34 | 0.7647 | 0.6471 |
| text019 | 26 | 0.8077 | 0.6154 |
| text020 | 32 | 0.8125 | 0.4375 |
