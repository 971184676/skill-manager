---
name: skill-manager
description: "管理所有已安装的 AI 技能(Skills)。在编程/开发任务的计划阶段自动分析项目并推荐技能组合，询问用户是否使用，支持自由调换技能。在同一任务的后续步骤中，询问用户是保持原有技能组合还是推荐新的组合。安装新 Skill 时自动同步到 Excel 仓库。用户询问技能管理、计划推荐、技能调换时触发：列出、推荐、分类、调换。Manage all installed AI skills for Claude Code. Automatically analyzes projects and recommends skill combos during task planning, asks user for confirmation, supports free skill swapping. In follow-up steps of the same task, asks user whether to keep existing combo or recommend new one. Auto-syncs to Excel database when new skills are installed."
---

# Skill Manager — 技能管理器 · Skill Manager

---

## 📖 概述 · Overview

**中文** | 本技能是全套 Skill 管理系统的核心入口。当你开始一个编程任务时，它会自动分析项目上下文、推荐最优技能组合、并让你自由调换。同时，每当有新技能被安装时，它会自动同步到 Excel 仓库。

**English** | This skill is the core entry point for the Skill Management system. When you start a programming task, it automatically analyzes the project context, recommends the best skill combination, and lets you freely swap skills. It also auto-syncs to the Excel database whenever new skills are installed.

### 三大核心能力 · Three Core Capabilities

| # | 能力 · Capability | 中文说明 | English Description |
|---|-------------------|---------|-------------------|
| 1 | **自动注册 Auto-Register** | 首次下载时自动扫描本机已有技能并创建 Excel 仓库；之后每安装一个新技能自动填入 | Auto-scan existing skills on first run & create database; auto-register every new skill |
| 2 | **智能推荐 Smart Recommend** | 在编程任务的计划阶段，分析项目类型和技术栈，推荐最匹配的技能组合 | Analyze project type & tech stack during planning, recommend best-matching skills |
| 3 | **自由调换 Free Swap** | 展示推荐组合后，询问用户是否确认；用户可自由添加/移除/替换任意技能 | Ask for user confirmation; let users add / remove / replace any skill freely |

---

## 🎯 触发时机 · When to Trigger

### ✅ 必须触发 · Must Trigger

| 场景 Scenario | 中文说明 | English Description |
|---|---|---|
| 编程任务计划 | 用户提出"做一个XX项目"、"实现XX功能"、"修复XX问题"时，编码**之前**必须先推荐 | Before coding ANY programming/dev task, run recommendation first |
| 新技能安装 | `npx skills add` 安装技能后自动同步 | Auto-sync after `npx skills add` via PostToolUse hook |
| 用户主动询问 | "有哪些技能"、"帮我推荐"、"管理技能"等 | User asks about skills, recommendations, or management |

### ⏹ 不触发 · Do NOT Trigger

| 场景 Scenario | 说明 Reason |
|---|---|
| 纯对话/问答 Pure chat | 不涉及编码或技能 · No coding or skills involved |
| 用户明确跳过 User says skip | "不用推荐"、"跳过" · "Don't recommend" / "Skip" |

---

### 🔄 后续任务触发 · Follow-up Task Trigger

| 场景 Scenario | 中文说明 | English Description |
|---|---|---|
| 同一任务后续追问 Follow-up | 询问用户：保持现有组合 OR 重新推荐 · Ask user: keep existing combo OR re-recommend |

---

## 🔄 核心工作流 · Core Workflows

### 流程 A：首次下载 → 自动检索已有技能
### Flow A: First Install → Auto-scan Existing Skills

**中文** | 当用户首次安装 skill-manager 时（检测到 `Skill仓库.xlsx` 不存在），自动执行以下步骤：

**English** | When the user first installs skill-manager (detected by missing `Skill仓库.xlsx`), automatically run:

```
1. Auto-run: python scripts/sync-skills-repo.py
2. Scan ~/.agents/skills/ and ~/.claude/skills/ for all installed skills
3. Read each skill's SKILL.md, extract name and description
4. Classify into 16 categories (keyword matching + weighted scoring)
5. Generate Skill仓库.xlsx (visual Excel spreadsheet)
6. Generate skills-index.json (index for recommendation engine)
7. Report total skills found and category distribution
```

---

### 流程 B：安装新技能 → 自动填入
### Flow B: New Skill Install → Auto-register

**中文** | 通过 `npx skills add` 安装新技能时，PostToolUse hook 自动触发同步：

**English** | When installing via `npx skills add`, the PostToolUse hook auto-triggers sync:

```
Trigger conditions:
  - .claude/settings.json has PostToolUse hook configured
  - Hook matches "npx skills (add|install|remove|update)"
  - Auto-executes: python scripts/sync-skills-repo.py

Manual trigger:
  python scripts/sync-skills-repo.py
  Or double-click sync-skills.bat (Windows)
```

---

### 流程 C：编程任务计划 → 技能推荐（核心流程）
### Flow C: Task Planning → Skill Recommendation (Core)

**中文** | 当用户提出一个编程/开发任务时，按照以下步骤执行：

**English** | When the user starts a programming/development task, follow these steps:

```
Step 1: Analyze project context
   Run: python scripts/skill-recommend.py --project <path> --output json
   Read output for:
   - Project type: frontend / backend / fullstack / AI / CLI
   - Tech stack: React, Python, Node.js...
   - Language: TypeScript, Python, Go...
   - Has tests? Has database?

Step 2: Format and display recommendations

   =================================================================
     >> Skill 组合推荐 · Skill Combo Recommendation <<
     项目 Project: my-app
     类型 Type: 全栈项目 Full-stack
     技术栈 Stack: React, FastAPI, TypeScript
   =================================================================

     [核心技能 Core Skills]
       -> 无论项目类型，建议启用以下核心技能
       -> Core skills recommended regardless of project type
       1. find-skills      - 技能发现与安装 · Skill discovery & install
       2. skill-manager    - 技能管理 · Skill management
       3. skill-creator    - 技能创建 · Skill creation

     [前端开发 Frontend]
       -> 检测到全栈项目，推荐前端开发技能
       -> Full-stack project detected, recommending frontend skills
       4. frontend-design  - 前端界面设计 · Frontend UI design

   -----------------------------------------------------------------
   是否使用以上技能组合？Use this combo?
     1. 直接开始 · Start with this combo
     2. 替换技能 · Swap skills
     3. 跳过推荐 · Skip
   -----------------------------------------------------------------

Step 3: Wait for user choice
   - [1] -> Confirm combo, start task
   - [2] -> Enter skill swap flow
   - [3] -> Skip recommendation

Step 4: Start task
   Continue original task logic after user confirms.
```

---

### 流程 D：技能调换（组合自定义）
### Flow D: Skill Swapping (Combo Customization)

**中文** | 当用户选择 "替换组合中的技能" 时：

**English** | When the user chooses to "swap skills":

```
1. List all skills in the current recommendation (numbered)
2. List all available skills (grouped by category)
3. Ask user:
   "Remove which skill? (number/name, comma-separated, empty=skip)
    要移除哪个技能？(编号/名称, 多个用逗号分隔, 空=跳过)"
   "Add which skill? (name, comma-separated, empty=skip)
    要添加哪个技能？(名称, 多个用逗号分隔, 空=跳过)"
4. Adjust combo based on input
5. Show the new combo
6. Ask again: "Satisfied? [y/n] · 是否满意？[y/n]"
   - y: Confirm combo
   - n: Back to step 1
7. Optional: "Save preference? · 是否保存此偏好？"
   -> Auto-applied for similar projects next time
```

#### 调换规则 · Swap Rules

| 规则 Rule | 中文说明 | English Description |
|---|---|---|
| 核心技能 Core skills | skill-manager/find-skills 默认推荐但非必须，用户可移除 | Recommended by default but removable |
| 未安装的技能 Missing skills | 调用 `find-skills` 搜索安装 · Use find-skills to search & install |
| 偏好记忆 Preferences | 保存在 `.skill-preferences.json`，支持 `--add`/`--remove` 命令 · Persisted via CLI commands |

---

### 流程 E：同一任务后续步骤 · 选择技能组合
### Flow E: Same Task Follow-up · Choose Skill Combo

**中文** | 当用户在同一任务下提出后续编程/修改需求时，按照以下步骤执行：

**English** | When user presents follow-up programming/modification needs in the same task, follow these steps:

```
Step 1: Detect task context
   - Is this a follow-up to the same original task?
   - Has a skill combo already been selected for this task?

Step 2: Display confirmation prompt

   =================================================================
     >> 技能组合选择 · Skill Combo Choice <<
     检测到这是同一任务的后续步骤
     Detected: this is a follow-up to the same task
   =================================================================

     当前技能组合 Current Combo:
       1. find-skills      - 技能发现与安装
       2. skill-manager    - 技能管理
       3. frontend-design  - 前端界面设计

   -----------------------------------------------------------------
   选择操作 Choose action:
     1. 保持原有技能组合 · Keep current combo
     2. 重新推荐技能组合 · Recommend new combo
     3. 手动调整技能组合 · Adjust manually
   -----------------------------------------------------------------

Step 3: Wait for user choice
   - [1] -> Keep combo, continue with current skills
   - [2] -> Re-run full recommendation (Flow C)
   - [3] -> Enter skill swap flow (Flow D)

Step 4: Continue with task
   Proceed with original task logic based on user's choice.
```

---

## 🛠 CLI 工具参考 · CLI Reference

```bash
# 同步技能到 Excel（首次运行自动创建）
# Sync skills to Excel (auto-creates on first run)
python scripts/sync-skills-repo.py

# 分析项目并推荐技能（交互模式）
# Analyze project & recommend skills (interactive)
python scripts/skill-recommend.py --project . --interactive

# 列出所有技能 · List all skills
python scripts/skill-recommend.py --list-all

# 查看项目信息（JSON 格式）
# View project info (JSON format)
python scripts/skill-recommend.py --project . --output json

# 添加/移除偏好 · Add/remove preferences
python scripts/skill-recommend.py --add frontend-design
python scripts/skill-recommend.py --remove lark-vc
```

---

## 📦 安装 · Installation

### 前置依赖 · Prerequisites

```bash
pip install openpyxl
```

### 安装 skill-manager · Install the Skill

```bash
# 1. 克隆或下载本仓库
#    Clone or download this repository
git clone <repo-url> ~/xielaoban
cd ~/xielaoban

# 2. 安装技能到 Claude
#    Install skill to Claude
mkdir -p ~/.claude/skills/skill-manager
cp skills/skill-manager/SKILL.md ~/.claude/skills/skill-manager/

# 3. （可选）安装到 agents 目录
#    (Optional) Install to agents directory
mkdir -p ~/.agents/skills/skill-manager
cp skills/skill-manager/SKILL.md ~/.agents/skills/skill-manager/

# 4. 首次同步 — 自动创建 Excel 仓库
#    First sync — auto-create Excel database
python scripts/sync-skills-repo.py

# 5. 测试推荐功能 · Test recommendation
python scripts/skill-recommend.py --list-all
```

### 自动触发配置 · Auto-trigger Configuration

**中文** | 项目已内置 `.claude/settings.json`，配置了 PostToolUse hook，安装新技能后自动同步：

**English** | The project includes `.claude/settings.json` with a PostToolUse hook for auto-sync after installing new skills:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "npx skills (add|install|remove|update)",
        "hook": "python scripts/sync-skills-repo.py"
      }
    ]
  }
}
```

---

## 🔗 与其它技能的协作 · Ecosystem Integration

| 技能 Skill | 中文协作方式 | English Integration |
|---|---|---|
| **find-skills** | 推荐组合中缺失技能时，调用 find-skills 搜索安装 | Call find-skills to search & install missing skills |
| **skill-creator** | 用户需要自定义技能时，转向 skill-creator | Route to skill-creator for custom skills |
| **其他技能 Others** | 作为推荐组合的候选池，按分类和场景推荐 | Candidate pool for recommendations by category |

---

## 🏷️ 分类系统 · Classification System

**中文** | 技能通过 `scripts/skill-classifier.json` 中的规则进行智能分类，采用 **多维度关键词匹配 + 加权评分** 算法：

**English** | Skills are classified using `scripts/skill-classifier.json` rules with **multi-dimensional keyword matching + weighted scoring**:

| 维度 Dimension | 中文说明 | English Description | 权重 Weight |
|---|---|---|---|
| 名称匹配 Name | 技能名称中的关键词 | Keywords in skill name | × 3 |
| 描述匹配 Description | SKILL.md 中的功能描述 | Keywords in function description | × 2 |
| 目录匹配 Directory | 安装目录名称 | Install directory name | × 2 |
| 冲突消解 Conflict | Lark 技能不会误分到其他类 | Lark skills stay in Lark category | Auto |

### 16 个分类 · 16 Categories

| 分类 Category | 覆盖范围 Coverage |
|---|---|
| 前端开发 Frontend | React, Vue, Angular, Tailwind, Web |
| 后端开发 Backend | FastAPI, Django, Express, API |
| 飞书/Lark办公 Lark Office | 飞书文档、表格、审批、日历等 |
| AI/机器学习 AI/ML | LLM, PyTorch, RAG, Agent |
| DevOps/部署 DevOps | Docker, K8s, CI/CD |
| 数据库 Database | SQL, NoSQL, ORM, Redis |
| 测试 Testing | Jest, Pytest, Playwright, E2E |
| 文档写作 Documentation | Markdown, API文档, 知识库 |
| 设计/UI/UX Design | 界面设计, 图标, 配色 |
| 代码质量/安全 Code Quality | 代码审查, Lint, 安全审计 |
| 项目管理 Project Mgmt | 任务跟踪, 协作, Jira |
| 移动开发 Mobile | iOS, Android, Flutter |
| 性能优化 Performance | 性能分析, 打包优化, 缓存 |
| 数据分析 Data Analytics | 可视化, 报表, ETL |
| 技能管理 Skill Mgmt | 技能发现, 创建, 管理 |
| 办公自动化 Office Automation | 工作流, 报表自动化 |

---

## 📁 项目文件结构 · Project Structure

```
xielaoban/
├── skills/
│   └── skill-manager/
│       └── SKILL.md              ← 技能文件 Skill file (核心 Core)
├── scripts/
│   ├── sync-skills-repo.py       ← 同步引擎 Sync engine
│   ├── skill-recommend.py        ← 推荐引擎 Recommend engine
│   └── skill-classifier.json     ← 16类分类规则 Classification rules
├── .claude/
│   └── settings.json             ← PostToolUse hook 配置 Hook config
├── .gitignore
├── CLAUDE.md                     ← 工作区指令 Workspace instructions
└── README.md                     ← 项目说明 Project README
```

### 自动生成的文件（不提交 Git）· Auto-generated Files (Not Committed)

| 文件 File | 用途 Purpose |
|---|---|
| `Skill仓库.xlsx` | 可视化 Excel 数据库 · Visual Excel database |
| `skills-index.json` | JSON 索引，供推荐引擎快速查询 · JSON index for recommendation engine |
| `.skill-preferences.json` | 用户偏好（自动生成）· User preferences (auto-generated) |

---

## 🧪 技术细节 · Technical Details

### 推荐算法 · Recommendation Algorithm

**中文**:
1. 扫描项目目录，检测 `package.json`、`requirements.txt`、`Cargo.toml`、`go.mod` 等文件
2. 识别技术栈（React, Vue, FastAPI, Django 等）
3. 判断项目类型（前端/后端/全栈/AI/CLI）
4. 从 `skills-index.json` 中按分类匹配技能
5. 按优先级分组输出（核心 > 前端 > 后端 > 测试 > AI > 通用）

**English**:
1. Scan project directory for `package.json`, `requirements.txt`, `Cargo.toml`, `go.mod`, etc.
2. Detect tech stack (React, Vue, FastAPI, Django, etc.)
3. Determine project type (frontend/backend/fullstack/AI/CLI)
4. Match skills from `skills-index.json` by category
5. Group by priority (Core > Frontend > Backend > Testing > AI > General)

### 分类算法 · Classification Algorithm

```
score =
  name keyword matches × 3 × weight +
  desc keyword matches × 2 × weight +
  dir keyword matches × 2 × weight

confidence = normalize(score, 0-100)
```
