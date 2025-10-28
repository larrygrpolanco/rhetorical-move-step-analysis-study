# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 30  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8614 (86.14%)  

**Weighted Precision:** 0.8556  
**Weighted Recall:** 0.8614  
**Weighted F1:** 0.8580  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9056 | 0.9209 | 0.9132 | 177 |
| 2 | 0.5882 | 0.5128 | 0.5479 | 39 |
| 3 | 0.8868 | 0.9216 | 0.9038 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5805 (58.05%)  

**Weighted Precision:** 0.5589  
**Weighted Recall:** 0.5805  
**Weighted F1:** 0.5584  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.7143 | 0.4762 | 0.5714 | 21 |
| 1b | 0.6071 | 0.3778 | 0.4658 | 45 |
| 1c | 0.7029 | 0.8739 | 0.7791 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5000 | 0.4783 | 0.4889 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.3636 | 0.4000 | 0.3810 | 10 |
| 3b | 0.4516 | 0.5833 | 0.5091 | 24 |
| 3c | 0.1818 | 0.1250 | 0.1481 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.6875 |
| text012 | 33 | 1.0000 | 0.6364 |
| text013 | 25 | 0.8000 | 0.4400 |
| text014 | 23 | 0.8261 | 0.6522 |
| text015 | 29 | 0.8621 | 0.4483 |
| text016 | 31 | 0.9355 | 0.6774 |
| text017 | 18 | 0.7778 | 0.4444 |
| text018 | 34 | 0.8529 | 0.7059 |
| text019 | 26 | 0.8846 | 0.7308 |
| text020 | 32 | 0.7500 | 0.3750 |
