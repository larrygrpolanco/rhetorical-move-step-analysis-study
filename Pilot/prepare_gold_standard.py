"""
Gold Standard Preparation Script
==================================
Extracts annotated sentences from CaRS-50 XML files into JSON format for evaluation.

This script runs ONCE to prepare the gold standard data that will be compared
against LLM predictions.

Output format matches parser output for consistent evaluation:
- Each sentence gets a sentence_num (1, 2, 3, ...)
- Sentence text preserved for verification
- Tags converted to list format to handle multi-tag sentences
- Move extracted from step code (e.g., "1b" -> move "1")

Author: Larry Grullon-Polanco
Date: 2025
"""

import json
from pathlib import Path
from xml_extractor import extract_from_xml


def extract_move_from_step(step_code):
    """
    Extract move number from step code.

    Examples:
        "1a" -> "1"
        "2b" -> "2"
        "3c" -> "3"

    Args:
        step_code: Step code like "1a", "2b", etc.

    Returns:
        Move number as string ("1", "2", or "3")
    """
    return step_code[0] if step_code else None


def prepare_gold_standard_for_article(xml_path, output_path):
    """
    Convert a single XML file to gold standard JSON format.

    Args:
        xml_path: Path to input XML file
        output_path: Path to output JSON file

    Returns:
        Dictionary with article metadata and sentence count
    """
    # Extract from XML
    article = extract_from_xml(xml_path)

    # Build gold standard structure
    gold_standard = []

    for sentence_num, sentence in enumerate(article["sentences"], start=1):
        # Handle multi-tag sentences (if they exist in format "1a, 2b")
        step_code = sentence["step"]
        tags = (
            [tag.strip() for tag in step_code.split(",")]
            if "," in step_code
            else [step_code]
        )

        # Extract move from first tag (primary tag)
        primary_tag = tags[0]
        move = extract_move_from_step(primary_tag)

        gold_entry = {
            "sentence_num": sentence_num,
            "sentence_id": sentence["sentence_id"],
            "text": sentence["text"],
            "tags": tags,
            "primary_tag": primary_tag,
            "move": move,
        }

        gold_standard.append(gold_entry)

    # Save to JSON
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(gold_standard, f, indent=2, ensure_ascii=False)

    # Return metadata
    return {
        "article_id": article["article_id"],
        "title": article["title"],
        "sentence_count": len(gold_standard),
        "output_path": str(output_path),
    }


def prepare_all_gold_standards():
    """
    Process all XML files in the Annotated_Dataset directory.
    Creates gold standard JSON files in gold_standard/ directory.
    """
    xml_dir = Path("Annotated_Dataset")
    output_dir = Path("gold_standard")

    print("=" * 70)
    print("Gold Standard Preparation")
    print("=" * 70)
    print()

    xml_files = sorted(xml_dir.glob("*.xml"))
    results = []

    for xml_file in xml_files:
        article_id = xml_file.stem
        output_file = output_dir / f"{article_id}.json"

        print(f"Processing {article_id}...", end=" ")

        try:
            metadata = prepare_gold_standard_for_article(xml_file, output_file)
            results.append(metadata)
            print(f"✓ ({metadata['sentence_count']} sentences)")
        except Exception as e:
            print(f"✗ ERROR: {e}")

    print()
    print("=" * 70)
    print(f"Processed {len(results)} articles")
    print(f"Output directory: {output_dir}")
    print("=" * 70)

    # Save summary
    summary_file = output_dir / "_summary.json"
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(
            {"total_articles": len(results), "articles": results},
            f,
            indent=2,
            ensure_ascii=False,
        )

    print(f"\nSummary saved to: {summary_file}")


if __name__ == "__main__":
    prepare_all_gold_standards()
