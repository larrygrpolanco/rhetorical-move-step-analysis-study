# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** rq1  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8165 (81.65%)  

**Weighted Precision:** 0.8118  
**Weighted Recall:** 0.8165  
**Weighted F1:** 0.8109  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8971 | 0.8870 | 0.8920 | 177 |
| 2 | 0.5517 | 0.4103 | 0.4706 | 39 |
| 3 | 0.7143 | 0.8824 | 0.7895 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5506 (55.06%)  

**Weighted Precision:** 0.5234  
**Weighted Recall:** 0.5506  
**Weighted F1:** 0.5220  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.6429 | 0.4286 | 0.5143 | 21 |
| 1b | 0.4667 | 0.3111 | 0.3733 | 45 |
| 1c | 0.6794 | 0.8018 | 0.7355 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5500 | 0.4783 | 0.5116 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1176 | 0.2000 | 0.1481 | 10 |
| 3b | 0.5000 | 0.8750 | 0.6364 | 24 |
| 3c | 0.2500 | 0.0625 | 0.1000 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.8125 |
| text012 | 33 | 0.9394 | 0.5758 |
| text013 | 25 | 0.8400 | 0.3600 |
| text014 | 23 | 0.6957 | 0.4348 |
| text015 | 29 | 0.7586 | 0.4138 |
| text016 | 31 | 0.9355 | 0.7097 |
| text017 | 18 | 0.7222 | 0.5556 |
| text018 | 34 | 0.7353 | 0.6176 |
| text019 | 26 | 0.8462 | 0.6923 |
| text020 | 32 | 0.7812 | 0.4062 |
