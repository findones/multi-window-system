# 🔧 Engineer — Implementation Window

> This is the Engineer role's primary workspace. Record code changes, experiment runs, technical challenges faced, and technical decisions.
> Different from `CODE_MAP.md`: CODE_MAP is the "current interface bible"; this file is the "implementation journey".

---

## Implementation Log

### [DATE] [Feature/Module Name]

**Task**: [Instructions from Architect + background context]

**Implementation**:
- [Which files modified]
- [What was added]
- [What was removed]
- [Why this approach]

**Validation**:
- [CPU smoke test results]
- [GPU small-scale test results]
- [Final multi-seed results if applicable]

**Issues Encountered**:
- [Problem 1 + solution]
- [Problem 2 + solution]

**Code Quality**:
- [Performance metrics]
- [Memory usage]
- [Technical debt if any]

---

## Experiment Runs Log

### [DATE] [Experiment Name]

**Goal**: [What Architect wanted to validate?]

**Configuration**:
- Model: [...]
- Hyperparameters: [...]
- Dataset: [...]
- Seeds: [41, 73, 2026]

**Execution Status**:
- Device A (seed 41): [status]
- Device B (seed 73): [status]
- Device C (seed 2026): [status]

**Results**:
- [Metrics]
- [vs baseline comparison]
- [Conclusion]

**Code Changes**:
- [Which scripts modified]
- [New hyperparameters added]

---

## Pit Report (TL;DR)

[This section is a "pitfall guide" for future self and team. Record every important pitfall immediately when discovered.]

### Pitfall 1: [Pitfall Name]

**Symptom**: [When do you fall into this pit?]

**Root Cause**: [Why does this happen?]

**Solution**: [How to fix it]

**Prevention**: [How to avoid in the future]

---

## Performance Optimization Notes

[If you did any performance optimizations, record here]

- [Optimization 1]: Before [X] ms, after [Y] ms, method: [...]
- [Optimization 2]: ...

---

## Memory Optimization Notes

- [Optimization 1]: Before [X] GB, after [Y] GB, method: [...]
- [Optimization 2]: ...

---

## Feedback to Other Windows

[If you found design issues during implementation, write here. Use STATUS.md Handoff to notify Architect when design changes are needed.]

### [DATE] Design Feedback → Architect

**Issue**: [What specific problem did you encounter]

**Suggestion**: [What improvement would help]

**Impact**: [What happens if we don't fix this]

---

## Example (Realistic Structure)

```
Implementation Log

### 2026-06-15 Feature X Implementation

Task: Architect approved new architecture. Need to implement Module Y with the following requirements:
- Support input type A and type B
- Output should be optimized for latency
- Must integrate with existing Module Z

Implementation:
- Created models/feature_x.py with ModuleY class
- ModuleY: 
  - Takes inputs (data, config)
  - Produces optimized output
  - Includes validation checks
- Updated train.py to support --feature_x_enabled flag
- Created run_experiment.sh for ablation studies

Validation:
- CPU smoke test: forward/backward/eval all pass ✓
- GPU small test: 8 samples complete successfully ✓
- Full validation: 3-seed run with different configurations

Issues Encountered:
1. Initialization instability with certain configurations
   → Switched to Xavier initialization instead of Kaiming
   → Verified convergence is now stable
2. Input truncation issues
   → Adjusted max input length to 512
   → Verified zero truncation on full dataset (10K samples)

Code Quality:
- New parameters: 2.5M (3% increase relative to baseline)
- Memory at batch=16: ~16GB (acceptable)
- Inference overhead: +2% (minimal impact)

Performance Notes:
- Critical section: Module Y attention mechanism uses most memory
- Future optimization: could use Flash Attention if memory becomes bottleneck

---

Experiment Runs Log

### 2026-06-20 Feature X Ablation Study

Goal: Validate contribution of each component in Feature X

Configuration:
- Model: BaselineV1 + Feature X
- Hyperparameters: lr=0.001, batch=16, epochs=20
- Dataset: StandardBench
- Seeds: 41, 73, 2026

Results:
- Full system: 82.5% ± 0.8%
- Without component A: 81.2% ± 0.9% (-1.3%)
- Without component B: 82.1% ± 0.7% (-0.4%)
- Conclusion: Component A is the critical contribution; B is minor

Code Changes:
- run_experiment.sh: added --disable_component_a / --disable_component_b flags
- train.py: added feature_x_ablate_mode parameter
```

---

## Template Checklist

When completing implementation:
- [ ] All code modifications done
- [ ] Test results recorded
- [ ] Pitfalls documented
- [ ] Update CODE_MAP.md
- [ ] Write Handoff message in STATUS.md
- [ ] Update STATUS.md Role Dashboard
