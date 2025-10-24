# Pilot Study Evaluation Pipeline

This directory contains the complete evaluation pipeline for your CaRS move-step annotation pilot study.

## Overview

The pipeline follows a three-stage process:
1. **Run** → Execute LLM annotation (run_pilot.py)
2. **Parse** → Extract structured predictions (parse_pilot.py)  
3. **Evaluate** → Compare against gold standard (evaluate_pilot.py)

## Files

### 1. prepare_gold_standard.py
**Run ONCE at the beginning** to prepare gold standard data.

```bash
python prepare_gold_standard.py
```

**What it does:**
- Reads XML files from `Annotated_Dataset/`
- Converts to JSON format matching parser output
- Saves to `gold_standard/` directory
- Uses `sentence_num` field for consistency

**Output:**
```
gold_standard/
├── text001.json
├── text002.json
├── ...
└── _summary.json
```

### 2. run_pilot.py
Execute LLM annotation for a specific condition.

**Edit configuration:**
```python
CONDITION = "a1_zero_shot"  # Which prompt condition
LLM_FUNCTION = call_gpt_5_mini  # Which LLM
ARTICLES = range(1, 11)  # Which articles (1-10 for pilot)
```

**Output:**
```
pilot_outputs/
└── a1_zero_shot/
    └── gpt-5mini/
        └── output/
            ├── text001.txt
            ├── text002.txt
            └── ...
```

### 3. parse_pilot.py
Parse raw LLM outputs into structured JSON.

**Edit configuration:**
```python
CONDITION = "a1_zero_shot"
MODEL = "gpt-5mini"
```

**Output:**
```
pilot_outputs/
└── a1_zero_shot/
    └── gpt-5mini/
        └── parsed/
            ├── text001.json
            ├── text002.json
            └── ...
```

### 4. evaluate_pilot.py ⭐ NEW
Evaluate predictions against gold standard.

**Edit configuration:**
```python
CONDITION = "a1_zero_shot"
MODEL = "gpt-5mini"
```

**Output:**
```
pilot_outputs/
└── a1_zero_shot/
    └── gpt-5mini/
        └── evaluation.md
```

## Workflow

### Initial Setup (Once)
```bash
# 1. Prepare gold standard from XML files
python prepare_gold_standard.py
```

### For Each Condition (a1, a2, b1, b2, b3, c1, c2)

```bash
# 2. Edit run_pilot.py configuration, then run
python run_pilot.py

# 3. Edit parse_pilot.py configuration, then parse
python parse_pilot.py

# 4. Edit evaluate_pilot.py configuration, then evaluate
python evaluate_pilot.py
```

### Result
Read `pilot_outputs/{condition}/{model}/evaluation.md` to review:
- Overall accuracy at move and step levels
- Weighted and macro averages
- Per-move and per-step breakdowns
- Multi-tag statistics
- Alignment issues (if any)

## Evaluation Metrics

### Following Kim & Lu (2024)

**Move-Level:**
- Accuracy: % of sentences with correct move (1, 2, 3)
- Precision, Recall, F1: Per-move performance
- Weighted averages: Account for class imbalance
- Macro averages: Treat each move equally

**Step-Level:**
- Accuracy: % of sentences with correct step (1a, 1b, etc.)
- Precision, Recall, F1: Per-step performance
- Weighted averages: Account for class imbalance
- Macro averages: Treat each step equally

**Multi-tag Handling:**
- Match against primary_tag only
- Report % of multi-tag sentences

### Metric Definitions

**Precision**: Of all sentences predicted as class X, what % were actually X?
- High precision = few false positives

**Recall**: Of all sentences that are actually class X, what % were found?
- High recall = few false negatives

**F1 Score**: Harmonic mean of precision and recall
- Balances both metrics equally

**Weighted Average**: Average weighted by class frequency
- Reflects overall performance considering class imbalance

**Macro Average**: Unweighted average across classes
- Treats each class equally regardless of frequency

## Alignment Strategy

The evaluation uses a **hybrid alignment approach**:

1. **Primary**: Match by `sentence_num` (assumes clean sentence splitting)
2. **Verification**: Calculate text similarity ratio
3. **Flagging**: Report sentences with similarity < 0.8 for manual review

**If alignment issues occur:**
- Check the alignment issues section in evaluation.md
- Manually review flagged sentences
- Re-run if necessary (fix prompt or parsing issues)

## Directory Structure

```
project/
├── Annotated_Dataset/          # Original XML files
│   ├── text001.xml
│   └── ...
│
├── gold_standard/              # Gold standard JSON (run once)
│   ├── text001.json
│   └── ...
│
├── pilot_outputs/              # Results for each condition
│   ├── a1_zero_shot/
│   │   └── gpt-5mini/
│   │       ├── output/         # Raw LLM responses
│   │       ├── parsed/         # Structured predictions
│   │       └── evaluation.md   # Final metrics ⭐
│   │
│   ├── a2_few_shot/
│   ├── b1_cot_simple/
│   └── ...
│
└── prompts/                    # Prompt templates
    ├── a1_zero_shot.txt
    └── ...
```

## Next Steps

After running all pilot conditions:

1. **Compare Results**: Read each `evaluation.md` side-by-side
2. **Identify Patterns**: Which conditions perform best?
3. **Error Analysis**: Which moves/steps are hardest?
4. **Decide Focus**: Select 1-2 promising methods for main study
5. **Iterate**: Refine prompts if needed and re-evaluate

## Notes

- **No McNemar's test in pilot**: Just descriptive statistics
- **Clean data assumption**: Evaluation expects aligned sentences
- **Manual oversight**: Review alignment issues before trusting metrics
- **Condition isolation**: Each evaluation.md is self-contained

## Questions?

This pipeline is designed for:
- ✅ Quick iteration across multiple conditions
- ✅ Clean, readable reports for manual comparison
- ✅ Following Kim & Lu (2024) methodology
- ✅ Balancing automation with manual oversight

For issues or modifications, check the inline documentation in each script.
