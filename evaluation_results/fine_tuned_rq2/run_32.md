# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 32  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.7903 (79.03%)  

**Weighted Precision:** 0.7949  
**Weighted Recall:** 0.7903  
**Weighted F1:** 0.7897  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8810 | 0.8362 | 0.8580 | 177 |
| 2 | 0.5588 | 0.4872 | 0.5205 | 39 |
| 3 | 0.6769 | 0.8627 | 0.7586 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5768 (57.68%)  

**Weighted Precision:** 0.6106  
**Weighted Recall:** 0.5768  
**Weighted F1:** 0.5766  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.8333 | 0.4762 | 0.6061 | 21 |
| 1b | 0.7500 | 0.4000 | 0.5217 | 45 |
| 1c | 0.6818 | 0.8108 | 0.7407 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.6000 | 0.5217 | 0.5581 | 23 |
| 2c | 0.1667 | 0.2500 | 0.2000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1154 | 0.3000 | 0.1667 | 10 |
| 3b | 0.5417 | 0.5417 | 0.5417 | 24 |
| 3c | 0.4667 | 0.4375 | 0.4516 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.6250 |
| text012 | 33 | 0.8788 | 0.6667 |
| text013 | 25 | 1.0000 | 0.6800 |
| text014 | 23 | 0.8261 | 0.5652 |
| text015 | 29 | 0.6897 | 0.4483 |
| text016 | 31 | 0.7419 | 0.5806 |
| text017 | 18 | 0.7222 | 0.5000 |
| text018 | 34 | 0.7647 | 0.7059 |
| text019 | 26 | 0.6538 | 0.3846 |
| text020 | 32 | 0.7812 | 0.5625 |
