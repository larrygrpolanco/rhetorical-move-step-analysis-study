"""
Parse Pilot Study Outputs
Parses raw LLM outputs into structured JSON format for evaluation.
"""

import json
from pathlib import Path
from parse_llm_output import parse_llm_output


# ============================================================================
# CONFIGURATION - EDIT THESE VALUES
# ============================================================================

CONDITION = "a1_zero_shot"  # Which condition to parse
MODEL = "claude-sonnet-4-5"  # Which model's outputs to parse

# ============================================================================


def parse_pilot_outputs(condition, model):
    """
    Parse all output files for a given condition and model.

    Args:
        condition: Condition name (e.g., "a1_zero_shot")
        model: Model name (e.g., "gpt-5mini")
    """
    # Define paths
    output_dir = Path(f"pilot_outputs/{condition}/{model}/output")
    parsed_dir = Path(f"pilot_outputs/{condition}/{model}/parsed")

    # Check if output directory exists
    if not output_dir.exists():
        print(f"ERROR: Output directory not found: {output_dir}")
        return

    # Create parsed directory
    parsed_dir.mkdir(parents=True, exist_ok=True)

    # Get all text files
    output_files = sorted(output_dir.glob("*.txt"))

    if not output_files:
        print(f"WARNING: No .txt files found in {output_dir}")
        return

    print("=" * 70)
    print(f"Parsing: {condition}/{model}")
    print(f"Found {len(output_files)} files to parse")
    print("=" * 70)
    print()

    # Parse each file
    successful = 0
    failed = 0

    for output_file in output_files:
        article_id = output_file.stem  # e.g., "text001"

        print(f"Parsing {article_id}...", end=" ")

        try:
            # Read raw output
            with open(output_file, "r", encoding="utf-8") as f:
                raw_text = f.read()

            # Parse with existing parser
            parsed_sentences, stats = parse_llm_output(raw_text, article_id)

            # Build result object
            result = {
                "article_id": article_id,
                "condition": condition,
                "model": model,
                "source_file": str(output_file),
                "sentences": parsed_sentences,
                "parse_stats": stats.summary(),
            }

            # Save parsed JSON
            parsed_file = parsed_dir / f"{article_id}.json"
            with open(parsed_file, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)

            # Report results
            print(f"✓ {stats.parsed_sentences} sentences", end="")
            if stats.warnings:
                print(f" ({len(stats.warnings)} warnings)", end="")
            print()

            successful += 1

        except Exception as e:
            print(f"✗ ERROR: {e}")
            failed += 1

    # Summary
    print()
    print("=" * 70)
    print("PARSING COMPLETE")
    print("=" * 70)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Parsed files saved to: {parsed_dir}")


def main():
    """Main execution function."""
    parse_pilot_outputs(CONDITION, MODEL)


if __name__ == "__main__":
    main()
