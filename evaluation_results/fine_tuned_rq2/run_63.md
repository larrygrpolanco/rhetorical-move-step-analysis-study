# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 63  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8427 (84.27%)  

**Weighted Precision:** 0.8523  
**Weighted Recall:** 0.8427  
**Weighted F1:** 0.8420  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9394 | 0.8757 | 0.9064 | 177 |
| 2 | 0.6562 | 0.5385 | 0.5915 | 39 |
| 3 | 0.7000 | 0.9608 | 0.8099 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5581 (55.81%)  

**Weighted Precision:** 0.5641  
**Weighted Recall:** 0.5581  
**Weighted F1:** 0.5488  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.7692 | 0.4762 | 0.5882 | 21 |
| 1b | 0.5862 | 0.3778 | 0.4595 | 45 |
| 1c | 0.6911 | 0.7658 | 0.7265 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5909 | 0.5652 | 0.5778 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.2000 | 0.5000 | 0.2857 | 10 |
| 3b | 0.4571 | 0.6667 | 0.5424 | 24 |
| 3c | 0.3000 | 0.1875 | 0.2308 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.7500 |
| text012 | 33 | 1.0000 | 0.6364 |
| text013 | 25 | 1.0000 | 0.4400 |
| text014 | 23 | 0.7391 | 0.5652 |
| text015 | 29 | 0.8966 | 0.5862 |
| text016 | 31 | 0.8065 | 0.6129 |
| text017 | 18 | 0.7778 | 0.6111 |
| text018 | 34 | 0.8235 | 0.7059 |
| text019 | 26 | 0.8846 | 0.4231 |
| text020 | 32 | 0.5938 | 0.3125 |
