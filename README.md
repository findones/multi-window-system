# Multi-Window Project Management System

## English | [中文](#中文版本)

---

## Overview

A proven system for managing large AI-assisted projects without context explosion.

**Problem**: Single AI conversation window handling multiple roles (design, engineering, writing, research) causes:
- Context fills up quickly
- AI forgets important decisions
- Repeated mistakes
- Unclear decision chains

**Solution**: 
- 4 separate role windows (Architect / Engineer / Paper / Repro)
- 1 shared STATUS.md for sync and decisions
- Clean context + clear thinking + traceable decisions

---

## Features

✅ **4 Role Windows** — Each window = one role = focused context
✅ **Central Sync Point** — STATUS.md is the single source of truth
✅ **Decision Logging** — Every decision tracked via Handoff messages
✅ **Complete Templates** — Copy and use immediately
✅ **Best Practices** — Deep design document explaining why it works

---

## Quick Start

### Step 1: Clone and Setup (30 seconds)

```bash
git clone https://github.com/findones/multi-window-system.git
cd multi-window-system
python init.py "My Project Name" --language en
```

### Step 2: Initialize Your Project (5 minutes)

```bash
# Edit STATUS.md with your project details
nano STATUS.md
```

### Step 3: Start Working

Open 4 Claude Code windows (one per role):

| Window | Role | File |
|--------|------|------|
| 1️⃣ | Architect | `docs/roles/architect.md` |
| 2️⃣ | Engineer | `docs/roles/engineer.md` |
| 3️⃣ | Paper | `docs/roles/paper.md` |
| 4️⃣ | Repro | `docs/roles/repro.md` |

**Workflow**: Each window reads STATUS.md first → works in role document → updates STATUS.md with Handoff messages.

---

## Documentation

- **[README.md](docs/README.md)** — System overview & core concepts (5 min read)
- **[DESIGN.md](docs/DESIGN.md)** — Deep design principles (20 min read)
- **[QUICK_START.md](docs/QUICK_START.md)** — Step-by-step setup (3 min)
- **[best-practices.md](docs/best-practices.md)** — Do's and don'ts

---

## File Structure

```
templates/
├── STATUS.md                    # Cross-window status board
├── method.md                    # Architecture specification
├── CODE_MAP.md                  # Code interface guide
├── RESULTS.md                   # Experiment results
├── WORK_PLAN.md                 # Work changelog
└── docs/roles/
    ├── architect.md             # 🧭 Design decisions
    ├── engineer.md              # 🔧 Implementation logs
    ├── paper.md                 # ✍️ Writing & storytelling
    └── repro.md                 # 🔬 Research & references
```

---

## How It Works

### Window Workflow

Every time you enter a window:

```
1. Read STATUS.md
   ├─ "One sentence status"
   ├─ "Current roadmap"
   └─ "Handoff messages" (tasks for you?)

2. Enter your role's document
   ├─ docs/roles/architect.md (if you're Architect)
   ├─ docs/roles/engineer.md (if you're Engineer)
   └─ etc.

3. Complete work

4. Update STATUS.md
   ├─ Update your role section
   └─ Write Handoff message to next role
```

### Cross-Window Communication

All communication happens through **Handoff messages** in STATUS.md:

```markdown
## 🔁 Handoff Messages

- **[Date] Architect → Engineer**: 
  Please implement X architecture.
  - First implement models/a.py
  - Run 3-seed ablation
  - Report results back

- **[Date] Engineer → Architect**:
  Implementation complete. Results: Y=0.85
  - See RESULTS.md §2.1
  - Next: decide on direction
```

---

## Why It Works

### Single Window Problem
```
┌─────────────────────────────────────┐
│ Design + Code + Paper + Research    │
│ All mixed in one window             │
│ → Context explosion                 │
│ → AI quality ↓                      │
└─────────────────────────────────────┘
```

### Multi-Window Solution
```
┌──────────────┐  ┌──────────────┐
│ Design       │  │ Code         │
│ Clean        │  │ Clean        │
│ Focused      │  │ Focused      │
└──────────────┘  └──────────────┘

┌──────────────┐  ┌──────────────┐
│ Paper        │  │ Research     │
│ Clean        │  │ Clean        │
│ Focused      │  │ Focused      │
└──────────────┘  └──────────────┘

       ↓ ↓ ↓ ↓
    STATUS.md
   (Single Source
    of Truth)
```

---

## Key Concepts

### 1. Role Isolation
Each window focuses on one role → cleaner thinking → better output

### 2. Central Sync
STATUS.md is the **only** communication channel between windows
- No Slack / email / meeting needed
- Everything recorded
- Decisions traceable

### 3. Handoff Messages
Explicit task assignment + decision logging
```
- Date
- Who's asking
- Who's responsible
- What needs to be done
- Expected result
```

### 4. Deep Workspace Docs
Each role has its own journey record:
- architect.md: design evolution
- engineer.md: implementation logs + pitfalls
- paper.md: writing progress + narrative
- repro.md: research findings + code analysis

---

## FAQ

**Q: Do I need 4 real windows if I'm one person?**

A: Yes, but not simultaneously. You can work as Architect in the morning, Engineer in afternoon—each window stays clean.

**Q: Can I adapt this for 2 people / 6 roles?**

A: Absolutely. The system is flexible. Adjust to your needs.

**Q: How do teams coordinate?**

A: STATUS.md in git:
1. You complete work → update STATUS.md
2. git push
3. Team members git pull → see what happened
4. Write new Handoff messages
5. Async collaboration, no meetings needed

**Q: What problem does this actually solve?**

A: **The core problem**: Single conversation windows cause context explosion:
- AI/human forgets earlier decisions mid-project
- Duplicate work across different topics
- Mixed reasoning (design + implementation + writing logic all competing)
- Unclear decision chains when things change

**What this system does:**
- ✅ **Isolates context** — Each window holds only relevant information (3-5x more focused)
- ✅ **Preserves decisions** — STATUS.md acts as project memory
- ✅ **Clarifies thinking** — Each role has clean workspace without cross-domain noise
- ✅ **Enables async work** — Handoff messages replace meetings

**What this system does NOT replace:**
- You still need to verify outputs (whether from AI or humans)
- You still estimate timelines and set goals
- You still decide on technical direction
- You still need to test/validate results

**The key insight**: This system works because it **separates concerns**. Whether you use Claude, GPT, or humans in each window, the clean handoff and focused context means better quality work per role.

In fact, you can use **different AI models for different windows**:
- Architect window: Claude (for design thinking)
- Engineer window: Claude or Code-specific model (for implementation)
- Paper window: Claude (for writing)
- Repro window: Any model (for research)

The system ensures no "context thrashing" no matter who/what does the work.
- 🎯 No context loss across windows
- 🎯 Better organization = better output

---

## Window Initialization Prompts

When you enter each window, copy the relevant prompt below and paste it into Claude Code. This helps Claude understand its role.

### 🧭 Architect Window Prompt

```
You are the Architect in a multi-window project management system.

Your role: Strategic design decisions & architecture choices.

Your workspace: docs/roles/architect.md (your design journal)
Key reference: method.md (current architecture spec)
Status board: STATUS.md (project-wide status and handoffs)

BEFORE YOU START:
1. Read STATUS.md completely (one-sentence status, roadmap, handoff messages)
2. Check if there are any messages in "Handoff Messages" section for you (🧭 Architect)
3. Read docs/roles/architect.md to see your previous work

YOUR TASK:
- Design new features and architecture decisions
- Document your reasoning (WHY, not just WHAT)
- Run experiments to validate designs
- Write Handoff messages to Engineer when design is ready

AFTER YOU FINISH:
1. Update docs/roles/architect.md with your work
2. Update method.md if architecture changed
3. Go back to STATUS.md and write a Handoff message for the next role
4. Update STATUS.md "Role Dashboard" Architect row with latest work
```

### 🔧 Engineer Window Prompt

```
You are the Engineer in a multi-window project management system.

Your role: Implementation, experiments, debugging, code optimization.

Your workspace: docs/roles/engineer.md (your implementation journal)
Key reference: CODE_MAP.md (code interfaces and important files)
Status board: STATUS.md (project-wide status and handoffs)

BEFORE YOU START:
1. Read STATUS.md completely (one-sentence status, roadmap, handoff messages)
2. Check if there are any messages in "Handoff Messages" section for you (🔧 Engineer)
3. Read CODE_MAP.md to understand code structure
4. Read docs/roles/engineer.md to see your previous work

YOUR TASK:
- Implement architecture designs from Architect
- Run experiments and ablation studies
- Document code changes in CODE_MAP.md
- Record technical challenges and solutions
- Update RESULTS.md with experiment results

AFTER YOU FINISH:
1. Update docs/roles/engineer.md with implementation details
2. Update CODE_MAP.md with code changes
3. Update RESULTS.md with experiment results
4. Go back to STATUS.md and write a Handoff message for the next role
5. Update STATUS.md "Role Dashboard" Engineer row with latest work
```

### ✍️ Paper Window Prompt

```
You are the Paper writer in a multi-window project management system.

Your role: Writing, storytelling, connecting results to narrative.

Your workspace: docs/roles/paper.md (your writing journal)
Key references: RESULTS.md (experiment data), method.md (architecture)
Status board: STATUS.md (project-wide status and handoffs)

BEFORE YOU START:
1. Read STATUS.md completely (one-sentence status, roadmap, handoff messages)
2. Check if there are any messages in "Handoff Messages" section for you (✍️ Paper)
3. Read RESULTS.md to get latest experiment data
4. Read docs/roles/paper.md to see your previous work

YOUR TASK:
- Write paper sections (introduction, method, results, discussion)
- Connect experimental results to your narrative
- Ground all claims in RESULTS.md numbers
- Anticipate and address reviewer objections
- Maintain logical flow and argument strength

AFTER YOU FINISH:
1. Update docs/roles/paper.md with new sections and progress
2. Go back to STATUS.md and write a Handoff message for the next role
3. Update STATUS.md "Role Dashboard" Paper row with latest work
4. Note any design/implementation feedback in Handoff messages
```

### 🔬 Repro Window Prompt

```
You are the Repro (Research) researcher in a multi-window project management system.

Your role: Literature analysis, code investigation, feasibility assessment.

Your workspace: docs/roles/repro.md (your research journal)
Key reference: method.md (current architecture - what to research around)
Status board: STATUS.md (project-wide status and handoffs)

BEFORE YOU START:
1. Read STATUS.md completely (one-sentence status, roadmap, handoff messages)
2. Check if there are any messages in "Handoff Messages" section for you (🔬 Repro)
3. Read docs/roles/repro.md to see your previous research
4. Check method.md to understand what to research

YOUR TASK:
- Search and analyze relevant papers/code
- Assess feasibility of proposed approaches
- Document findings with sources
- Recommend what's worth trying vs. not worth trying
- Help Architect make informed design decisions

AFTER YOU FINISH:
1. Update docs/roles/repro.md with research findings
2. Go back to STATUS.md and write a Handoff message for Architect with recommendations
3. Update STATUS.md "Role Dashboard" Repro row with latest work
```

---

## Installation Methods

### Method 1: Copy Templates Directly

```bash
git clone https://github.com/findones/multi-window-system.git
cp -r multi-window-system/templates/* /your/project/
```

### Method 2: Python Script (Recommended)

```bash
# Clone the repository
git clone https://github.com/findones/multi-window-system.git
cd multi-window-system

# Run the initialization script
python init.py "Project Name" --language en

# Or specify output directory
python init.py "Project Name" --output /your/project/path --language en
```

### Method 3: Claude Code Skill (Global Installation)

Install as a reusable skill in Claude Code - available in all your projects:

```bash
# For macOS / Linux
mkdir -p ~/.claude/skills/multi-window-system
git clone https://github.com/findones/multi-window-system.git ~/.claude/skills/multi-window-system

# For Windows (PowerShell)
mkdir -Path "$env:USERPROFILE\.claude\skills\multi-window-system"
git clone https://github.com/findones/multi-window-system.git "$env:USERPROFILE\.claude\skills\multi-window-system"
```

**Usage in Claude Code:**
```
/multi-window-project-init "My Project Name" --language en
/multi-window-project-init "我的项目" --language zh
/multi-window-project-init "My Project" --roles architect,engineer
```

**Benefits of Skill Installation:**
- ✅ Available in any project
- ✅ One-command setup
- ✅ No need to clone multiple times
- ✅ Easy updates (just git pull in the skill directory)

---

## Community & Contribution

- **Issues**: Report bugs or suggest improvements
- **Examples**: Share how you adapted this for your field
- **Translations**: Help translate to other languages
- **Tools**: Contribute automation (GitHub Actions, etc.)

---

## License

MIT License — Free to use and adapt

---

---

# 中文版本

## 概述

一个经过验证的系统，用于管理大型 AI 辅助项目，避免上下文爆炸。

**问题**：单个 AI 对话窗口处理多个角色（设计、工程、写作、研究）导致：
- 上下文快速填满
- AI 遗忘重要决策
- 重复犯错
- 决策链不清晰

**解决方案**：
- 4 个分离的角色窗口（架构师 / 工程师 / 论文 / 复现）
- 1 个共享的 STATUS.md 用于同步和决策
- 清爽的上下文 + 清晰的思维 + 可追踪的决策

---

## 功能特性

✅ **4 个角色窗口** — 每个窗口 = 一个角色 = 专注的上下文
✅ **中央同步点** — STATUS.md 是唯一的真实来源
✅ **决策日志** — 每个决策通过 Handoff 消息追踪
✅ **完整模板** — 复制即用
✅ **最佳实践** — 深度设计文档解释工作原理

---

## 快速开始

### 步骤 1：克隆和设置（30 秒）

```bash
git clone https://github.com/findones/multi-window-system.git
cd multi-window-system
python init.py "我的项目名称" --language zh
```

### 步骤 2：初始化项目（5 分钟）

编辑 `STATUS.md`，填入你的项目信息：
```bash
nano STATUS.md
```

### 步骤 3：开始工作

打开 4 个 Claude Code 窗口（每个角色一个）：

| 窗口 | 角色 | 文件 |
|------|------|------|
| 1️⃣ | 架构师 | `docs/roles/architect.md` |
| 2️⃣ | 工程师 | `docs/roles/engineer.md` |
| 3️⃣ | 论文 | `docs/roles/paper.md` |
| 4️⃣ | 复现 | `docs/roles/repro.md` |

**工作流程**：每个窗口先读 STATUS.md → 进入角色文档工作 → 更新 STATUS.md 的 Handoff 消息。

---

## 文档

- **[README_CN.md](docs/README_CN.md)** — 系统概览和核心概念（5 分钟阅读）
- **[DESIGN_CN.md](docs/DESIGN_CN.md)** — 深度设计原理（20 分钟）
- **[QUICK_START_CN.md](docs/QUICK_START_CN.md)** — 分步设置（3 分钟）
- **[best-practices_CN.md](docs/best-practices_CN.md)** — 最佳实践

---

## 文件结构

```
templates/
├── STATUS.md                    # 跨窗口状态板
├── method.md                    # 架构规范
├── CODE_MAP.md                  # 代码接口指南
├── RESULTS.md                   # 实验结果
├── WORK_PLAN.md                 # 工作日志
└── docs/roles/
    ├── architect.md             # 🧭 设计决策
    ├── engineer.md              # 🔧 实现日志
    ├── paper.md                 # ✍️ 写作和叙事
    └── repro.md                 # 🔬 研究和参考
```

---

## 工作原理

### 窗口工作流程

每次进入窗口时：

```
1. 读 STATUS.md
   ├─ "一句话现状"
   ├─ "当前路线图"
   └─ "Handoff 消息"（有给你的任务吗？）

2. 进入你角色的文档
   ├─ docs/roles/architect.md（如果你是架构师）
   ├─ docs/roles/engineer.md（如果你是工程师）
   └─ 等等

3. 完成工作

4. 更新 STATUS.md
   ├─ 更新你角色的部分
   └─ 写 Handoff 消息给下一个角色
```

### 跨窗口通信

所有通信通过 STATUS.md 中的 **Handoff 消息** 进行：

```markdown
## 🔁 Handoff 消息

- **【日期】架构师 → 工程师**：
  请实现 X 架构。
  - 首先实现 models/a.py
  - 运行 3-seed 消融
  - 回报结果

- **【日期】工程师 → 架构师**：
  实现完成。结果：Y=0.85
  - 见 RESULTS.md §2.1
  - 接下来：决定方向
```

---

## 为什么有效

### 单窗口问题
```
┌─────────────────────────────────────┐
│ 设计 + 代码 + 论文 + 研究            │
│ 全部混在一个窗口里                   │
│ → 上下文爆炸                        │
│ → AI 质量 ↓                        │
└─────────────────────────────────────┘
```

### 多窗口方案
```
┌──────────────┐  ┌──────────────┐
│ 设计         │  │ 代码         │
│ 清爽         │  │ 清爽         │
│ 专注         │  │ 专注         │
└──────────────┘  └──────────────┘

┌──────────────┐  ┌──────────────┐
│ 论文         │  │ 研究         │
│ 清爽         │  │ 清爽         │
│ 专注         │  │ 专注         │
└──────────────┘  └──────────────┘

       ↓ ↓ ↓ ↓
    STATUS.md
   （唯一的真实来源）
```

---

## 核心概念

### 1. 角色隔离
每个窗口专注一个角色 → 思维清晰 → 输出更好

### 2. 中央同步
STATUS.md 是**唯一的**窗口间通信渠道
- 无需 Slack / 邮件 / 会议
- 一切都有记录
- 决策可追踪

### 3. Handoff 消息
明确的任务分配 + 决策日志
```
- 日期
- 谁在要求
- 谁负责
- 需要做什么
- 期望的结果
```

### 4. 深度工作空间文档
每个角色有自己的旅程记录：
- architect.md：设计演进
- engineer.md：实现日志 + 踩坑
- paper.md：写作进度 + 叙事
- repro.md：研究发现 + 代码分析

---

## 常见问题

**Q：如果我是一个人，需要 4 个真实的窗口吗？**

A：是的，但不需要同时打开。你可以上午作为架构师工作，下午作为工程师工作——每个窗口都保持清爽。

**Q：能否为 2 个人 / 6 个角色适配这个系统？**

A：完全可以。这个系统很灵活。根据你的需求调整即可。

**Q：团队如何协调？**

A：STATUS.md 在 git 中：
1. 你完成工作 → 更新 STATUS.md
2. git push
3. 团队成员 git pull → 看到发生了什么
4. 写新的 Handoff 消息
5. 异步协作，无需会议

**Q：这个系统解决什么问题？**

A：**核心问题**：单个对话窗口处理大项目会导致：
- AI/人忘记之前的决策
- 重复工作
- 思维混乱（设计+代码+写作逻辑在一个窗口竞争）
- 决策链条不清晰

**这个系统做什么：**
- ✅ **隔离上下文** — 每个窗口只包含相关信息（清晰度提高 3-5 倍）
- ✅ **保留决策** — STATUS.md 作为项目记忆
- ✅ **清晰思考** — 每个角色有独立工作空间，没有跨域干扰
- ✅ **异步工作** — Handoff 消息替代会议

**这个系统不替代：**
- 你需要验证输出（无论来自AI还是人）
- 你需要估计时间表和设定目标
- 你需要决定技术方向
- 你需要测试/验证结果

**关键洞察**：这个系统有效，因为它**分离关注点**。无论每个窗口使用Claude、GPT还是人类，清晰的交接和专注的上下文都能保证更好的输出质量。

实际上，你可以**为不同窗口使用不同的AI模型**：
- 架构师窗口：Claude（设计思考）
- 工程师窗口：Claude 或代码特定模型（实现）
- 论文窗口：Claude（写作）
- 复现窗口：任何模型（研究）

系统确保无论谁做工作，都不会出现"上下文混乱"。

---

## 窗口初始化提示词

进入每个窗口时，复制下面的相应提示词，粘贴到 Claude Code。这帮助 Claude 理解它的角色。

### 🧭 架构师窗口提示词

```
你是一个多窗口项目管理系统中的架构师。

你的角色：战略性设计决策和架构选择。

你的工作空间：docs/roles/architect.md（你的设计日志）
关键参考：method.md（当前架构规范）
状态板：STATUS.md（项目范围内的状态和交接消息）

开始之前：
1. 完整读 STATUS.md（一句话现状、路线图、交接消息）
2. 检查"交接消息"部分中是否有给你的消息（🧭 架构师）
3. 读 docs/roles/architect.md 看你之前的工作

你的任务：
- 设计新功能和架构决策
- 文档化你的推理（为什么，而不仅仅是什么）
- 运行实验验证设计
- 当设计准备好时，给工程师写交接消息

完成后：
1. 更新 docs/roles/architect.md
2. 如果架构改变，更新 method.md
3. 回到 STATUS.md 给下一个角色写交接消息
4. 更新 STATUS.md "角色看板"中架构师行
```

### 🔧 工程师窗口提示词

```
你是一个多窗口项目管理系统中的工程师。

你的角色：实现、实验、调试、代码优化。

你的工作空间：docs/roles/engineer.md（你的实现日志）
关键参考：CODE_MAP.md（代码接口和重要文件）
状态板：STATUS.md（项目范围内的状态和交接消息）

开始之前：
1. 完整读 STATUS.md（一句话现状、路线图、交接消息）
2. 检查"交接消息"部分中是否有给你的消息（🔧 工程师）
3. 读 CODE_MAP.md 理解代码结构
4. 读 docs/roles/engineer.md 看你之前的工作

你的任务：
- 实现来自架构师的设计
- 运行实验和消融研究
- 在 CODE_MAP.md 中文档化代码改动
- 记录技术挑战和解决方案
- 更新 RESULTS.md 中的实验结果

完成后：
1. 更新 docs/roles/engineer.md
2. 更新 CODE_MAP.md
3. 更新 RESULTS.md
4. 回到 STATUS.md 写交接消息
5. 更新 STATUS.md "角色看板"工程师行
```

### ✍️ 论文窗口提示词

```
你是一个多窗口项目管理系统中的论文作者。

你的角色：写作、叙述、连接结果到故事。

你的工作空间：docs/roles/paper.md（你的写作日志）
关键参考：RESULTS.md（实验数据）、method.md（架构）
状态板：STATUS.md（项目范围内的状态和交接消息）

开始之前：
1. 完整读 STATUS.md（一句话现状、路线图、交接消息）
2. 检查"交接消息"部分中是否有给你的消息（✍️ 论文）
3. 读 RESULTS.md 获取最新实验数据
4. 读 docs/roles/paper.md 看你之前的工作

你的任务：
- 写论文各部分（介绍、方法、结果、讨论）
- 连接实验结果到你的叙述
- 所有主张都要用 RESULTS.md 的数据支持
- 预期并回应审稿人的疑问
- 维持逻辑流畅和论证强度

完成后：
1. 更新 docs/roles/paper.md
2. 回到 STATUS.md 写交接消息
3. 更新 STATUS.md "角色看板"论文行
```

### 🔬 复现窗口提示词

```
你是一个多窗口项目管理系统中的研究员。

你的角色：文献分析、代码调查、可行性评估。

你的工作空间：docs/roles/repro.md（你的研究日志）
关键参考：method.md（当前架构）
状态板：STATUS.md（项目范围内的状态和交接消息）

开始之前：
1. 完整读 STATUS.md（一句话现状、路线图、交接消息）
2. 检查"交接消息"部分中是否有给你的消息（🔬 复现）
3. 读 docs/roles/repro.md 看你之前的研究
4. 检查 method.md 理解要研究什么

你的任务：
- 搜索和分析相关论文/代码
- 评估提议方法的可行性
- 用来源文档化发现
- 推荐什么值得尝试 vs 不值得
- 帮助架构师做出明智的设计决策

完成后：
1. 更新 docs/roles/repro.md
2. 回到 STATUS.md 给架构师写交接消息
3. 更新 STATUS.md "角色看板"复现行
```

---

## 安装方法

### 方法 1：直接复制模板

```bash
git clone https://github.com/findones/multi-window-system.git
cp -r multi-window-system/templates/* /your/project/
```

### 方法 2：使用 Python 脚本（推荐）

```bash
# 克隆仓库
git clone https://github.com/findones/multi-window-system.git
cd multi-window-system

# 运行初始化脚本
python init.py "项目名称" --language zh

# 或指定输出目录
python init.py "项目名称" --output /your/project/path --language zh
```

---

## 社区和贡献

- **问题报告**：报告 bug 或建议改进
- **示例分享**：分享你如何为你的领域适配这个系统
- **翻译**：帮助翻译成其他语言
- **工具**：贡献自动化工具（GitHub Actions 等）

---

## 许可证

MIT 许可证 — 免费使用和改编
