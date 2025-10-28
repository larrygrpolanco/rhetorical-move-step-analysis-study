# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 64  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8652 (86.52%)  

**Weighted Precision:** 0.8662  
**Weighted Recall:** 0.8652  
**Weighted F1:** 0.8612  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9298 | 0.8983 | 0.9138 | 177 |
| 2 | 0.7000 | 0.5385 | 0.6087 | 39 |
| 3 | 0.7727 | 1.0000 | 0.8718 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5918 (59.18%)  

**Weighted Precision:** 0.5874  
**Weighted Recall:** 0.5918  
**Weighted F1:** 0.5613  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.6923 | 0.4286 | 0.5294 | 21 |
| 1b | 0.6500 | 0.2889 | 0.4000 | 45 |
| 1c | 0.7174 | 0.8919 | 0.7952 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5500 | 0.4783 | 0.5116 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.2857 | 0.4000 | 0.3333 | 10 |
| 3b | 0.4130 | 0.7917 | 0.5429 | 24 |
| 3c | 0.5000 | 0.1875 | 0.2727 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.6875 |
| text012 | 33 | 0.9697 | 0.6667 |
| text013 | 25 | 1.0000 | 0.5200 |
| text014 | 23 | 0.8696 | 0.6522 |
| text015 | 29 | 0.7931 | 0.5517 |
| text016 | 31 | 0.9032 | 0.6774 |
| text017 | 18 | 0.7222 | 0.5000 |
| text018 | 34 | 0.8235 | 0.6176 |
| text019 | 26 | 0.9231 | 0.7692 |
| text020 | 32 | 0.7500 | 0.3125 |
