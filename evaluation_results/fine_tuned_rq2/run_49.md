# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 49  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8464 (84.64%)  

**Weighted Precision:** 0.8473  
**Weighted Recall:** 0.8464  
**Weighted F1:** 0.8441  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9186 | 0.8927 | 0.9054 | 177 |
| 2 | 0.6562 | 0.5385 | 0.5915 | 39 |
| 3 | 0.7460 | 0.9216 | 0.8246 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5955 (59.55%)  

**Weighted Precision:** 0.5918  
**Weighted Recall:** 0.5955  
**Weighted F1:** 0.5787  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.4737 | 0.4286 | 0.4500 | 21 |
| 1b | 0.6522 | 0.3333 | 0.4412 | 45 |
| 1c | 0.7154 | 0.8378 | 0.7718 | 111 |
| 2a | 0.5000 | 0.2000 | 0.2857 | 5 |
| 2b | 0.5000 | 0.4783 | 0.4889 | 23 |
| 2c | 0.2857 | 0.5000 | 0.3636 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.2105 | 0.4000 | 0.2759 | 10 |
| 3b | 0.5714 | 0.5000 | 0.5333 | 24 |
| 3c | 0.5217 | 0.7500 | 0.6154 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8125 | 0.7500 |
| text012 | 33 | 0.9697 | 0.6667 |
| text013 | 25 | 0.8800 | 0.6000 |
| text014 | 23 | 0.8261 | 0.6522 |
| text015 | 29 | 0.8276 | 0.4483 |
| text016 | 31 | 0.9032 | 0.6774 |
| text017 | 18 | 0.7778 | 0.7222 |
| text018 | 34 | 0.7647 | 0.5882 |
| text019 | 26 | 0.8846 | 0.7692 |
| text020 | 32 | 0.7812 | 0.2500 |
