"""
Visualize RQ2 - Create Publication-Ready Figures
=================================================
Generates all figures for RQ2 consistency analysis.

Creates:
1. Accuracy distribution plots (histograms + density)
2. CV comparison bar chart
3. Sentence consistency heatmaps
4. Accuracy-consistency trade-off scatter plot
5. Consistency by move type comparison

Author: Larry Grullon-Polanco
Date: 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-paper')
sns.set_palette("husl")

# ============================================================================
# CONFIGURATION
# ============================================================================

DATASET = "test"
DPI = 300  # High resolution for publication

# ============================================================================


def load_analysis_data():
    """
    Load all necessary data for visualization.
    
    Returns:
        dict: All data files
    """
    analysis_dir = Path("evaluation_results") / "rq2_analysis"
    
    data = {
        'zs_runs': pd.read_csv(analysis_dir / "zero_shot_all_runs.csv"),
        'ft_runs': pd.read_csv(analysis_dir / "fine_tuned_all_runs.csv"),
        'zs_stats': pd.read_csv(analysis_dir / "zero_shot_descriptive_stats.csv"),
        'ft_stats': pd.read_csv(analysis_dir / "fine_tuned_descriptive_stats.csv"),
        'zs_sentences': pd.read_csv(analysis_dir / "sentences_zero_shot_move.csv"),
        'ft_sentences': pd.read_csv(analysis_dir / "sentences_fine_tuned_move.csv"),
    }
    
    return data


def create_distribution_plots(data, output_dir):
    """
    Figure 1: Accuracy distribution plots for both conditions.
    
    Args:
        data: Dictionary with analysis data
        output_dir: Output directory for figures
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Zero-shot move accuracy
    axes[0, 0].hist(data['zs_runs']['move_accuracy'], bins=15, alpha=0.7, 
                    color='steelblue', edgecolor='black', density=True)
    axes[0, 0].axvline(data['zs_runs']['move_accuracy'].mean(), 
                       color='red', linestyle='--', linewidth=2, label='Mean')
    axes[0, 0].set_xlabel('Move Accuracy')
    axes[0, 0].set_ylabel('Density')
    axes[0, 0].set_title('Zero-shot: Move Accuracy Distribution')
    axes[0, 0].legend()
    axes[0, 0].grid(alpha=0.3)
    
    # Fine-tuned move accuracy
    axes[0, 1].hist(data['ft_runs']['move_accuracy'], bins=15, alpha=0.7,
                    color='coral', edgecolor='black', density=True)
    axes[0, 1].axvline(data['ft_runs']['move_accuracy'].mean(),
                       color='red', linestyle='--', linewidth=2, label='Mean')
    axes[0, 1].set_xlabel('Move Accuracy')
    axes[0, 1].set_ylabel('Density')
    axes[0, 1].set_title('Fine-tuned: Move Accuracy Distribution')
    axes[0, 1].legend()
    axes[0, 1].grid(alpha=0.3)
    
    # Zero-shot step accuracy
    axes[1, 0].hist(data['zs_runs']['step_accuracy'], bins=15, alpha=0.7,
                    color='steelblue', edgecolor='black', density=True)
    axes[1, 0].axvline(data['zs_runs']['step_accuracy'].mean(),
                       color='red', linestyle='--', linewidth=2, label='Mean')
    axes[1, 0].set_xlabel('Step Accuracy')
    axes[1, 0].set_ylabel('Density')
    axes[1, 0].set_title('Zero-shot: Step Accuracy Distribution')
    axes[1, 0].legend()
    axes[1, 0].grid(alpha=0.3)
    
    # Fine-tuned step accuracy
    axes[1, 1].hist(data['ft_runs']['step_accuracy'], bins=15, alpha=0.7,
                    color='coral', edgecolor='black', density=True)
    axes[1, 1].axvline(data['ft_runs']['step_accuracy'].mean(),
                       color='red', linestyle='--', linewidth=2, label='Mean')
    axes[1, 1].set_xlabel('Step Accuracy')
    axes[1, 1].set_ylabel('Density')
    axes[1, 1].set_title('Fine-tuned: Step Accuracy Distribution')
    axes[1, 1].legend()
    axes[1, 1].grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'figure1_distributions.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    
    print("  ✓ Figure 1: Accuracy distributions")


def create_cv_comparison(data, output_dir):
    """
    Figure 2: Coefficient of Variation comparison.
    
    Args:
        data: Dictionary with analysis data
        output_dir: Output directory for figures
    """
    # Extract CV values
    zs_move_cv = data['zs_stats'][data['zs_stats']['metric'] == 'Move Accuracy']['cv'].values[0]
    ft_move_cv = data['ft_stats'][data['ft_stats']['metric'] == 'Move Accuracy']['cv'].values[0]
    zs_step_cv = data['zs_stats'][data['zs_stats']['metric'] == 'Step Accuracy']['cv'].values[0]
    ft_step_cv = data['ft_stats'][data['ft_stats']['metric'] == 'Step Accuracy']['cv'].values[0]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x = np.arange(2)
    width = 0.35
    
    move_cvs = [zs_move_cv, ft_move_cv]
    step_cvs = [zs_step_cv, ft_step_cv]
    
    bars1 = ax.bar(x - width/2, move_cvs, width, label='Move-level', alpha=0.8, color='steelblue')
    bars2 = ax.bar(x + width/2, step_cvs, width, label='Step-level', alpha=0.8, color='coral')
    
    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.2f}%',
                   ha='center', va='bottom', fontsize=10)
    
    # Reference lines for consistency levels
    ax.axhline(y=5, color='green', linestyle='--', alpha=0.5, label='Excellent (CV<5%)')
    ax.axhline(y=10, color='orange', linestyle='--', alpha=0.5, label='Good (CV<10%)')
    
    ax.set_ylabel('Coefficient of Variation (%)', fontsize=12)
    ax.set_title('Consistency Comparison: Zero-shot vs Fine-tuned', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(['Zero-shot', 'Fine-tuned'], fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'figure2_cv_comparison.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    
    print("  ✓ Figure 2: CV comparison")


def create_sentence_heatmaps(data, output_dir):
    """
    Figure 3: Sentence-level consistency heatmaps.
    
    Args:
        data: Dictionary with analysis data
        output_dir: Output directory for figures
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 8))
    
    # Zero-shot
    df_zs_sorted = data['zs_sentences'].sort_values('agreement_rate', ascending=False)
    y_pos = np.arange(len(df_zs_sorted))
    
    colors = df_zs_sorted['agreement_rate'].apply(
        lambda x: 'green' if x >= 0.9 else ('orange' if x >= 0.7 else 'red')
    )
    
    axes[0].barh(y_pos, df_zs_sorted['agreement_rate'], alpha=0.7, color=colors)
    axes[0].axvline(x=0.9, color='green', linestyle='--', alpha=0.5, linewidth=2, label='High (≥90%)')
    axes[0].axvline(x=0.7, color='orange', linestyle='--', alpha=0.5, linewidth=2, label='Moderate (≥70%)')
    axes[0].set_xlabel('Agreement Rate', fontsize=11)
    axes[0].set_ylabel('Sentence (sorted)', fontsize=11)
    axes[0].set_title('Zero-shot: Sentence-Level Consistency', fontsize=12, fontweight='bold')
    axes[0].set_yticks([])  # Too many sentences to show individually
    axes[0].legend(fontsize=9)
    axes[0].grid(axis='x', alpha=0.3)
    
    # Fine-tuned
    df_ft_sorted = data['ft_sentences'].sort_values('agreement_rate', ascending=False)
    y_pos = np.arange(len(df_ft_sorted))
    
    colors = df_ft_sorted['agreement_rate'].apply(
        lambda x: 'green' if x >= 0.9 else ('orange' if x >= 0.7 else 'red')
    )
    
    axes[1].barh(y_pos, df_ft_sorted['agreement_rate'], alpha=0.7, color=colors)
    axes[1].axvline(x=0.9, color='green', linestyle='--', alpha=0.5, linewidth=2, label='High (≥90%)')
    axes[1].axvline(x=0.7, color='orange', linestyle='--', alpha=0.5, linewidth=2, label='Moderate (≥70%)')
    axes[1].set_xlabel('Agreement Rate', fontsize=11)
    axes[1].set_ylabel('Sentence (sorted)', fontsize=11)
    axes[1].set_title('Fine-tuned: Sentence-Level Consistency', fontsize=12, fontweight='bold')
    axes[1].set_yticks([])
    axes[1].legend(fontsize=9)
    axes[1].grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'figure3_sentence_consistency.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    
    print("  ✓ Figure 3: Sentence consistency heatmaps")


def create_tradeoff_plot(data, output_dir):
    """
    Figure 4: Accuracy-consistency trade-off scatter plot.
    
    Args:
        data: Dictionary with analysis data
        output_dir: Output directory for figures
    """
    # Extract values
    zs_move = data['zs_stats'][data['zs_stats']['metric'] == 'Move Accuracy']
    ft_move = data['ft_stats'][data['ft_stats']['metric'] == 'Move Accuracy']
    
    zs_mean = zs_move['mean'].values[0] * 100
    zs_cv = zs_move['cv'].values[0]
    ft_mean = ft_move['mean'].values[0] * 100
    ft_cv = ft_move['cv'].values[0]
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Plot points
    ax.scatter(zs_mean, zs_cv, s=300, alpha=0.7, label='Zero-shot', 
              color='steelblue', edgecolor='black', linewidth=2)
    ax.scatter(ft_mean, ft_cv, s=300, alpha=0.7, label='Fine-tuned',
              color='coral', edgecolor='black', linewidth=2)
    
    # Annotate points
    ax.annotate('Zero-shot', (zs_mean, zs_cv),
               xytext=(10, 10), textcoords='offset points', fontsize=12,
               bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.7))
    ax.annotate('Fine-tuned', (ft_mean, ft_cv),
               xytext=(10, 10), textcoords='offset points', fontsize=12,
               bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.7))
    
    # Ideal regions
    ax.axhspan(0, 5, alpha=0.1, color='green', label='Excellent consistency (CV<5%)')
    ax.axhspan(5, 10, alpha=0.1, color='yellow', label='Good consistency (CV 5-10%)')
    ax.axvspan(85, 100, alpha=0.05, color='green')
    
    ax.set_xlabel('Mean Accuracy (%)', fontsize=12)
    ax.set_ylabel('Coefficient of Variation (%)', fontsize=12)
    ax.set_title('Accuracy-Consistency Trade-off: Move-Level', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10, loc='upper left')
    ax.grid(alpha=0.3)
    
    # Set reasonable axis limits
    ax.set_xlim(min(zs_mean, ft_mean) - 5, max(zs_mean, ft_mean) + 5)
    ax.set_ylim(0, max(zs_cv, ft_cv) * 1.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'figure4_tradeoff.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    
    print("  ✓ Figure 4: Accuracy-consistency trade-off")


def create_boxplot_comparison(data, output_dir):
    """
    Figure 5: Boxplot comparison of accuracy distributions.
    
    Args:
        data: Dictionary with analysis data
        output_dir: Output directory for figures
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Prepare data for boxplots
    move_data = [
        data['zs_runs']['move_accuracy'].values,
        data['ft_runs']['move_accuracy'].values
    ]
    
    step_data = [
        data['zs_runs']['step_accuracy'].values,
        data['ft_runs']['step_accuracy'].values
    ]
    
    # Move-level boxplot
    bp1 = axes[0].boxplot(move_data, labels=['Zero-shot', 'Fine-tuned'],
                          patch_artist=True, widths=0.6)
    
    # Color the boxes
    colors = ['steelblue', 'coral']
    for patch, color in zip(bp1['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    axes[0].set_ylabel('Move Accuracy', fontsize=11)
    axes[0].set_title('Move-Level Accuracy Distribution', fontsize=12, fontweight='bold')
    axes[0].grid(axis='y', alpha=0.3)
    
    # Step-level boxplot
    bp2 = axes[1].boxplot(step_data, labels=['Zero-shot', 'Fine-tuned'],
                          patch_artist=True, widths=0.6)
    
    for patch, color in zip(bp2['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    axes[1].set_ylabel('Step Accuracy', fontsize=11)
    axes[1].set_title('Step-Level Accuracy Distribution', fontsize=12, fontweight='bold')
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'figure5_boxplots.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    
    print("  ✓ Figure 5: Boxplot comparison")


def create_supplementary_figures(data, output_dir):
    """
    Create additional supplementary figures.
    
    Args:
        data: Dictionary with analysis data
        output_dir: Output directory for figures
    """
    # Q-Q plots for normality assessment
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Zero-shot move
    stats.probplot(data['zs_runs']['move_accuracy'], dist="norm", plot=axes[0, 0])
    axes[0, 0].set_title('Zero-shot Move Accuracy: Q-Q Plot', fontsize=11)
    axes[0, 0].grid(alpha=0.3)
    
    # Fine-tuned move
    stats.probplot(data['ft_runs']['move_accuracy'], dist="norm", plot=axes[0, 1])
    axes[0, 1].set_title('Fine-tuned Move Accuracy: Q-Q Plot', fontsize=11)
    axes[0, 1].grid(alpha=0.3)
    
    # Zero-shot step
    stats.probplot(data['zs_runs']['step_accuracy'], dist="norm", plot=axes[1, 0])
    axes[1, 0].set_title('Zero-shot Step Accuracy: Q-Q Plot', fontsize=11)
    axes[1, 0].grid(alpha=0.3)
    
    # Fine-tuned step
    stats.probplot(data['ft_runs']['step_accuracy'], dist="norm", plot=axes[1, 1])
    axes[1, 1].set_title('Fine-tuned Step Accuracy: Q-Q Plot', fontsize=11)
    axes[1, 1].grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'supplementary_qqplots.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    
    print("  ✓ Supplementary: Q-Q plots")


def main():
    """Main execution."""
    
    print("=" * 70)
    print("CREATING RQ2 VISUALIZATIONS")
    print("=" * 70)
    print()
    
    # Create output directory
    output_dir = Path("figures") / "rq2"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Load data
        print("Loading analysis data...")
        data = load_analysis_data()
        print("  ✓ All data loaded")
        print()
        
        # Create figures
        print("Creating figures...")
        
        create_distribution_plots(data, output_dir)
        create_cv_comparison(data, output_dir)
        create_sentence_heatmaps(data, output_dir)
        create_tradeoff_plot(data, output_dir)
        create_boxplot_comparison(data, output_dir)
        
        print()
        print("Creating supplementary figures...")
        create_supplementary_figures(data, output_dir)
        
        print()
        print("=" * 70)
        print("✅ ALL FIGURES CREATED")
        print("=" * 70)
        
        print(f"\nOutput directory: {output_dir}/")
        print("\nMain figures:")
        print("  1. figure1_distributions.png - Accuracy distributions")
        print("  2. figure2_cv_comparison.png - CV comparison")
        print("  3. figure3_sentence_consistency.png - Sentence heatmaps")
        print("  4. figure4_tradeoff.png - Accuracy-consistency trade-off")
        print("  5. figure5_boxplots.png - Distribution comparisons")
        print("\nSupplementary:")
        print("  - supplementary_qqplots.png - Normality assessment")
        
        print(f"\nAll figures saved at {DPI} DPI for publication quality.")
        print()
        
    except FileNotFoundError as e:
        print(f"\n❌ ERROR: {e}")
        print("\nMake sure you've run the analysis scripts first:")
        print("  1. analyze_consistency_rq2.py")
        print("  2. analyze_sentences_rq2.py")
        return 1
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    from scipy import stats  # Import here to avoid issues if not needed
    exit(main())
