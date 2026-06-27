# Claude Code Skill 安装指南 | Installation Guide

**English** | [中文](#中文版本)

---

## English Version

### What is a Skill?

Claude Code skills are reusable tools/commands you can invoke in the Claude Code terminal.

**Invocation format:**
```
/skill-name argument1 argument2 --option value
```

**Example:**
```
/multi-role-project-init "My Project" --language en
```

---

## Installation Methods

### Method 1: Global Installation (Recommended)

Install for all your projects worldwide:

```bash
# 1. Clone the repository
git clone https://github.com/findones/multi-role-project-skill.git ~/.claude/skills/multi-role-project-skill

# 2. Verify installation
ls ~/.claude/skills/multi-role-project-skill/
# Should show: skill.yaml, init.py, templates/, README.md

# 3. That's it! You can now use:
# /multi-role-project-init "Project Name"
```

### Method 2: Project-Level Installation

Install just for this project:

```bash
# 1. In your project directory
cd /your/project
mkdir -p .claude/skills/multi-role-project-skill

# 2. Copy skill files
cp -r [skill-source]/* .claude/skills/multi-role-project-skill/

# 3. Use in this project:
# /multi-role-project-init "Project Name"
```

### Method 3: Download and Extract

```bash
# Download as ZIP
wget https://github.com/findones/multi-role-project-skill/archive/main.zip

# Extract to skills directory
mkdir -p ~/.claude/skills/multi-role-project-skill
unzip main.zip -d ~/.claude/skills/multi-role-project-skill
```

---

## File Structure

After installation, you should have:

```
~/.claude/skills/multi-role-project-skill/
│
├── skill.yaml                      ← Skill definition (required)
├── init.py                         ← Implementation (required)
├── templates/                      ← Project templates (required)
│   ├── STATUS.md
│   ├── method.md
│   ├── CODE_MAP.md
│   ├── RESULTS.md
│   ├── WORK_PLAN.md
│   └── docs/roles/
│       ├── architect.md
│       ├── engineer.md
│       ├── paper.md
│       └── repro.md
│
├── README.md                       ← Documentation
├── INSTALL.md                      ← Installation guide
└── LICENSE                         ← License file
```

---

## Usage After Installation

After successful installation, you can use in any Claude Code window:

```bash
# Basic usage
/multi-role-project-init "My Project Name"

# With language option
/multi-role-project-init "My Project" --language zh

# With specific roles
/multi-role-project-init "My Project" --roles architect,engineer

# With custom output directory
/multi-role-project-init "My Project" --output /path/to/project
```

---

## Verification

To verify the skill is properly installed:

```bash
# Check files exist
ls ~/.claude/skills/multi-role-project-skill/skill.yaml
ls ~/.claude/skills/multi-role-project-skill/init.py

# In Claude Code, try to use it:
# /multi-role-project-init "Test"

# Should create:
# - STATUS.md
# - method.md
# - CODE_MAP.md
# - etc.
```

---

## Troubleshooting

### Skill doesn't show up

```bash
# Make sure directory exists
mkdir -p ~/.claude/skills/multi-role-project-skill

# Make sure files are there
ls ~/.claude/skills/multi-role-project-skill/skill.yaml
ls ~/.claude/skills/multi-role-project-skill/init.py

# Restart Claude Code
# (Close and reopen the application)
```

### Script won't run

```bash
# Make sure init.py is executable
chmod +x ~/.claude/skills/multi-role-project-skill/init.py

# Make sure Python 3 is installed
python3 --version

# Test the script manually
python3 ~/.claude/skills/multi-role-project-skill/init.py "Test Project"
```

### Permission denied

```bash
# Give proper permissions
chmod 755 ~/.claude/skills/multi-role-project-skill/
chmod 755 ~/.claude/skills/multi-role-project-skill/init.py
```

---

---

## 中文版本

### 什么是 Skill？

Claude Code skills 是可以在 Claude Code 终端中调用的可复用工具/命令。

**调用格式：**
```
/skill-name 参数1 参数2 --选项 值
```

**例子：**
```
/multi-role-project-init "我的项目" --language zh
```

---

## 安装方法

### 方法 1：全局安装（推荐）

为你的所有项目安装：

```bash
# 1. Clone 仓库
git clone https://github.com/findones/multi-role-project-skill.git ~/.claude/skills/multi-role-project-skill

# 2. 验证安装
ls ~/.claude/skills/multi-role-project-skill/
# 应该显示: skill.yaml, init.py, templates/, README.md

# 3. 完成！现在可以使用：
# /multi-role-project-init "项目名称"
```

### 方法 2：项目级安装

只为这个项目安装：

```bash
# 1. 进入你的项目目录
cd /your/project
mkdir -p .claude/skills/multi-role-project-skill

# 2. 复制 skill 文件
cp -r [skill-source]/* .claude/skills/multi-role-project-skill/

# 3. 在这个项目中使用：
# /multi-role-project-init "项目名称"
```

### 方法 3：下载并解压

```bash
# 下载 ZIP
wget https://github.com/findones/multi-role-project-skill/archive/main.zip

# 解压到 skills 目录
mkdir -p ~/.claude/skills/multi-role-project-skill
unzip main.zip -d ~/.claude/skills/multi-role-project-skill
```

---

## 文件结构

安装后，你应该有：

```
~/.claude/skills/multi-role-project-skill/
│
├── skill.yaml                      ← Skill 定义（必需）
├── init.py                         ← 实现代码（必需）
├── templates/                      ← 项目模板（必需）
│   ├── STATUS.md
│   ├── method.md
│   ├── CODE_MAP.md
│   ├── RESULTS.md
│   ├── WORK_PLAN.md
│   └── docs/roles/
│       ├── architect.md
│       ├── engineer.md
│       ├── paper.md
│       └── repro.md
│
├── README.md                       ← 文档
├── INSTALL.md                      ← 安装指南
└── LICENSE                         ← 许可证
```

---

## 安装后的使用

安装成功后，在任何 Claude Code 窗口中可以使用：

```bash
# 基本用法
/multi-role-project-init "我的项目名称"

# 指定语言
/multi-role-project-init "我的项目" --language zh

# 指定角色
/multi-role-project-init "我的项目" --roles architect,engineer

# 指定输出目录
/multi-role-project-init "我的项目" --output /path/to/project
```

---

## 验证安装

验证 skill 是否正确安装：

```bash
# 检查文件存在
ls ~/.claude/skills/multi-role-project-skill/skill.yaml
ls ~/.claude/skills/multi-role-project-skill/init.py

# 在 Claude Code 中尝试使用：
# /multi-role-project-init "测试"

# 应该创建：
# - STATUS.md
# - method.md
# - CODE_MAP.md
# - 等等
```

---

## 故障排除

### Skill 没有出现

```bash
# 确保目录存在
mkdir -p ~/.claude/skills/multi-role-project-skill

# 确保文件在那里
ls ~/.claude/skills/multi-role-project-skill/skill.yaml
ls ~/.claude/skills/multi-role-project-skill/init.py

# 重启 Claude Code
# （关闭并重新打开应用程序）
```

### 脚本无法运行

```bash
# 确保 init.py 可执行
chmod +x ~/.claude/skills/multi-role-project-skill/init.py

# 确保 Python 3 已安装
python3 --version

# 手动测试脚本
python3 ~/.claude/skills/multi-role-project-skill/init.py "测试项目"
```

### 权限被拒绝

```bash
# 给予适当的权限
chmod 755 ~/.claude/skills/multi-role-project-skill/
chmod 755 ~/.claude/skills/multi-role-project-skill/init.py
```
