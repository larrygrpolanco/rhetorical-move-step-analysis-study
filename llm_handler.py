"""
LLM Handler - Condition-Specific API Calls
===========================================
Clean, simple functions for each experimental condition.

Each function returns (response_text, model_name) tuple.

Author: Larry Grullon-Polanco
Date: 2025
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic

# Load environment variables
load_dotenv()


def call_zero_shot(prompt, article_text):
    """
    Zero-shot: Prompt + article text only.

    Args:
        prompt: System prompt with instructions
        article_text: Article to annotate (plain text)

    Returns:
        (response_text, model_name)
    """
    client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=4096,
        temperature=1.0,
        messages=[{"role": "user", "content": f"{prompt}\n\n{article_text}"}],
    )

    response_text = response.content[0].text
    model_name = "claude-sonnet-4-5"

    return response_text, model_name


def call_three_shot(prompt, article_text, examples):
    """
    3-shot: Prompt + 3 examples + article text.

    Args:
        prompt: System prompt with instructions
        article_text: Article to annotate (plain text)
        examples: List of 3 example dicts with 'input' and 'output' keys

    Returns:
        (response_text, model_name)
    """
    client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    # Build message with examples
    content = f"{prompt}\n\n"
    content += "Here are 3 examples of correct annotations:\n\n"

    for i, example in enumerate(examples, 1):
        content += f"Example {i}:\n"
        content += f"{example['input']}\n\n"
        content += f"Correct annotation:\n"
        content += f"{example['output']}\n\n"

    content += "Now annotate this article:\n"
    content += article_text

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=4096,
        temperature=1.0,
        messages=[{"role": "user", "content": content}],
    )

    response_text = response.content[0].text
    model_name = "claude-sonnet-4-5"

    return response_text, model_name


def call_eight_shot(prompt, article_text, examples):
    """
    8-shot: Prompt + 8 examples + article text.

    Args:
        prompt: System prompt with instructions
        article_text: Article to annotate (plain text)
        examples: List of 8 example dicts with 'input' and 'output' keys

    Returns:
        (response_text, model_name)
    """
    client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    # Build message with examples
    content = f"{prompt}\n\n"
    content += "Here are 8 examples of correct annotations:\n\n"

    for i, example in enumerate(examples, 1):
        content += f"Example {i}:\n"
        content += f"{example['input']}\n\n"
        content += f"Correct annotation:\n"
        content += f"{example['output']}\n\n"

    content += "Now annotate this article:\n"
    content += article_text

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=4096,
        temperature=1.0,
        messages=[{"role": "user", "content": content}],
    )

    response_text = response.content[0].text
    model_name = "claude-sonnet-4-5"

    return response_text, model_name


def call_fine_tuned(prompt, article_text, model_id):
    """
    Fine-tuned model: Prompt + article text (examples baked into model).

    NOTE: This is a placeholder. Fine-tuning will be implemented separately.

    Args:
        prompt: System prompt with instructions
        article_text: Article to annotate (plain text)
        model_id: Fine-tuned model ID from OpenAI

    Returns:
        (response_text, model_name)
    """
    # TODO: Implement when fine-tuning is ready
    raise NotImplementedError(
        "Fine-tuning not yet implemented. Focus on zero-shot and few-shot first."
    )
