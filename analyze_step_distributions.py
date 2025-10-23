"""
Step Distribution Analysis
===========================
Analyzes move and step distributions across all dataset splits.

Reports:
1. Overall statistics per dataset (validation, test, train)
2. Few-shot example analysis (3-shot and 8-shot sets)
3. Comparison tables and visualizations
4. Class imbalance metrics

Author: Larry Grullon-Polanco
Date: 2025
"""

import json
from pathlib import Path
from collections import Counter, defaultdict
import pandas as pd


# Dataset configurations
DATASETS = {
    "validation": {"range": range(1, 11), "count": 10},
    "test": {"range": range(11, 21), "count": 10},
    "train": {"range": range(21, 51), "count": 30},
}

# Valid tags
MOVE_LABELS = ["1", "2", "3"]
STEP_LABELS = ["1a", "1b", "1c", "2a", "2b", "2c", "2d", "3a", "3b", "3c", "3d"]


def load_gold_standard_json(article_num, dataset):
    """
    Load gold standard JSON for an article.

    Args:
        article_num: Article number
        dataset: 'validation', 'test', or 'train'

    Returns:
        dict: Parsed JSON data
    """
    article_id = f"text{article_num:03d}"
    json_file = Path(f"gold_standard/CaRS-50/{dataset}/json/{article_id}.json")

    if not json_file.exists():
        return None

    with open(json_file, "r", encoding="utf-8") as f:
        return json.load(f)


def analyze_dataset(dataset_name):
    """
    Analyze move and step distributions for a dataset.

    Args:
        dataset_name: 'validation', 'test', or 'train'

    Returns:
        dict: Statistics including counts, distributions, articles analyzed
    """
    article_range = DATASETS[dataset_name]["range"]

    move_counts = Counter()
    step_counts = Counter()
    total_sentences = 0
    articles_analyzed = 0
    sentences_per_article = []

    for article_num in article_range:
        data = load_gold_standard_json(article_num, dataset_name)

        if data is None:
            continue

        articles_analyzed += 1
        article_sentences = len(data["sentences"])
        sentences_per_article.append(article_sentences)
        total_sentences += article_sentences

        for sentence in data["sentences"]:
            move_counts[sentence["move"]] += 1
            step_counts[sentence["step"]] += 1

    return {
        "dataset": dataset_name,
        "articles_analyzed": articles_analyzed,
        "total_articles": DATASETS[dataset_name]["count"],
        "total_sentences": total_sentences,
        "sentences_per_article": {
            "mean": sum(sentences_per_article) / len(sentences_per_article)
            if sentences_per_article
            else 0,
            "min": min(sentences_per_article) if sentences_per_article else 0,
            "max": max(sentences_per_article) if sentences_per_article else 0,
        },
        "move_counts": dict(move_counts),
        "step_counts": dict(step_counts),
    }


def load_few_shot_examples():
    """
    Load few-shot example selections.

    Returns:
        dict: Few-shot selections or None if file doesn't exist
    """
    selection_file = Path("gold_standard/CaRS-50/train/few_shot_examples.json")

    if not selection_file.exists():
        return None

    with open(selection_file, "r", encoding="utf-8") as f:
        return json.load(f)


def analyze_few_shot_set(article_ids, set_name):
    """
    Analyze a specific few-shot example set.

    Args:
        article_ids: List of article IDs (e.g., ['text021', 'text024'])
        set_name: Name of the set (e.g., '3-shot')

    Returns:
        dict: Statistics for this few-shot set
    """
    move_counts = Counter()
    step_counts = Counter()
    total_sentences = 0
    articles_analyzed = 0
    sentences_per_article = []
    article_details = []

    for article_id in article_ids:
        # Extract article number from ID (e.g., 'text021' -> 21)
        article_num = int(article_id.replace("text", ""))
        data = load_gold_standard_json(article_num, "train")

        if data is None:
            continue

        articles_analyzed += 1
        article_sentences = len(data["sentences"])
        sentences_per_article.append(article_sentences)
        total_sentences += article_sentences

        article_move_counts = Counter()
        article_step_counts = Counter()

        for sentence in data["sentences"]:
            move_counts[sentence["move"]] += 1
            step_counts[sentence["step"]] += 1
            article_move_counts[sentence["move"]] += 1
            article_step_counts[sentence["step"]] += 1

        article_details.append(
            {
                "article_id": article_id,
                "sentences": article_sentences,
                "move_counts": dict(article_move_counts),
                "step_counts": dict(article_step_counts),
            }
        )

    return {
        "set_name": set_name,
        "article_ids": article_ids,
        "articles_analyzed": articles_analyzed,
        "total_sentences": total_sentences,
        "sentences_per_article": {
            "mean": sum(sentences_per_article) / len(sentences_per_article)
            if sentences_per_article
            else 0,
            "min": min(sentences_per_article) if sentences_per_article else 0,
            "max": max(sentences_per_article) if sentences_per_article else 0,
        },
        "move_counts": dict(move_counts),
        "step_counts": dict(step_counts),
        "article_details": article_details,
    }


def calculate_distributions(counts, total):
    """
    Calculate percentage distributions.

    Args:
        counts: Dictionary of label counts
        total: Total count

    Returns:
        dict: Percentages for each label
    """
    return {label: (count / total * 100) if total > 0 else 0 
            for label, count in counts.items()}


def print_dataset_summary(stats):
    """Print summary statistics for a dataset."""
    print(f"\n{'='*70}")
    print(f"Dataset: {stats['dataset'].upper()}")
    print(f"{'='*70}")
    print(f"Articles: {stats['articles_analyzed']}/{stats['total_articles']}")
    print(f"Total Sentences: {stats['total_sentences']}")
    print(
        f"Sentences per Article: {stats['sentences_per_article']['mean']:.1f} "
        f"(min: {stats['sentences_per_article']['min']}, "
        f"max: {stats['sentences_per_article']['max']})"
    )

    # Move distribution
    print(f"\n--- Move Distribution ---")
    move_dist = calculate_distributions(stats["move_counts"], stats["total_sentences"])
    for move in MOVE_LABELS:
        count = stats["move_counts"].get(move, 0)
        pct = move_dist.get(move, 0)
        print(f"  Move {move}: {count:4d} sentences ({pct:5.2f}%)")

    # Step distribution
    print(f"\n--- Step Distribution ---")
    step_dist = calculate_distributions(stats["step_counts"], stats["total_sentences"])
    for step in STEP_LABELS:
        count = stats["step_counts"].get(step, 0)
        pct = step_dist.get(step, 0)
        print(f"  Step {step}: {count:4d} sentences ({pct:5.2f}%)")


def print_few_shot_summary(stats):
    """Print summary for few-shot examples."""
    print(f"\n{'='*70}")
    print(f"Few-Shot Set: {stats['set_name']}")
    print(f"{'='*70}")
    print(f"Articles: {stats['article_ids']}")
    print(f"Total Sentences: {stats['total_sentences']}")
    print(
        f"Sentences per Article: {stats['sentences_per_article']['mean']:.1f} "
        f"(min: {stats['sentences_per_article']['min']}, "
        f"max: {stats['sentences_per_article']['max']})"
    )

    # Move distribution
    print(f"\n--- Move Distribution ---")
    move_dist = calculate_distributions(stats["move_counts"], stats["total_sentences"])
    for move in MOVE_LABELS:
        count = stats["move_counts"].get(move, 0)
        pct = move_dist.get(move, 0)
        print(f"  Move {move}: {count:4d} sentences ({pct:5.2f}%)")

    # Step distribution
    print(f"\n--- Step Distribution ---")
    step_dist = calculate_distributions(stats["step_counts"], stats["total_sentences"])
    for step in STEP_LABELS:
        count = stats["step_counts"].get(step, 0)
        pct = step_dist.get(step, 0)
        print(f"  Step {step}: {count:4d} sentences ({pct:5.2f}%)")

    # Article-level breakdown
    print(f"\n--- Article Breakdown ---")
    for article in stats["article_details"]:
        print(f"\n  {article['article_id']} ({article['sentences']} sentences):")
        print(f"    Moves: {article['move_counts']}")
        print(f"    Steps: {article['step_counts']}")


def create_comparison_table(all_stats):
    """
    Create a comparison table across datasets.

    Args:
        all_stats: List of dataset statistics dictionaries

    Returns:
        pd.DataFrame: Comparison table
    """
    rows = []

    for stats in all_stats:
        row = {
            "Dataset": stats["dataset"],
            "Articles": stats["articles_analyzed"],
            "Total Sentences": stats["total_sentences"],
            "Avg Sentences/Article": f"{stats['sentences_per_article']['mean']:.1f}",
        }

        # Add move counts
        for move in MOVE_LABELS:
            count = stats["move_counts"].get(move, 0)
            pct = (count / stats["total_sentences"] * 100) if stats["total_sentences"] > 0 else 0
            row[f"Move {move}"] = f"{count} ({pct:.1f}%)"

        rows.append(row)

    return pd.DataFrame(rows)


def create_step_comparison_table(all_stats):
    """
    Create a detailed step-level comparison table.

    Args:
        all_stats: List of dataset statistics dictionaries

    Returns:
        pd.DataFrame: Step comparison table
    """
    rows = []

    for step in STEP_LABELS:
        row = {"Step": step}

        for stats in all_stats:
            count = stats["step_counts"].get(step, 0)
            pct = (count / stats["total_sentences"] * 100) if stats["total_sentences"] > 0 else 0
            row[stats["dataset"]] = f"{count} ({pct:.1f}%)"

        rows.append(row)

    return pd.DataFrame(rows)


def save_results(all_stats, few_shot_stats, output_dir="analysis_results"):
    """
    Save analysis results to files.

    Args:
        all_stats: List of dataset statistics
        few_shot_stats: List of few-shot statistics
        output_dir: Output directory path
    """
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # Save full statistics as JSON
    full_results = {
        "datasets": all_stats,
        "few_shot": few_shot_stats if few_shot_stats else [],
    }

    with open(output_path / "step_distributions.json", "w", encoding="utf-8") as f:
        json.dump(full_results, f, indent=2)

    # Save comparison tables as CSV
    comparison_df = create_comparison_table(all_stats)
    comparison_df.to_csv(output_path / "dataset_comparison.csv", index=False)

    step_comparison_df = create_step_comparison_table(all_stats)
    step_comparison_df.to_csv(output_path / "step_comparison.csv", index=False)

    # Save markdown report
    with open(output_path / "distribution_report.md", "w", encoding="utf-8") as f:
        f.write("# Step Distribution Analysis Report\n\n")
        
        f.write("## Dataset Summary\n\n")
        f.write(comparison_df.to_markdown(index=False))
        f.write("\n\n")
        
        f.write("## Step-Level Comparison\n\n")
        f.write(step_comparison_df.to_markdown(index=False))
        f.write("\n\n")

        if few_shot_stats:
            f.write("## Few-Shot Example Sets\n\n")
            for fs_stats in few_shot_stats:
                f.write(f"### {fs_stats['set_name']}\n\n")
                f.write(f"- Articles: {', '.join(fs_stats['article_ids'])}\n")
                f.write(f"- Total Sentences: {fs_stats['total_sentences']}\n")
                f.write(f"- Avg Sentences/Article: {fs_stats['sentences_per_article']['mean']:.1f}\n\n")
                
                f.write("**Move Distribution:**\n\n")
                for move in MOVE_LABELS:
                    count = fs_stats["move_counts"].get(move, 0)
                    pct = (count / fs_stats["total_sentences"] * 100) if fs_stats["total_sentences"] > 0 else 0
                    f.write(f"- Move {move}: {count} ({pct:.1f}%)\n")
                
                f.write("\n**Step Distribution:**\n\n")
                for step in STEP_LABELS:
                    count = fs_stats["step_counts"].get(step, 0)
                    pct = (count / fs_stats["total_sentences"] * 100) if fs_stats["total_sentences"] > 0 else 0
                    f.write(f"- Step {step}: {count} ({pct:.1f}%)\n")
                f.write("\n")

    print(f"\n✓ Results saved to {output_dir}/")
    print(f"  - step_distributions.json")
    print(f"  - dataset_comparison.csv")
    print(f"  - step_comparison.csv")
    print(f"  - distribution_report.md")


def main():
    """Main execution."""
    print("="*70)
    print("STEP DISTRIBUTION ANALYSIS")
    print("="*70)

    # Analyze all datasets
    all_stats = []
    for dataset_name in ["validation", "test", "train"]:
        print(f"\nAnalyzing {dataset_name} dataset...")
        stats = analyze_dataset(dataset_name)
        all_stats.append(stats)
        print_dataset_summary(stats)

    # Analyze few-shot examples
    few_shot_stats = []
    few_shot_config = load_few_shot_examples()

    if few_shot_config:
        print(f"\n{'='*70}")
        print("FEW-SHOT EXAMPLE ANALYSIS")
        print(f"{'='*70}")

        # 3-shot
        if "three_shot" in few_shot_config:
            three_shot_stats = analyze_few_shot_set(
                few_shot_config["three_shot"]["article_ids"], "3-shot"
            )
            few_shot_stats.append(three_shot_stats)
            print_few_shot_summary(three_shot_stats)

        # 8-shot
        if "eight_shot" in few_shot_config:
            eight_shot_stats = analyze_few_shot_set(
                few_shot_config["eight_shot"]["article_ids"], "8-shot"
            )
            few_shot_stats.append(eight_shot_stats)
            print_few_shot_summary(eight_shot_stats)
    else:
        print("\n⚠️  Few-shot examples file not found. Skipping few-shot analysis.")

    # Print comparison table
    print(f"\n{'='*70}")
    print("DATASET COMPARISON")
    print(f"{'='*70}\n")
    print(create_comparison_table(all_stats).to_string(index=False))

    print(f"\n{'='*70}")
    print("STEP-LEVEL COMPARISON")
    print(f"{'='*70}\n")
    print(create_step_comparison_table(all_stats).to_string(index=False))

    # Save results
    save_results(all_stats, few_shot_stats)

    print(f"\n{'='*70}")
    print("ANALYSIS COMPLETE")
    print(f"{'='*70}\n")


if __name__ == "__main__":
    main()
