# Methodological Transparency Document

## Study Classification

**This is a METHODOLOGICAL REPLICATION with adaptations, NOT a perfect replication.**

### What We Replicated from Kim & Lu (2024):
1. ✅ Core methodology (zero-shot, few-shot, fine-tuning comparison)
2. ✅ Evaluation metrics (precision, recall, F1, McNemar's test)
3. ✅ Statistical analysis approach
4. ✅ GPT-3.5-turbo model family
5. ✅ Target genre (research article introductions)

### What We Changed:
1. ❌ **Annotation framework**: Kim & Lu's 23-category system → CaRS-50's 11-category system
2. ❌ **Domain**: Applied Linguistics → Biology
3. ❌ **Dataset**: COSSRAI → CaRS-50
4. ❌ **Prompt structure**: Added minimal formatting instructions (see below)

---

## Prompt Modifications

### Kim & Lu's Original Prompt Philosophy:
- Designed for human readability
- Natural language instructions
- Open-ended output format
- Implicit formatting expectations

### Our Modifications (a1_zero_shot_v2_parseable.txt):
We added **4 lines** of explicit formatting instructions:

```diff
+ - Format your output as ONE tag and sentence per line
+ - Use EXACTLY this format: [tag] sentence text
+ - Do NOT add extra commentary, numbering, or explanation
+ - Begin each line with the tag(s) in square brackets
+ 
+ Example output format:
+ [1b] Photosynthesis is a fundamental process in plant biology.
+ [1c] Smith et al. (2020) demonstrated that light intensity affects chlorophyll production.
```

### Justification:
1. **Scientific**: Kim & Lu likely parsed outputs manually or semi-manually. For reproducible automation, explicit format specification is necessary.
2. **Conservative**: We added constraints on OUTPUT FORMAT, not on annotation decisions. The semantic instructions remain identical.
3. **Transparent**: We document this change clearly in methods section.

### What We Did NOT Change:
- ✅ The conceptual framing of genre analysis
- ✅ The definitions of moves and steps
- ✅ The examples provided
- ✅ The annotation decision-making guidance
- ✅ The instruction to use multiple tags when appropriate

---

## What to Say in Your Paper

### In the Methods Section:

> **Modifications from Kim & Lu (2024)**
>
> While we followed Kim & Lu's (2024) core methodology, we made three key adaptations:
>
> 1. **Annotation Framework**: We used the CaRS-50 scheme (Omotola et al., 2025) with 11 step-level categories instead of Kim & Lu's 23-category framework. This choice was dictated by our dataset's existing annotations. While this limits direct numerical comparison of step-level accuracy, it allows us to evaluate the **methodological approach** (prompting strategies) rather than the specific performance numbers.
>
> 2. **Domain**: We tested on Biology research articles rather than Applied Linguistics articles to assess cross-domain generalizability.
>
> 3. **Prompt Structure**: We added four lines specifying output format (e.g., "[tag] sentence text") to enable deterministic parsing. This modification affects output structure but not annotation decisions. The core instructional content—definitions, examples, and decision-making guidance—remains identical to Kim & Lu's approach. (See Appendix A for full prompt comparison.)

### In the Discussion Section:

> Our results demonstrate that Kim & Lu's (2024) **methodological approach** transfers effectively to [your findings]. While we cannot directly compare our 11-category step-level accuracy to their 23-category results, the **move-level accuracy** remains comparable, suggesting that their prompting strategies are robust to framework granularity. Future work should test their approach on the identical 23-category framework to enable direct numerical comparison.

### In the Abstract:

> Building on Kim & Lu's (2024) pioneering work, we conducted a **methodological replication** applying their prompting strategies (zero-shot, few-shot, fine-tuning) to Biology research articles using the CaRS-50 annotation framework. [Your results]

---

## What You CAN Compare

### ✅ Valid Comparisons:

1. **Move-level accuracy** (both have 3 moves)
   - Your Move 1 accuracy vs. Kim & Lu's Move 1 accuracy
   - Statistical significance of differences

2. **Methodological effectiveness**
   - Does few-shot improve over zero-shot? (direction and magnitude)
   - Does fine-tuning substantially outperform? (direction and magnitude)
   - Cost-benefit tradeoffs

3. **Statistical rigor**
   - McNemar's test results
   - Confidence intervals
   - Effect sizes

4. **Qualitative patterns**
   - Which moves/steps are hardest?
   - Error types
   - Model behavior

### ❌ Invalid Comparisons:

1. **Direct step-level accuracy numbers**
   - Your 11-category accuracy vs. their 23-category accuracy
   - REASON: Different number of classes affects difficulty

2. **Specific step performance**
   - Your "1a" performance vs. their "M1_S1a" performance
   - REASON: Categories may not align semantically

3. **Claims about "replicating their findings"**
   - REASON: Too many variables changed

---

## Contribution Statement

**What this study contributes:**

1. **Cross-domain validation**: First test of Kim & Lu's approach on Biology
2. **Framework robustness**: Test on simplified annotation scheme
3. **Methodological transparency**: Fully reproducible automated pipeline
4. **Practical extension**: Demonstrates applicability beyond Applied Linguistics

**What this study does NOT claim:**

1. ❌ "Replicating Kim & Lu's results"
2. ❌ "Validating their specific performance numbers"
3. ❌ "Testing the same annotation framework"

**Honest Framing:**

> We extend Kim & Lu's (2024) methodology to a new domain and annotation framework, demonstrating that their approach to LLM-assisted genre analysis is **methodologically sound and transferable**, while acknowledging that differences in framework granularity preclude direct numerical comparison of step-level performance.

---

## Parsing Strategy

**Decision: Deterministic rules-based parsing (NO LLM fallback)**

### Rationale:

1. **Reproducibility**: LLM-based parsing introduces non-determinism
2. **Transparency**: Rule-based logic is fully auditable
3. **Cost**: Avoid additional API costs
4. **Simplicity**: Direct regex parsing is sufficient for structured output

### Tradeoffs:

- **Pro**: 100% reproducible, no added complexity
- **Con**: May reject some valid but malformed outputs

### Conservative Approach:

- When uncertain → flag for manual review
- Comprehensive logging of all parsing decisions
- Statistics on parse success rates

This aligns with scientific best practices: **explicit > implicit**, **reproducible > flexible**.

---

## Summary

**This is methodological science, not perfect replication.**

You are testing whether **Kim & Lu's approach** (prompting strategies) works across:
- Different domains (Biology vs. Applied Linguistics)
- Different frameworks (11 vs. 23 categories)
- Automated pipelines (vs. their manual/semi-manual approach)

**This is valuable and publishable.**

Frame it honestly, document changes transparently, and focus on **methodological transfer** rather than numerical replication.
