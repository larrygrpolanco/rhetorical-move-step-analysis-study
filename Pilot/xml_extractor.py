"""
Simple XML extractor for CaRS-50 Biology dataset.

Extracts sentences with their step annotations from XML files.
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict, Any


def extract_from_xml(xml_path: str) -> Dict[str, Any]:
    """
    Extract article data from a single XML file.

    Args:
        xml_path: Path to the XML file

    Returns:
        Dictionary with article metadata and sentences:
        {
            'article_id': str,
            'title': str,
            'doi': str,
            'source': str,
            'category': str,
            'sentences': [
                {
                    'sentence_id': str,
                    'text': str,
                    'step': str
                },
                ...
            ]
        }
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Extract metadata
    article_data = {
        "article_id": root.find("fulltextID").text,
        "title": root.find("title").text,
        "doi": root.find("doi").text,
        "source": root.find("source").text,
        "category": root.find("category").text,
        "sentences": [],
    }

    # Extract sentences from all paragraphs
    fulltext = root.find("fulltext")
    for paragraph in fulltext.findall("paragraph"):
        for sentence in paragraph.findall("sentence"):
            sentence_data = {
                "sentence_id": sentence.find("sentenceID").text,
                "text": sentence.find("text").text,
                "step": sentence.find("step").text,
            }
            article_data["sentences"].append(sentence_data)

    return article_data


def extract_from_directory(directory_path: str) -> List[Dict[str, Any]]:
    """
    Extract data from all XML files in a directory.

    Args:
        directory_path: Path to directory containing XML files

    Returns:
        List of article dictionaries
    """
    directory = Path(directory_path)
    articles = []

    for xml_file in sorted(directory.glob("*.xml")):
        article_data = extract_from_xml(str(xml_file))
        articles.append(article_data)

    return articles


def get_sentences_only(articles: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """
    Extract just the sentences and steps from all articles.

    Args:
        articles: List of article dictionaries

    Returns:
        Flat list of sentence dictionaries with article_id added:
        [
            {
                'article_id': str,
                'sentence_id': str,
                'text': str,
                'step': str
            },
            ...
        ]
    """
    all_sentences = []
    for article in articles:
        for sentence in article["sentences"]:
            all_sentences.append(
                {
                    "article_id": article["article_id"],
                    "sentence_id": sentence["sentence_id"],
                    "text": sentence["text"],
                    "step": sentence["step"],
                }
            )
    return all_sentences


def count_sentences(articles: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Count total sentences and sentences per step.

    Args:
        articles: List of article dictionaries

    Returns:
        Dictionary with counts
    """
    step_counts = {}
    total = 0

    for article in articles:
        for sentence in article["sentences"]:
            step = sentence["step"]
            step_counts[step] = step_counts.get(step, 0) + 1
            total += 1

    return {"total": total, "by_step": step_counts}


def format_article_for_llm(article: Dict[str, Any]) -> str:
    """
    Format a single article's sentences as plain text for LLM input.
    Each sentence on its own line.

    Args:
        article: Article dictionary

    Returns:
        Plain text with one sentence per line
    """
    sentences = [sent["text"] for sent in article["sentences"]]
    return "\n".join(sentences)


def format_articles_for_llm(articles: List[Dict[str, Any]]) -> List[str]:
    """
    Format multiple articles for LLM input.

    Args:
        articles: List of article dictionaries

    Returns:
        List of formatted text strings, one per article
    """
    return [format_article_for_llm(article) for article in articles]
