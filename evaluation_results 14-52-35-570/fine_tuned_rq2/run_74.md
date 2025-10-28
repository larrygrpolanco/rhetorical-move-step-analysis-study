# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 74  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8427 (84.27%)  

**Weighted Precision:** 0.8389  
**Weighted Recall:** 0.8427  
**Weighted F1:** 0.8385  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8989 | 0.9040 | 0.9014 | 177 |
| 2 | 0.6667 | 0.5128 | 0.5797 | 39 |
| 3 | 0.7627 | 0.8824 | 0.8182 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5768 (57.68%)  

**Weighted Precision:** 0.5443  
**Weighted Recall:** 0.5768  
**Weighted F1:** 0.5401  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.8333 | 0.4762 | 0.6061 | 21 |
| 1b | 0.6087 | 0.3111 | 0.4118 | 45 |
| 1c | 0.6783 | 0.8739 | 0.7638 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5217 | 0.5217 | 0.5217 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1765 | 0.3000 | 0.2222 | 10 |
| 3b | 0.4737 | 0.7500 | 0.5806 | 24 |
| 3c | 0.0000 | 0.0000 | 0.0000 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.6250 |
| text012 | 33 | 0.9091 | 0.6364 |
| text013 | 25 | 1.0000 | 0.4400 |
| text014 | 23 | 0.7826 | 0.5217 |
| text015 | 29 | 0.6897 | 0.5172 |
| text016 | 31 | 0.9032 | 0.6774 |
| text017 | 18 | 0.8333 | 0.6667 |
| text018 | 34 | 0.7647 | 0.5588 |
| text019 | 26 | 0.9231 | 0.6923 |
| text020 | 32 | 0.7812 | 0.4688 |
