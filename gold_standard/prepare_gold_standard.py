"""
Gold Standard Preparation
==========================
Converts CaRS-50 XML files into three clean formats ready for use.

Splits:
  - Validation: Articles 1-10  (prompt development)
  - Test:       Articles 11-20 (final evaluation)
  - Train:      Articles 21-50 (fine-tuning)

Output Formats:
  - input/   Plain text, one sentence per line
  - output/  [tag] sentence format (for few-shot examples & training)
  - json/    Structured data with metadata (for evaluation)

Usage:
    python prepare_gold_standard.py

Author: Larry Grullon-Polanco
Date: 2025
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path


def extract_move(step_code):
    """Extract move number from step code (e.g., '1b' -> '1')."""
    return step_code[0] if step_code else None


def parse_xml(xml_path):
    """
    Parse a single XML file and extract article data.
    
    Returns:
        dict: Article with metadata and sentences
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    # Extract metadata
    article = {
        "article_id": root.find("fulltextID").text,
        "title": root.find("title").text,
        "sentences": []
    }
    
    # Extract all sentences from all paragraphs
    fulltext = root.find("fulltext")
    sentence_num = 1
    
    for paragraph in fulltext.findall("paragraph"):
        for sentence in paragraph.findall("sentence"):
            article["sentences"].append({
                "sentence_num": sentence_num,
                "sentence_id": sentence.find("sentenceID").text,
                "text": sentence.find("text").text,
                "step": sentence.find("step").text,
                "move": extract_move(sentence.find("step").text)
            })
            sentence_num += 1
    
    return article


def save_input_format(article, output_path):
    """Save as plain text - one sentence per line."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        for sent in article["sentences"]:
            f.write(sent["text"] + "\n")


def save_output_format(article, output_path):
    """Save as [tag] sentence format."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        for sent in article["sentences"]:
            f.write(f"[{sent['step']}] {sent['text']}\n")


def save_json_format(article, output_path):
    """Save as structured JSON with full metadata."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(article, f, indent=2, ensure_ascii=False)


def process_article(xml_path, split_name):
    """
    Process one XML file into all three formats.
    
    Args:
        xml_path: Path to XML file
        split_name: 'validation', 'test', or 'train'
    """
    article = parse_xml(xml_path)
    article_id = article["article_id"]
    
    # Define output paths
    base_dir = Path("gold_standard") / split_name
    
    input_path = base_dir / "input" / f"{article_id}.txt"
    output_path = base_dir / "output" / f"{article_id}.txt"
    json_path = base_dir / "json" / f"{article_id}.json"
    
    # Save in all three formats
    save_input_format(article, input_path)
    save_output_format(article, output_path)
    save_json_format(article, json_path)
    
    return {
        "article_id": article_id,
        "title": article["title"],
        "sentence_count": len(article["sentences"]),
        "split": split_name
    }


def main():
    """Process all XML files and split into validation/test/train."""
    
    xml_dir = Path("Annotated_Dataset")
    
    # Define splits
    splits = {
        "validation": range(1, 11),    # Articles 1-10
        "test": range(11, 21),          # Articles 11-20
        "train": range(21, 51)          # Articles 21-50
    }
    
    print("=" * 70)
    print("Gold Standard Preparation")
    print("=" * 70)
    print()
    
    all_results = []
    
    for split_name, article_nums in splits.items():
        print(f"\n{split_name.upper()} SET")
        print("-" * 70)
        
        for num in article_nums:
            xml_file = xml_dir / f"text{num:03d}.xml"
            
            if not xml_file.exists():
                print(f"  ⚠ text{num:03d}.xml not found")
                continue
            
            result = process_article(xml_file, split_name)
            all_results.append(result)
            
            print(f"  ✓ {result['article_id']}: {result['sentence_count']} sentences")
    
    # Save summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    for split_name in ["validation", "test", "train"]:
        split_articles = [r for r in all_results if r["split"] == split_name]
        total_sentences = sum(r["sentence_count"] for r in split_articles)
        print(f"{split_name.capitalize():12} {len(split_articles):2} articles, {total_sentences:4} sentences")
    
    print()
    
    # Save detailed summary as JSON
    summary_path = Path("gold_standard") / "summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump({
            "total_articles": len(all_results),
            "articles": all_results
        }, f, indent=2, ensure_ascii=False)
    
    print(f"Summary saved: {summary_path}")
    print("\nGold standard ready! ✓")


if __name__ == "__main__":
    main()
