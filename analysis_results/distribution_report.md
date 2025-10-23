# Step Distribution Analysis Report

## Dataset Summary

| Dataset    |   Articles |   Total Sentences |   Avg Sentences/Article | Move 1      | Move 2     | Move 3      |
|:-----------|-----------:|------------------:|------------------------:|:------------|:-----------|:------------|
| validation |         10 |               204 |                    20.4 | 123 (60.3%) | 28 (13.7%) | 53 (26.0%)  |
| test       |         10 |               267 |                    26.7 | 177 (66.3%) | 39 (14.6%) | 51 (19.1%)  |
| train      |         30 |               826 |                    27.5 | 569 (68.9%) | 73 (8.8%)  | 184 (22.3%) |

## Step-Level Comparison

| Step   | validation   | test        | train       |
|:-------|:-------------|:------------|:------------|
| 1a     | 15 (7.4%)    | 21 (7.9%)   | 55 (6.7%)   |
| 1b     | 42 (20.6%)   | 45 (16.9%)  | 124 (15.0%) |
| 1c     | 66 (32.4%)   | 111 (41.6%) | 390 (47.2%) |
| 2a     | 13 (6.4%)    | 5 (1.9%)    | 11 (1.3%)   |
| 2b     | 8 (3.9%)     | 23 (8.6%)   | 39 (4.7%)   |
| 2c     | 6 (2.9%)     | 4 (1.5%)    | 18 (2.2%)   |
| 2d     | 1 (0.5%)     | 7 (2.6%)    | 5 (0.6%)    |
| 3a     | 12 (5.9%)    | 10 (3.7%)   | 56 (6.8%)   |
| 3b     | 21 (10.3%)   | 24 (9.0%)   | 82 (9.9%)   |
| 3c     | 20 (9.8%)    | 16 (6.0%)   | 46 (5.6%)   |
| 3d     | 0 (0.0%)     | 1 (0.4%)    | 0 (0.0%)    |

## Few-Shot Example Sets

### 3-shot

- Articles: text021, text024, text041
- Total Sentences: 77
- Avg Sentences/Article: 25.7

**Move Distribution:**

- Move 1: 48 (62.3%)
- Move 2: 7 (9.1%)
- Move 3: 22 (28.6%)

**Step Distribution:**

- Step 1a: 2 (2.6%)
- Step 1b: 8 (10.4%)
- Step 1c: 38 (49.4%)
- Step 2a: 0 (0.0%)
- Step 2b: 5 (6.5%)
- Step 2c: 1 (1.3%)
- Step 2d: 1 (1.3%)
- Step 3a: 3 (3.9%)
- Step 3b: 15 (19.5%)
- Step 3c: 4 (5.2%)
- Step 3d: 0 (0.0%)

### 8-shot

- Articles: text022, text025, text030, text032, text035, text042, text043, text045
- Total Sentences: 248
- Avg Sentences/Article: 31.0

**Move Distribution:**

- Move 1: 162 (65.3%)
- Move 2: 24 (9.7%)
- Move 3: 62 (25.0%)

**Step Distribution:**

- Step 1a: 18 (7.3%)
- Step 1b: 32 (12.9%)
- Step 1c: 112 (45.2%)
- Step 2a: 9 (3.6%)
- Step 2b: 8 (3.2%)
- Step 2c: 4 (1.6%)
- Step 2d: 3 (1.2%)
- Step 3a: 25 (10.1%)
- Step 3b: 27 (10.9%)
- Step 3c: 10 (4.0%)
- Step 3d: 0 (0.0%)

