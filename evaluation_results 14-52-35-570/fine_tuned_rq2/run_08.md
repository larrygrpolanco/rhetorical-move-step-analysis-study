# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 8  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.7753 (77.53%)  

**Weighted Precision:** 0.7872  
**Weighted Recall:** 0.7753  
**Weighted F1:** 0.7766  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8882 | 0.8079 | 0.8462 | 177 |
| 2 | 0.4865 | 0.4615 | 0.4737 | 39 |
| 3 | 0.6667 | 0.9020 | 0.7667 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5468 (54.68%)  

**Weighted Precision:** 0.5898  
**Weighted Recall:** 0.5468  
**Weighted F1:** 0.5400  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.7500 | 0.5714 | 0.6486 | 21 |
| 1b | 0.8125 | 0.2889 | 0.4262 | 45 |
| 1c | 0.6434 | 0.7477 | 0.6917 | 111 |
| 2a | 0.5000 | 0.2000 | 0.2857 | 5 |
| 2b | 0.4167 | 0.4348 | 0.4255 | 23 |
| 2c | 0.1667 | 0.2500 | 0.2000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1667 | 0.3000 | 0.2143 | 10 |
| 3b | 0.3947 | 0.6250 | 0.4839 | 24 |
| 3c | 0.6154 | 0.5000 | 0.5517 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.6875 |
| text012 | 33 | 0.9394 | 0.6970 |
| text013 | 25 | 1.0000 | 0.6000 |
| text014 | 23 | 0.5652 | 0.2609 |
| text015 | 29 | 0.6897 | 0.4138 |
| text016 | 31 | 0.6452 | 0.5161 |
| text017 | 18 | 0.7222 | 0.5556 |
| text018 | 34 | 0.7353 | 0.6471 |
| text019 | 26 | 0.8462 | 0.5769 |
| text020 | 32 | 0.7188 | 0.5000 |
