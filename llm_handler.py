"""
LLM Handler - Condition-Specific API Calls
===========================================
Clean, simple functions for each experimental condition.

Message Structure:
- System message: Contains the annotation instructions (system_prompt.txt)
- User/Assistant pairs: For few-shot examples (3-shot, 8-shot)
- Final User message: The article to annotate

Each function returns (response_text, model_name) tuple.

Author: Larry Grullon-Polanco
Date: 2025
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Model configuration
MODEL_NAME = "gpt-4.1-2025-04-14"  # Only model available for fine-tuning


def call_zero_shot(prompt, article_text):
    """
    Zero-shot: System prompt + article text only.

    Message structure:
        System: [annotation instructions]
        User: [article to annotate]

    Args:
        prompt: System prompt with annotation instructions
        article_text: Article to annotate (plain text)

    Returns:
        (response_text, model_name)
    """
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": article_text},
    ]

    response = client.chat.completions.create(
        model=MODEL_NAME, messages=messages, temperature=1.0, max_tokens=4096
    )

    response_text = response.choices[0].message.content

    return response_text, MODEL_NAME


def call_three_shot(prompt, article_text, examples):
    """
    3-shot: System prompt + 3 example pairs + article text.

    Message structure:
        System: [annotation instructions]
        User: [example 1 input]
        Assistant: [example 1 output]
        User: [example 2 input]
        Assistant: [example 2 output]
        User: [example 3 input]
        Assistant: [example 3 output]
        User: [article to annotate]

    Args:
        prompt: System prompt with annotation instructions
        article_text: Article to annotate (plain text)
        examples: List of 3 example dicts with 'input' and 'output' keys

    Returns:
        (response_text, model_name)
    """
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    # Start with system message
    messages = [{"role": "system", "content": prompt}]

    # Add 3 example pairs (user → assistant)
    for example in examples[:3]:
        messages.append({"role": "user", "content": example["input"]})
        messages.append({"role": "assistant", "content": example["output"]})

    # Add the article to annotate
    messages.append({"role": "user", "content": article_text})

    response = client.chat.completions.create(
        model=MODEL_NAME, messages=messages, temperature=1.0, max_tokens=4096
    )

    response_text = response.choices[0].message.content

    return response_text, MODEL_NAME


def call_eight_shot(prompt, article_text, examples):
    """
    8-shot: System prompt + 8 example pairs + article text.

    Message structure:
        System: [annotation instructions]
        User: [example 1 input]
        Assistant: [example 1 output]
        ... (repeat for 8 examples)
        User: [article to annotate]

    Args:
        prompt: System prompt with annotation instructions
        article_text: Article to annotate (plain text)
        examples: List of 8 example dicts with 'input' and 'output' keys

    Returns:
        (response_text, model_name)
    """
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    # Start with system message
    messages = [{"role": "system", "content": prompt}]

    # Add 8 example pairs (user → assistant)
    for example in examples[:8]:
        messages.append({"role": "user", "content": example["input"]})
        messages.append({"role": "assistant", "content": example["output"]})

    # Add the article to annotate
    messages.append({"role": "user", "content": article_text})

    response = client.chat.completions.create(
        model=MODEL_NAME, messages=messages, temperature=1.0, max_tokens=4096
    )

    response_text = response.choices[0].message.content

    return response_text, MODEL_NAME


def call_fine_tuned(prompt, article_text, model_id):
    """
    Fine-tuned model: System prompt + article text.
    Examples are baked into the model weights during fine-tuning.

    Message structure:
        System: [annotation instructions]
        User: [article to annotate]

    Args:
        prompt: System prompt with annotation instructions
        article_text: Article to annotate (plain text)
        model_id: Fine-tuned model ID from OpenAI (e.g., "ft:gpt-4.1:...")

    Returns:
        (response_text, model_name)
    """
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": article_text},
    ]

    response = client.chat.completions.create(
        model=model_id,  # Use the fine-tuned model ID
        messages=messages,
        temperature=1.0,
        max_tokens=4096,
    )

    response_text = response.choices[0].message.content

    return response_text, model_id
