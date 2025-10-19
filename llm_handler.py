"""
LLM Handler Module
Simple functions to call different LLMs for the pilot study.
Each function returns (response_text, folder_name)
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()


def call_gpt_5_mini(prompt, text):
    """
    Call GPT-5 mini with the given prompt and text.

    Args:
        prompt: The system/instruction prompt
        text: The article text to annotate

    Returns:
        tuple: (response_text, folder_name)
    """
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    response = client.responses.create(
        model="gpt-5-mini-2025-08-07", input=prompt + "\n\n" + text
    )

    response_text = response.output_text
    folder_name = "gpt-5mini"

    return response_text, folder_name


def call_gpt_4(prompt, text):
    """
    Call GPT-4 with the given prompt and text.

    Args:
        prompt: The system/instruction prompt
        text: The article text to annotate

    Returns:
        tuple: (response_text, folder_name)
    """
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text},
        ],
        temperature=1.0,
        max_tokens=2048,
    )

    response_text = response.choices[0].message.content
    folder_name = "gpt-4"

    return response_text, folder_name


def call_claude_sonnet(prompt, text):
    """
    Call Claude Sonnet 4.5 with the given prompt and text.

    Args:
        prompt: The system/instruction prompt
        text: The article text to annotate

    Returns:
        tuple: (response_text, folder_name)
    """
    import anthropic

    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2048,
        system=prompt,
        messages=[{"role": "user", "content": text}],
    )

    response_text = response.content[0].text
    folder_name = "claude-sonnet-4-5"

    return response_text, folder_name


# Add more LLM functions here as needed
# def call_llama(prompt, text):
#     ...
