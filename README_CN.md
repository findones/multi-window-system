# 多窗口项目管理系统

[English](#english-version-) | [中文](#中文版本-)

---

## 中文版本

### 概述

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

### 核心特性

✅ **4 个角色窗口** — 每个窗口 = 一个角色 = 专注的上下文
✅ **中央同步点** — STATUS.md 是唯一的真实来源
✅ **决策日志** — 每个决策通过 Handoff 消息追踪
✅ **完整模板** — 复制即用，无需从零开始
✅ **双语支持** — 英文和中文完整文档

---

### 快速开始

#### 步骤 1：克隆和设置（30 秒）

```bash
git clone https://github.com/findones/multi-window-system.git
cd multi-window-system
python init.py "我的项目名称" --language zh
```

#### 步骤 2：初始化项目（5 分钟）

编辑 `STATUS.md`，填入你的项目信息：
```bash
nano STATUS.md
```

#### 步骤 3：开始工作

打开 4 个 Claude Code 窗口（每个角色一个）：

| 窗口 | 角色 | 文件 |
|------|------|------|
| 1️⃣ | 架构师 | `docs/roles/architect.md` |
| 2️⃣ | 工程师 | `docs/roles/engineer.md` |
| 3️⃣ | 论文 | `docs/roles/paper.md` |
| 4️⃣ | 复现 | `docs/roles/repro.md` |

**工作流程**：每个窗口先读 STATUS.md → 进入角色文档工作 → 更新 STATUS.md 的 Handoff 消息。

---

### 文件结构

```
templates/
├── STATUS.md                    # 跨窗口状态板
├── method.md                    # 架构规范
├── CODE_MAP.md                  # 代码接口指南
├── RESULTS.md                   # 实验结果
├── WORK_PLAN.md                 # 工作日志
└── docs/roles/
    ├── architect.md             # 🧭 架构师主场
    ├── engineer.md              # 🔧 工程师主场
    ├── paper.md                 # ✍️ 论文主场
    └── repro.md                 # 🔬 复现师主场
```

---

### 工作原理

#### 窗口工作流程

每次进入窗口时的标准流程：

```
1️⃣ 读 STATUS.md
   ├─ 「一句话现状」→ 了解全局
   ├─ 「当前路线图」→ 了解方向
   └─ 「Handoff 消息」→ 看有没有给我的任务

2️⃣ 进入你的角色文档
   ├─ docs/roles/architect.md（如果你是架构师）
   ├─ docs/roles/engineer.md（如果你是工程师）
   ├─ docs/roles/paper.md（如果你是论文）
   └─ docs/roles/repro.md（如果你是复现）

3️⃣ 完成工作

4️⃣ 更新 STATUS.md
   ├─ 更新你角色部分（「最近产出」）
   └─ 写 Handoff 消息给下一个角色
```

#### Handoff 消息示例

所有跨窗口通信都通过 STATUS.md 中的 Handoff 消息：

```markdown
## 🔁 Handoff 消息

- **【2024-01-15】 🧭架构师 → 🔧工程师**：
  新的 X 架构设计完成，请实现。
  - 详见 method.md §1
  - 新建 models/new_arch.py
  - 跑 3-seed 验证
  - 结果回报给我

- **【2024-01-16】 🔧工程师 → 🧭架构师**：
  实现完成，数字是 Y=0.85。
  - 代码改动见 CODE_MAP.md
  - 结果见 RESULTS.md §2.1
  - 接下来：你决定方向
```

---

### 为什么有效

#### 单窗口问题

```
┌─────────────────────────────────────┐
│ 设计 + 代码 + 论文 + 研究            │
│ 全部混在一个窗口里                   │
│ ↓                                   │
│ 上下文爆炸                          │
│ AI 质量下降                         │
│ 重复犯错                            │
└─────────────────────────────────────┘
```

#### 多窗口方案

```
┌──────────────┐  ┌──────────────┐
│ 设计窗口     │  │ 代码窗口     │
│ 清爽上下文   │  │ 清爽上下文   │
│ 深度思考     │  │ 深度思考     │
└──────────────┘  └──────────────┘

┌──────────────┐  ┌──────────────┐
│ 论文窗口     │  │ 研究窗口     │
│ 清爽上下文   │  │ 清爽上下文   │
│ 深度思考     │  │ 深度思考     │
└──────────────┘  └──────────────┘

        ↓ 通过 STATUS.md 同步 ↓
      高效的决策链条
```

---

### 核心概念

#### 1. 角色隔离
每个窗口专注一个角色 → 思维清晰 → 输出质量高

#### 2. 中央同步点
STATUS.md 是**唯一的**窗口间通信渠道：
- 无需 Slack / 邮件 / 会议
- 一切都有记录
- 决策可追踪

#### 3. Handoff 消息
明确的任务分配 + 决策日志：
```
- 日期（什么时候）
- 谁在要求（谁→谁）
- 具体任务（要做什么）
- 期望结果（什么时候交）
```

#### 4. 深度工作空间文档
每个角色有自己的旅程记录：
- **architect.md**：设计演进、为什么这样选择
- **engineer.md**：实现细节、踩过的坑
- **paper.md**：写作进度、故事演变
- **repro.md**：研究发现、参考分析

---

### 适用场景

✅ **ML 研究项目** — 多个架构同时探索，消融实验众多
✅ **软件工程项目** — 产品/设计/工程/QA 需要协调
✅ **论文写作** — 编辑/作者/研究者/评审者分工
✅ **产品开发** — PM/设计师/工程师/营销需要同步
✅ **任何大型项目** — 多角色、多决策、需要追踪

---

### 常见问题

**Q：一个人需要真的打开 4 个窗口吗？**

A：是的，但不需要同时打开。可以按顺序工作：
- 上午：架构师模式 (window 1)
- 下午：工程师模式 (window 2)
- 明天：论文模式 (window 3)

每个窗口都保持清爽的上下文。

**Q：能不能改成 2 个角色或 6 个角色？**

A：完全可以！这只是模板，适配到你的需求：
- 简单项目：2 个角色（架构师 + 工程师）
- 复杂项目：6 个角色（加上 PM、QA 等）
- 按需组合

**Q：多人团队怎么协调？**

A：STATUS.md 在 git 中：
1. 你完成工作 → 更新 STATUS.md
2. git push
3. 队友 git pull → 看到发生了什么
4. 写新 Handoff 消息
5. 完全异步协作，无需会议

**Q：这个系统是"银弹"吗？**

A：不是。它只解决"上下文混乱"，不能解决：
- ❌ 技术正确性（你来决定）
- ❌ 数据质量（你来验证）
- ❌ 项目估计（你来规划）

但它帮助你**清晰地思考**这些问题。

---

### 后续步骤

1. **阅读 INSTALL.md** — 详细的安装说明
2. **复制模板到你的项目** — `python init.py "项目名" --language zh`
3. **打开 4 个 Claude 窗口** — 一个窗口一个角色
4. **开始工作** — 按照流程执行

---

### 获取帮助

- **安装问题** → 看 [INSTALL.md](INSTALL.md)
- **使用问题** → 看 STATUS.md 和各角色文档
- **反馈/改进** → 在 GitHub 提 issue

---

### 许可证

MIT 许可证 — 免费使用和改编

---

---

## English Version

### Overview

A proven system for managing large AI-assisted projects without context explosion.

**Problem**: Single AI conversation window handling multiple roles causes:
- Context fills up quickly
- AI forgets important decisions
- Repeated mistakes
- Unclear decision chains

**Solution**:
- 4 separate role windows (Architect / Engineer / Paper / Repro)
- 1 shared STATUS.md for sync
- Clean context + clear thinking + traceable decisions

### Key Features

✅ **4 Role Windows** — Each window = one role = focused context
✅ **Central Sync Point** — STATUS.md is single source of truth
✅ **Decision Logging** — Every decision tracked via Handoff messages
✅ **Complete Templates** — Copy and use immediately
✅ **Bilingual Support** — English and Chinese full docs

### Quick Start

See [INSTALL.md](INSTALL.md) for detailed installation instructions.

```bash
# Method 1: Python script
python init.py "Project Name" --language en

# Method 2: Manual copy
cp -r templates/* /your/project/
```

### File Structure

```
templates/
├── STATUS.md                    # Cross-window status board
├── method.md                    # Architecture spec
├── CODE_MAP.md                  # Code interface guide
├── RESULTS.md                   # Experiment results
├── WORK_PLAN.md                 # Work changelog
└── docs/roles/
    ├── architect.md             # 🧭 Design decisions
    ├── engineer.md              # 🔧 Implementation
    ├── paper.md                 # ✍️ Writing
    └── repro.md                 # 🔬 Research
```

### How It Works

Every time you enter a window:
```
1. Read STATUS.md for tasks and status
2. Enter your role's document
3. Complete work
4. Write Handoff message to next role
5. Hand off
```

### Why It Works

Four clean windows with focused context > one cluttered window

Each window can maintain complete project context while focusing on one role's work.

### Common Questions

**Q: Do I need 4 real windows if I'm one person?**

A: Yes, but not simultaneously. Work as different roles in sequence—each window stays clean.

**Q: Can I adapt this for 2 people / 6 roles?**

A: Yes. Templates are flexible. Adjust to your team structure.

**Q: How do teams use this?**

A: STATUS.md in git. Each person pushes their updates. Async collaboration, no meetings needed.

### Next Steps

1. Read [INSTALL.md](INSTALL.md) for setup instructions
2. Copy templates: `python init.py "Project Name"`
3. Open 4 Claude windows (one per role)
4. Start working!

### License

MIT — Free to use and adapt

---

**Ready to try? Start here**: [INSTALL.md](INSTALL.md)
