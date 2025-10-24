# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 31  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8427 (84.27%)  

**Weighted Precision:** 0.8421  
**Weighted Recall:** 0.8427  
**Weighted F1:** 0.8349  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8852 | 0.9153 | 0.9000 | 177 |
| 2 | 0.7826 | 0.4615 | 0.5806 | 39 |
| 3 | 0.7377 | 0.8824 | 0.8036 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.6217 (62.17%)  

**Weighted Precision:** 0.5866  
**Weighted Recall:** 0.6217  
**Weighted F1:** 0.5908  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.6316 | 0.5714 | 0.6000 | 21 |
| 1b | 0.6400 | 0.3556 | 0.4571 | 45 |
| 1c | 0.6835 | 0.8559 | 0.7600 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.6087 | 0.6087 | 0.6087 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.2143 | 0.3000 | 0.2500 | 10 |
| 3b | 0.5294 | 0.7500 | 0.6207 | 24 |
| 3c | 0.6154 | 0.5000 | 0.5517 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.7500 |
| text012 | 33 | 0.9091 | 0.6364 |
| text013 | 25 | 1.0000 | 0.6800 |
| text014 | 23 | 0.7826 | 0.5217 |
| text015 | 29 | 0.7586 | 0.4828 |
| text016 | 31 | 0.8710 | 0.6129 |
| text017 | 18 | 0.6667 | 0.4444 |
| text018 | 34 | 0.8529 | 0.8235 |
| text019 | 26 | 0.9615 | 0.8462 |
| text020 | 32 | 0.7188 | 0.4062 |
