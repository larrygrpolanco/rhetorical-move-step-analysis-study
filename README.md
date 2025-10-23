# Rhetorical Move-Step Analysis Study

Systematic evaluation of LLM annotation consistency for rhetorical move-step analysis using the CaRS framework on Biology research articles.

## Study Overview

**Research Questions:**
- RQ1: How do zero-shot, few-shot (3-shot, 8-shot), and fine-tuned approaches perform on Biology research article move-step annotation?
- RQ2: How does annotation consistency vary across prompting conditions?

**Dataset:** CaRS-50 (50 Biology research article introductions)
- Validation: Articles 1-10
- Test: Articles 11-20  
- Training: Articles 21-50

## Setup

### 1. Install Dependencies
```bash
pip install -r requirement.txt
```

### 2. Environment Variables
Create `.env` file with:
```
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
```

### 3. Prepare Data (ONE TIME ONLY)

**Step 1: Create Gold Standard**
```bash
python prepare_gold_standard.py
```
Creates `gold_standard/CaRS-50/` with three formats (input, output, json) for each split.

**Step 2: Select Few-Shot Examples**
```bash
python setup_few_shot_examples.py
```
Randomly selects fixed examples for 3-shot and 8-shot conditions (seed=42).

### 4. Create System Prompt
Add your annotation instructions to `prompts/system_prompt.txt`

## Running Conditions

Edit configuration in `run_condition.py`:
```python
CONDITION = "zero_shot"       # Options: zero_shot, three_shot, eight_shot
DATASET = "validation"        # Options: validation, test
RESEARCH_QUESTION = "rq1"     # Options: rq1, rq2
ARTICLES = range(1, 11)       # Which articles to process
RUNS = range(1, 2)            # RQ1: single run, RQ2: multiple runs
```

Then run:
```bash
python run_condition.py
```

### Example Configurations

**Zero-shot on validation (RQ1):**
```python
CONDITION = "zero_shot"
DATASET = "validation"
RESEARCH_QUESTION = "rq1"
ARTICLES = range(1, 11)
RUNS = range(1, 2)
```

**3-shot on test set (RQ1):**
```python
CONDITION = "three_shot"
DATASET = "test"
RESEARCH_QUESTION = "rq1"
ARTICLES = range(11, 21)
RUNS = range(1, 2)
```

**Zero-shot consistency runs (RQ2):**
```python
CONDITION = "zero_shot"
DATASET = "test"
RESEARCH_QUESTION = "rq2"
ARTICLES = range(11, 21)
RUNS = range(1, 31)  # 30 runs
```

**Resume from run 15 if interrupted:**
```python
RUNS = range(15, 31)  # Continue from run 15
```

## Output Structure
```
outputs/
├── zero_shot/
│   ├── rq1_validation/
│   │   ├── raw/      # Raw LLM outputs
│   │   └── parsed/   # Parsed JSON files
│   ├── rq1_test/
│   ├── rq2_run_01/
│   ├── rq2_run_02/
│   └── ...
├── three_shot/
└── eight_shot/
```

## File Descriptions

**Data Preparation:**
- `prepare_gold_standard.py` - Converts XML to three formats (input, output, json)
- `setup_few_shot_examples.py` - Selects fixed training examples

**Core Pipeline:**
- `run_condition.py` - Main script: runs LLM calls and parsing
- `llm_handler.py` - Condition-specific LLM API calls
- `parse_llm_output.py` - Deterministic parser for LLM outputs

**Data:**
- `gold_standard/CaRS-50/` - Prepared dataset in three formats
- `prompts/system_prompt.txt` - Annotation instructions

## Workflow

1. ✓ Prepare gold standard data (once)
2. ✓ Select few-shot examples (once)
3. Create system prompt
4. Run RQ1: Single run per condition on validation set
5. Evaluate and refine if needed
6. Run RQ1: Single run per condition on test set
7. Run RQ2: 30 runs per condition on test set
8. Evaluate results (separate scripts)

## Notes

- **Fixed examples:** Few-shot examples are locked after selection for consistency
- **Resumable:** Can restart from any article or run number if interrupted
- **Parser:** Automatically runs after each LLM call
- **Evaluation:** Handled separately (not in this pipeline)

---

Author: Larry Grullon-Polanco  
Date: 2025


