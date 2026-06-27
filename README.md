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

**Q: Is this a "silver bullet"?**

A: No. It solves "context confusion" but not:
- Technical correctness (you decide)
- Data quality (you verify)
- Project deadlines (you estimate)

But it helps you think clearly about all of these.

---

## Installation Methods

### Method 1: Copy Templates Directly

```bash
git clone https://github.com/findones/multi-window-system.git
cp -r multi-window-system/templates/* /your/project/
```

### Method 2: Claude Code Skill (coming soon)

```
In Claude Code terminal:
/multi-window-system-init "Project Name" "Description"
```

This will automatically:
- Create all 9 template files
- Initialize STATUS.md with your project info
- Set up git (optional)

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

### 步骤 1：安装 skill

```bash
# 即将推出：Claude Code 自动安装
# 现在：手动设置（见下文）
```

### 步骤 2：初始化项目（5 分钟）

```bash
# 复制模板
cp -r skill/templates/* /your/project/

# 编辑 STATUS.md，填入你的项目名
nano STATUS.md
```

### 步骤 3：开始工作

打开 4 个 Claude Code 窗口：
- 窗口 1：架构师 — `docs/roles/architect.md`
- 窗口 2：工程师 — `docs/roles/engineer.md`
- 窗口 3：论文 — `docs/roles/paper.md`
- 窗口 4：复现 — `docs/roles/repro.md`

每个窗口先读 STATUS.md，然后在自己的角色文档中工作。

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

**Q：这是"银弹"吗？**

A：不是。它解决"上下文混乱"，但不能解决：
- 技术正确性（你来决定）
- 数据质量（你来验证）
- 项目截止日期（你来估计）

但它帮助你清晰地思考所有这些问题。

---

## 安装方法

### 方法 1：直接复制模板

```bash
git clone https://github.com/findones/multi-window-system.git
cp -r multi-window-system/templates/* /your/project/
```

### 方法 2：Claude Code Skill（即将推出）

```
在 Claude Code 终端中：
/multi-window-system-init "项目名称" "描述"
```

这将自动：
- 创建所有 9 个模板文件
- 用你的项目信息初始化 STATUS.md
- 设置 git（可选）

---

## 社区和贡献

- **问题报告**：报告 bug 或建议改进
- **示例分享**：分享你如何为你的领域适配这个系统
- **翻译**：帮助翻译成其他语言
- **工具**：贡献自动化工具（GitHub Actions 等）

---

## 许可证

MIT 许可证 — 免费使用和改编
