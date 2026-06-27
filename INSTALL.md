# Installation Guide | 安装指南

## English Version

### Installation Methods

#### Method 1: Using Python Script (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/findones/multi-role-project-skill.git
cd multi-role-project-skill

# 2. Make script executable
chmod +x init.py

# 3. Initialize your project
python init.py "My Project Name" --language en

# The script creates:
# - STATUS.md
# - method.md, CODE_MAP.md, RESULTS.md, WORK_PLAN.md
# - docs/roles/architect.md, engineer.md, paper.md, repro.md
```

#### Method 2: Manual Setup (5 minutes)

```bash
# 1. Copy templates
cp -r multi-role-project-skill/templates/* /your/project/

# 2. Edit STATUS.md
nano /your/project/STATUS.md
# Replace [Project name] with your project

# 3. Done!
```

#### Method 3: Claude Code Skill (When Available)

```
In Claude Code terminal:
/multi-role-project-init "Project Name" --language en
```

---

### Quick Start After Installation

```bash
# 1. Navigate to your project
cd /your/project

# 2. Open 4 Claude Code windows simultaneously:
#    Window 1: This is your "Architect" window
#    Window 2: This is your "Engineer" window
#    Window 3: This is your "Paper" window
#    Window 4: This is your "Repro" window

# 3. In EACH window:
#    - Read STATUS.md first (for task assignments)
#    - Then enter your role file:
#      - Architect: docs/roles/architect.md
#      - Engineer: docs/roles/engineer.md
#      - Paper: docs/roles/paper.md
#      - Repro: docs/roles/repro.md

# 4. Start working! When done:
#    - Update your role file
#    - Update STATUS.md (Handoff section)
#    - Hand off to next role/window
```

---

### System Requirements

- Claude Code (any recent version)
- Git (for team collaboration)
- Python 3.7+ (for init.py script)

### File Structure After Setup

```
your-project/
├── STATUS.md                    ← Start here
├── method.md
├── CODE_MAP.md
├── RESULTS.md
├── WORK_PLAN.md
├── docs/
│   └── roles/
│       ├── architect.md
│       ├── engineer.md
│       ├── paper.md
│       └── repro.md
└── [your other project files...]
```

---

### Verification

After setup, verify all files were created:

```bash
# Check main files exist
ls -la STATUS.md method.md CODE_MAP.md RESULTS.md WORK_PLAN.md

# Check role files exist
ls -la docs/roles/

# You should see:
# - architect.md ✓
# - engineer.md ✓
# - paper.md ✓
# - repro.md ✓
```

---

### Customization

You can adapt the system to your needs:

**Change number of roles**:
```bash
python init.py "My Project" --roles architect,engineer
# Only creates 2 roles instead of 4
```

**Add new roles** (after initial setup):
```bash
# Manually create docs/roles/new_role.md with your template
nano docs/roles/new_role.md

# Add to STATUS.md role dashboard section
```

**Change language**:
```bash
python init.py "My Project" --language zh
# Creates Chinese-language templates
```

---

### Troubleshooting

**Q: Python script won't run**

A: 
```bash
# Make sure Python 3 is installed
python3 --version

# Use python3 explicitly
python3 init.py "My Project"
```

**Q: `Init.py not found`**

A:
```bash
# Make sure you're in the multi-role-project-skill directory
cd multi-role-project-skill
ls init.py  # Should show init.py

# Then run:
python init.py "My Project"
```

**Q: Files created but in wrong location**

A:
```bash
# Specify output directory
python init.py "My Project" --output /path/to/project
```

---

### Next Steps After Installation

1. **Read STATUS.md** — Understand the structure
2. **Read the system README** — Learn core concepts
3. **Open 4 Claude windows** — One per role
4. **Start your first workflow** — Check STATUS.md for initial state

---

---

# 中文版本

### 安装方法

#### 方法 1：使用 Python 脚本（推荐）

```bash
# 1. 克隆仓库
git clone https://github.com/findones/multi-role-project-skill.git
cd multi-role-project-skill

# 2. 给脚本执行权限
chmod +x init.py

# 3. 初始化你的项目
python init.py "我的项目名称" --language zh

# 脚本会创建：
# - STATUS.md
# - method.md, CODE_MAP.md, RESULTS.md, WORK_PLAN.md
# - docs/roles/architect.md, engineer.md, paper.md, repro.md
```

#### 方法 2：手动设置（5 分钟）

```bash
# 1. 复制模板
cp -r multi-role-project-skill/templates/* /your/project/

# 2. 编辑 STATUS.md
nano /your/project/STATUS.md
# 将 [项目名] 替换为你的项目名

# 3. 完成！
```

#### 方法 3：Claude Code Skill（推出后）

```
在 Claude Code 终端中：
/multi-role-project-init "项目名称" --language zh
```

---

### 安装后快速开始

```bash
# 1. 进入你的项目目录
cd /your/project

# 2. 同时打开 4 个 Claude Code 窗口：
#    窗口 1：这是你的"架构师"窗口
#    窗口 2：这是你的"工程师"窗口
#    窗口 3：这是你的"论文"窗口
#    窗口 4：这是你的"复现"窗口

# 3. 在 EACH 窗口中：
#    - 先读 STATUS.md（看是否有给你的任务）
#    - 然后进入你的角色文件：
#      - 架构师：docs/roles/architect.md
#      - 工程师：docs/roles/engineer.md
#      - 论文：docs/roles/paper.md
#      - 复现：docs/roles/repro.md

# 4. 开始工作！完成后：
#    - 更新你的角色文件
#    - 更新 STATUS.md（Handoff 部分）
#    - 交接给下一个角色/窗口
```

---

### 系统要求

- Claude Code（任何最新版本）
- Git（用于团队协作）
- Python 3.7+（运行 init.py）

### 设置后的文件结构

```
your-project/
├── STATUS.md                    ← 从这里开始
├── method.md
├── CODE_MAP.md
├── RESULTS.md
├── WORK_PLAN.md
├── docs/
│   └── roles/
│       ├── architect.md
│       ├── engineer.md
│       ├── paper.md
│       └── repro.md
└── [你的其他项目文件...]
```

---

### 验证

设置后，验证所有文件都已创建：

```bash
# 检查主要文件
ls -la STATUS.md method.md CODE_MAP.md RESULTS.md WORK_PLAN.md

# 检查角色文件
ls -la docs/roles/

# 你应该看到：
# - architect.md ✓
# - engineer.md ✓
# - paper.md ✓
# - repro.md ✓
```

---

### 自定义

你可以根据需要调整系统：

**改变角色数量**：
```bash
python init.py "我的项目" --roles architect,engineer
# 只创建 2 个角色而不是 4 个
```

**添加新角色**（初始设置后）：
```bash
# 手动创建 docs/roles/new_role.md
nano docs/roles/new_role.md

# 在 STATUS.md 的角色看板部分添加
```

**改变语言**：
```bash
python init.py "我的项目" --language zh
# 创建中文模板
```

---

### 故障排除

**Q：Python 脚本无法运行**

A：
```bash
# 确保已安装 Python 3
python3 --version

# 明确使用 python3
python3 init.py "我的项目"
```

**Q：找不到 init.py**

A：
```bash
# 确保你在 multi-role-project-skill 目录中
cd multi-role-project-skill
ls init.py  # 应该显示 init.py

# 然后运行：
python init.py "我的项目"
```

**Q：文件创建在错误的位置**

A：
```bash
# 指定输出目录
python init.py "我的项目" --output /path/to/project
```

---

### 安装后的后续步骤

1. **读 STATUS.md** — 理解结构
2. **读系统 README** — 学习核心概念
3. **打开 4 个 Claude 窗口** — 每个角色一个
4. **开始你的第一个工作流** — 检查 STATUS.md 的初始状态
