"""
Test the parser with realistic examples.
"""

from parse_llm_output import parse_llm_output

# Test Case 1: Perfect format
test_perfect = """
[1b] Photosynthesis is a fundamental biological process.
[1c] Smith et al. (2020) demonstrated key mechanisms in plant cells.
[2b] However, few studies have examined aquatic species.
[3a] This study aims to address this gap.
"""

print("="*60)
print("TEST 1: Perfect Format")
print("="*60)
sentences, stats = parse_llm_output(test_perfect, "test1")
print(f"\nParsed {stats.parsed_sentences} sentences")
print(f"Warnings: {len(stats.warnings)}")
print("\nSample output:")
print(sentences[0] if sentences else "No sentences parsed")

# Test Case 2: Multi-tag sentences
test_multitag = """
[1a][3a] This research addresses a critical gap in our understanding.
[1c] Previous work by Jones (2019) laid the foundation.
[2b][2c] Yet it remains unclear whether these findings generalize to other contexts.
"""

print("\n" + "="*60)
print("TEST 2: Multi-Tag Sentences")
print("="*60)
sentences, stats = parse_llm_output(test_multitag, "test2")
print(f"\nParsed {stats.parsed_sentences} sentences")
print(f"Multi-tag sentences: {stats.multi_tag_sentences}")
print("\nSample multi-tag:")
for s in sentences:
    if len(s['tags']) > 1:
        print(f"  Tags: {s['tags']}")
        print(f"  Text: {s['text'][:50]}...")
        break

# Test Case 3: Messy with invalid tags
test_messy = """
Move 1: Establishing territory

[1b] Biological systems exhibit complex behaviors.
[INVALID] This should be skipped.
[1c] Research by Smith et al. (2021) showed important results.

Some commentary that should be ignored.

[2a] However, these findings have been challenged.
"""

print("\n" + "="*60)
print("TEST 3: Messy Input with Invalid Content")
print("="*60)
sentences, stats = parse_llm_output(test_messy, "test3")
print(f"\nParsed {stats.parsed_sentences} sentences")
print(f"Skipped lines: {stats.skipped_lines}")
print(f"Warnings: {len(stats.warnings)}")

if stats.warnings:
    print("\nWarning examples:")
    for w in stats.warnings[:2]:
        print(f"  Line {w['line']}: {w['message']}")

# Test Case 4: Edge cases
test_edge = """
[1a]No space after tag.
[1b]    Extra spaces    in the sentence.
[1c] Sentence with "quotes" and special chars: $100!
[2a] Multi-line should work
if the format is correct.
"""

print("\n" + "="*60)
print("TEST 4: Edge Cases")
print("="*60)
sentences, stats = parse_llm_output(test_edge, "test4")
print(f"\nParsed {stats.parsed_sentences} sentences")
print("\nParsed examples:")
for s in sentences[:2]:
    print(f"  [{s['primary_tag']}] {s['text'][:60]}...")

print("\n" + "="*60)
print("PARSER VALIDATION COMPLETE")
print("="*60)
print("\nReady to parse real LLM outputs!")
print("Usage: python parse_llm_output.py")
