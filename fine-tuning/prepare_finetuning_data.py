"""
Fine-Tuning Data Preparation Script
====================================
Prepares training data for GPT-4 fine-tuning in OpenAI's JSONL format.

This script:
1. Loads the system prompt (system_prompt.txt)
2. Loads all 30 training articles (text021-050) with their gold annotations
3. Formats each as a training example in OpenAI's format
4. Validates the format rigorously
5. Saves to JSONL file ready for OpenAI UI upload

Format per line:
{"messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
]}

Author: Larry Grullon-Polanco
Date: 2025
Study: LLM Consistency in Rhetorical Move-Step Annotation
"""

import json
from pathlib import Path
from typing import Dict, List


def load_system_prompt(prompt_path: Path) -> str:
    """
    Load the system prompt that will be used in all training examples.
    
    Args:
        prompt_path: Path to system_prompt.txt
        
    Returns:
        System prompt text
    """
    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt = f.read().strip()
    
    if not prompt:
        raise ValueError("System prompt is empty!")
    
    print(f"✓ Loaded system prompt ({len(prompt)} characters)")
    return prompt


def load_training_pair(article_id: str, base_path: Path) -> Dict[str, str]:
    """
    Load input (article) and output (annotations) for one training article.
    
    Args:
        article_id: e.g., "text021"
        base_path: Path to gold_standard/CaRS-50/train/
        
    Returns:
        Dict with 'input' and 'output' keys
    """
    input_path = base_path / "input" / f"{article_id}.txt"
    output_path = base_path / "output" / f"{article_id}.txt"
    
    # Load input (article text)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    with open(input_path, "r", encoding="utf-8") as f:
        input_text = f.read().strip()
    
    # Load output (gold annotations)
    if not output_path.exists():
        raise FileNotFoundError(f"Output file not found: {output_path}")
    
    with open(output_path, "r", encoding="utf-8") as f:
        output_text = f.read().strip()
    
    if not input_text or not output_text:
        raise ValueError(f"Empty file for {article_id}")
    
    return {"input": input_text, "output": output_text}


def create_training_example(
    system_prompt: str, 
    article_text: str, 
    gold_annotations: str
) -> Dict:
    """
    Create a single training example in OpenAI's fine-tuning format.
    
    Args:
        system_prompt: The annotation instructions
        article_text: The article to annotate (user message)
        gold_annotations: The correct annotations (assistant message)
        
    Returns:
        Dict with "messages" key containing the three messages
    """
    return {
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": article_text},
            {"role": "assistant", "content": gold_annotations}
        ]
    }


def validate_training_example(example: Dict, article_id: str) -> None:
    """
    Validate that a training example has the correct format.
    
    Args:
        example: The training example to validate
        article_id: ID for error reporting
        
    Raises:
        ValueError: If format is invalid
    """
    # Check top-level structure
    if "messages" not in example:
        raise ValueError(f"{article_id}: Missing 'messages' key")
    
    messages = example["messages"]
    
    # Check we have exactly 3 messages
    if len(messages) != 3:
        raise ValueError(
            f"{article_id}: Expected 3 messages, got {len(messages)}"
        )
    
    # Check roles are correct
    expected_roles = ["system", "user", "assistant"]
    actual_roles = [msg["role"] for msg in messages]
    
    if actual_roles != expected_roles:
        raise ValueError(
            f"{article_id}: Expected roles {expected_roles}, got {actual_roles}"
        )
    
    # Check all content is non-empty
    for i, msg in enumerate(messages):
        if "content" not in msg:
            raise ValueError(f"{article_id}: Message {i} missing 'content' key")
        
        if not msg["content"] or not isinstance(msg["content"], str):
            raise ValueError(f"{article_id}: Message {i} has invalid content")
    
    # Check that assistant response has tags (basic sanity check)
    assistant_content = messages[2]["content"]
    if not any(tag in assistant_content for tag in ["[1a]", "[1b]", "[1c]", "[2a]", "[2b]", "[3a]", "[3b]"]):
        raise ValueError(
            f"{article_id}: Assistant message doesn't contain expected tags"
        )


def save_jsonl(examples: List[Dict], output_path: Path) -> None:
    """
    Save training examples to JSONL file (one JSON object per line).
    
    Args:
        examples: List of training examples
        output_path: Where to save the JSONL file
    """
    with open(output_path, "w", encoding="utf-8") as f:
        for example in examples:
            # Write each example as a single line of JSON
            f.write(json.dumps(example, ensure_ascii=False) + "\n")
    
    print(f"✓ Saved {len(examples)} examples to: {output_path}")


def print_example_preview(example: Dict, article_id: str) -> None:
    """
    Print a preview of one training example for verification.
    
    Args:
        example: Training example to preview
        article_id: ID for display
    """
    print(f"\n{'='*70}")
    print(f"PREVIEW: {article_id}")
    print('='*70)
    
    messages = example["messages"]
    
    print("\n[SYSTEM] (first 200 chars):")
    print(messages[0]["content"][:200] + "...")
    
    print("\n[USER] (first 200 chars):")
    print(messages[1]["content"][:200] + "...")
    
    print("\n[ASSISTANT] (first 500 chars):")
    print(messages[2]["content"][:500] + "...")
    
    print(f"\n{'='*70}\n")


def calculate_token_estimate(examples: List[Dict]) -> Dict[str, int]:
    """
    Rough token estimate for fine-tuning cost calculation.
    
    OpenAI charges per token during fine-tuning. This gives approximate counts.
    Actual tokenization may differ slightly.
    
    Args:
        examples: List of training examples
        
    Returns:
        Dict with token statistics
    """
    total_chars = 0
    for example in examples:
        for message in example["messages"]:
            total_chars += len(message["content"])
    
    # Rough estimate: 1 token ≈ 4 characters for English text
    estimated_tokens = total_chars // 4
    
    # OpenAI fine-tuning typically trains for 3-5 epochs
    estimated_training_tokens = estimated_tokens * 4  # Conservative estimate
    
    return {
        "total_chars": total_chars,
        "estimated_tokens_per_example": estimated_tokens // len(examples),
        "estimated_total_tokens": estimated_tokens,
        "estimated_training_tokens": estimated_training_tokens
    }


def main():
    """Main execution function."""
    
    print("\n" + "="*70)
    print("FINE-TUNING DATA PREPARATION")
    print("="*70)
    print("\nPreparing training data for GPT-4 fine-tuning...")
    print("Model: gpt-4.1-2025-04-14")
    print("Training articles: text021-text050 (n=30)")
    print()
    
    # Set up paths
    base_dir = Path(__file__).parent
    prompt_path = base_dir / "prompts" / "system_prompt.txt"
    train_path = base_dir / "gold_standard" / "CaRS-50" / "train"
    output_path = base_dir / "finetuning_data.jsonl"
    
    # Step 1: Load system prompt
    print("Step 1: Loading system prompt...")
    system_prompt = load_system_prompt(prompt_path)
    
    # Step 2: Load all 30 training articles
    print("\nStep 2: Loading training articles...")
    training_articles = [f"text{i:03d}" for i in range(21, 51)]
    print(f"Expected articles: {len(training_articles)}")
    
    training_pairs = []
    for article_id in training_articles:
        try:
            pair = load_training_pair(article_id, train_path)
            training_pairs.append((article_id, pair))
            print(f"  ✓ Loaded {article_id}")
        except Exception as e:
            print(f"  ✗ ERROR loading {article_id}: {e}")
            raise
    
    print(f"\n✓ Successfully loaded {len(training_pairs)} article pairs")
    
    # Step 3: Create training examples
    print("\nStep 3: Creating training examples...")
    training_examples = []
    
    for article_id, pair in training_pairs:
        example = create_training_example(
            system_prompt=system_prompt,
            article_text=pair["input"],
            gold_annotations=pair["output"]
        )
        training_examples.append((article_id, example))
    
    print(f"✓ Created {len(training_examples)} training examples")
    
    # Step 4: Validate each example
    print("\nStep 4: Validating training examples...")
    validation_errors = []
    
    for article_id, example in training_examples:
        try:
            validate_training_example(example, article_id)
        except ValueError as e:
            validation_errors.append(f"{article_id}: {e}")
    
    if validation_errors:
        print("\n✗ VALIDATION ERRORS:")
        for error in validation_errors:
            print(f"  - {error}")
        raise ValueError(f"Found {len(validation_errors)} validation errors!")
    
    print(f"✓ All {len(training_examples)} examples validated successfully")
    
    # Step 5: Show preview of first example
    print("\nStep 5: Preview of first training example...")
    print_example_preview(training_examples[0][1], training_examples[0][0])
    
    # Step 6: Calculate token estimates
    print("Step 6: Estimating tokens...")
    examples_only = [ex for _, ex in training_examples]
    token_stats = calculate_token_estimate(examples_only)
    
    print(f"  Total characters: {token_stats['total_chars']:,}")
    print(f"  Estimated tokens/example: {token_stats['estimated_tokens_per_example']:,}")
    print(f"  Estimated total tokens: {token_stats['estimated_total_tokens']:,}")
    print(f"  Estimated training tokens (4 epochs): {token_stats['estimated_training_tokens']:,}")
    print(f"\n  Estimated fine-tuning cost: ~${token_stats['estimated_training_tokens'] * 0.008 / 1000:.2f}")
    print(f"  (Actual cost depends on final token count and epochs)")
    
    # Step 7: Save to JSONL
    print("\nStep 7: Saving to JSONL file...")
    save_jsonl(examples_only, output_path)
    
    # Final summary
    print("\n" + "="*70)
    print("SUCCESS! Fine-tuning data is ready.")
    print("="*70)
    print(f"\nOutput file: {output_path}")
    print(f"Training examples: {len(training_examples)}")
    print(f"File size: {output_path.stat().st_size / 1024:.1f} KB")
    
    print("\n" + "-"*70)
    print("NEXT STEPS:")
    print("-"*70)
    print("1. Review the preview above to confirm formatting")
    print("2. Open the JSONL file and spot-check a few examples")
    print("3. Go to: https://platform.openai.com/finetune")
    print("4. Click 'Create' and upload finetuning_data.jsonl")
    print("5. Use model: gpt-4.1-2025-04-14")
    print("6. Use default hyperparameters (epochs: auto, batch: auto)")
    print("7. Start fine-tuning and wait for completion (~30-60 min)")
    print("8. Note the fine-tuned model ID (e.g., ft:gpt-4.1:...)")
    print("9. Update llm_handler.py with the model ID")
    print("10. Run Phase 2 evaluation: python run_condition.py A4")
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        raise
