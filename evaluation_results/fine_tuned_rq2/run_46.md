# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 46  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8464 (84.64%)  

**Weighted Precision:** 0.8601  
**Weighted Recall:** 0.8464  
**Weighted F1:** 0.8455  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9231 | 0.8814 | 0.9017 | 177 |
| 2 | 0.8148 | 0.5641 | 0.6667 | 39 |
| 3 | 0.6761 | 0.9412 | 0.7869 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5993 (59.93%)  

**Weighted Precision:** 0.6051  
**Weighted Recall:** 0.5993  
**Weighted F1:** 0.5912  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.6250 | 0.4762 | 0.5405 | 21 |
| 1b | 0.6538 | 0.3778 | 0.4789 | 45 |
| 1c | 0.7402 | 0.8468 | 0.7899 | 111 |
| 2a | 0.3333 | 0.2000 | 0.2500 | 5 |
| 2b | 0.5909 | 0.5652 | 0.5778 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1071 | 0.3000 | 0.1579 | 10 |
| 3b | 0.5217 | 0.5000 | 0.5106 | 24 |
| 3c | 0.5000 | 0.6250 | 0.5556 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.6250 |
| text012 | 33 | 0.9394 | 0.5758 |
| text013 | 25 | 1.0000 | 0.6400 |
| text014 | 23 | 0.8261 | 0.5217 |
| text015 | 29 | 0.8966 | 0.4483 |
| text016 | 31 | 0.9032 | 0.7097 |
| text017 | 18 | 0.7222 | 0.6111 |
| text018 | 34 | 0.7941 | 0.7353 |
| text019 | 26 | 0.6538 | 0.5000 |
| text020 | 32 | 0.7812 | 0.5938 |
