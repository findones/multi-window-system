#!/usr/bin/env python3
"""
Multi-Window Project Management System Skill
Initialize project templates for clean multi-window AI collaboration
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime

# Template content for each file (minimal defaults)
TEMPLATES = {
    "STATUS.md": """# 🚦 STATUS — {project_name}

> **Every window reads this file first** to sync status and tasks.
> This is the only cross-window communication channel.

## One-Sentence Status

[Project status in 1-2 sentences]

## Current Roadmap

- [Main line]: [What we're working on]
- [Sub-line 1]: [Status]
- [Sub-line 2]: [Status]

## 📁 Document Map

| Role | Main Doc | Start Here |
|---|---|---|
| 🧭 Architect | `docs/roles/architect.md` | STATUS → method.md → architect.md |
| 🔧 Engineer | `docs/roles/engineer.md` | STATUS → CODE_MAP.md → engineer.md |
| ✍️ Paper | `docs/roles/paper.md` | STATUS → RESULTS.md → paper.md |
| 🔬 Repro | `docs/roles/repro.md` | STATUS → method.md → repro.md |

## 👥 Role Dashboard

### 🧭 Architect
- Working on: [Task]
- Next: [Task]
- Latest output: [Date] — [What completed]

### 🔧 Engineer
- Working on: —
- Next: —
- Latest output: —

### ✍️ Paper
- Working on: —
- Next: —
- Latest output: —

### 🔬 Repro
- Working on: —
- Next: —
- Latest output: —

## 🔁 Handoff Messages

Format: **[Date] [From] → [To]: [Title]**
- Details as bullet points

Example:
```
- **2024-01-15 Architect → Engineer**:
  New architecture design ready for implementation
  - See method.md §1 for spec
  - Implement models/new_arch.py
  - Run 3-seed validation
  - Report results back
```

---

Generated: {date}
""",

    "method.md": """# Architecture & Method

## 1. Overview

[Describe your project's core architecture]

## 2. Key Components

### Component A
[Responsibility, interface, design choices]

### Component B
[...]

## 3. Training Strategy

[Optimizer, learning rate, batch size, schedule, etc.]

## 4. Evaluation Metrics

[Primary and secondary metrics]

## 5. Design Decisions

- [Decision 1] → [Validation result]
- [Decision 2] → [Validation result]

---

See `docs/roles/architect.md` for design evolution
""",

    "CODE_MAP.md": """# Code Interface Guide

> **Living document of your codebase**. Update whenever code changes.

## File Structure

```
project/
├── models/
│   ├── model_a.py       [Main model]
│   └── model_b.py       [Helper model]
├── data/
│   └── dataset.py       [Data loading]
├── scripts/
│   ├── run_train.sh     [Training script]
│   └── run_eval.sh      [Evaluation script]
└── configs/
    └── base.py          [Configuration hub]
```

## Key Files

### models/model_a.py

**Responsibility**: [What it does]

**Key Classes**:

#### class ModelA(nn.Module)

**Init Parameters**:
- `param1` (type, default): [Description]
- `param2` (type, default): [Description]

**Key Methods**:

##### forward(input_a, input_b) → output

Input shapes: [...]
Output shapes: [...]
⚠️ Important: [Modifications affect...]

## Modification Risk

| File | Change | Risk | Sync With |
|---|---|---|---|
| models/model_a.py | forward signature | High ⚠️ | eval.py, train.py |
| data/dataset.py | return keys | High ⚠️ | train.py |
| configs/base.py | defaults | Low | Engineer (for reproducibility) |

## Known Technical Debt

- [Item 1]: [When? Priority? Fix?]
- [Item 2]: [...]

---

See `docs/roles/engineer.md` for implementation details
""",

    "RESULTS.md": """# Experiment Results

## Summary

| Config | Metric | Date | Notes |
|---|---|---|---|
| Baseline | [Value] | YYYY-MM-DD | Reference point |
| Version 1 | [Value] | YYYY-MM-DD | [Status] |

## Detailed Results

### [Experiment Name]

| Setting | Value | vs Baseline | Status |
|---|---|---|---|
| [Setting 1] | [Value] | [Δ] | ✓/✗ |
| [Setting 2] | [Value] | [Δ] | ✓/✗ |

## Ablation Studies

[When you run ablations, record results here]

---

Updated: {date}
""",

    "WORK_PLAN.md": """# Work Changelog

> **Time-indexed log** (not status board).
> For status, see STATUS.md.

## Changelog

### {date}

- [Work 1]: [Brief summary]
- [Work 2]: [Brief summary]
- [Key metrics]: [Numbers]

### [Earlier Dates]

[Earlier work...]

---

## Early Planning (if applicable)

- Phase 0: [Goals + timeline]
- Phase 1: [...]
- Phase 2: [...]
"""
}

ROLE_TEMPLATES = {
    "architect": """# 🧭 Architect — Design Window

> Your role: Strategic design decisions & architecture evolution.
> Record WHY, not just WHAT.

## Design Evolution

### Version N: [Architecture Name]

**Motivation**: [Why this approach?]

**Core Ideas**:
- [Idea 1]
- [Idea 2]

**Validation**:
- Experiment 1: [Result]
- Experiment 2: [Result]
- **Conclusion**: [Success/Failure]

**Open Questions**:
- [Question 1]
- [Question 2]

### Version N-1: [Previous Architecture]

[Same structure as above]

## Current Design Spec

[Summarize current architecture briefly]

**Architecture diagram** (ASCII or description):
```
[Your architecture here]
```

## Pending Decisions

### Decision Topic 1

**Question**: [What to decide?]

**Option A**: [Pros/cons]

**Option B**: [Pros/cons]

**Recommendation**: [Your initial thought]

---

Related files:
- method.md — Current architecture spec
- STATUS.md — Cross-window decisions
""",

    "engineer": """# 🔧 Engineer — Implementation Window

> Your role: Code implementation, experiments, troubleshooting.
> Record HOW and encountered issues.

## Implementation Log

### [Date] [Feature/Module Name]

**Task**: [What Architect asked for]

**Implementation**:
- Modified files: [...]
- New code: [...]
- Deleted: [...]
- Why: [...]

**Validation**:
- CPU smoke test: ✓
- GPU small test: ✓
- Full 3-seed: [Results]

**Issues Encountered**:
- Issue 1: [How solved]
- Issue 2: [How solved]

## Experiment Log

### [Date] [Experiment Name]

**Goal**: [What we're testing]

**Config**:
- Model: [...]
- Params: [...]
- Dataset: [...]
- Seeds: [41, 73, 2026]

**Results**:
- [Numbers]
- vs baseline: [Comparison]
- Conclusion: [...]

## Pitfall Record

### Pitfall: [Name]

**Symptoms**: [When does it occur?]

**Root Cause**: [Why?]

**Solution**: [How to fix]

**Prevention**: [How to avoid next time]

---

Related files:
- CODE_MAP.md — Code interfaces
- STATUS.md — Task assignments
""",

    "paper": """# ✍️ Paper — Writing Window

> Your role: Storytelling, narrative, writing.
> Connect results to bigger picture.

## Main Narrative

[What's the core story of this project?]

## Paper Outline

### 1. Introduction
- Problem statement
- Related work
- Our contribution

### 2. Method
- [Core method name]
- [Design choices]

### 3. Experiments
- Baselines
- Ablations
- Results analysis

### 4. Discussion
- Findings
- Limitations
- Future work

## Key Arguments

### Argument 1: [Title]

**Supporting Evidence**:
- [Evidence from RESULTS.md]
- [Ablation that shows...]

**Anticipated Criticisms**:
- Objection 1 → Our response
- Objection 2 → Our response

## Writing Progress

- [ ] Introduction draft
- [ ] Method section draft
- [ ] Results section draft
- [ ] Full draft complete
- [ ] First review
- [ ] Final revision

## Key Data Points

[Keep updated from RESULTS.md]

| Configuration | Result | Notes |
|---|---|---|
| Baseline | [Value] | Reference |
| Our Method | [Value] | Main result |

---

Related files:
- RESULTS.md — Experiment data
- method.md — Architecture details
""",

    "repro": """# 🔬 Repro — Research Window

> Your role: Literature analysis, reference investigation, feasibility studies.
> Help Architect expand horizons.

## Research Topics (from Architect)

### Topic 1: [Research Question]

**Goal**: [What to find out?]

**Progress**:
- [ ] Search literature
- [ ] Analyze code/papers
- [ ] Feasibility assessment
- [ ] Report findings

**Findings**:
[What did you discover?]

**Recommendations**:
- Worth trying: [...]
- Worth investigating: [...]
- Not recommended: [... because ...]

## Reference Paper Analysis

### Paper: [Title & Authors]

**Published**: [Conference/Journal]

**Core Innovation**: [1-sentence summary]

**Technical Details**:
- Technique 1: [How does it work?]
- Technique 2: [How does it work?]

**Relevance to Our Project**:
- [Problem overlap]
- [Potential insights]

**Reference**: [DOI / GitHub]

## Reference Code Analysis

### Project: [Name & Link]

**Purpose**: [What does it do?]

**Key Modules**:

#### Module A
- File: [...]
- Function: [...]
- Core logic: [...]
- Relevance: [...]

**Feasibility**:
- Could we use this? [Yes/No/Maybe]
- Cost: [What's required?]
- Benefit: [What would we gain?]

**Recommendation**: [Should we try?]

## Knowledge Base

[Collect useful snippets, references, ideas here]

- [Resource 1]: [Why relevant]
- [Resource 2]: [Why relevant]

---

Related files:
- method.md — Architecture to inform
- architect.md — Design discussions
"""
}

def create_template_files(output_dir, project_name, language, roles):
    """Create all template files in output directory"""

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True, parents=True)

    # Create main templates
    date = datetime.now().strftime("%Y-%m-%d")

    # STATUS.md with project name
    status_content = TEMPLATES["STATUS.md"].format(
        project_name=project_name,
        date=date
    )
    (output_path / "STATUS.md").write_text(status_content)

    # Other main templates
    for filename in ["method.md", "CODE_MAP.md", "RESULTS.md"]:
        content = TEMPLATES[filename]
        (output_path / filename).write_text(content)

    # WORK_PLAN with date
    work_plan = TEMPLATES["WORK_PLAN.md"].format(date=date)
    (output_path / "WORK_PLAN.md").write_text(work_plan)

    # Create role documents
    docs_roles = output_path / "docs" / "roles"
    docs_roles.mkdir(exist_ok=True, parents=True)

    for role in roles:
        if role in ROLE_TEMPLATES:
            content = ROLE_TEMPLATES[role]
            (docs_roles / f"{role}.md").write_text(content)

    return output_path

def main():
    parser = argparse.ArgumentParser(
        description="Initialize Multi-Window Project Management System"
    )
    parser.add_argument("project_name", help="Name of your project")
    parser.add_argument("--description", "-d", help="Project description")
    parser.add_argument(
        "--language", "-l",
        choices=["en", "zh"],
        default="en",
        help="Documentation language"
    )
    parser.add_argument(
        "--roles", "-r",
        default="architect,engineer,paper,repro",
        help="Comma-separated list of roles to initialize"
    )
    parser.add_argument(
        "--output", "-o",
        default=".",
        help="Output directory"
    )

    args = parser.parse_args()

    roles = [r.strip() for r in args.roles.split(",")]

    print(f"🚀 Initializing Multi-Window Project: {args.project_name}")
    print(f"   Language: {args.language}")
    print(f"   Roles: {', '.join(roles)}")
    print(f"   Output: {args.output}")

    try:
        output_path = create_template_files(
            args.output,
            args.project_name,
            args.language,
            roles
        )

        print(f"\n✅ Successfully created:")
        print(f"   - STATUS.md (cross-window status board)")
        print(f"   - method.md (architecture spec)")
        print(f"   - CODE_MAP.md (code interface)")
        print(f"   - RESULTS.md (experiment results)")
        print(f"   - WORK_PLAN.md (changelog)")
        for role in roles:
            print(f"   - docs/roles/{role}.md ({role} workspace)")

        print(f"\n📖 Next steps:")
        print(f"   1. Edit STATUS.md with your project details")
        print(f"   2. Open 4 Claude Code windows (one per role)")
        print(f"   3. Each window: read STATUS.md first, then role file")
        print(f"   4. Start working!")

        return 0

    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
