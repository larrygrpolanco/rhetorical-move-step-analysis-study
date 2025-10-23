# Evaluation Results

**Condition:** zero_shot  
**Dataset:** validation  
**Research Question:** rq1  
**Articles Evaluated:** 10  
**Total Sentences:** 204  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8725 (87.25%)  

**Weighted Precision:** 0.8881  
**Weighted Recall:** 0.8725  
**Weighted F1:** 0.8776  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.9250 | 0.9024 | 0.9136 | 123 |
| 2 | 0.5946 | 0.7857 | 0.6769 | 28 |
| 3 | 0.9574 | 0.8491 | 0.9000 | 53 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.5196 (51.96%)  

**Weighted Precision:** 0.5503  
**Weighted Recall:** 0.5196  
**Weighted F1:** 0.5229  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.3750 | 0.4000 | 0.3871 | 15 |
| 1b | 0.5128 | 0.4762 | 0.4938 | 42 |
| 1c | 0.7231 | 0.7121 | 0.7176 | 66 |
| 2a | 0.3333 | 0.0769 | 0.1250 | 13 |
| 2b | 0.1724 | 0.6250 | 0.2703 | 8 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 6 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 1 |
| 3a | 0.3846 | 0.4167 | 0.4000 | 12 |
| 3b | 0.6000 | 0.4286 | 0.5000 | 21 |
| 3c | 0.7222 | 0.6500 | 0.6842 | 20 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 0 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text001 | 26 | 0.8462 | 0.6154 |
| text002 | 14 | 0.8571 | 0.4286 |
| text003 | 15 | 0.8667 | 0.6667 |
| text004 | 16 | 0.9375 | 0.3750 |
| text005 | 23 | 0.9130 | 0.5652 |
| text006 | 19 | 0.8421 | 0.4737 |
| text007 | 16 | 0.7500 | 0.2500 |
| text008 | 27 | 0.8889 | 0.5185 |
| text009 | 22 | 0.9091 | 0.4545 |
| text010 | 26 | 0.8846 | 0.6923 |
