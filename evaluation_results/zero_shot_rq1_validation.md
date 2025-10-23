# Evaluation Results

**Condition:** zero_shot  
**Dataset:** validation  
**Research Question:** rq1  
**Articles Evaluated:** 10  
**Total Sentences:** 204  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8578 (85.78%)  

**Weighted Precision:** 0.8776  
**Weighted Recall:** 0.8578  
**Weighted F1:** 0.8642  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9237 | 0.8862 | 0.9046 | 123 |
| 2 | 0.5641 | 0.7857 | 0.6567 | 28 |
| 3 | 0.9362 | 0.8302 | 0.8800 | 53 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5049 (50.49%)  

**Weighted Precision:** 0.5611  
**Weighted Recall:** 0.5049  
**Weighted F1:** 0.5169  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.4375 | 0.4667 | 0.4516 | 15 |
| 1b | 0.5000 | 0.5000 | 0.5000 | 42 |
| 1c | 0.7333 | 0.6667 | 0.6984 | 66 |
| 2a | 0.5000 | 0.0769 | 0.1333 | 13 |
| 2b | 0.1600 | 0.5000 | 0.2424 | 8 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 6 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 1 |
| 3a | 0.3571 | 0.4167 | 0.3846 | 12 |
| 3b | 0.5714 | 0.3810 | 0.4571 | 21 |
| 3c | 0.7222 | 0.6500 | 0.6842 | 20 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 0 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text001 | 26 | 0.8077 | 0.5385 |
| text002 | 14 | 0.9286 | 0.4286 |
| text003 | 15 | 0.8667 | 0.8000 |
| text004 | 16 | 0.8750 | 0.2500 |
| text005 | 23 | 0.9130 | 0.5217 |
| text006 | 19 | 0.7895 | 0.4737 |
| text007 | 16 | 0.7500 | 0.1875 |
| text008 | 27 | 0.8519 | 0.5185 |
| text009 | 22 | 0.9091 | 0.4545 |
| text010 | 26 | 0.8846 | 0.7308 |
