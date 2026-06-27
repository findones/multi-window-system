# 🧭 Architect — Design Window

> This is the Architect role's primary workspace. Record design decisions, architecture evolution, open design questions.
> Different from `STATUS.md`: STATUS is cross-window and concise; this file is deep personal design journey.

---

## Design Decision Journey

### Version N: [Direction Name] (DATE)

**Motivation**: [Why design this way? What problem needs solving?]

**Core Ideas**:
- [Key idea 1]
- [Key idea 2]
- [Tradeoffs made]

**Validation Results**:
- [Experiment 1]: How to validate? What were the results?
- [Experiment 2]: [...]
- **Conclusion**: [Success/Failure, why?]

**Open Questions**:
- [Issue 1: Might need handling later]
- [Issue 2: ...]

---

### Version N-1: [Direction Name] (DATE)

**Motivation**: ...

---

## Current Design Spec

[Brief explanation of current architecture's core components]

**Architecture Diagram**:
```
[ASCII art or text description]

Input → [Module A] → [Module B] → [Module C] → Output
                        ↓
                   [Loss Function]
```

**Interface Requirements for Engineer**:
- Input: [shapes, types, ranges]
- Output: [shapes, types, ranges]
- Critical hyperparameters: [...]
- Target performance: [...]

**Why This Design**: [Deep explanation - this goes here, not in method.md which is just the spec]

---

## Open Design Questions

### Question 1: [Title]

**Background**: [Why is this a problem?]

**Option A**: [Pros/cons of approach A]
- Pros: [...]
- Cons: [...]

**Option B**: [Pros/cons of approach B]
- Pros: [...]
- Cons: [...]

**Suggested Experiment**: [How to validate?]

**Current Lean**: [Architect's preliminary thinking]

---

## Feedback for Engineer

[Any design feedback for Engineer goes here. Not instructions (those go in STATUS.md Handoff), but background information.]

---

## References / Inspiration

- [Paper 1]: [Why reference this]
- [Project 1]: [Why reference this]

---

## Example (Realistic Structure)

```
Design Decision Journey

### Version 3: Gated Residual Architecture (YYYY-MM-DD)

Motivation: 
Previous version (V2) used multiplicative fusion which showed instability in ablation tests.
Hypothesis: Additive residual connection would be more stable and preserve main signal.
Inspiration: Similar techniques work well in other domains.

Core Ideas:
- Use additive residual instead of multiplicative fusion
- Gate mechanism to control contribution weight
- Dropout on gating weights for regularization
- Bidirectional attention between feature streams

Validation:
- Experiment 1 (Stability test): V3 converges smoothly, loss curves are stable ✓
  → V2 by comparison shows oscillating loss in first 100 steps
- Experiment 2 (Ablation): Gating mechanism contributes +2.3% performance
  → Without gating: 79.5% → With gating: 81.8%
- Experiment 3 (Residual strength): Verified signal preservation (main stream 85% of output)
- Conclusion: V3 design is both stable and effective

Open Questions:
1. Should gating be learned per-sample or global?
   → Preliminary: per-sample is more flexible, but uses more parameters
2. Could we use attention instead of hardcoded gating?
   → Preliminary: yes, but more complex, defer to V4

### Version 2: Multiplicative Fusion (YYYY-MM-DD)

Motivation: ...
[Previous version details]

---

Current Design Spec

**Architecture Diagram**:
```
Text Input ────→ [Encoder A] ──→ [Fusion Module] ──→ [Classification] → Prediction
                                       ↑
Image Input ────→ [Encoder B] ────────┘
                  (with Gating)
```

**Interface for Engineer**:
- Input A (text): shape (batch, seq_len, 512), dtype float32
- Input B (image): shape (batch, channels, height, width), dtype float32  
- Output: shape (batch, num_classes), dtype float32
- Critical hyperparameters: 
  - gate_dropout: 0.1
  - fusion_attention_heads: 8
  - residual_strength: 0.5
- Target: ≥82% accuracy on validation set

---

Open Design Questions

### Question 1: Cross-stream Attention Direction

Background: Should secondary stream attend to primary, or bidirectional?

Option A (Unidirectional):
- Pros: Simpler, fewer parameters, faster inference
- Cons: May miss useful secondary→primary contributions

Option B (Bidirectional):
- Pros: Richer interaction, might improve results
- Cons: More parameters, slower inference, harder to debug

Suggested Experiment: 
- Run same setup with both approaches
- Compare accuracy, latency, parameter count
- Analyze attention weight distributions

Current Lean: Bidirectional is worth the overhead for this problem
```

---

## Checklist

When completing design iteration:
- [ ] Motivation clearly explained
- [ ] Validation experiments specified
- [ ] Open questions identified
- [ ] Update method.md with spec
- [ ] Write Handoff message in STATUS.md
- [ ] Update STATUS.md Role Dashboard
