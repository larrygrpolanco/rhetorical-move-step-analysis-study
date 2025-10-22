"""
Reference Code: LLM API Calls for Few-Shot vs Fine-Tuning
==========================================================
OUTDATED!

This is REFERENCE CODE showing how to structure API calls for:
- Zero-shot (no examples)
- Few-shot (3-shot, 8-shot, or N-shot)
- Fine-tuned model

Adapt this to your actual codebase schema.
"""

from openai import OpenAI
from typing import List, Dict, Optional


# ==============================================================================
# BASIC STRUCTURE: Understanding the Messages Array
# ==============================================================================

def explain_messages_structure():
    """
    The OpenAI API uses a 'messages' array where:
    - Each message has a 'role' (system/user/assistant) and 'content' (text)
    - Conversation flows: system → user → assistant → user → assistant → ...
    
    For annotation tasks:
    - System: Your main prompt/instructions
    - User: Article text to annotate
    - Assistant: The gold standard annotations
    
    For few-shot learning, you show examples by alternating user/assistant messages.
    """
    pass


# ==============================================================================
# ZERO-SHOT: No Examples
# ==============================================================================

def zero_shot_call(
    prompt: str,
    article_text: str,
    model: str = "gpt-4-0613",
    temperature: float = 1.0,
    max_tokens: int = 4096
) -> str:
    """
    Zero-shot annotation: Just prompt + article, no examples.
    
    Args:
        prompt: Your main instruction prompt (e.g., "Annotate this article...")
        article_text: The article to annotate
        model: GPT model to use
        temperature: Sampling temperature (1.0 = default variability)
        max_tokens: Maximum response length
    
    Returns:
        Model's annotation output as string
    """
    client = OpenAI()  # Assumes OPENAI_API_KEY is set in environment
    
    messages = [
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user", 
            "content": article_text
        }
    ]
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    return response.choices[0].message.content


# ==============================================================================
# FEW-SHOT: With Examples (3-shot, 8-shot, or N-shot)
# ==============================================================================

def few_shot_call(
    prompt: str,
    article_text: str,
    examples: List[Dict[str, str]],
    model: str = "gpt-4-0613",
    temperature: float = 1.0,
    max_tokens: int = 4096
) -> str:
    """
    Few-shot annotation: Prompt + examples + article.
    
    The 'examples' list provides exemplar annotations to help the model
    understand the task through demonstration.
    
    Args:
        prompt: Your main instruction prompt
        article_text: The article to annotate
        examples: List of example dicts, each with:
                  - 'article': example article text
                  - 'annotation': gold standard annotation for that article
        model: GPT model to use
        temperature: Sampling temperature
        max_tokens: Maximum response length
    
    Returns:
        Model's annotation output as string
    
    Example usage:
        examples = [
            {
                'article': "Example article 1 text...",
                'annotation': "[M1_S1] First sentence.\n[M1_S2] Second sentence."
            },
            {
                'article': "Example article 2 text...",
                'annotation': "[M2_S1a] Another sentence."
            },
            # ... more examples
        ]
        
        result = few_shot_call(prompt, article_text, examples)
    """
    client = OpenAI()
    
    # Start with system message (your prompt)
    messages = [
        {
            "role": "system",
            "content": prompt
        }
    ]
    
    # Add examples as user/assistant pairs
    # This shows the model: "When you see THIS input, you should output THIS"
    for example in examples:
        messages.append({
            "role": "user",
            "content": example['article']
        })
        messages.append({
            "role": "assistant", 
            "content": example['annotation']
        })
    
    # Finally, add the actual article to annotate
    messages.append({
        "role": "user",
        "content": article_text
    })
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    return response.choices[0].message.content


# ==============================================================================
# CONVENIENCE WRAPPERS: 3-Shot and 8-Shot
# ==============================================================================

def three_shot_call(
    prompt: str,
    article_text: str,
    example_1: Dict[str, str],
    example_2: Dict[str, str],
    example_3: Dict[str, str],
    **kwargs
) -> str:
    """
    3-shot annotation: Prompt + 3 examples + article.
    
    This is just a convenience wrapper around few_shot_call.
    """
    examples = [example_1, example_2, example_3]
    return few_shot_call(prompt, article_text, examples, **kwargs)


def eight_shot_call(
    prompt: str,
    article_text: str,
    examples_list: List[Dict[str, str]],  # Should have exactly 8 examples
    **kwargs
) -> str:
    """
    8-shot annotation: Prompt + 8 examples + article.
    
    Args:
        examples_list: Must contain exactly 8 example dicts
    """
    assert len(examples_list) == 8, "Must provide exactly 8 examples"
    return few_shot_call(prompt, article_text, examples_list, **kwargs)


# ==============================================================================
# FINE-TUNED MODEL: Using Your Custom Model
# ==============================================================================

def fine_tuned_call(
    prompt: str,
    article_text: str,
    fine_tuned_model_id: str,  # e.g., "ft:gpt-4-0613:your-org:model-name:abc123"
    temperature: float = 1.0,
    max_tokens: int = 4096
) -> str:
    """
    Fine-tuned model annotation: Same structure as zero-shot, but uses your
    fine-tuned model which has the examples "baked in" to its weights.
    
    Args:
        prompt: Your main instruction prompt (same as zero-shot)
        article_text: The article to annotate
        fine_tuned_model_id: The ID of your fine-tuned model from OpenAI
                            (you get this after fine-tuning completes)
        temperature: Sampling temperature
        max_tokens: Maximum response length
    
    Returns:
        Model's annotation output as string
    
    Note:
        Fine-tuning must be done separately via OpenAI's API or dashboard.
        This function just uses the resulting model.
    """
    client = OpenAI()
    
    # SAME structure as zero-shot - no examples needed!
    # The examples are already in the model's weights from fine-tuning
    messages = [
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": article_text
        }
    ]
    
    response = client.chat.completions.create(
        model=fine_tuned_model_id,  # <-- Only difference: custom model ID
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    return response.choices[0].message.content


# ==============================================================================
# EXAMPLE: Loading Examples from Your Data
# ==============================================================================

def load_examples_from_files(
    training_article_files: List[str],
    training_annotation_files: List[str],
    n_examples: int = 3
) -> List[Dict[str, str]]:
    """
    Helper function: Load examples from your actual data files.
    
    This is PSEUDOCODE - adapt to your actual file structure.
    
    Args:
        training_article_files: Paths to training article text files
        training_annotation_files: Paths to corresponding annotation files
        n_examples: How many examples to use (3, 8, etc.)
    
    Returns:
        List of example dicts ready for few_shot_call()
    """
    examples = []
    
    for i in range(n_examples):
        # Read article text
        with open(training_article_files[i], 'r') as f:
            article = f.read()
        
        # Read gold standard annotation
        with open(training_annotation_files[i], 'r') as f:
            annotation = f.read()
        
        examples.append({
            'article': article,
            'annotation': annotation
        })
    
    return examples


# ==============================================================================
# EXAMPLE: Complete Workflow for Your Study
# ==============================================================================

def example_workflow():
    """
    Example showing how you might use these functions in your study.
    
    This shows the pattern - adapt to your actual data structure.
    """
    
    # Your prompt (same for all conditions)
    prompt = """You are an expert at rhetorical move-step annotation.
Annotate the following research article introduction using the CaRS framework.
Output format: [TAG] sentence text
Available tags: [M1_S1], [M1_S2], [M2_S1a], etc.
"""
    
    # The article you want to annotate
    test_article = "This study investigates..."  # Your actual article text
    
    # ----- CONDITION 1: ZERO-SHOT -----
    print("Running zero-shot...")
    result_zero = zero_shot_call(
        prompt=prompt,
        article_text=test_article,
        model="gpt-4-0613",
        temperature=1.0
    )
    
    # ----- CONDITION 2: 3-SHOT -----
    print("Running 3-shot...")
    
    # Load your 3 training examples (adapt to your data structure)
    examples_3 = [
        {'article': "Training article 1...", 'annotation': "[M1_S1] Sentence."},
        {'article': "Training article 2...", 'annotation': "[M1_S2] Sentence."},
        {'article': "Training article 3...", 'annotation': "[M2_S1a] Sentence."},
    ]
    
    result_3shot = few_shot_call(
        prompt=prompt,
        article_text=test_article,
        examples=examples_3,
        model="gpt-4-0613",
        temperature=1.0
    )
    
    # ----- CONDITION 3: 8-SHOT -----
    print("Running 8-shot...")
    
    # Load your 8 training examples
    examples_8 = [
        {'article': "Training article 1...", 'annotation': "[M1_S1] Sentence."},
        # ... 7 more examples
    ]
    
    result_8shot = few_shot_call(
        prompt=prompt,
        article_text=test_article,
        examples=examples_8,
        model="gpt-4-0613",
        temperature=1.0
    )
    
    # ----- CONDITION 4: FINE-TUNED -----
    print("Running fine-tuned model...")
    
    result_finetuned = fine_tuned_call(
        prompt=prompt,
        article_text=test_article,
        fine_tuned_model_id="ft:gpt-4-0613:your-org:cars-bio:abc123",  # Your model ID
        temperature=1.0
    )
    
    # Save all results
    # ... your evaluation code ...


# ==============================================================================
# KEY TAKEAWAYS
# ==============================================================================

"""
IMPORTANT DIFFERENCES:

1. ZERO-SHOT:
   messages = [system, user]
   - Fast, cheap
   - Lower accuracy

2. FEW-SHOT (3 or 8):
   messages = [system, user, assistant, user, assistant, ..., user]
   - Slower (more tokens)
   - More expensive (paying for example tokens every time)
   - Better than zero-shot
   - Still not as good as fine-tuned

3. FINE-TUNED:
   messages = [system, user]  (same as zero-shot!)
   - Fast, cheap (no example tokens)
   - Much better accuracy
   - Examples are "baked in" to model weights
   - One-time training cost

YOUR STUDY:
- Use the SAME prompt for all conditions
- Use the SAME test articles for all conditions
- Use FIXED examples for 3-shot and 8-shot (don't change between runs)
- Run each condition 30 times with temperature=1.0 to measure consistency
"""


# ==============================================================================
# COST ESTIMATION
# ==============================================================================

def estimate_costs():
    """
    Quick cost estimation for your reference.
    
    GPT-4 pricing (as of 2024):
    - Input: $0.03 per 1K tokens
    - Output: $0.06 per 1K tokens
    """
    
    # Assumptions
    prompt_tokens = 500
    article_tokens = 800
    annotation_output_tokens = 400
    
    # Zero-shot cost per call
    zero_shot_input = prompt_tokens + article_tokens  # 1,300 tokens
    zero_shot_cost = (zero_shot_input * 0.03 / 1000) + (annotation_output_tokens * 0.06 / 1000)
    print(f"Zero-shot cost per call: ${zero_shot_cost:.3f}")
    
    # 3-shot cost per call (each example ~800 input + 400 output tokens)
    three_shot_input = prompt_tokens + (3 * 1200) + article_tokens  # 4,900 tokens
    three_shot_cost = (three_shot_input * 0.03 / 1000) + (annotation_output_tokens * 0.06 / 1000)
    print(f"3-shot cost per call: ${three_shot_cost:.3f}")
    
    # 8-shot cost per call
    eight_shot_input = prompt_tokens + (8 * 1200) + article_tokens  # 10,900 tokens
    eight_shot_cost = (eight_shot_input * 0.03 / 1000) + (annotation_output_tokens * 0.06 / 1000)
    print(f"8-shot cost per call: ${eight_shot_cost:.3f}")
    
    # Fine-tuned: same as zero-shot at inference
    print(f"Fine-tuned cost per call: ${zero_shot_cost:.3f} (+ one-time training cost)")
    
    # For 30 runs × 10 test articles
    total_calls = 30 * 10
    print(f"\nFor {total_calls} calls per condition:")
    print(f"  Zero-shot total: ${zero_shot_cost * total_calls:.2f}")
    print(f"  3-shot total: ${three_shot_cost * total_calls:.2f}")
    print(f"  8-shot total: ${eight_shot_cost * total_calls:.2f}")
    print(f"  Fine-tuned total: ${zero_shot_cost * total_calls:.2f}")


if __name__ == "__main__":
    print("This is reference code - adapt to your actual codebase!")
    print("\nCost estimates:")
    estimate_costs()
