# ✍️ Paper — Writing Window

> This is the Paper role's primary workspace. Record narrative, outline, writing progress, key data points.
> Different from `RESULTS.md`: RESULTS is data table (pure numbers); this file is writing log (story and arguments).

---

## Main Narrative

[What's the core story of this project? What problem does it solve? What's the key contribution? Summarize in 2-3 paragraphs]

---

## Paper Outline

### 1. Introduction
- Problem statement
- Related work gap
- Our contribution
- Paper structure

### 2. Related Work
- [Related area 1]
- [Related area 2]
- [Related area 3]

### 3. Method
- Core approach/algorithm
- Design choices and motivation
- Key innovations

### 4. Experiments
- Experimental setup
- Baselines and comparisons
- Ablation studies
- Analysis and insights

### 5. Results & Discussion
- Main findings
- Comparison with prior work
- Limitations
- Future work

### 6. Conclusion

---

## Core Arguments

### Argument 1: [Main Claim]

**Supporting Evidence**:
- [Evidence from RESULTS.md]
- [Comparative analysis showing...]
- [Statistical significance]

**Anticipated Objections**:
- Objection 1 → Our response
- Objection 2 → Our response

### Argument 2: [Secondary Claim]

[Similar structure]

---

## Writing Progress

- [ ] Introduction draft
- [ ] Related work draft
- [ ] Method section draft
- [ ] Experiments section draft
- [ ] Results summary draft
- [ ] Full draft complete
- [ ] First review
- [ ] Final revisions

---

## Key Data Points (from RESULTS.md)

[Keep updated from RESULTS.md - don't repeat lookup work]

| Configuration | Result | Notes |
|---|---|---|
| Baseline | [value] | Reference |
| Our Method | [value] | Main result |
| Ablation 1 | [value] | Shows component importance |
| Ablation 2 | [value] | Shows component importance |

---

## Figures & Tables to Generate

- [ ] Architecture comparison diagram
- [ ] Results comparison table
- [ ] Ablation analysis chart
- [ ] Case studies (3-5 examples)
- [ ] Performance breakdown by category

---

## Writing Notes

### [DATE] [Section Name]

**Current Status**: [Where writing stands]

**Challenges**:
- [Challenge 1 + solution]
- [Challenge 2 + solution]

**Feedback Needed From**:
- [Architect feedback on design discussion]
- [Engineer feedback on implementation details]

---

## Example (Realistic Structure)

```
Main Narrative

In real-world classification tasks, combining multiple information sources (text and image) 
is crucial but challenging. Existing approaches struggle to properly integrate diverse modalities.

We propose a Multi-Modal Fusion architecture that uses learnable gating mechanisms to 
dynamically weight different information streams. Compared to baseline approaches, our method 
achieves +2.5% improvement while using 30% less parameters.

Core evaluation on the benchmark dataset shows consistent gains across multiple configurations 
and ablation studies validate the importance of each design component.

---

Core Arguments

### Argument 1: Our Architecture Outperforms Baselines

Supporting Evidence:
- RESULTS.md Table 1: Our method 84.5% > Baseline A 83.2% (+1.3%)
- Statistical significance: difference > 2× standard deviation
- Ablation Study (Table 2): Each component contributes +0.3-0.5%

Anticipated Objections:
- "Isn't the improvement just from using more parameters?" 
  → No. RESULTS.md Table 3 shows our method has 30% FEWER parameters than baseline
- "Maybe it's just better hyperparameter tuning?"
  → We used identical hyperparameters and training procedure for fair comparison

### Argument 2: Design Components Are Necessary

Supporting Evidence:
- Ablation Study in RESULTS.md Table 2
- Without gating: 83.8% (-0.7%)
- Without attention: 83.1% (-1.4%)
- Conclusion: All components are important

---

Key Data Points

| Config | Accuracy | Parameters | Memory | Notes |
|---|---|---|---|---|
| Baseline A | 83.2% | 95M | 12GB | Reference |
| Baseline B | 83.8% | 120M | 16GB | Alternative |
| Our Method | 84.5% | 65M | 8GB | Proposed |
| - No Gating | 83.8% | 60M | 7GB | Ablation |
| - No Attention | 83.1% | 55M | 6GB | Ablation |

```

---

## Tone & Style Reminders

- Keep technical but accessible to broad audience
- Ground all claims in RESULTS.md numbers
- Avoid overclaiming - stick to evidence
- Balance "what" with "why"
- Use concrete examples from ablations

---

## Checklist

When completing writing section:
- [ ] Claims grounded in RESULTS.md
- [ ] Evidence supports conclusions
- [ ] Anticipated criticisms addressed
- [ ] Data cited accurately
- [ ] Write Handoff in STATUS.md
- [ ] Update STATUS.md Role Dashboard
