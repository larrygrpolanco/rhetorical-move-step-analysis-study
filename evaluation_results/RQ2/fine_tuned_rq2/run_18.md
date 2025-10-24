# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 18  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8764 (87.64%)  

**Weighted Precision:** 0.8743  
**Weighted Recall:** 0.8764  
**Weighted F1:** 0.8735  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9106 | 0.9209 | 0.9157 | 177 |
| 2 | 0.7742 | 0.6154 | 0.6857 | 39 |
| 3 | 0.8246 | 0.9216 | 0.8704 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5918 (59.18%)  

**Weighted Precision:** 0.5697  
**Weighted Recall:** 0.5918  
**Weighted F1:** 0.5708  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.5714 | 0.5714 | 0.5714 | 21 |
| 1b | 0.5862 | 0.3778 | 0.4595 | 45 |
| 1c | 0.6899 | 0.8018 | 0.7417 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5769 | 0.6522 | 0.6122 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.3000 | 0.6000 | 0.4000 | 10 |
| 3b | 0.5000 | 0.5833 | 0.5385 | 24 |
| 3c | 0.5556 | 0.3125 | 0.4000 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.6875 |
| text012 | 33 | 0.9697 | 0.6667 |
| text013 | 25 | 1.0000 | 0.6400 |
| text014 | 23 | 0.7391 | 0.5217 |
| text015 | 29 | 0.7586 | 0.4828 |
| text016 | 31 | 0.9677 | 0.7097 |
| text017 | 18 | 0.8333 | 0.6111 |
| text018 | 34 | 0.8529 | 0.6765 |
| text019 | 26 | 0.9615 | 0.5769 |
| text020 | 32 | 0.7812 | 0.3750 |
