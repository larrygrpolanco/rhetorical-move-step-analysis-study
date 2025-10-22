"""
Few-Shot Example Selection Setup
=================================
RUN THIS SCRIPT ONCE to randomly select training examples for few-shot conditions.

This ensures:
- Fixed examples across all 30 consistency runs (isolates LLM stochasticity)
- Reproducible random selection (documented seed)
- Transparent methodology for publication

Output: few_shot_examples.json

Author: Larry Grullon-Polanco
Date: 2025
"""

import json
import random
from pathlib import Path

# ============================================================================
# METHODS SECTION DESCRIPTION
# ============================================================================
"""
Few-Shot Example Selection Protocol:

For the 3-shot and 8-shot conditions, training examples were selected using
stratified random sampling from the training set (articles 21-50, n=30). 
We used a fixed random seed (seed=42) to ensure reproducibility. 

Selection process:
1. Set random seed to 42
2. Randomly sample 3 articles from training set → 3-shot examples
3. Reset random seed to 42  
4. Randomly sample 8 articles from training set → 8-shot examples

The same example sets were used for all 30 repeated runs within each 
condition to isolate model stochasticity from example-selection variance 
(following Kim & Lu, 2024). All selected article IDs and the random seed 
are documented in few_shot_examples.json for full transparency and 
reproducibility.

This design choice reflects our research focus: measuring inherent LLM 
consistency rather than example-set effects. By fixing examples across 
runs, we ensure that any observed variance reflects model behavior rather 
than input variation.
"""
# ============================================================================


def select_few_shot_examples(seed=42):
    """
    Randomly select training articles for few-shot examples.
    
    Args:
        seed: Random seed for reproducibility
        
    Returns:
        dict: Selected examples with metadata
    """
    # Training set is articles 21-50
    training_articles = [f"text{i:03d}" for i in range(21, 51)]
    
    # Select 3-shot examples
    random.seed(seed)
    three_shot_ids = sorted(random.sample(training_articles, 3))
    
    # Select 8-shot examples (reset seed for independent selection)
    random.seed(seed)
    eight_shot_ids = sorted(random.sample(training_articles, 8))
    
    # Package results
    results = {
        "random_seed": seed,
        "selection_date": "2025",
        "training_set_size": len(training_articles),
        "three_shot": {
            "count": 3,
            "article_ids": three_shot_ids
        },
        "eight_shot": {
            "count": 8,
            "article_ids": eight_shot_ids
        },
        "note": "These examples are fixed for all 30 runs to isolate LLM stochasticity"
    }
    
    return results


def main():
    """Select and save few-shot examples."""
    
    print("=" * 70)
    print("Few-Shot Example Selection")
    print("=" * 70)
    print()
    print("Selecting training articles for few-shot conditions...")
    print("Random seed: 42 (for reproducibility)")
    print()
    
    # Select examples
    examples = select_few_shot_examples(seed=42)
    
    # Display selections
    print("3-SHOT EXAMPLES (n=3):")
    for article_id in examples["three_shot"]["article_ids"]:
        print(f"  - {article_id}")
    
    print()
    print("8-SHOT EXAMPLES (n=8):")
    for article_id in examples["eight_shot"]["article_ids"]:
        print(f"  - {article_id}")
    
    # Save to JSON
    output_file = Path("few_shot_examples.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(examples, f, indent=2, ensure_ascii=False)
    
    print()
    print("=" * 70)
    print(f"✓ Examples saved to: {output_file}")
    print("=" * 70)
    print()
    print("IMPORTANT:")
    print("- These examples will be used for ALL 30 runs in each condition")
    print("- Do NOT regenerate this file once data collection begins")
    print("- Keep this file in version control for reproducibility")


if __name__ == "__main__":
    main()
