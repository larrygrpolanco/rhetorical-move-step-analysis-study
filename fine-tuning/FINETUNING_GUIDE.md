# Fine-Tuning Guide: Step-by-Step Instructions

## Overview
This guide walks you through fine-tuning GPT-4 for rhetorical move-step annotation using OpenAI's web interface (recommended for first-time fine-tuning).

**Model**: gpt-4.1-2025-04-14  
**Training Data**: 30 articles (text021-text050)  
**Expected Time**: ~30-60 minutes for training  
**Expected Cost**: ~$10-20

---

## Phase 1: Prepare Training Data (Local - 5 minutes)

### Step 1: Verify Setup
```bash
python verify_finetuning_setup.py
```

**Expected Output**: All checkmarks (✓)  
**If any ✗**: Fix missing files before proceeding

### Step 2: Generate Training File
```bash
python prepare_finetuning_data.py
```

**This script will**:
- Load your system prompt (prompts/system_prompt.txt)
- Load all 30 training article pairs
- Format them in OpenAI's JSONL format
- Validate the format rigorously
- Save to `finetuning_data.jsonl`

**Expected Output**:
```
✓ Loaded system prompt (3,234 characters)
✓ Loaded text021
✓ Loaded text022
...
✓ Loaded text050
✓ Successfully loaded 30 article pairs
✓ Created 30 training examples
✓ All 30 examples validated successfully
✓ Saved 30 examples to: finetuning_data.jsonl

SUCCESS! Fine-tuning data is ready.
```

**Verify the output**:
1. Open `finetuning_data.jsonl` in a text editor
2. Check that it has exactly 30 lines (one per article)
3. Spot-check line 1: Should start with `{"messages":`
4. Each line should be valid JSON with 3 messages (system, user, assistant)

---

## Phase 2: Upload and Fine-Tune (OpenAI Web UI - 30-60 minutes)

### Step 3: Access OpenAI Fine-Tuning Dashboard

1. Go to: https://platform.openai.com/finetune
2. Log in to your OpenAI account
3. You should see the "Fine-tuning" page

### Step 4: Create a New Fine-Tuning Job

**Click "Create"** button (top right)

You'll see a form with several sections:

#### A. Training Data
1. **Click "Upload file"**
2. Select your `finetuning_data.jsonl` file
3. Wait for upload to complete (~10 seconds)
4. OpenAI will automatically validate the format
   - ✓ Green checkmark = format is correct
   - ✗ Red X = format error (run the prep script again)

#### B. Model Selection
1. **Base model**: Select `gpt-4.1-2025-04-14`
   - This is the only GPT-4 model available for fine-tuning as of 2025
   - DO NOT use gpt-3.5-turbo or other models

#### C. Hyperparameters (Leave as DEFAULT)
According to your study design, use OpenAI's defaults:
- ✓ **Epochs**: Auto (typically 3-5)
- ✓ **Batch size**: Auto  
- ✓ **Learning rate multiplier**: Auto
- ✓ **Validation split**: Auto (typically 10-20%)

**Why defaults?**
- Kim & Lu (2024) used defaults
- Matches your study design for reproducibility
- OpenAI's auto-tuning is generally optimal

#### D. Model Suffix (Optional but Recommended)
- Enter a descriptive name: `cars50-biology-30articles`
- This helps you identify the model later
- Final model ID will be: `ft:gpt-4.1-2025-04-14:your-org:cars50-biology-30articles:xxxxx`

#### E. Validation File (Skip This)
- Leave blank - OpenAI will auto-split your training data

### Step 5: Start Fine-Tuning

1. Review the summary:
   - Training file: finetuning_data.jsonl (30 examples)
   - Base model: gpt-4.1-2025-04-14
   - Hyperparameters: Auto

2. **Click "Start fine-tuning"**

3. You'll see a confirmation with estimated cost
   - Expected: ~$10-20 for 30 examples
   - Click "Confirm"

### Step 6: Monitor Progress

**Training will go through these stages:**

1. **Validating files** (~30 seconds)
   - OpenAI checks your data format

2. **Queued** (~0-10 minutes)
   - Waiting for compute resources
   - Don't worry if this takes a few minutes

3. **Running** (~20-40 minutes)
   - Actual training happening
   - You'll see:
     - Current epoch (e.g., "Epoch 2/4")
     - Training loss (decreasing = good)
     - Validation loss (decreasing = good)
   - **You can close the browser** - training continues on OpenAI's servers

4. **Succeeded** 
   - Training complete!
   - Your model is ready to use

**What if it fails?**
- Check the error message
- Common issues:
  - Format error → re-run prepare_finetuning_data.py
  - Insufficient credits → add payment method
  - Invalid model selection → use gpt-4.1-2025-04-14

### Step 7: Get Your Fine-Tuned Model ID

**Once training succeeds:**

1. Click on your completed fine-tuning job
2. Look for **"Fine-tuned model"**
3. Copy the full model ID
   - Format: `ft:gpt-4.1-2025-04-14:your-org:cars50-biology-30articles:AbC123`
   - You'll need this for inference

4. **Save it somewhere safe** (you'll use it in the next step)

---

## Phase 3: Update Your Code (Local - 2 minutes)

### Step 8: Update llm_handler.py

Open `llm_handler.py` and find the `call_fine_tuned()` function.

**Before** (example placeholder):
```python
def call_fine_tuned(prompt, article_text, model_id):
    # model_id will be provided when calling this function
```

**After** (no changes needed in the function):
The function already accepts `model_id` as a parameter, so you're all set!

### Step 9: Test the Fine-Tuned Model

Create a simple test script:

```python
# test_finetuned.py
from llm_handler import call_fine_tuned
from pathlib import Path

# Load prompt
with open("prompts/system_prompt.txt", "r") as f:
    prompt = f.read()

# Load a test article (from validation or test set)
with open("gold_standard/CaRS-50/test/input/text001.txt", "r") as f:
    article = f.read()

# Your fine-tuned model ID (replace with yours!)
MODEL_ID = "ft:gpt-4.1-2025-04-14:your-org:cars50-biology-30articles:AbC123"

# Test the model
response, model_name = call_fine_tuned(prompt, article, MODEL_ID)

print("Model:", model_name)
print("\nResponse preview:")
print(response[:500])
```

Run it:
```bash
python test_finetuned.py
```

**Expected**: Annotated output with tags like [1a], [1b], etc.

---

## Phase 4: Run Your Study (Following Your Study Design)

### Phase 2: Single-Run Evaluation

From your STUDY_DESIGN_FINAL.md:

```bash
# A4: Fine-tuned (1 run on test set)
python run_condition.py A4 --model-id "ft:gpt-4.1-2025-04-14:your-org:cars50-biology-30articles:AbC123"
```

### Phase 3: Consistency Analysis

```bash
# Run 30 times for consistency analysis
for i in {1..30}; do
    python run_condition.py A4 --run-number $i --model-id "YOUR_MODEL_ID"
done
```

---

## Troubleshooting

### Issue: "File format invalid"
**Solution**: 
- Re-run `python prepare_finetuning_data.py`
- Check that output has exactly 30 lines
- Each line must be valid JSON

### Issue: "Model not available"
**Solution**: 
- Ensure you selected `gpt-4.1-2025-04-14`
- Check OpenAI's status page for availability

### Issue: "Insufficient quota"
**Solution**: 
- Add payment method to your OpenAI account
- Check your usage limits at https://platform.openai.com/usage

### Issue: Training loss not decreasing
**Solution**: 
- This is rare with good data
- If loss plateaus after 1 epoch, your data might have issues
- Check a few examples in finetuning_data.jsonl manually

### Issue: Model is overfitting (training loss << validation loss)
**Solution**: 
- This might happen with only 30 examples
- It's OK for your study design
- Document in your paper's limitations section

---

## Expected Results (From Kim & Lu 2024)

Based on similar studies, you can expect:

**Move-Level Accuracy**:
- Zero-shot: ~40-60%
- Few-shot: ~50-70%
- Fine-tuned: ~70-90% ✨

**Step-Level Accuracy**:
- Zero-shot: ~30-50%
- Few-shot: ~40-60%
- Fine-tuned: ~60-80% ✨

**Your results may vary** due to:
- Smaller training set (30 vs. Kim & Lu's 80)
- Different domain (Biology vs. Applied Linguistics)
- Simpler framework (11 vs. 23 categories)

---

## Checklist

**Before fine-tuning**:
- [ ] Ran verify_finetuning_setup.py (all ✓)
- [ ] Ran prepare_finetuning_data.py (success)
- [ ] Checked finetuning_data.jsonl (30 lines, valid JSON)
- [ ] Have OpenAI API key with credits

**During fine-tuning**:
- [ ] Uploaded finetuning_data.jsonl to OpenAI
- [ ] Selected model: gpt-4.1-2025-04-14
- [ ] Used default hyperparameters
- [ ] Started training
- [ ] Monitored progress (optional)

**After fine-tuning**:
- [ ] Copied fine-tuned model ID
- [ ] Saved model ID in safe place
- [ ] Tested model with test script
- [ ] Verified output format is correct
- [ ] Ready to run Phase 2 evaluation

---

## Questions to Consider

Before running your full study, confirm:

1. ✓ Do you have sufficient API credits for 124 total runs?
   - Phase 2: 4 runs
   - Phase 3: 120 runs (4 conditions × 30)
   - Estimated total: ~$150

2. ✓ Do you have time for consistency runs?
   - Each run: ~2-3 minutes
   - Total: ~6-8 hours of API time
   - Can run overnight or in batches

3. ✓ Have you documented your model ID?
   - You'll need it for all 30 fine-tuned runs
   - If you lose it, you'll have to fine-tune again

---

## Notes for Your Paper (Methods Section)

**Fine-Tuning Configuration**:

> We fine-tuned GPT-4 (gpt-4.1-2025-04-14) using OpenAI's supervised fine-tuning API with 30 training articles from the CaRS-50 Biology subset. The fine-tuning process used OpenAI's default hyperparameters (auto-configured epochs, batch size, and learning rate multiplier), following the methodology established by Kim & Lu (2024). Training took approximately [XX] minutes and achieved a final training loss of [X.XX] and validation loss of [X.XX]. The same fine-tuned model checkpoint was used for all 30 consistency evaluation runs.

**Record for your paper**:
- Fine-tuning start time: ___________
- Fine-tuning end time: ___________
- Total epochs: ___________
- Final training loss: ___________
- Final validation loss: ___________
- Fine-tuned model ID: ___________

---

## Good luck! 🚀

Remember:
- ✓ **First time fine-tuning is always a learning experience**
- ✓ **The UI is your friend** (much easier than API for first time)
- ✓ **Document everything** (model IDs, timestamps, losses)
- ✓ **Test before full runs** (verify output format)
- ✓ **Ask questions if stuck** (OpenAI support is responsive)

You've got this! Your preparation work has been excellent, and this is the final technical hurdle before you can run your actual study.
