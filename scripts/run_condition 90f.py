"""
Run Condition - Main Data Collection Script
============================================
Runs LLM annotation and parsing for a specified condition.

Handles:
- Zero-shot (no examples)
- 3-shot (3 training examples)
- 8-shot (8 training examples)
- Fine-tuned (placeholder for future implementation)

Automatically parses outputs immediately after LLM call.

Author: Larry Grullon-Polanco
Date: 2025
"""

import json
from pathlib import Path
from llm_handler import (
    call_zero_shot,
    call_three_shot,
    call_eight_shot,
    call_fine_tuned,
)
from parse_llm_output import parse_llm_output

# ============================================================================
# CONFIGURATION
# ============================================================================

CONDITION = "fine_tuned"  # Options: zero_shot, three_shot, eight_shot, fine_tuned
DATASET = "test"  # Options: validation, test
RESEARCH_QUESTION = "rq2"  # Options: rq1 (single run), rq2 (consistency)
ARTICLES = range(11, 21)  # Validation: range(1, 11), Test: range(11, 21)
RUNS = range(91, 101)  # RQ1: range(1, 2), RQ2: range(1, 51) or subset

# ============================================================================


def load_prompt():
    """Load the system prompt."""
    prompt_file = Path("prompts/system_prompt.txt")

    if not prompt_file.exists():
        raise FileNotFoundError(f"Prompt not found: {prompt_file}")

    with open(prompt_file, "r", encoding="utf-8") as f:
        return f.read()


def get_output_folder(condition, research_question, dataset, run_num):
    """
    Determine output folder based on research question and run number.

    Returns:
        Path to output folder
    """
    base = Path("outputs") / condition

    if research_question == "rq1":
        # Single run: rq1_validation or rq1_test
        return base / f"rq1_{dataset}"
    else:
        # Consistency runs: rq2_run_01, rq2_run_02, etc.
        return base / f"rq2_run_{run_num:02d}"


def load_article_text(article_num, dataset):
    """
    Load article text from gold standard.

    Args:
        article_num: Article number (e.g., 1, 11, 21)
        dataset: 'validation' or 'test'

    Returns:
        Article text as string
    """
    article_id = f"text{article_num:03d}"
    input_file = Path(f"gold_standard/CaRS-50/{dataset}/input/{article_id}.txt")

    if not input_file.exists():
        raise FileNotFoundError(f"Article not found: {input_file}")

    with open(input_file, "r", encoding="utf-8") as f:
        return f.read()


def load_few_shot_examples(condition):
    """
    Load few-shot examples for 3-shot or 8-shot conditions.

    Args:
        condition: 'three_shot' or 'eight_shot'

    Returns:
        List of example dicts with 'input' and 'output' keys
    """
    # Load the selection file
    selection_file = Path("gold_standard/CaRS-50/train/few_shot_examples.json")

    if not selection_file.exists():
        raise FileNotFoundError(
            f"Few-shot examples not found: {selection_file}\n"
            "Run setup_few_shot_examples.py first!"
        )

    with open(selection_file, "r", encoding="utf-8") as f:
        selections = json.load(f)

    # Get the article IDs for this condition
    if condition == "three_shot":
        article_ids = selections["three_shot"]["article_ids"]
    elif condition == "eight_shot":
        article_ids = selections["eight_shot"]["article_ids"]
    else:
        raise ValueError(f"Invalid condition for few-shot: {condition}")

    # Load the actual example texts
    examples = []
    for article_id in article_ids:
        # Load input (plain text)
        input_file = Path(f"gold_standard/CaRS-50/train/input/{article_id}.txt")
        with open(input_file, "r", encoding="utf-8") as f:
            input_text = f.read()

        # Load output (annotated format)
        output_file = Path(f"gold_standard/CaRS-50/train/output/{article_id}.txt")
        with open(output_file, "r", encoding="utf-8") as f:
            output_text = f.read()

        examples.append(
            {"article_id": article_id, "input": input_text, "output": output_text}
        )

    return examples


def call_llm(condition, prompt, article_text, examples=None):
    """
    Call appropriate LLM function based on condition.

    Args:
        condition: Which condition to run
        prompt: System prompt
        article_text: Article to annotate
        examples: Few-shot examples (if applicable)

    Returns:
        (response_text, model_name)
    """
    if condition == "zero_shot":
        return call_zero_shot(prompt, article_text)

    elif condition == "three_shot":
        if not examples:
            raise ValueError("Examples required for 3-shot condition")
        return call_three_shot(prompt, article_text, examples[:3])

    elif condition == "eight_shot":
        if not examples:
            raise ValueError("Examples required for 8-shot condition")
        return call_eight_shot(prompt, article_text, examples[:8])

    elif condition == "fine_tuned":
        return call_fine_tuned(prompt, article_text, model_id="placeholder")

    else:
        raise ValueError(f"Unknown condition: {condition}")


def process_article(
    article_num, run_num, condition, dataset, research_question, prompt, examples=None
):
    """
    Process a single article: call LLM, save raw output, parse, save parsed.

    Args:
        article_num: Article number
        run_num: Run number (for RQ2)
        condition: Experimental condition
        dataset: validation or test
        research_question: rq1 or rq2
        prompt: System prompt
        examples: Few-shot examples (if applicable)
    """
    article_id = f"text{article_num:03d}"

    # Load article text
    article_text = load_article_text(article_num, dataset)

    # Call LLM
    response_text, model_name = call_llm(condition, prompt, article_text, examples)

    # Determine output folder
    output_folder = get_output_folder(condition, research_question, dataset, run_num)

    # Save raw output
    raw_dir = output_folder / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    raw_file = raw_dir / f"{article_id}.txt"

    with open(raw_file, "w", encoding="utf-8") as f:
        f.write(response_text)

    # Parse output
    parsed_sentences, stats = parse_llm_output(response_text, article_id)

    # Save parsed JSON
    parsed_dir = output_folder / "parsed"
    parsed_dir.mkdir(parents=True, exist_ok=True)
    parsed_file = parsed_dir / f"{article_id}.json"

    parsed_data = {
        "article_id": article_id,
        "condition": condition,
        "dataset": dataset,
        "research_question": research_question,
        "run_number": run_num,
        "model": model_name,
        "sentences": parsed_sentences,
        "parse_stats": stats.summary(),
    }

    with open(parsed_file, "w", encoding="utf-8") as f:
        json.dump(parsed_data, f, indent=2, ensure_ascii=False)

    return stats


def main():
    """Main execution."""

    print("=" * 70)
    print(f"Running Condition: {CONDITION}")
    print(f"Dataset: {DATASET}")
    print(f"Research Question: {RESEARCH_QUESTION}")
    print(f"Articles: {min(ARTICLES)}-{max(ARTICLES)}")
    print(f"Runs: {min(RUNS)}-{max(RUNS)}")
    print("=" * 70)
    print()

    # Load prompt
    prompt = load_prompt()
    print(f"✓ Loaded prompt from prompts/system_prompt.txt")

    # Load few-shot examples if needed
    examples = None
    if CONDITION in ["three_shot", "eight_shot"]:
        examples = load_few_shot_examples(CONDITION)
        print(f"✓ Loaded {len(examples)} few-shot examples")

    print()

    # Process all runs and articles
    total_processed = 0

    for run_num in RUNS:
        if RESEARCH_QUESTION == "rq2":
            print(f"RUN {run_num:02d}/{max(RUNS)}")
            print("-" * 70)

        for article_num in ARTICLES:
            article_id = f"text{article_num:03d}"
            print(f"  Processing {article_id}...", end=" ", flush=True)

            try:
                stats = process_article(
                    article_num,
                    run_num,
                    CONDITION,
                    DATASET,
                    RESEARCH_QUESTION,
                    prompt,
                    examples,
                )
                print(f"✓ ({stats.parsed_sentences} sentences)")
                total_processed += 1

            except Exception as e:
                print(f"✗ ERROR: {e}")

        if RESEARCH_QUESTION == "rq2":
            print()

    print("=" * 70)
    print(f"COMPLETE: Processed {total_processed} articles")
    print("=" * 70)


if __name__ == "__main__":
    main()
