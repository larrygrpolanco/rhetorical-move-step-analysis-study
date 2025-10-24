"""
Deterministic Parser for LLM Move-Step Annotations
===================================================

Parses LLM outputs into standardized JSON format for evaluation.

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
from typing import List, Dict, Tuple


# Valid CaRS-50 tags
VALID_TAGS = {"1a", "1b", "1c", "2a", "2b", "2c", "2d", "3a", "3b", "3c", "3d"}

# Map tags to moves
TAG_TO_MOVE = {
    "1a": "1",
    "1b": "1",
    "1c": "1",
    "2a": "2",
    "2b": "2",
    "2c": "2",
    "2d": "2",
    "3a": "3",
    "3b": "3",
    "3c": "3",
    "3d": "3",
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
        """Add a warning for manual review."""
        self.warnings.append(
            {
                "line": line_num,
                "message": message,
                "text": line_text[:100],  # Truncate long lines
            }
        )

    def summary(self) -> Dict:
        """Return summary statistics as a dictionary."""
        return {
            "total_lines": self.total_lines,
            "parsed_sentences": self.parsed_sentences,
            "skipped_lines": self.skipped_lines,
            "invalid_tags": self.invalid_tags,
            "multi_tag_sentences": self.multi_tag_sentences,
            "warnings": self.warnings,
        }


def parse_llm_output(
    raw_text: str, article_id: str = "unknown"
) -> Tuple[List[Dict], ParserStats]:
    """
    Parse LLM output into structured format.

    Args:
        raw_text: Raw text output from LLM
        article_id: Identifier for the article (for logging)

    Returns:
        (parsed_sentences, stats)
        - parsed_sentences: List of parsed sentence dictionaries
        - stats: ParserStats object with parsing metadata
    """
    stats = ParserStats()
    parsed_sentences = []

    # Pattern: [tag1][tag2]... sentence text
    # Capture all tags at start, then remaining text
    pattern = (
        r"^(\[(?:1[abc]|2[abcd]|3[abcd])\](?:\[(?:1[abc]|2[abcd]|3[abcd])\])*)\s*(.+)$"
    )

    lines = raw_text.strip().split("\n")
    sentence_num = 0

    for line_idx, line in enumerate(lines, 1):
        stats.total_lines += 1
        line = line.strip()

        # Skip empty lines
        if not line:
            stats.skipped_lines += 1
            continue

        # Skip lines that are clearly not annotations
        if not line.startswith("["):
            # Could be part of multi-line sentence or preamble
            if any(
                keyword in line.lower()
                for keyword in ["move", "step", "example:", "note:", "format:"]
            ):
                stats.skipped_lines += 1
                continue
            else:
                stats.add_warning(line_idx, "Line doesn't start with tag bracket", line)
                stats.skipped_lines += 1
                continue

        # Try to parse with regex
        match = re.match(pattern, line)

        if not match:
            stats.add_warning(
                line_idx, "Line structure doesn't match expected format", line
            )
            stats.skipped_lines += 1
            continue

        # Extract tags and text
        tags_str = match.group(1)  # e.g., "[1a][2b]"
        sentence_text = match.group(2).strip()

        # Parse individual tags
        tags = re.findall(r"\[([^\]]+)\]", tags_str)

        # Validate tags
        valid_tags = [tag for tag in tags if tag in VALID_TAGS]
        invalid_tags = [tag for tag in tags if tag not in VALID_TAGS]

        if invalid_tags:
            stats.invalid_tags += len(invalid_tags)
            stats.add_warning(line_idx, f"Invalid tags: {invalid_tags}", line)

        if not valid_tags:
            stats.add_warning(line_idx, "No valid tags found", line)
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
            "original_line": line,
        }

        parsed_sentences.append(parsed_sentence)
        stats.parsed_sentences += 1

        if len(valid_tags) > 1:
            stats.multi_tag_sentences += 1

    return parsed_sentences, stats
