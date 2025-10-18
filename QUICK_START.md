# Quick Start: Test Your Parser

## Step 1: Test the Parser (2 minutes)

```bash
python test_parser.py
```

**Expected output:**
```
============================================================
TEST 1: Perfect Format
============================================================

Parsed 4 sentences
Warnings: 0

Sample output:
{'sentence_num': 1, 'text': 'Photosynthesis is a fundamental biological process.', ...}

... (more tests) ...

============================================================
PARSER VALIDATION COMPLETE
============================================================

Ready to parse real LLM outputs!
```

---

## Step 2: Update Your Run Script (1 minute)

Edit `run_pilot.py`:

```python
# Change this line:
CONDITION = "a1_zero_shot"

# To this:
CONDITION = "a1_zero_shot_v2_parseable"

# And make sure your prompt path is:
PROMPT_FILE = f"prompts/{CONDITION}.txt"
```

---

## Step 3: Run a Single Test Article (3 minutes)

```python
# In run_pilot.py, set:
ARTICLES = range(1, 2)  # Just text001

# Then run:
python run_pilot.py
```

**Expected**: LLM outputs saved to `pilot_outputs/a1_zero_shot_v2_parseable/text001_a1_zero_shot_v2_parseable.txt`

---

## Step 4: Parse the Output (1 minute)

```bash
python parse_llm_output.py
```

**Expected output:**
```
Found 1 files to parse

Parsing: text001_a1_zero_shot_v2_parseable.txt
  ✓ Parsed 23 sentences
  ⚠️  2 warnings

==================================================
BATCH SUMMARY
==================================================
Total sentences parsed: 23
Total warnings: 2

⚠️  Check individual JSON files for warning details
```

---

## Step 5: Check the Parsed JSON (1 minute)

```bash
# View the parsed output
cat pilot_outputs/a1_zero_shot_v2_parseable_parsed/text001_a1_zero_shot_v2_parseable_parsed.json
```

**Expected structure:**
```json
{
  "article_id": "text001_a1_zero_shot_v2_parseable",
  "source_file": "...",
  "parsed_at": "2025-01-18T...",
  "sentences": [
    {
      "sentence_num": 1,
      "text": "Central components of animal cognition are...",
      "tags": ["1b"],
      "primary_tag": "1b",
      "move": "1",
      "parse_confidence": "high",
      "original_line": "[1b] Central components of animal cognition are..."
    },
    ...
  ],
  "parse_stats": {
    "total_lines": 25,
    "parsed_sentences": 23,
    "skipped_lines": 2,
    "warnings": [...]
  }
}
```

---

## Step 6: Review Warnings (if any)

Warnings indicate lines that couldn't be parsed. Common causes:
- Empty lines (harmless)
- Preamble text (e.g., "Here are my annotations:")
- Invalid tag formats

**Check the parse_stats.warnings** in the JSON to see what was skipped.

---

## Step 7: Compare to Gold Standard (Manual Check)

```bash
# View gold standard for text001
cat gold_standard/text001.json

# Compare visually with parsed output
# Do the tags match?
```

**Quick check:**
- Are sentence numbers aligned?
- Do tags match?
- Are multi-tag sentences handled correctly?

---

## If Everything Looks Good: Run Full Pilot

```python
# In run_pilot.py, change to:
ARTICLES = range(1, 11)  # All 10 pilot articles

# Run full pilot
python run_pilot.py

# Parse all outputs
python parse_llm_output.py

# Next: Build evaluation script (coming soon)
```

---

## Troubleshooting

### Problem: "No files found"

**Solution**: Check that your output directory exists and has the right files:
```bash
ls pilot_outputs/a1_zero_shot_v2_parseable/
```

### Problem: "Parse confidence: medium" or many warnings

**Solution**: Inspect the warnings in the JSON file:
```python
import json
with open('pilot_outputs/.../text001_parsed.json') as f:
    data = json.load(f)
    for w in data['parse_stats']['warnings']:
        print(f"Line {w['line']}: {w['message']}")
        print(f"  Text: {w['text']}\n")
```

Common issues:
- LLM added commentary → Adjust prompt
- Inconsistent formatting → Check LLM output manually
- Invalid tags → Check if LLM hallucinated new tags

### Problem: Very few sentences parsed

**Solution**: 
1. Check raw LLM output file manually
2. Verify it's using the new prompt format
3. Look for systematic formatting issues

---

## What's Next?

After successful parsing:

1. **Build evaluation script** (compares parsed vs. gold standard)
2. **Calculate metrics** (precision, recall, F1, accuracy)
3. **Run all 7 pilot conditions**
4. **Analyze results**
5. **Choose best method for Phase 2**

---

## Quick Reference

| Command | Purpose |
|---------|---------|
| `python test_parser.py` | Test parser on synthetic data |
| `python run_pilot.py` | Generate LLM annotations |
| `python parse_llm_output.py` | Parse LLM outputs to JSON |
| `cat gold_standard/text001.json` | View gold standard |
| `cat pilot_outputs/.../text001_parsed.json` | View parsed output |

---

## Success Criteria

✅ **Parser works** if:
- Parsed >80% of sentences
- <5 warnings per article
- JSON structure matches gold standard format
- Multi-tag sentences handled correctly

✅ **Prompt works** if:
- LLM follows format instructions
- Tags are valid CaRS-50 codes
- Sentences are properly segmented
- No hallucinated commentary

**If both pass → You're ready for full pilot! 🚀**
