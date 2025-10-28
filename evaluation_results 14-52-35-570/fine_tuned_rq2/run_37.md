# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 37  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8652 (86.52%)  

**Weighted Precision:** 0.8697  
**Weighted Recall:** 0.8652  
**Weighted F1:** 0.8625  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9353 | 0.8983 | 0.9164 | 177 |
| 2 | 0.7333 | 0.5641 | 0.6377 | 39 |
| 3 | 0.7463 | 0.9804 | 0.8475 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5693 (56.93%)  

**Weighted Precision:** 0.5662  
**Weighted Recall:** 0.5693  
**Weighted F1:** 0.5537  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.7333 | 0.5238 | 0.6111 | 21 |
| 1b | 0.5714 | 0.3556 | 0.4384 | 45 |
| 1c | 0.7165 | 0.8198 | 0.7647 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.4828 | 0.6087 | 0.5385 | 23 |
| 2c | 1.0000 | 0.2500 | 0.4000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1923 | 0.5000 | 0.2778 | 10 |
| 3b | 0.3571 | 0.4167 | 0.3846 | 24 |
| 3c | 0.3077 | 0.2500 | 0.2759 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.6250 |
| text012 | 33 | 0.9091 | 0.6364 |
| text013 | 25 | 1.0000 | 0.6000 |
| text014 | 23 | 0.7826 | 0.5217 |
| text015 | 29 | 0.7931 | 0.4138 |
| text016 | 31 | 0.9677 | 0.6774 |
| text017 | 18 | 0.8333 | 0.7222 |
| text018 | 34 | 0.7941 | 0.5000 |
| text019 | 26 | 0.9231 | 0.7308 |
| text020 | 32 | 0.7500 | 0.3750 |
