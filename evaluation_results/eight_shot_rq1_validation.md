# Evaluation Results

**Condition:** eight_shot  
**Dataset:** validation  
**Research Question:** rq1  
**Articles Evaluated:** 10  
**Total Sentences:** 204  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8382 (83.82%)  

**Weighted Precision:** 0.8593  
**Weighted Recall:** 0.8382  
**Weighted F1:** 0.8450  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9130 | 0.8537 | 0.8824 | 123 |
| 2 | 0.5500 | 0.7857 | 0.6471 | 28 |
| 3 | 0.8980 | 0.8302 | 0.8627 | 53 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.4853 (48.53%)  

**Weighted Precision:** 0.5337  
**Weighted Recall:** 0.4853  
**Weighted F1:** 0.4912  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.3333 | 0.4667 | 0.3889 | 15 |
| 1b | 0.5200 | 0.3095 | 0.3881 | 42 |
| 1c | 0.6812 | 0.7121 | 0.6963 | 66 |
| 2a | 0.3333 | 0.0769 | 0.1250 | 13 |
| 2b | 0.2727 | 0.7500 | 0.4000 | 8 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 6 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 1 |
| 3a | 0.1765 | 0.2500 | 0.2069 | 12 |
| 3b | 0.5294 | 0.4286 | 0.4737 | 21 |
| 3c | 0.8667 | 0.6500 | 0.7429 | 20 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 0 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text001 | 26 | 0.9231 | 0.5769 |
| text002 | 14 | 0.9286 | 0.4286 |
| text003 | 15 | 0.7333 | 0.3333 |
| text004 | 16 | 1.0000 | 0.5625 |
| text005 | 23 | 0.8261 | 0.5652 |
| text006 | 19 | 0.8421 | 0.4737 |
| text007 | 16 | 0.6250 | 0.1250 |
| text008 | 27 | 0.8148 | 0.3704 |
| text009 | 22 | 0.9091 | 0.5000 |
| text010 | 26 | 0.7692 | 0.7308 |
