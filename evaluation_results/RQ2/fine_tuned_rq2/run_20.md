# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 20  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8277 (82.77%)  

**Weighted Precision:** 0.8338  
**Weighted Recall:** 0.8277  
**Weighted F1:** 0.8268  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9217 | 0.8644 | 0.8921 | 177 |
| 2 | 0.5882 | 0.5128 | 0.5479 | 39 |
| 3 | 0.7164 | 0.9412 | 0.8136 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5805 (58.05%)  

**Weighted Precision:** 0.5765  
**Weighted Recall:** 0.5805  
**Weighted F1:** 0.5633  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.5882 | 0.4762 | 0.5263 | 21 |
| 1b | 0.6667 | 0.3111 | 0.4242 | 45 |
| 1c | 0.7109 | 0.8198 | 0.7615 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.4643 | 0.5652 | 0.5098 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1500 | 0.3000 | 0.2000 | 10 |
| 3b | 0.5200 | 0.5417 | 0.5306 | 24 |
| 3c | 0.5000 | 0.6875 | 0.5789 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.6875 |
| text012 | 33 | 0.9697 | 0.6667 |
| text013 | 25 | 0.8800 | 0.5600 |
| text014 | 23 | 0.7391 | 0.4783 |
| text015 | 29 | 0.7931 | 0.4138 |
| text016 | 31 | 0.7419 | 0.5806 |
| text017 | 18 | 0.8333 | 0.6111 |
| text018 | 34 | 0.7647 | 0.6176 |
| text019 | 26 | 0.8846 | 0.7308 |
| text020 | 32 | 0.8125 | 0.5000 |
