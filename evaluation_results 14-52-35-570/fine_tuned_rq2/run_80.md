# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 80  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8240 (82.40%)  

**Weighted Precision:** 0.8267  
**Weighted Recall:** 0.8240  
**Weighted F1:** 0.8222  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9102 | 0.8588 | 0.8837 | 177 |
| 2 | 0.5429 | 0.4872 | 0.5135 | 39 |
| 3 | 0.7538 | 0.9608 | 0.8448 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5318 (53.18%)  

**Weighted Precision:** 0.5380  
**Weighted Recall:** 0.5318  
**Weighted F1:** 0.5168  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.8333 | 0.4762 | 0.6061 | 21 |
| 1b | 0.5652 | 0.2889 | 0.3824 | 45 |
| 1c | 0.6667 | 0.7928 | 0.7243 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.4091 | 0.3913 | 0.4000 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.2381 | 0.5000 | 0.3226 | 10 |
| 3b | 0.4000 | 0.5833 | 0.4746 | 24 |
| 3c | 0.3333 | 0.1875 | 0.2400 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.8750 | 0.6875 |
| text012 | 33 | 0.8788 | 0.5758 |
| text013 | 25 | 1.0000 | 0.5200 |
| text014 | 23 | 0.7826 | 0.5217 |
| text015 | 29 | 0.7931 | 0.4483 |
| text016 | 31 | 0.7742 | 0.5161 |
| text017 | 18 | 0.7778 | 0.5556 |
| text018 | 34 | 0.8235 | 0.6471 |
| text019 | 26 | 0.7692 | 0.6538 |
| text020 | 32 | 0.7812 | 0.2812 |
