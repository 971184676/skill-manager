
<p align="center">
  <h1 align="center">🧠 Skill Manager</h1>
  <p align="center"><strong>Claude Code 技能管理器 · Skill Manager for Claude Code</strong></p>
  <p align="center">
    <em>自动管理 · 智能推荐 · 自由调换</em><br>
    <em>Auto-manage · Smart Recommend · Free Swap</em>
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Claude%20Code-Skill%20Manager-blue">
    <img src="https://img.shields.io/badge/Python-3.8+-green">
    <img src="https://img.shields.io/badge/License-MIT-orange">
  </p>
</p>

---

## 📖 项目介绍 · Introduction

**中文** | Skill Manager 是 **Claude Code** 的一个元技能（Meta-Skill），用于管理所有已安装的 AI 开发技能。它解决了三个痛点：

1. **技能太多无从选择** — 电脑里存了 100+ 技能，每次不知道用哪个
2. **质量参差不齐** — 装了不合适的技能反而影响效率
3. **缺乏上下文感知** — 做前端项目时推荐无关技能，牛头不对马嘴

**English** | Skill Manager is a **Meta-Skill** for Claude Code that manages all your installed AI development skills. It solves three pain points:

1. **Too many choices** — 100+ skills installed, no idea which to use
2. **Inconsistent quality** — wrong skills hurt more than help
3. **No context awareness** — recommending irrelevant skills for the task at hand

---

## ✨ 核心功能 · Features

| 功能 Feature | 说明 Description | 状态 Status |
|---|---|---|
| 🔄 **自动注册 Auto-Register** | 首次下载自动扫描本机已有技能，创建数据库 · Auto-scan existing skills on first run | ✅ |
| 🔌 **自动同步 Auto-Sync** | 通过 PostToolUse hook，安装新技能后自动填入 · Auto-register new skills via hook | ✅ |
| 🧠 **智能推荐 Smart Recommend** | 分析项目目录，识别技术栈，推荐匹配的技能 · Analyze project stack & recommend | ✅ |
| 🔀 **自由调换 Free Swap** | 用户可添加/移除/替换任意技能 · Add / remove / replace any skill freely | ✅ |
| 🏷️ **智能分类 Smart Classification** | 16 个分类，多维度加权评分 · 16 categories with weighted scoring | ✅ |
| 💾 **偏好记忆 Preference Memory** | 记住用户的技能偏好 · Remember user's skill preferences | ✅ |

---

## 🚀 快速开始 · Quick Start

### 前置依赖 · Prerequisites

| 依赖 Dependency | 说明 Description |
|---|---|
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) | 已安装 installed |
| Python 3.8+ | 已安装 installed |
| openpyxl | `pip install openpyxl` |

### 安装步骤 · Installation

```bash
# 克隆仓库 · Clone the repository
git clone <your-repo-url>
cd xielaoban

# 安装 skill-manager 到 Claude · Install skill to Claude
mkdir -p ~/.claude/skills/skill-manager
cp skills/skill-manager/SKILL.md ~/.claude/skills/skill-manager/

# 首次同步 — 自动扫描本机已有技能并创建 Excel 仓库
# First sync — auto-scan existing skills and create database
python scripts/sync-skills-repo.py

# 查看所有已注册技能 · List all registered skills
python scripts/skill-recommend.py --list-all
```

### 验证安装 · Verify Installation

```bash
# 确认技能被识别（应该看到 skill-manager 在列表中）
# Confirm skill is recognized (should see skill-manager in the list)
python scripts/sync-skills-repo.py

# 打开 Excel 查看可视化仓库
# Open Excel to view the visual database
start Skill仓库.xlsx   # Windows
open Skill仓库.xlsx     # macOS
```

---

## 📚 使用指南 · Usage Guide

### 场景 1：首次安装 — 自动检索已有技能
### Scenario 1: First Install — Auto-scan Existing Skills

```bash
python scripts/sync-skills-repo.py
```

**中文** | 系统会自动：
1. 扫描 `~/.agents/skills/` 和 `~/.claude/skills/` 下的所有技能
2. 提取每个技能的名称、描述、目录名
3. 通过智能分类算法分配到 16 个分类
4. 生成 `Skill仓库.xlsx`（可视化 Excel）和 `skills-index.json`（推荐索引）

**English** | The system will automatically:
1. Scan all skills under `~/.agents/skills/` and `~/.claude/skills/`
2. Extract each skill's name, description, and directory name
3. Classify them into 16 categories using intelligent algorithms
4. Generate `Skill仓库.xlsx` (Excel spreadsheet) and `skills-index.json` (recommendation index)

---

### 场景 2：安装新技能 — 自动同步
### Scenario 2: Installing New Skills — Auto-sync

**中文** | 通过 `npx skills add` 安装新技能后，由于 `.claude/settings.json` 中的 PostToolUse hook 配置，系统会自动运行同步脚本将新技能加入仓库。

**English** | After installing a new skill via `npx skills add`, the PostToolUse hook in `.claude/settings.json` will automatically run the sync script to register the new skill.

也可以手动触发 · Or trigger manually:

```bash
python scripts/sync-skills-repo.py
```

---

### 场景 3：开始编程任务 — 技能推荐
### Scenario 3: Starting a Coding Task — Skill Recommendation

**中文** | 当你对 Claude 说"做一个 XX 项目"时，skill-manager 会自动触发推荐。

**English** | When you ask Claude to "build a project", skill-manager will automatically trigger a recommendation.

```bash
# 分析当前项目并推荐技能组合
# Analyze current project and recommend skills
python scripts/skill-recommend.py --project .

# 交互式模式（可调换技能）
# Interactive mode (allows skill swapping)
python scripts/skill-recommend.py --project . --interactive
```

输出示例 · Example output:

```
=================================================================
  >> Skill 组合推荐 · Skill Combo Recommendation <<
  项目 Project: my-app
  类型 Type: 全栈项目 Full-stack
  技术栈 Stack: React, FastAPI, TypeScript
=================================================================

  [核心技能 Core Skills]
    1. find-skills      - 技能发现与安装 · Skill discovery & install
    2. skill-manager    - 技能管理 · Skill management
    3. skill-creator    - 技能创建 · Skill creation

  [前端开发 Frontend]
    4. frontend-design  - 前端界面设计 · Frontend UI design

  [通用工具 General Tools]
    5. code-review      - 代码审查 · Code review

-----------------------------------------------------------------
是否使用以上技能组合？Use this combo?
  1. 直接开始 · Start with this combo
  2. 替换技能 · Swap skills
  3. 跳过推荐 · Skip
```

---

### 场景 4：自定义技能组合
### Scenario 4: Customizing Skill Combinations

```bash
# 让某个技能始终出现 · Always include a skill
python scripts/skill-recommend.py --add frontend-design

# 让某个技能永不出现 · Always exclude a skill
python scripts/skill-recommend.py --remove lark-vc

# 交互式调整 · Interactive adjustment
python scripts/skill-recommend.py --project . -i
```

---

## 🏗️ 项目架构 · Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     Claude Code                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │          skill-manager (SKILL.md)               │   │
│  │    Trigger: task planning / new skill / query   │   │
│  └────────────┬──────────────────────┬──────────────┘   │
│               │                      │                  │
│         ┌─────▼──────┐        ┌──────▼──────┐          │
│         │  Sync Engine│        │  Recommend  │          │
│         │ sync-skills│        │skill-recomm.│          │
│         │ -repo.py   │        │   -end.py   │          │
│         └────┬───────┘        └──────┬───────┘          │
│              │                       │                  │
│         ┌────▼────┐           ┌──────▼──────┐          │
│         │Classifier│          │  Project    │          │
│         │ rules    │          │  Analyzer   │          │
│         │ .json    │          │  (detect    │          │
│         └─────────┘           │   stack)    │          │
│                               └──────┬───────┘          │
│                                      │                  │
│         ┌────────────────────────────▼─────────┐       │
│         │       Skill Database                 │       │
│         │  Skill仓库.xlsx  ←→  skills-index.json│       │
│         └──────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────┘
```

### 文件说明 · File Reference

| File | Role | Committed |
|------|------|-----------|
| `skills/skill-manager/SKILL.md` | Skill definition — entry point for Claude Code | ✅ |
| `scripts/sync-skills-repo.py` | Sync engine — scan, classify, generate database | ✅ |
| `scripts/skill-recommend.py` | Recommend engine — analyze project, recommend combos | ✅ |
| `scripts/skill-classifier.json` | 16-category classification rules | ✅ |
| `.claude/settings.json` | PostToolUse hook — auto-sync on new skill install | ✅ |
| `CLAUDE.md` | Workspace instructions — auto-loaded per session | ✅ |
| `Skill仓库.xlsx` | Excel database (auto-generated) | ❌ |
| `skills-index.json` | JSON index for recommendation (auto-generated) | ❌ |
| `.skill-preferences.json` | User preferences (auto-generated) | ❌ |

---

## 🧪 技术细节 · Technical Details

### 分类算法 · Classification Algorithm

采用**多维度关键词匹配 + 加权评分**，从三个维度评估：

Multi-dimensional keyword matching with weighted scoring from three dimensions:

```
score_name  = keyword matches in name × 3 × category_weight
score_desc  = keyword matches in description × 2 × category_weight
score_dir   = keyword matches in directory × 2 × category_weight

total_score = score_name + score_desc + score_dir
confidence  = normalize(total_score, 0-100)
```

**冲突消解 · Conflict Resolution**:
- Lark skills (dir starting with `lark-`) → strongly biased toward "飞书/Lark办公" category
- Skills with `skill` in name → biased toward "技能管理" category
- Highest score wins, with confidence calculation

### 推荐算法 · Recommendation Algorithm

1. **文件扫描 File Scan** — Detect `package.json`, `requirements.txt`, `Cargo.toml`, `go.mod`, etc.
2. **技术栈识别 Stack Detection** — Extract framework names from dependencies
3. **项目分类 Project Classification** — Frontend / Backend / Full-stack / AI / CLI / Library
4. **技能匹配 Skill Matching** — Match by category and tags from `skills-index.json`
5. **优先级排序 Priority Ordering** — Core > Frontend > Backend > Testing > AI/ML > General

### 16 个分类 · 16 Categories

| 分类 Category | Weight | Example Skills |
|---|---|---|
| 前端开发 Frontend | 10 | frontend-design, react-* |
| 后端开发 Backend | 9 | api-builder, server-* |
| 飞书/Lark办公 Lark Office | 10 | lark-doc, lark-sheets |
| AI/机器学习 AI/ML | 8 | rag-builder, llm-toolkit |
| DevOps/部署 DevOps | 8 | deployer, docker-helper |
| 数据库 Database | 7 | prisma-helper, db-manager |
| 测试 Testing | 7 | jest-helper, playwright-* |
| 代码质量/安全 Code Quality | 7 | code-review, security-audit |
| 设计/UI/UX Design | 6 | design-system, icon-maker |
| 文档写作 Documentation | 6 | doc-generator, readme-maker |
| 项目管理 Project Mgmt | 6 | jira-helper, notion-tool |
| 移动开发 Mobile | 6 | flutter-helper, react-native |
| 数据分析 Data Analytics | 6 | chart-builder, etl-tool |
| 性能优化 Performance | 5 | perf-analyzer, bundle-opt |
| 技能管理 Skill Mgmt | 5 | find-skills, skill-creator |
| 办公自动化 Office Automation | 5 | workflow-builder |

---

## 🔧 配置 · Configuration

### PostToolUse Hook（自动同步 · Auto-sync）

项目 `.claude/settings.json` 已预配 · Pre-configured in `.claude/settings.json`:

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

This configuration auto-syncs your skill database whenever you run `npx skills add`.

### 用户偏好持久化 · User Preference Persistence

Preferences are saved in `.skill-preferences.json` (auto-generated):

```json
{
  "always_include": ["frontend-design"],
  "always_exclude": ["lark-vc"],
  "last_combo": { ... },
  "history": [ ... ]
}
```

---

## 🔄 与现有生态的协作 · Ecosystem Integration

| 生态位 Ecosystem | 协作方式 Integration |
|---|---|
| **find-skills** | 推荐组合中缺失的技能→调用 find-skills 搜索安装 · Search & install missing skills |
| **skill-creator** | 用户需要自定义技能→转向 skill-creator · Route to skill creator |
| **code-review** | 作为通用开发技能被推荐 · Recommended as general dev skill |
| **其他 100+ skill** | 作为推荐组合的候选池 · Candidate pool for recommendations |

---

## ❓ 常见问题 · FAQ

**Q: 需要手动运行同步吗？Do I need to sync manually?**

**中文** | 不需要。首次安装会自动创建仓库，之后每次 `npx skills add` 会自动触发同步。你也可以随时手动运行 `python scripts/sync-skills-repo.py`。

**English** | No. The first install auto-creates the database, and every `npx skills add` auto-triggers a sync. You can also manually run `python scripts/sync-skills-repo.py` anytime.

---

**Q: 推荐会推荐所有技能吗？Does it recommend all skills?**

**中文** | 不会。推荐引擎只推荐与你当前项目匹配的技能。例如做 React 项目不会推荐 Lark 办公技能。

**English** | No. The engine only recommends skills relevant to your current project. For example, it won't recommend Lark office skills when you're building a React app.

---

**Q: 分类不准怎么办？Inaccurate classification?**

**中文** | 可以编辑 `scripts/skill-classifier.json` 中的关键词规则。欢迎提 PR 优化分类！

**English** | Edit the keyword rules in `scripts/skill-classifier.json`. PRs welcome!

---

**Q: 支持自定义分类吗？Can I add custom categories?**

**中文** | 支持。在 `skill-classifier.json` 中添加新的分类和关键词即可。

**English** | Yes. Add new categories and keywords to `skill-classifier.json`.

---

**Q: 必须用 Excel 吗？Is Excel required?**

**中文** | Excel 只是可视化展示。推荐引擎实际使用 `skills-index.json`（JSON 格式），你完全可以直接解析 JSON。

**English** | Excel is just for visual display. The recommendation engine uses `skills-index.json` (JSON format). You can parse the JSON directly if you prefer.

---

## 📦 路线图 · Roadmap

- [x] 基础同步引擎 · Basic sync engine
- [x] JSON 索引 · JSON index
- [x] 项目分析器 · Project analyzer
- [x] 技能推荐 · Skill recommendation
- [x] 用户偏好持久化 · User preference persistence
- [x] PostToolUse 自动触发 · PostToolUse auto-trigger
- [ ] 多语言 SKILL.md · Multi-language SKILL.md
- [ ] Web UI · Web management interface
- [ ] 推荐效果评估 · Recommendation A/B testing
- [ ] 社区分类规则共享 · Community classification sharing

---

## 🤝 贡献指南 · Contributing

欢迎贡献！请遵循以下原则 · Contributions welcome! Please follow these guidelines:

1. Fork 本仓库 · Fork this repository
2. 创建特性分支 · Create feature branch (`git checkout -b feature/amazing-feature`)
3. 提交修改 · Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. 推送到分支 · Push to branch (`git push origin feature/amazing-feature`)
5. 创建 Pull Request · Open a Pull Request

### 开发指引 · Development Guide

| 修改什么 What to change | 编辑哪个文件 Edit this file |
|---|---|
| 分类规则 Classification rules | `scripts/skill-classifier.json` |
| 推荐算法 Recommendation algorithm | `scripts/skill-recommend.py` |
| 同步逻辑 Sync logic | `scripts/sync-skills-repo.py` |
| 技能描述 Skill description | `skills/skill-manager/SKILL.md` |

---

## 📄 许可证 · License

MIT License — 详见 [LICENSE](LICENSE) 文件 · See [LICENSE](LICENSE) for details.

---

## 🙏 致谢 · Acknowledgments

- **Claude Code** — 提供技能系统平台 · The skill system platform
- **Skills 生态** — npx skills 包管理器 · The skills package manager
- **所有技能作者** — 让 AI 开发更高效 · Every skill author making AI development better

---

<p align="center">
  <strong>Skill Manager</strong><br>
  <em>让每一次对话都用对技能 · Use the right skills, every time</em><br>
  <sub>Made with ❤️ by xielaoban</sub>
</p>
