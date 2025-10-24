# LLM Consistency in Rhetorical Move-Step Annotation

Systematic evaluation of GPT-4 annotation consistency and performance for Biology research article introductions using the CaRS framework.

## Study Overview

**RQ1:** How do zero-shot, few-shot, and fine-tuned approaches perform on move-step annotation?  
**RQ2:** How consistent are zero-shot and fine-tuned annotations across repeated runs?

**Dataset:** CaRS-50 (50 Biology articles, 11 steps, 3 moves)  
**Model:** GPT-4 (gpt-4.1-2025-04-14)  
**Design:** 4 conditions × 1 run (RQ1) + 2 conditions × 50 runs (RQ2)

## Quick Start

### 1. Setup
```bash
pip install -r requirement.txt
cp .env.example .env  # Add your OpenAI API key
```

### 2. Prepare Data
```bash
# Setup gold standard and few-shot examples
python gold_standard/prepare_gold_standard.py
python gold_standard/setup_few_shot_examples.py

# Prepare fine-tuning data (if needed)
python fine-tuning/prepare_finetuning_data.py
```

### 3. Run RQ1 (Single-run performance)
```bash
# Run each condition separately:
python scripts/run_condition.py --condition zero_shot
python scripts/run_condition.py --condition three_shot  
python scripts/run_condition.py --condition eight_shot
python scripts/run_condition.py --condition fine_tuned

# Evaluate results
python scripts/RQ1/1_evaluate_rq1.py
python scripts/RQ1/2_compare_rq1.py
```

### 4. Run RQ2 (Consistency analysis)
```bash
# Run 50 iterations for zero-shot and fine-tuned
python scripts/run_condition.py --condition zero_shot --runs 50
python scripts/run_condition.py --condition fine_tuned --runs 50

# Analyze consistency
python scripts/RQ2/1_evaluate_rq2_runs.py
python scripts/RQ2/2_analyze_consistency_rq2.py
python scripts/RQ2/3_compare_consistency_rq2.py
python scripts/RQ2/4_analyze_sentences_rq2.py
python scripts/RQ2/visualize_rq2.py
```

## Directory Structure

```
├── scripts/
│   ├── run_condition.py          # Main execution script
│   ├── llm_handler.py             # OpenAI API interface
│   ├── parse_llm_output.py        # Parse model outputs
│   ├── RQ1/                       # Performance evaluation
│   │   ├── 1_evaluate_rq1.py
│   │   └── 2_compare_rq1.py
│   └── RQ2/                       # Consistency analysis
│       ├── 1_evaluate_rq2_runs.py
│       ├── 2_analyze_consistency_rq2.py
│       ├── 3_compare_consistency_rq2.py
│       └── 4_analyze_sentences_rq2.py
├── prompts/
│   └── system_prompt.txt          # Base prompt for all conditions
├── gold_standard/
│   ├── CaRS-50/                   # Annotated dataset
│   ├── prepare_gold_standard.py
│   └── setup_few_shot_examples.py
└── fine-tuning/
    ├── prepare_finetuning_data.py
    └── finetuning_data.jsonl
```

## Data Splits

- **Training:** 30 articles (60%) - Fine-tuning only
- **Validation:** 10 articles (20%) - Prompt development
- **Test:** 10 articles (20%) - All evaluations (held out)

## Key Design Decisions

- **Temperature:** 1.0 (matches Kim & Lu 2024; measures natural variability)
- **Runs:** 50 per condition for RQ2 (vs. Kim & Lu's 3 runs)
- **Focus:** Move-level accuracy (primary) + Step-level (secondary)
- **Conditions:** Zero-shot, 3-shot, 8-shot, fine-tuned

## Citation

Extends Kim & Lu (2024) methodology with systematic consistency analysis.

## Notes

- Results are saved in `scripts/RQ1/evaluation_results/` and `scripts/RQ2/evaluation_results/`
- Fine-tuning requires OpenAI API access and credits
- Full study design available in `STUDY_DESIGN_FINAL.md` and `RQ2_STUDY_DESIGN_REVISED.md`
