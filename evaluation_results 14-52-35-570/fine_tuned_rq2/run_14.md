# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** test  
**Research Question:** RQ2  
**Run Number:** 14  
**Articles Evaluated:** 10  
**Total Sentences:** 267  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8427 (84.27%)  

**Weighted Precision:** 0.8441  
**Weighted Recall:** 0.8427  
**Weighted F1:** 0.8426  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9128 | 0.8870 | 0.8997 | 177 |
| 2 | 0.6216 | 0.5897 | 0.6053 | 39 |
| 3 | 0.7759 | 0.8824 | 0.8257 | 51 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.6030 (60.30%)  

**Weighted Precision:** 0.6023  
**Weighted Recall:** 0.6030  
**Weighted F1:** 0.5939  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.6667 | 0.4762 | 0.5556 | 21 |
| 1b | 0.6333 | 0.4222 | 0.5067 | 45 |
| 1c | 0.7165 | 0.8198 | 0.7647 | 111 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 5 |
| 2b | 0.5185 | 0.6087 | 0.5600 | 23 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 4 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 7 |
| 3a | 0.1905 | 0.4000 | 0.2581 | 10 |
| 3b | 0.6316 | 0.5000 | 0.5581 | 24 |
| 3c | 0.6111 | 0.6875 | 0.6471 | 16 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 1 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text011 | 16 | 0.9375 | 0.5625 |
| text012 | 33 | 0.9394 | 0.6970 |
| text013 | 25 | 0.9600 | 0.6800 |
| text014 | 23 | 0.8261 | 0.5652 |
| text015 | 29 | 0.6897 | 0.4483 |
| text016 | 31 | 0.8387 | 0.5161 |
| text017 | 18 | 0.7778 | 0.5556 |
| text018 | 34 | 0.7941 | 0.7059 |
| text019 | 26 | 0.9231 | 0.7692 |
| text020 | 32 | 0.7812 | 0.5000 |
