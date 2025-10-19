"""
LLM Handler Module
Simple functions to call different LLMs for the pilot study.
Each function returns (response_text, folder_name)
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic

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


def call_gpt_5(prompt, text):
    """
    Call GPT-5 with the given prompt and text.

    Args:
        prompt: The system/instruction prompt
        text: The article text to annotate

    Returns:
        tuple: (response_text, folder_name)
    """
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    response = client.responses.create(
        model="gpt-5-2025-08-07", input=prompt + "\n\n" + text
    )

    response_text = response.output_text
    folder_name = "gpt-5"

    return response_text, folder_name


def call_claude_sonnet45(prompt, text):
    """
    Call Claude Sonnet 4.5 with the given prompt and text.

    Args:
        prompt: The system/instruction prompt
        text: The article text to annotate

    Returns:
        tuple: (response_text, folder_name)
    """

    client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=2048,
        messages=[
            {
                "role": "user",
                "content": f"{prompt} + \n\n + {text}",
            },
        ],
    )

    response_text = response.content[0].text
    folder_name = "claude-sonnet-4-5"

    return response_text, folder_name


# Add more LLM functions here as needed
# def call_llama(prompt, text):
#     ...
