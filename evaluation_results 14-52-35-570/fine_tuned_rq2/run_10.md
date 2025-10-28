# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 10  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8240 (82.40%)  

**Weighted Precision:** 0.8297  
**Weighted Recall:** 0.8240  
**Weighted F1:** 0.8209  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9207 | 0.8531 | 0.8856 | 177 |
| 2 | 0.5625 | 0.4615 | 0.5070 | 39 |
| 3 | 0.7183 | 1.0000 | 0.8361 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.6105 (61.05%)  

**Weighted Precision:** 0.6054  
**Weighted Recall:** 0.6105  
**Weighted F1:** 0.5901  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.5789 | 0.5238 | 0.5500 | 21 |
| 1b | 0.7273 | 0.3556 | 0.4776 | 45 |
| 1c | 0.7480 | 0.8288 | 0.7863 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.4444 | 0.5217 | 0.4800 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.3182 | 0.7000 | 0.4375 | 10 |
| 3b | 0.5135 | 0.7917 | 0.6230 | 24 |
| 3c | 0.5000 | 0.3750 | 0.4286 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.6875 |
| text012 | 33 | 0.9394 | 0.6364 |
| text013 | 25 | 0.9600 | 0.5200 |
| text014 | 23 | 0.7826 | 0.4783 |
| text015 | 29 | 0.7931 | 0.5172 |
| text016 | 31 | 0.8065 | 0.6452 |
| text017 | 18 | 0.8333 | 0.6111 |
| text018 | 34 | 0.7059 | 0.6471 |
| text019 | 26 | 0.7692 | 0.6923 |
| text020 | 32 | 0.7812 | 0.6562 |
