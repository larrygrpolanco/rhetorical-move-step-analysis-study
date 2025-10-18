"""
Test script for xml_extractor module.
Run this to verify the extractor is working correctly.
"""

from xml_extractor import (
    extract_from_xml,
    extract_from_directory,
    get_sentences_only,
    count_sentences,
    format_article_for_llm,
    format_articles_for_llm,
)


def test_single_file():
    """Test extracting a single XML file."""
    print("Testing single file extraction...")
    article = extract_from_xml("Annotated_Dataset/text001.xml")

    print(f"Article ID: {article['article_id']}")
    print(f"Title: {article['title']}")
    print(f"Number of sentences: {len(article['sentences'])}")
    print()

    # Show first few sentences
    print("First 3 sentences:")
    for i, sent in enumerate(article["sentences"][:3], 1):
        print(f"{i}. [{sent['step']}] {sent['text'][:80]}...")
    print()

    # Count steps
    counts = count_sentences([article])
    print("Step distribution:")
    for step, count in sorted(counts["by_step"].items()):
        print(f"  Step {step}: {count} sentences")
    print(f"  Total: {counts['total']} sentences")
    print()

    return article


def test_llm_formatting(article):
    """Test formatting for LLM."""
    print("=" * 80)
    print("Testing LLM formatting...")
    print("=" * 80)

    llm_text = format_article_for_llm(article)
    print(llm_text[:500])  # Show first 500 chars
    print("...")
    print(f"\n[Total length: {len(llm_text)} characters]")
    print()


if __name__ == "__main__":
    article = test_single_file()
    test_llm_formatting(article)

    print("✓ All tests passed!")
