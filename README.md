🧠 Skill Manager
===============

Claude Code / OpenClaw / Codex / Tree / Hermes 技能管理器 · Skill Manager for Multi-Agent Platforms

自动管理 · 智能推荐 · 自由调换 · 跨平台支持
Auto-manage · Smart Recommend · Free Swap · Multi-platform Support

[![Claude Code](https://img.shields.io/badge/Claude%20Code-skill-blue)]()
[![OpenClaw](https://img.shields.io/badge/OpenClaw-skill-green)]()
[![Codex](https://img.shields.io/badge/Codex-skill-purple)]()
[![Tree](https://img.shields.io/badge/Tree-skill-orange)]()
[![Hermes](https://img.shields.io/badge/Hermes-skill-pink)]()
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-brightgreen)]()
[![License MIT](https://img.shields.io/badge/License-MIT-orange)]()

---

📖 项目介绍 · Introduction
-----------------------

**中文** | Skill Manager 是一个**元技能（Meta-Skill）**，用于管理所有已安装的 AI 开发技能。它支持 Claude Code、OpenClaw、Codex、Tree、Hermes 等多种智能体平台，让你在任何平台上都能轻松管理技能。

它解决了四个痛点：

1.  **技能太多无从选择** — 电脑里存了 100+ 技能，每次不知道用哪个
2.  **质量参差不齐** — 装了不合适的技能反而影响效率
3.  **缺乏上下文感知** — 做前端项目时推荐无关技能，牛头不对马嘴
4.  **跨平台管理麻烦** — 不同智能体平台技能分散，难以统一管理

**English** | Skill Manager is a **Meta-Skill** for managing all your installed AI development skills. It supports Claude Code, OpenClaw, Codex, Tree, Hermes and other agent platforms, letting you easily manage skills anywhere.

It solves four pain points:

1.  **Too many choices** — 100+ skills installed, no idea which to use
2.  **Inconsistent quality** — wrong skills hurt more than help
3.  **No context awareness** — recommending irrelevant skills for the task at hand
4.  **Cross-platform hassle** — skills scattered across different agents, hard to unify

---

✨ 核心功能 · Core Features
---------------------------

### 🎯 智能技能推荐 · Smart Skill Recommendation

在编程任务的计划阶段，自动分析项目类型、技术栈，推荐最合适的技能组合。

Automatically analyzes project type and tech stack during planning, recommends the best skill combination.

### 🔄 同一任务后续步骤 · Follow-up Steps in Same Task

同一任务的后续需求时，询问用户是保持原有技能组合，还是重新推荐新的组合。

For follow-up needs in same task, asks whether to keep existing combo or re-recommend.

### 🎭 自由调换技能 · Free Skill Swap

展示推荐组合后，你可以自由添加、移除、替换任意技能，直到满意为止。

After showing recommendations, you can freely add/remove/replace any skills until satisfied.

### 📊 Excel 可视化仓库 · Excel Visual Repository

自动扫描所有已安装技能，生成分类的 Excel 表格，直观浏览。

Automatically scans all installed skills, generates categorized Excel spreadsheet for intuitive browsing.

### ⚙️ 自动同步 · Auto-sync

安装新技能时，PostToolUse hook 自动触发同步，无需手动操作。

Auto-triggers sync when new skills are installed via PostToolUse hook - no manual work needed.

---

🌐 支持的智能体平台 · Supported Agent Platforms
-------------------------------------------------

| 平台 Platform | 说明 Description | 状态 Status |
|---|---|---|
| **Claude Code** | 主要目标平台，优先支持 · Primary target, first-class support | ✅ 完全支持 · Full Support |
| **OpenClaw** | 多智能体协作平台 · Multi-agent collaboration | ✅ 完全支持 · Full Support |
| **Codex** | 代码生成与编辑 · Code generation & editing | ✅ 兼容 · Compatible |
| **Tree** | 树状结构项目导航 · Tree-structured navigation | ✅ 兼容 · Compatible |
| **Hermes** | 消息传递与任务编排 · Messaging & orchestration | ✅ 兼容 · Compatible |

---

🚀 快速开始 · Quick Start
--------------------------

### 前置依赖 · Prerequisites

确保已安装 Python 3.8+ 和 `openpyxl`：

Make sure you have Python 3.8+ and `openpyxl` installed:

```bash
pip install openpyxl
# 或者 / or
pip install -r requirements.txt
```

### 安装 · Install

```bash
# 1. 克隆仓库 · Clone repository
git clone https://github.com/971184676/skill-manager.git
cd skill-manager

# 2. 首次同步技能 · First-time skill sync
python scripts/sync-skills-repo.py
# → 自动扫描并创建 Excel 仓库 · Auto-scan and create Excel repo

# 3. 测试推荐 · Test recommendation
python scripts/skill-recommend.py --project . --interactive
```

---

📁 项目结构 · Project Structure
----------------------------------

```
skill-manager/
├── skills/
│   └── skill-manager/
│       └── SKILL.md           # 技能主文件 · Main skill file
├── scripts/
│   ├── sync-skills-repo.py    # 同步引擎 · Sync engine
│   ├── skill-recommend.py     # 推荐引擎 · Recommendation engine
│   └── skill-classifier.json  # 16类分类规则 · 16-category rules
├── .claude/
│   └── settings.json          # PostToolUse hook 配置 · Hook config
├── .gitignore
├── CLAUDE.md
├── README.md                  # 本文件 · This file
└── requirements.txt
```

---

🔧 命令参考 · Command Reference
--------------------------------

### 同步技能 · Sync Skills

```bash
python scripts/sync-skills-repo.py
# 或者扫描特定目录 / or scan specific directory
python scripts/sync-skills-repo.py --dir ~/.claude/skills
```

### 推荐技能 · Recommend Skills

```bash
# 交互模式 · Interactive mode
python scripts/skill-recommend.py --project . --interactive

# JSON 输出 · JSON output
python scripts/skill-recommend.py --project . --output json

# 列出所有技能 · List all skills
python scripts/skill-recommend.py --list-all
```

---

🏷️ 技能分类系统 · Skill Classification System
-----------------------------------------------

16个自动分类 · 16 auto-categories:

| 分类 Category | 英文 English | 示例 Examples |
|---|---|---|
| 前端开发 | Frontend | React, Vue, Tailwind |
| 后端开发 | Backend | FastAPI, Django, Express |
| 飞书/Lark办公 | Lark Office | 文档、表格、审批 · Docs, Sheets, Approval |
| AI/机器学习 | AI/ML | LLM, PyTorch, RAG |
| DevOps/部署 | DevOps | Docker, K8s, CI/CD |
| 数据库 | Database | SQL, ORM, Redis |
| 测试 | Testing | Jest, Pytest, Playwright |
| 文档写作 | Documentation | Markdown, API Docs |
| 设计/UI/UX | Design | UI, Icons, Figma |
| 代码质量/安全 | Code Quality | Lint, Audit |
| 项目管理 | Project Mgmt | Jira, Tasks |
| 移动开发 | Mobile | iOS, Android, Flutter |
| 性能优化 | Performance | Profiling, Cache |
| 数据分析 | Data Analytics | Visualization, ETL |
| 技能管理 | Skill Mgmt | Skill Manager, Find Skills |
| 办公自动化 | Office Automation | Workflows, Reports |

---

💡 使用场景 · Usage Scenarios
--------------------------------

### 场景 1：开始新项目 · Start New Project

1.  你说："帮我做一个 React 前端项目"
2.  Skill Manager 自动分析，推荐技能组合
3.  你选择：确认/调换/跳过
4.  开始编码！

### 场景 2：同一任务后续 · Same Task Follow-up

1.  你接着说："刚才的项目，帮我加个后端 API"
2.  Skill Manager 询问：保持现有组合？还是重新推荐？
3.  你选择后继续！

### 场景 3：安装新技能 · Install New Skill

1.  运行：`npx skills add some-skill`
2.  PostToolUse hook 自动触发同步
3.  Excel 仓库自动更新！

---

📄 License
------------

MIT License - 详见 [LICENSE](LICENSE) 文件。

---

🤝 贡献 · Contributing
-----------------------

欢迎提交 Issue 和 Pull Request！

---

📞 反馈 · Feedback
--------------------

如有问题或建议，请在 [GitHub Issues](https://github.com/971184676/skill-manager/issues) 中提出。
