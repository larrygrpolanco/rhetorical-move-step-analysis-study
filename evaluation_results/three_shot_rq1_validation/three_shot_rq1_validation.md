# Evaluation Results

**Condition:** three_shot  
**Dataset:** validation  
**Research Question:** rq1  
**Articles Evaluated:** 10  
**Total Sentences:** 204  

---

## Move-Level Results (3 classes)

**Overall Accuracy:** 0.8775 (87.75%)  

**Weighted Precision:** 0.8777  
**Weighted Recall:** 0.8775  
**Weighted F1:** 0.8770  

### Per-Move Performance

| Move | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1 | 0.8906 | 0.9268 | 0.9084 | 123 |
| 2 | 0.6667 | 0.6429 | 0.6545 | 28 |
| 3 | 0.9592 | 0.8868 | 0.9216 | 53 |

---

## Step-Level Results (11 classes)

**Overall Accuracy:** 0.4853 (48.53%)  

**Weighted Precision:** 0.4840  
**Weighted Recall:** 0.4853  
**Weighted F1:** 0.4790  

### Per-Step Performance

| Step | Precision | Recall | F1 | Support |
|------|-----------|--------|----|---------|
| 1a | 0.4545 | 0.3333 | 0.3846 | 15 |
| 1b | 0.4800 | 0.5714 | 0.5217 | 42 |
| 1c | 0.6418 | 0.6515 | 0.6466 | 66 |
| 2a | 0.0000 | 0.0000 | 0.0000 | 13 |
| 2b | 0.1429 | 0.3750 | 0.2069 | 8 |
| 2c | 0.0000 | 0.0000 | 0.0000 | 6 |
| 2d | 0.0000 | 0.0000 | 0.0000 | 1 |
| 3a | 0.2353 | 0.3333 | 0.2759 | 12 |
| 3b | 0.4375 | 0.3333 | 0.3784 | 21 |
| 3c | 0.8125 | 0.6500 | 0.7222 | 20 |
| 3d | 0.0000 | 0.0000 | 0.0000 | 0 |

---

## Article-Level Breakdown

| Article | Sentences | Move Accuracy | Step Accuracy |
|---------|-----------|---------------|---------------|
| text001 | 26 | 0.8462 | 0.5769 |
| text002 | 14 | 0.9286 | 0.4286 |
| text003 | 15 | 0.7333 | 0.5333 |
| text004 | 16 | 0.9375 | 0.4375 |
| text005 | 23 | 0.9565 | 0.5217 |
| text006 | 19 | 0.8947 | 0.4737 |
| text007 | 16 | 0.6875 | 0.1875 |
| text008 | 27 | 0.8889 | 0.5556 |
| text009 | 22 | 0.9091 | 0.3182 |
| text010 | 26 | 0.9231 | 0.6538 |
