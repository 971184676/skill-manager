# Skill Manager — 技能管理器

**中文** | 跨平台 AI 技能管理与智能推荐系统，支持 Claude Code、OpenClaw、Codex、Tree、Hermes 等多种智能体。

**English** | Cross-platform AI skill management and smart recommendation system for Claude Code, OpenClaw, Codex, Tree, Hermes and other agents.

---

## 📋 目录 · Table of Contents

1. [功能特性 · Features](#功能特性--features)
2. [支持的智能体平台 · Supported Platforms](#支持的智能体平台--supported-platforms)
3. [快速开始 · Quick Start](#快速开始--quick-start)
4. [安装指南 · Installation](#安装指南--installation)
5. [核心工作流 · Core Workflows](#核心工作流--core-workflows)
6. [项目结构 · Project Structure](#项目结构--project-structure)
7. [开发说明 · Development](#开发说明--development)

---

## ✨ 功能特性 · Features

**中文**:

| 特性 Feature | 详细说明 Description |
|---|---|
| 🔄 **跨平台技能管理** | 支持 Claude Code、OpenClaw、Codex、Tree、Hermes 等多种智能体，统一管理所有技能 |
| 🧠 **智能技能推荐** | 基于项目类型和技术栈自动匹配最佳技能组合 |
| 🎯 **灵活技能调换** | 展示推荐组合后，可自由添加、移除或替换任意技能 |
| 📊 **Excel 可视化仓库** | 自动生成技能分类 Excel 表格，直观展示所有技能信息 |
| ⚙️ **自动同步** | 安装新技能时自动同步到 Excel 仓库 |
| 🔄 **同一任务后续步骤** | 同一任务的后续步骤可保持原有技能组合或重新推荐 |
| 💾 **用户偏好记忆** | 记住用户的技能组合偏好，下次自动应用 |

**English**:

| 特性 Feature | 详细说明 Description |
|---|---|
| 🔄 **Cross-platform Skill Management** | Supports Claude Code, OpenClaw, Codex, Tree, Hermes and other agents, unified skill management |
| 🧠 **Smart Skill Recommendation** | Auto-matches best skill combination based on project type & stack |
| 🎯 **Flexible Skill Swapping** | After showing combo, freely add/remove/replace any skill |
| 📊 **Excel Visual Repository** | Auto-generates categorized Excel spreadsheet for intuitive skill display |
| ⚙️ **Auto-sync** | Auto-syncs to Excel repository when new skills are installed |
| 🔄 **Same Task Follow-up** | Keep existing combo or re-recommend for follow-up steps in same task |
| 💾 **User Preference Memory** | Remembers user's skill combo preferences, auto-applies next time |

---

## 🌐 支持的智能体平台 · Supported Agent Platforms

Skill Manager 可以在以下平台上使用：

**中文**:
| 平台 Platform | 说明 Description | 技能存储路径 Skill Storage |
|---|---|---|
| **Claude Code** | 主要目标平台，优先支持 · Primary target, first-class support | `~/.claude/skills/` |
| **OpenClaw** | 多智能体协作平台 · Multi-agent collaboration | `~/.agents/skills/` |
| **Codex** | 代码生成与编辑 · Code generation & editing | 兼容路径 Compatible paths |
| **Tree** | 树状结构项目导航 · Tree-structured navigation | 兼容路径 Compatible paths |
| **Hermes** | 消息传递与任务编排 · Messaging & orchestration | 兼容路径 Compatible paths |

**English**:
| 平台 Platform | 说明 Description | 技能存储路径 Skill Storage |
|---|---|---|
| **Claude Code** | Primary target, first-class support | `~/.claude/skills/` |
| **OpenClaw** | Multi-agent collaboration | `~/.agents/skills/` |
| **Codex** | Code generation & editing | Compatible paths |
| **Tree** | Tree-structured navigation | Compatible paths |
| **Hermes** | Messaging & orchestration | Compatible paths |

---

## 🚀 快速开始 · Quick Start

### 前置依赖 · Prerequisites

**中文** | 确保你已安装 Python 3.7+ 和 `openpyxl` 库：

**English** | Make sure you have Python 3.7+ and `openpyxl` installed:

```bash
pip install -r requirements.txt
```

### 安装与使用 · Install & Use

**中文**:
```bash
# 1. 克隆项目 · Clone the project
git clone https://github.com/971184676/skill-manager.git
cd skill-manager

# 2. 首次同步技能 · First time sync skills
python scripts/sync-skills-repo.py
# → 这会自动扫描所有已安装的技能并创建 Excel 仓库
# → This will auto-scan all installed skills and create Excel repository

# 3. 测试推荐功能 · Test recommendation
python scripts/skill-recommend.py --project . --interactive
# → 分析当前项目并推荐技能组合
# → Analyze current project and recommend skill combo

# 4. 列出所有技能 · List all skills
python scripts/skill-recommend.py --list-all
```

**English**:
```bash
# 1. 克隆项目 · Clone the project
git clone https://github.com/971184676/skill-manager.git
cd skill-manager

# 2. 首次同步技能 · First time sync skills
python scripts/sync-skills-repo.py
# → This will auto-scan all installed skills and create Excel repository

# 3. 测试推荐功能 · Test recommendation
python scripts/skill-recommend.py --project . --interactive
# → Analyze current project and recommend skill combo

# 4. 列出所有技能 · List all skills
python scripts/skill-recommend.py --list-all
```

---

## 📦 安装指南 · Installation

### 方法一：作为技能安装 · Method 1: Install as a Skill

**中文**:
```bash
# 1. 确保你有目标平台的技能目录
#    Make sure you have skill directory for your target platform
mkdir -p ~/.claude/skills/skill-manager
mkdir -p ~/.agents/skills/skill-manager

# 2. 复制 SKILL.md 到技能目录
#    Copy SKILL.md to skill directory
cp skills/skill-manager/SKILL.md ~/.claude/skills/skill-manager/
cp skills/skill-manager/SKILL.md ~/.agents/skills/skill-manager/

# 3. 首次运行同步 · First run sync
python scripts/sync-skills-repo.py
```

**English**:
```bash
# 1. 确保你有目标平台的技能目录
#    Make sure you have skill directory for your target platform
mkdir -p ~/.claude/skills/skill-manager
mkdir -p ~/.agents/skills/skill-manager

# 2. 复制 SKILL.md 到技能目录
#    Copy SKILL.md to skill directory
cp skills/skill-manager/SKILL.md ~/.claude/skills/skill-manager/
cp skills/skill-manager/SKILL.md ~/.agents/skills/skill-manager/

# 3. 首次运行同步 · First run sync
python scripts/sync-skills-repo.py
```

### 方法二：仅使用工具脚本 · Method 2: Use Tool Scripts Only

**中文** | 你也可以直接使用工具脚本而不安装为技能：

**English** | You can also use the tool scripts directly without installing as a skill:

```bash
# 只需把 scripts/ 目录放到你喜欢的位置，就可以使用所有功能
# Just place the scripts/ directory in your preferred location
```

---

## 🔄 核心工作流 · Core Workflows

### 工作流 1：编程任务开始 · Workflow 1: Start a Programming Task

**中文**:
1. 用户提出任务："帮我做一个 React 项目"
2. skill-manager 自动分析项目，推荐技能组合
3. 用户选择：确认/调换/跳过
4. 开始任务

**English**:
1. User proposes task: "Help me make a React project"
2. skill-manager auto-analyzes project, recommends skill combo
3. User chooses: Confirm / Swap / Skip
4. Start task

### 工作流 2：安装新技能 · Workflow 2: Install a New Skill

**中文**:
1. 用户运行：`npx skills add some-skill`
2. PostToolUse hook 自动触发同步
3. Excel 仓库自动更新

**English**:
1. User runs: `npx skills add some-skill`
2. PostToolUse hook auto-triggers sync
3. Excel repository auto-updates

### 工作流 3：同一任务后续步骤 · Workflow 3: Follow-up in Same Task

**中文**:
1. 用户在同一任务下提出后续需求
2. skill-manager 询问：保持原有组合 OR 重新推荐
3. 用户选择后继续

**English**:
1. User proposes follow-up needs in same task
2. skill-manager asks: Keep existing combo OR re-recommend
3. Continue after user chooses

---

## 📁 项目结构 · Project Structure

```
skill-manager/
├── skills/                          # 技能目录 · Skills directory
│   └── skill-manager/              # skill-manager 技能（你开发的）· Your skill
│       └── SKILL.md                # 技能定义文件 · Skill definition
│
├── scripts/                        # 工具脚本 · Tool scripts
│   ├── sync-skills-repo.py        # 同步引擎 · Sync engine
│   ├── skill-recommend.py         # 推荐引擎 · Recommend engine
│   └── skill-classifier.json      # 16类分类规则 · Classification rules
│
├── .claude/                       # Claude 配置 · Claude config
│   └── settings.json              # PostToolUse hook 配置 · Hook config
│
├── .gitignore                     # Git 忽略规则 · Git ignore rules
├── CLAUDE.md                      # 工作区指令 · Workspace instructions
├── README.md                      # 项目说明 · This file
├── requirements.txt               # Python 依赖 · Python dependencies
│
├── (生成的文件，不提交 · Generated files, not committed)
│   ├── Skill仓库.xlsx             # 技能 Excel 仓库 · Skill Excel repository
│   ├── skills-index.json          # 技能索引 · Skill index
│   └── .skill-preferences.json    # 用户偏好 · User preferences
```

---

## 🛠 CLI 命令参考 · CLI Reference

### sync-skills-repo.py · 同步工具

**中文**:
```bash
# 完整语法 · Full syntax
python scripts/sync-skills-repo.py [--help] [--dir <path>]

# 示例 · Examples
python scripts/sync-skills-repo.py                    # 同步所有技能 · Sync all
python scripts/sync-skills-repo.py --dir ~/.claude/skills  # 只同步指定目录 · Only sync specific dir
```

**English**:
```bash
# 完整语法 · Full syntax
python scripts/sync-skills-repo.py [--help] [--dir <path>]

# 示例 · Examples
python scripts/sync-skills-repo.py                    # 同步所有技能 · Sync all
python scripts/sync-skills-repo.py --dir ~/.claude/skills  # 只同步指定目录 · Only sync specific dir
```

### skill-recommend.py · 推荐工具

**中文**:
```bash
# 完整语法 · Full syntax
python scripts/skill-recommend.py --project <path> [--interactive] [--output json]
python scripts/skill-recommend.py --list-all
python scripts/skill-recommend.py --add <skill> --remove <skill>

# 示例 · Examples
python scripts/skill-recommend.py --project . --interactive  # 交互模式 · Interactive
python scripts/skill-recommend.py --project . --output json  # JSON 输出 · JSON output
python scripts/skill-recommend.py --list-all                # 列出所有 · List all
python scripts/skill-recommend.py --add frontend-design     # 添加偏好 · Add preference
python scripts/skill-recommend.py --remove lark-vc           # 移除偏好 · Remove preference
```

**English**:
```bash
# 完整语法 · Full syntax
python scripts/skill-recommend.py --project <path> [--interactive] [--output json]
python scripts/skill-recommend.py --list-all
python scripts/skill-recommend.py --add <skill> --remove <skill>

# 示例 · Examples
python scripts/skill-recommend.py --project . --interactive  # 交互模式 · Interactive
python scripts/skill-recommend.py --project . --output json  # JSON 输出 · JSON output
python scripts/skill-recommend.py --list-all                # 列出所有 · List all
python scripts/skill-recommend.py --add frontend-design     # 添加偏好 · Add preference
python scripts/skill-recommend.py --remove lark-vc           # 移除偏好 · Remove preference
```

---

## 🏷️ 技能分类系统 · Skill Classification System

**中文** | 技能被自动分类为 16 个类别：

**English** | Skills are auto-classified into 16 categories:

| 分类 Category | 英文名称 | 覆盖范围 Coverage |
|---|---|---|
| 前端开发 | Frontend | React, Vue, Angular, Tailwind, Web |
| 后端开发 | Backend | FastAPI, Django, Express, API |
| 飞书/Lark办公 | Lark Office | 飞书文档、表格、审批、日历等 |
| AI/机器学习 | AI/ML | LLM, PyTorch, RAG, Agent |
| DevOps/部署 | DevOps | Docker, K8s, CI/CD |
| 数据库 | Database | SQL, NoSQL, ORM, Redis |
| 测试 | Testing | Jest, Pytest, Playwright, E2E |
| 文档写作 | Documentation | Markdown, API文档, 知识库 |
| 设计/UI/UX | Design | 界面设计, 图标, 配色 |
| 代码质量/安全 | Code Quality | 代码审查, Lint, 安全审计 |
| 项目管理 | Project Mgmt | 任务跟踪, 协作, Jira |
| 移动开发 | Mobile | iOS, Android, Flutter |
| 性能优化 | Performance | 性能分析, 打包优化, 缓存 |
| 数据分析 | Data Analytics | 可视化, 报表, ETL |
| 技能管理 | Skill Mgmt | 技能发现, 创建, 管理 |
| 办公自动化 | Office Automation | 工作流, 报表自动化 |

---

## 💡 使用技巧 · Usage Tips

**中文**:

1. **首次使用**：先运行一次 `sync-skills-repo.py` 初始化仓库
2. **推荐新技能**：安装新技能后，同步会自动触发
3. **自定义组合**：推荐不满意可以随时手动调换
4. **多平台使用**：在不同智能体平台上都可以使用相同的技能管理方式

**English**:

1. **First Use**: Run `sync-skills-repo.py` once to initialize repository
2. **Recommend New Skills**: After installing new skills, sync auto-triggers
3. **Custom Combos**: If recommendations aren't perfect, manually swap anytime
4. **Multi-platform Use**: Same skill management approach works on all agent platforms

---

## 🔧 开发说明 · Development

如果你想修改或扩展 Skill Manager：

**中文**:
1. `skills/skill-manager/SKILL.md` → 技能的主要描述和使用说明
2. `scripts/skill-classifier.json` → 技能分类规则
3. `scripts/sync-skills-repo.py` → 同步引擎
4. `scripts/skill-recommend.py` → 推荐引擎

**English**:
1. `skills/skill-manager/SKILL.md` → Main skill description & usage
2. `scripts/skill-classifier.json` → Skill classification rules
3. `scripts/sync-skills-repo.py` → Sync engine
4. `scripts/skill-recommend.py` → Recommendation engine

---

## 📄 License

MIT License - 详见 [LICENSE](LICENSE) 文件。

---

## 🤝 贡献 · Contributing

欢迎提交 Issue 和 Pull Request！

---

## 📞 问题与反馈 · Issues & Feedback

如有问题或建议，请在 [GitHub Issues](https://github.com/971184676/skill-manager/issues) 中提出。
