# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 26  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8165 (81.65%)  

**Weighted Precision:** 0.8191  
**Weighted Recall:** 0.8165  
**Weighted F1:** 0.8118  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8895 | 0.8644 | 0.8768 | 177 |
| 2 | 0.6667 | 0.4615 | 0.5455 | 39 |
| 3 | 0.6912 | 0.9216 | 0.7899 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5581 (55.81%)  

**Weighted Precision:** 0.5676  
**Weighted Recall:** 0.5581  
**Weighted F1:** 0.5341  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.5625 | 0.4286 | 0.4865 | 21 |
| 1b | 0.7895 | 0.3333 | 0.4688 | 45 |
| 1c | 0.6569 | 0.8108 | 0.7258 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5217 | 0.5217 | 0.5217 | 23 |
| 2c | 1.0000 | 0.2500 | 0.4000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1600 | 0.4000 | 0.2286 | 10 |
| 3b | 0.4595 | 0.7083 | 0.5574 | 24 |
| 3c | 0.1667 | 0.0625 | 0.0909 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.6875 |
| text012 | 33 | 0.9394 | 0.6061 |
| text013 | 25 | 0.9600 | 0.4400 |
| text014 | 23 | 0.8261 | 0.6087 |
| text015 | 29 | 0.7586 | 0.5172 |
| text016 | 31 | 0.8065 | 0.6129 |
| text017 | 18 | 0.6667 | 0.5000 |
| text018 | 34 | 0.8235 | 0.6765 |
| text019 | 26 | 0.8077 | 0.6154 |
| text020 | 32 | 0.6562 | 0.3438 |
