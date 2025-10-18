"""
Deterministic Parser for LLM Move-Step Annotations
===================================================

Purpose:
    Parse GPT-3.5 outputs into standardized JSON format for evaluation.
    
Design Philosophy:
    - Deterministic rules-based parsing (NO LLM fallback)
    - Graceful degradation for malformed outputs
    - Comprehensive logging for manual review
    - Conservative: when uncertain, flag for review
    
Prompt Changes from Kim & Lu:
    1. Added explicit format instructions: "[tag] sentence text"
    2. Emphasized "ONE tag and sentence per line"
    3. Provided concrete output format example
    4. Forbidden extra commentary/numbering
    
    RATIONALE: Kim & Lu's prompt was designed for human readability.
    We add minimal structure for deterministic parsing while preserving
    the core instructional content.

Expected Input Format:
    [1a] First sentence here.
    [1b][2a] Multi-tag sentence here.
    [3c] Another sentence.

Output Format:
    [
        {
            "sentence_num": 1,
            "text": "First sentence here.",
            "tags": ["1a"],
            "primary_tag": "1a",
            "move": "1",
            "parse_confidence": "high"
        },
        ...
    ]
"""

import re
import json
from pathlib import Path
from typing import List, Dict, Tuple
from datetime import datetime

# Valid CaRS-50 tags
VALID_TAGS = {"1a", "1b", "1c", "2a", "2b", "2c", "2d", "3a", "3b", "3c", "3d"}

# Map tags to moves
TAG_TO_MOVE = {
    "1a": "1", "1b": "1", "1c": "1",
    "2a": "2", "2b": "2", "2c": "2", "2d": "2",
    "3a": "3", "3b": "3", "3c": "3", "3d": "3"
}


class ParserStats:
    """Track parsing statistics for debugging."""
    def __init__(self):
        self.total_lines = 0
        self.parsed_sentences = 0
        self.skipped_lines = 0
        self.invalid_tags = 0
        self.multi_tag_sentences = 0
        self.warnings = []
    
    def add_warning(self, line_num: int, message: str, line_text: str):
        self.warnings.append({
            "line": line_num,
            "message": message,
            "text": line_text[:100]  # Truncate long lines
        })
    
    def summary(self) -> Dict:
        return {
            "total_lines": self.total_lines,
            "parsed_sentences": self.parsed_sentences,
            "skipped_lines": self.skipped_lines,
            "invalid_tags": self.invalid_tags,
            "multi_tag_sentences": self.multi_tag_sentences,
            "warnings": self.warnings
        }


def parse_llm_output(raw_text: str, article_id: str = "unknown") -> Tuple[List[Dict], ParserStats]:
    """
    Parse LLM output into structured format.
    
    Args:
        raw_text: Raw text output from GPT-3.5
        article_id: Identifier for the article (for logging)
    
    Returns:
        (parsed_sentences, stats)
    """
    stats = ParserStats()
    parsed_sentences = []
    
    # Pattern: [tag1][tag2]... sentence text
    # Capture all tags at start, then remaining text
    pattern = r'^(\[(?:1[abc]|2[abcd]|3[abcd])\](?:\[(?:1[abc]|2[abcd]|3[abcd])\])*)\s*(.+)$'
    
    lines = raw_text.strip().split('\n')
    sentence_num = 0
    
    for line_idx, line in enumerate(lines, 1):
        stats.total_lines += 1
        line = line.strip()
        
        # Skip empty lines
        if not line:
            stats.skipped_lines += 1
            continue
        
        # Skip lines that are clearly not annotations
        if not line.startswith('['):
            # Could be part of multi-line sentence or preamble
            if any(keyword in line.lower() for keyword in ['move', 'step', 'example:', 'note:', 'format:']):
                stats.skipped_lines += 1
                continue
            else:
                stats.add_warning(
                    line_idx, 
                    "Line doesn't start with tag bracket", 
                    line
                )
                stats.skipped_lines += 1
                continue
        
        # Try to parse with regex
        match = re.match(pattern, line)
        
        if not match:
            stats.add_warning(
                line_idx,
                "Line structure doesn't match expected format",
                line
            )
            stats.skipped_lines += 1
            continue
        
        # Extract tags and text
        tags_str = match.group(1)  # e.g., "[1a][2b]"
        sentence_text = match.group(2).strip()
        
        # Parse individual tags
        tags = re.findall(r'\[([^\]]+)\]', tags_str)
        
        # Validate tags
        valid_tags = [tag for tag in tags if tag in VALID_TAGS]
        invalid_tags = [tag for tag in tags if tag not in VALID_TAGS]
        
        if invalid_tags:
            stats.invalid_tags += len(invalid_tags)
            stats.add_warning(
                line_idx,
                f"Invalid tags: {invalid_tags}",
                line
            )
        
        if not valid_tags:
            stats.add_warning(
                line_idx,
                "No valid tags found",
                line
            )
            stats.skipped_lines += 1
            continue
        
        # Success! Build sentence object
        sentence_num += 1
        primary_tag = valid_tags[0]
        
        parsed_sentence = {
            "sentence_num": sentence_num,
            "text": sentence_text,
            "tags": valid_tags,
            "primary_tag": primary_tag,
            "move": TAG_TO_MOVE[primary_tag],
            "parse_confidence": "high" if not invalid_tags else "medium",
            "original_line": line
        }
        
        parsed_sentences.append(parsed_sentence)
        stats.parsed_sentences += 1
        
        if len(valid_tags) > 1:
            stats.multi_tag_sentences += 1
    
    return parsed_sentences, stats


def parse_file(input_path: Path, output_path: Path = None) -> Dict:
    """
    Parse a single LLM output file.
    
    Args:
        input_path: Path to raw LLM output file
        output_path: Path to save parsed JSON (optional)
    
    Returns:
        Dictionary with parsed data and metadata
    """
    with open(input_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()
    
    article_id = input_path.stem  # e.g., "text001_a1_zero_shot"
    
    parsed_sentences, stats = parse_llm_output(raw_text, article_id)
    
    result = {
        "article_id": article_id,
        "source_file": str(input_path),
        "parsed_at": datetime.now().isoformat(),
        "sentences": parsed_sentences,
        "parse_stats": stats.summary()
    }
    
    # Save if output path provided
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2)
        print(f"✓ Saved parsed output to {output_path}")
    
    return result


def parse_batch(input_dir: Path, output_dir: Path, condition: str = "*"):
    """
    Parse all files in a directory.
    
    Args:
        input_dir: Directory containing raw LLM outputs
        output_dir: Directory to save parsed JSONs
        condition: Glob pattern for files (e.g., "*a1_zero_shot*")
    """
    input_files = list(input_dir.glob(f"{condition}.txt"))
    
    if not input_files:
        print(f"⚠️  No files found matching pattern: {condition}.txt")
        return
    
    print(f"Found {len(input_files)} files to parse\n")
    
    all_stats = []
    
    for input_file in input_files:
        print(f"Parsing: {input_file.name}")
        
        output_file = output_dir / f"{input_file.stem}_parsed.json"
        result = parse_file(input_file, output_file)
        
        # Print summary
        stats = result['parse_stats']
        print(f"  ✓ Parsed {stats['parsed_sentences']} sentences")
        
        if stats['warnings']:
            print(f"  ⚠️  {len(stats['warnings'])} warnings")
        
        if stats['invalid_tags'] > 0:
            print(f"  ⚠️  {stats['invalid_tags']} invalid tags")
        
        print()
        all_stats.append(stats)
    
    # Overall summary
    print("\n" + "="*50)
    print("BATCH SUMMARY")
    print("="*50)
    total_parsed = sum(s['parsed_sentences'] for s in all_stats)
    total_warnings = sum(len(s['warnings']) for s in all_stats)
    
    print(f"Total sentences parsed: {total_parsed}")
    print(f"Total warnings: {total_warnings}")
    
    if total_warnings > 0:
        print(f"\n⚠️  Check individual JSON files for warning details")


# Example usage
if __name__ == "__main__":
    # Test on pilot outputs
    input_dir = Path("pilot_outputs/a1_zero_shot")
    output_dir = Path("pilot_outputs/a1_zero_shot/parsed")
    
    if input_dir.exists():
        parse_batch(input_dir, output_dir)
    else:
        print(f"Directory not found: {input_dir}")
        print("\nUsage:")
        print("  python parse_llm_output.py")
        print("\nOr import and use:")
        print("  from parse_llm_output import parse_file, parse_batch")
