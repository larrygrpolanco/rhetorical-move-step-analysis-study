"""
Pilot Study Runner
Manually edit the configuration section below to run different conditions and models.
"""

import os
import sys
from pathlib import Path

# Add parent directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from xml_extractor import extract_from_xml, format_article_for_llm
from llm_handler import call_gpt_35, call_gpt_4, call_claude_sonnet


# ============================================================================
# CONFIGURATION - EDIT THESE VALUES
# ============================================================================

CONDITION = "a1_zero_shot"          # Which condition (matches prompt filename)
LLM_FUNCTION = call_gpt_35          # Which LLM function to use
ARTICLES = range(1,2)             # Which articles to process

# ============================================================================


def load_prompt(condition):
    """Load the prompt text for the given condition."""
    prompt_file = Path(f"prompts/{condition}.txt")
    if not prompt_file.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_file}")
    
    with open(prompt_file, 'r', encoding='utf-8') as f:
        return f.read()


def ensure_directory(path):
    """Create directory if it doesn't exist."""
    Path(path).mkdir(parents=True, exist_ok=True)


def split_into_paragraphs(text):
    """
    Split text into paragraphs (double newline separated).
    
    Args:
        text: Full article text
        
    Returns:
        List of paragraph strings
    """
    # Split on double newlines
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    return paragraphs


def process_article(article_num, condition, prompt, llm_function):
    """
    Process a single article through the LLM pipeline.
    Processes paragraph-by-paragraph to avoid overwhelming the LLM.
    
    Args:
        article_num: Article number (e.g., 1 for text001.xml)
        condition: Condition name (e.g., "a1_zero_shot")
        prompt: The prompt text
        llm_function: The LLM function to call
    """
    # Format article ID
    article_id = f"text{article_num:03d}"
    xml_path = f"Annotated_Dataset/{article_id}.xml"
    
    print(f"Processing {article_id}...")
    
    # Extract article text
    try:
        article = extract_from_xml(xml_path)
        article_text = format_article_for_llm(article)
    except Exception as e:
        print(f"  ERROR extracting {article_id}: {e}")
        return
    
    # Split into paragraphs
    paragraphs = split_into_paragraphs(article_text)
    print(f"  Found {len(paragraphs)} paragraphs")
    
    # Process each paragraph
    all_responses = []
    folder_name = None
    
    for i, paragraph in enumerate(paragraphs, 1):
        print(f"    Processing paragraph {i}/{len(paragraphs)}...", end=" ")
        
        try:
            response_text, folder_name = llm_function(prompt, paragraph)
            all_responses.append(response_text)
            print("✓")
        except Exception as e:
            print(f"ERROR: {e}")
            all_responses.append(f"[ERROR processing paragraph {i}]")
    
    # Concatenate all responses
    final_response = "\n\n".join(all_responses)
    
    # Create output directory
    output_dir = Path(f"pilot_outputs/{condition}")
    ensure_directory(output_dir)
    
    # Save full input (all paragraphs)
    input_file = output_dir / f"{article_id}_input.txt"
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(article_text)
    
    # Save concatenated output
    output_file = output_dir / f"{article_id}_{condition}.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_response)
    
    print(f"  ✓ Saved to {output_file}")


def main():
    """Main execution function."""
    print("=" * 70)
    print(f"Pilot Study: {CONDITION}")
    print(f"LLM: {LLM_FUNCTION.__name__}")
    print(f"Articles: {min(ARTICLES)} to {max(ARTICLES)}")
    print("=" * 70)
    print()
    
    # Load prompt
    try:
        prompt = load_prompt(CONDITION)
        print(f"✓ Loaded prompt from prompts/{CONDITION}.txt")
        print()
    except Exception as e:
        print(f"ERROR: {e}")
        return
    
    # Process each article
    for article_num in ARTICLES:
        process_article(article_num, CONDITION, prompt, LLM_FUNCTION)
    
    print()
    print("=" * 70)
    print("Done!")
    print("=" * 70)


if __name__ == "__main__":
    main()
