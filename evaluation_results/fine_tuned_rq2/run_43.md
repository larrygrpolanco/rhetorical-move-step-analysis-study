# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 43  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8352 (83.52%)  

**Weighted Precision:** 0.8317  
**Weighted Recall:** 0.8352  
**Weighted F1:** 0.8286  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8883 | 0.8983 | 0.8933 | 177 |
| 2 | 0.6923 | 0.4615 | 0.5538 | 39 |
| 3 | 0.7419 | 0.9020 | 0.8142 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5768 (57.68%)  

**Weighted Precision:** 0.5679  
**Weighted Recall:** 0.5768  
**Weighted F1:** 0.5448  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.7692 | 0.4762 | 0.5882 | 21 |
| 1b | 0.7059 | 0.2667 | 0.3871 | 45 |
| 1c | 0.6443 | 0.8649 | 0.7385 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.6667 | 0.6957 | 0.6809 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1111 | 0.2000 | 0.1429 | 10 |
| 3b | 0.4516 | 0.5833 | 0.5091 | 24 |
| 3c | 0.3077 | 0.2500 | 0.2759 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.7500 |
| text012 | 33 | 0.8788 | 0.6364 |
| text013 | 25 | 0.9600 | 0.6000 |
| text014 | 23 | 0.7391 | 0.5652 |
| text015 | 29 | 0.7586 | 0.4483 |
| text016 | 31 | 0.9032 | 0.6774 |
| text017 | 18 | 0.7222 | 0.5000 |
| text018 | 34 | 0.7059 | 0.5294 |
| text019 | 26 | 0.9231 | 0.6538 |
| text020 | 32 | 0.8750 | 0.4688 |
