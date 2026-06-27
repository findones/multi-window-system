# 🚦 STATUS — {project_name}

> **Every window reads this file first**, then reads your role document (see "Document Map" below).
> This board is the **ONLY real-time communication channel** between 4 role windows (🧭 Architect / 🔧 Engineer / ✍️ Paper / 🔬 Repro) — windows don't share context, only communicate via this document.
> **After completing work, you MUST update this board's "Role Dashboard" + "Handoff Messages"**. Latest update: **[DATE]** by 【WINDOW】.

---

## One-Sentence Status

[What is the project status? What's the key progress/bottleneck? Summarize in 1-2 sentences]

**Examples:**
- Core architecture is validated. Current focus: optimization and edge case handling.
- MVP complete, currently testing integration with external systems.

---

## Current Roadmap & Next Steps

### Main Lines
- [✅/🚧] **[Main Line Name]** — [Brief description]
- [✅/🚧] **[Sub-line 1]** — [Description, validated/archived/in progress]
- [❌/📋] **[Failed Line]** — [Why it failed, when stopped]

### Priority Queue
1. [Highest] — [Why priority, when to do]
2. [Medium] — [...]
3. [Can Parallel] — [Which tasks are independent]

**Examples:**
- ✅ **Architecture V1** — Baseline complete, 82.5% accuracy on test set
- 🚧 **Performance Optimization** — Latency improvements in progress (target: <100ms)
- ❌ **Experimental Approach X** — Did not meet success criteria, archived as negative result
- **Next Priority**: ① Implement feature Y ② Write comprehensive tests ③ Deployment preparation

---

## 📁 Document Map & Reading Protocol

| Role | Primary Doc (you write here) | Orientation (read first) |
|---|---|---|
| 🧭 Architect | `docs/roles/architect.md` (design decisions) + `method.md` (architecture spec) | STATUS → method.md → docs/roles/architect.md |
| 🔧 Engineer | `docs/roles/engineer.md` (implementation logs) + `CODE_MAP.md` (interfaces) + code | STATUS → CODE_MAP.md → docs/roles/engineer.md |
| ✍️ Paper | `docs/roles/paper.md` (narrative/outline/draft) + `RESULTS.md` (results) | STATUS → RESULTS.md → method.md → docs/roles/paper.md |
| 🔬 Repro | `docs/roles/repro.md` (reference analysis) | STATUS → method.md → docs/roles/repro.md |
| — Shared Results | `RESULTS.md` (results table, updater updates after getting data) | All roles as needed |
| — Work Log | `WORK_PLAN.md` (time-indexed changelog, NOT status board) | Check when needing historical details |

> Deep documents (method/CODE_MAP/RESULTS/WORK_PLAN) stay in root directory (heavily referenced); role documents are in `docs/roles/`.

---

## 👥 Role Dashboard (Current / Next / Latest Output)

### 🧭 Architect
- Current: [Current task]
- Next: [Next priority task]
- Latest output (DATE): [What completed]

**Example:**
- Current: Designing feature Y based on performance bottleneck analysis
- Next: Create V2 architecture spec with optimizations
- Latest output (YYYY-MM-DD): Performance analysis complete, documented in method.md §3

### 🔧 Engineer
- Current: [...]
- Next: [...]
- Latest output (DATE): [...]

### ✍️ Paper
- Current: [...]
- Next: [...]
- Latest output (DATE): [...]

### 🔬 Repro
- Current: [...]
- Next: [...]
- Latest output (DATE): [...]

---

## 🔁 Handoff Messages (Newest First - Cross-Window Communication)

> Format: `- **【DATE】 【SENDER】 → 【RECIPIENT】**: 【Brief Title】`
> Then indent sub-bullets with detailed information. This is the **ONLY communication channel** between windows.

**Example:**
```
- **YYYY-MM-DD 🧭 Architect → 🔧 Engineer**:
  **Feature Y architecture design complete, ready for implementation.**
  - Architecture spec added to method.md §3.2
  - Requires optimization in module X
  - Expected implementation time: 3 days
  - Run tests after implementation

- **YYYY-MM-DD 🔧 Engineer → 🧭 Architect / ✍️ Paper**:
  **Feature Y implementation complete, performance test results ready.**
  - Latency improved from 250ms to 95ms
  - All tests passing (20/20)
  - See CODE_MAP.md for code changes
  - See RESULTS.md §2.1 for performance numbers

- **YYYY-MM-DD 🧭 Architect → 🔧 Engineer**:
  **Please implement Feature X with the following requirements:**
  - Performance target: <100ms response time
  - Memory usage: <500MB
  - Code modifications needed: modules/core.py, modules/optimizer.py
  - Implementation approach: See method.md §2.3
  - Validation: Run test suite in tests/test_core.py
```

---

## Red Lines (All Windows Must Follow)

**Everyone must obey:**

1. **STATUS.md is the ONLY cross-window communication channel** — no Slack / email / notes. Everything goes here.
2. **Update immediately after completing tasks** — don't wait until project end. Update at every checkpoint.
3. **Read STATUS.md first every time you enter a window** — understand global state and check for Handoff messages for you.
4. **Strict role boundaries** — Architect only modifies method.md, Engineer only modifies code + CODE_MAP.md, etc.
5. **Keep deep documents in root directory** — don't move method.md/CODE_MAP.md/RESULTS.md to docs/roles/

---

## Quick Navigation

| Need | Go to |
|---|---|
| New to project, want overview | Read this board's "One-Sentence Status" + "Current Roadmap" |
| I'm Architect, want to continue design | Check "Handoff Messages" for tasks for you → go to docs/roles/architect.md |
| I'm Engineer, want to implement | Check "Handoff Messages" for Architect's instructions → reference CODE_MAP.md for code changes |
| I'm Paper, want to write | Read RESULTS.md latest data → read method.md architecture → modify docs/roles/paper.md |
| I want detailed design | Read method.md (current spec) + docs/roles/architect.md (design evolution) |
| I want code changes | Read CODE_MAP.md + docs/roles/engineer.md (technical challenges faced) |
| I want results | Read RESULTS.md (results table) + STATUS.md Handoff (results summary) |
| I want work history | Read WORK_PLAN.md (time-indexed changelog) |

---

## Example: Complete Workflow

Suppose you're the Architect entering today:

1. **Read this file's** "One-Sentence Status"
   ```
   Status: Core architecture validated. Current focus: optimization and deployment readiness.
   ```

2. **Read this file's** "Handoff Messages" to find messages for you
   ```
   - **YYYY-MM-DD 🔧 Engineer → 🧭 Architect**: Feature Y complete, see RESULTS.md...
   ```

3. **Jump to** `docs/roles/architect.md`
   ```
   Read "Latest Output" to see what you did last time
   Read "Next Tasks" to see what to do next
   ```

4. **After completing work** (e.g., designing optimization strategy)
   ```
   1. Update method.md with new design (e.g., add §3.5 Optimization Strategy)
   2. Update docs/roles/architect.md with your work
   3. Come back here and write a Handoff to Engineer:
      - **YYYY-MM-DD 🧭 Architect → 🔧 Engineer**:
        **Optimization strategy design complete, ready for implementation.**
        - method.md §3.5 defines the optimization approach
        - Expected performance improvement: 40%
        - New modules needed: modules/optimizer.py
        - 3 ablation experiments suggested: see method.md
   4. Update this board's "Role Dashboard" Architect row with "Latest Output"
   ```

5. **Next window's Engineer enters**
   ```
   1. Read STATUS.md "One-Sentence Status" + "Handoff Messages"
   2. See Architect's task for you
   3. Go to docs/roles/engineer.md and start implementation
   4. After experiments, come back to STATUS.md with Handoff: task complete, results in RESULTS.md
   ```

---

## Why This System Works

### 1. Context Isolation
Each window focuses only on its role and related information. 4 windows = 4× total context.

### 2. Async Collaboration
No "real-time meetings" needed. Everyone works at their own pace, syncs via STATUS.md.

### 3. Traceable Decisions
Handoff messages form a complete "decision history." Months later, you can ask "why did we abandon approach X?" and find the answer.

### 4. Lower Cognitive Load
One window = one role = one mindset. No constant context switching.

---

## FAQ

**Q: Is splitting into 4 windows overkill for one person?**

A: No. Even solo, you can:
- Morning: Architect mode (design)
- Afternoon: Engineer mode (coding)
- Next day: Paper mode (writing)
- Each window stays clean

**Q: How to handle urgent interruptions?**

A: Mark with 🚨 in STATUS.md Handoff messages. The next person in that role will see it immediately.

**Q: Can we add new roles mid-project?**

A: Yes. Create `docs/roles/new_role.md` and add a new row to this board.

---

Generated: {date}
