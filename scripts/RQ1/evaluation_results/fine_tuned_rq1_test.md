# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** rq1  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8390 (83.90%)  

**Weighted Precision:** 0.8526  
**Weighted Recall:** 0.8390  
**Weighted F1:** 0.8426  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9379 | 0.8531 | 0.8935 | 177 |
| 2 | 0.5682 | 0.6410 | 0.6024 | 39 |
| 3 | 0.7742 | 0.9412 | 0.8496 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5206 (52.06%)  

**Weighted Precision:** 0.5356  
**Weighted Recall:** 0.5206  
**Weighted F1:** 0.5159  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.4688 | 0.7143 | 0.5660 | 21 |
| 1b | 0.5000 | 0.3111 | 0.3836 | 45 |
| 1c | 0.6634 | 0.6036 | 0.6321 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5200 | 0.5652 | 0.5417 | 23 |
| 2c | 0.1333 | 0.5000 | 0.2105 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.2222 | 0.4000 | 0.2857 | 10 |
| 3b | 0.5294 | 0.7500 | 0.6207 | 24 |
| 3c | 0.6000 | 0.3750 | 0.4615 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.7500 |
| text012 | 33 | 0.9091 | 0.6364 |
| text013 | 25 | 1.0000 | 0.5600 |
| text014 | 23 | 0.6957 | 0.4348 |
| text015 | 29 | 0.8276 | 0.4138 |
| text016 | 31 | 0.9032 | 0.5161 |
| text017 | 18 | 0.6667 | 0.4444 |
| text018 | 34 | 0.8824 | 0.5588 |
| text019 | 26 | 0.6923 | 0.3846 |
| text020 | 32 | 0.8125 | 0.5312 |
