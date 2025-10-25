# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 27  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8427 (84.27%)  

**Weighted Precision:** 0.8407  
**Weighted Recall:** 0.8427  
**Weighted F1:** 0.8416  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9040 | 0.9040 | 0.9040 | 177 |
| 2 | 0.5676 | 0.5385 | 0.5526 | 39 |
| 3 | 0.8302 | 0.8627 | 0.8462 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5393 (53.93%)  

**Weighted Precision:** 0.5251  
**Weighted Recall:** 0.5393  
**Weighted F1:** 0.5289  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.5000 | 0.5714 | 0.5333 | 21 |
| 1b | 0.3871 | 0.2667 | 0.3158 | 45 |
| 1c | 0.6885 | 0.7568 | 0.7210 | 111 |
| 2a | 0.2000 | 0.2000 | 0.2000 | 5 |
| 2b | 0.5714 | 0.5217 | 0.5455 | 23 |
| 2c | 0.2000 | 0.2500 | 0.2222 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.3571 | 0.5000 | 0.4167 | 10 |
| 3b | 0.5000 | 0.5000 | 0.5000 | 24 |
| 3c | 0.3333 | 0.3125 | 0.3226 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.6250 |
| text012 | 33 | 0.9091 | 0.6061 |
| text013 | 25 | 1.0000 | 0.4800 |
| text014 | 23 | 0.7826 | 0.5217 |
| text015 | 29 | 0.6897 | 0.4483 |
| text016 | 31 | 0.7742 | 0.3226 |
| text017 | 18 | 0.8333 | 0.5000 |
| text018 | 34 | 0.8235 | 0.5882 |
| text019 | 26 | 1.0000 | 0.8077 |
| text020 | 32 | 0.7500 | 0.5312 |
