"""
Pre-Flight Check for Fine-Tuning Data Preparation
==================================================
Run this FIRST to verify all required files are in place.

Author: Larry Grullon-Polanco
Date: 2025
"""

from pathlib import Path


def check_file_exists(filepath: Path, description: str) -> bool:
    """Check if a file exists and report."""
    exists = filepath.exists()
    status = "✓" if exists else "✗"
    print(f"{status} {description}: {filepath}")
    return exists


def main():
    print("\n" + "="*70)
    print("PRE-FLIGHT CHECK: Fine-Tuning Data Preparation")
    print("="*70 + "\n")
    
    base_dir = Path(__file__).parent
    all_good = True
    
    # Check 1: System prompt
    print("Checking required files...\n")
    prompt_path = base_dir / "prompts" / "system_prompt.txt"
    all_good &= check_file_exists(prompt_path, "System prompt")
    
    # Check 2: Training directory structure
    train_base = base_dir / "gold_standard" / "CaRS-50" / "train"
    input_dir = train_base / "input"
    output_dir = train_base / "output"
    
    all_good &= check_file_exists(input_dir, "Training input directory")
    all_good &= check_file_exists(output_dir, "Training output directory")
    
    # Check 3: Count training files
    print("\nChecking training articles (text021-text050)...\n")
    
    missing_inputs = []
    missing_outputs = []
    
    for i in range(21, 51):
        article_id = f"text{i:03d}"
        input_file = input_dir / f"{article_id}.txt"
        output_file = output_dir / f"{article_id}.txt"
        
        if not input_file.exists():
            missing_inputs.append(article_id)
        
        if not output_file.exists():
            missing_outputs.append(article_id)
    
    if not missing_inputs and not missing_outputs:
        print("✓ All 30 training article pairs found")
    else:
        all_good = False
        if missing_inputs:
            print(f"✗ Missing {len(missing_inputs)} input files:")
            for article_id in missing_inputs:
                print(f"  - {article_id}")
        
        if missing_outputs:
            print(f"✗ Missing {len(missing_outputs)} output files:")
            for article_id in missing_outputs:
                print(f"  - {article_id}")
    
    # Summary
    print("\n" + "="*70)
    if all_good:
        print("SUCCESS! All required files are in place.")
        print("="*70)
        print("\n✓ You can now run: python prepare_finetuning_data.py\n")
    else:
        print("ISSUES FOUND! Please fix the problems above.")
        print("="*70 + "\n")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
