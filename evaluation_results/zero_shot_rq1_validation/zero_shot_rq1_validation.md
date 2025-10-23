# Evaluation Results

**Condition:** zero_shot  
**Dataset:** validation  
**Research Question:** rq1  
**Articles Evaluated:** 10  
**Total Sentences:** 204  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8529 (85.29%)  

**Weighted Precision:** 0.8626  
**Weighted Recall:** 0.8529  
**Weighted F1:** 0.8556  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8810 | 0.9024 | 0.8916 | 123 |
| 2 | 0.6061 | 0.7143 | 0.6557 | 28 |
| 3 | 0.9556 | 0.8113 | 0.8776 | 53 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5098 (50.98%)  

**Weighted Precision:** 0.5658  
**Weighted Recall:** 0.5098  
**Weighted F1:** 0.5119  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.4615 | 0.4000 | 0.4286 | 15 |
| 1b | 0.4833 | 0.6905 | 0.5686 | 42 |
| 1c | 0.7358 | 0.5909 | 0.6555 | 66 |
| 2a | 0.5000 | 0.0769 | 0.1333 | 13 |
| 2b | 0.1481 | 0.5000 | 0.2286 | 8 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 6 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 1 |
| 3a | 0.3529 | 0.5000 | 0.4138 | 12 |
| 3b | 0.5455 | 0.2857 | 0.3750 | 21 |
| 3c | 0.8125 | 0.6500 | 0.7222 | 20 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 0 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text001 | 26 | 0.8462 | 0.6154 |
| text002 | 14 | 0.9286 | 0.4286 |
| text003 | 15 | 0.7333 | 0.5333 |
| text004 | 16 | 0.9375 | 0.4375 |
| text005 | 23 | 0.9130 | 0.5217 |
| text006 | 19 | 0.7895 | 0.4211 |
| text007 | 16 | 0.7500 | 0.3125 |
| text008 | 27 | 0.8889 | 0.5185 |
| text009 | 22 | 0.8182 | 0.3636 |
| text010 | 26 | 0.8846 | 0.7692 |
