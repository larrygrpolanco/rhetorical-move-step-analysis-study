# Progress Update: CaRS-50 Adaptation Complete

## ✅ What We've Done

### 1. Identified Critical Mapping Issue
- **Problem**: Your dataset uses CaRS-50 scheme (1a, 1b, 1c) but original prompt used Kim & Lu scheme (M1_S1a, M1_S2, etc.)
- **Solution**: Adapted study to use CaRS-50 scheme throughout
- **Impact**: Your study is now an **extension** of Kim & Lu methodology, not a perfect replication

### 2. Created Updated Prompt
- **File**: `prompts/a1_zero_shot_cars50.txt`
- **Changes**: 
  - Removed Kim & Lu's 23-category system
  - Implemented CaRS-50's 13-category system (1a, 1b, 1c, 2a, 2b, 2c, 2d, 3a, 3b, 3c, 3d)
  - Added examples for each category
  - Changed from "Applied Linguistics" to "Biology" research articles
- **Status**: Ready to test

### 3. Created Gold Standard Preparation Script
- **File**: `prepare_gold_standard.py`
- **Purpose**: Converts all 50 XML files → JSON format for evaluation
- **Output Structure**:
```json
[
  {
    "position": 1,
    "sentence_id": "t001s0001",
    "text": "Central components of animal cognition are...",
    "tags": ["1b"],
    "primary_tag": "1b",
    "move": "1"
  },
  ...
]
```
- **Status**: Ready to run

## 📋 CaRS-50 Annotation Scheme (Your Study)

| Code | Description | Move |
|------|-------------|------|
| 1a | Claim centrality | Move 1 |
| 1b | Make topic generalizations | Move 1 |
| 1c | Review previous research | Move 1 |
| 2a | Counter-claiming | Move 2 |
| 2b | Indicate a gap | Move 2 |
| 2c | Question-raising | Move 2 |
| 2d | Continue a tradition | Move 2 |
| 3a | Outline purposes | Move 3 |
| 3b | Announce present research | Move 3 |
| 3c | Announce main findings | Move 3 |
| 3d | Indicate article structure | Move 3 |

**Total**: 11 step-level categories, 3 move-level categories

## 🎯 Next Steps (In Order)

### Step 1: Prepare Gold Standard (5 minutes)
```bash
python prepare_gold_standard.py
```
This creates `gold_standard/` directory with 50 JSON files.

### Step 2: Re-run text001 with Corrected Prompt (2 minutes)
```python
# In run_pilot.py, change:
CONDITION = "a1_zero_shot_cars50"
ARTICLES = range(1, 2)  # Just text001 first
```
Then run: `python run_pilot.py`

### Step 3: Verify Output Format
Check if the new output uses CaRS-50 codes (1a, 1b, etc.) instead of Kim & Lu codes.

### Step 4: Build LLM-Assisted Parser (Next session)
Create `parse_llm_output.py` that:
- Stage 1: Deterministic regex parser
- Stage 2: LLM fallback for messy outputs
- Stage 3: Manual review queue
- Output: `parsed.json` with standardized format

### Step 5: Build Evaluation Script (Next session)
Create `evaluate_pilot.py` that:
- Compares parsed predictions vs gold standard
- Calculates ALL Kim & Lu metrics:
  - Move-level accuracy
  - Step-level accuracy
  - Precision, Recall, F1 (per category)
  - Weighted averages
- Outputs timestamped markdown report

## 📊 Evaluation Metrics You'll Calculate

Based on Kim & Lu methodology:

1. **Overall Accuracy** (move and step level)
2. **Per-Category Metrics**:
   - Precision = TP / (TP + FP)
   - Recall = TP / (TP + FN)
   - F1 = 2 * (Precision * Recall) / (Precision + Recall)
3. **Weighted Averages** (across all categories)
4. **McNemar's Test** (for comparing conditions later)
5. **Confusion Matrix** (optional - you said you won't iterate on prompts)

### Multi-Tag Handling (Kim & Lu Rule)
"Sentence considered correct if at least one predicted tag matches the primary tag (first tag)"

Example:
- Gold: `[1a, 3b]` (primary: 1a)
- Predicted: `[1a]` → ✓ **Correct**
- Predicted: `[3b]` → ✓ **Correct** 
- Predicted: `[2a]` → ✗ **Wrong**

## ⚠️ Important Notes for Your Paper

### What to Say:
> "We replicated Kim & Lu's (2024) methodology on Biology research articles using the CaRS-50 annotation scheme (Omotola et al., 2025). While CaRS-50 uses a simplified 13-category system compared to Kim & Lu's 23-category system, we maintained identical evaluation methodology (precision, recall, F1, McNemar's test) to assess the effectiveness of various prompting strategies."

### What NOT to Say:
- ~~"We perfectly replicated Kim & Lu"~~ (you didn't - different scheme)
- ~~"We used the same annotation framework"~~ (you didn't - CaRS-50 vs Kim & Lu)

### What IS Valid to Compare:
- ✅ Move-level accuracy (both have 3 moves)
- ✅ Methodology effectiveness (zero-shot, few-shot, fine-tuning)
- ✅ Statistical rigor (same tests and metrics)
- ✅ Cost-effectiveness comparisons

### What is NOT Valid to Compare:
- ❌ Step-level accuracy numbers (different granularity: 11 vs 23 categories)
- ❌ Specific category performance (categories don't align 1:1)

## 🚀 Ready to Continue?

Your immediate next actions:

1. **Run**: `python prepare_gold_standard.py`
2. **Update run_pilot.py**: Change condition to `"a1_zero_shot_cars50"`
3. **Run**: `python run_pilot.py` 
4. **Review**: Check if output format looks better
5. **Report back**: Share the new output so we can build the parser

Then we'll build:
- Parser script (handles messy LLM outputs)
- Evaluation script (calculates all metrics)

Sound good? 🎯
