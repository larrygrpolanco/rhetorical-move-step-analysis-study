# Evaluation Results

**Condition:** fine_tuned  
**Dataset:** validation  
**Research Question:** rq1  
**Articles Evaluated:** 10  
**Total Sentences:** 204  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8382 (83.82%)  

**Weighted Precision:** 0.8334  
**Weighted Recall:** 0.8382  
**Weighted F1:** 0.8344  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8730 | 0.8943 | 0.8835 | 123 |
| 2 | 0.6818 | 0.5357 | 0.6000 | 28 |
| 3 | 0.8214 | 0.8679 | 0.8440 | 53 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.4510 (45.10%)  

**Weighted Precision:** 0.4567  
**Weighted Recall:** 0.4510  
**Weighted F1:** 0.4327  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.3333 | 0.3333 | 0.3333 | 15 |
| 1b | 0.5714 | 0.3810 | 0.4571 | 42 |
| 1c | 0.5663 | 0.7121 | 0.6309 | 66 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 13 |
| 2b | 0.2667 | 0.5000 | 0.3478 | 8 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 6 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 1 |
| 3a | 0.2000 | 0.3333 | 0.2500 | 12 |
| 3b | 0.3793 | 0.5238 | 0.4400 | 21 |
| 3c | 0.7143 | 0.2500 | 0.3704 | 20 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 0 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text001 | 26 | 0.8462 | 0.6154 |
| text002 | 14 | 0.8571 | 0.2143 |
| text003 | 15 | 0.6667 | 0.4000 |
| text004 | 16 | 0.9375 | 0.5625 |
| text005 | 23 | 0.8261 | 0.3478 |
| text006 | 19 | 0.8947 | 0.4211 |
| text007 | 16 | 0.7500 | 0.3125 |
| text008 | 27 | 0.8889 | 0.4815 |
| text009 | 22 | 0.7273 | 0.2727 |
| text010 | 26 | 0.9231 | 0.6923 |
