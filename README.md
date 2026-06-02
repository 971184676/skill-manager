# Skill Manager — 技能管理器

**中文** | AI 技能管理与推荐系统，用于管理和推荐 Claude Code 技能。

**English** | AI skill management and recommendation system for Claude Code.

---

## 功能特性 · Features

**中文**:
- 自动扫描并分类已安装的技能
- 智能技能推荐（根据项目类型推荐合适的技能）
- 技能组合管理
- Excel 技能仓库可视化
- 同一任务后续步骤的技能选择

**English**:
- Auto-scan and classify installed skills
- Smart skill recommendations (based on project type)
- Skill combination management
- Excel skill repository visualization
- Skill selection for follow-up steps in the same task

---

## 安装依赖 · Installation

```bash
pip install -r requirements.txt
```

---

## 使用方法 · Usage

### 同步技能仓库 · Sync Skill Repository

**中文**: 同步本地技能到 Excel 仓库
**English**: Sync local skills to Excel repository

```bash
python scripts/sync-skills-repo.py
```

### 推荐技能 · Recommend Skills

**中文**: 分析项目并推荐技能组合
**English**: Analyze project and recommend skill combination

```bash
python scripts/skill-recommend.py --project .
```

---

## 项目结构 · Project Structure

```
skill-manager/
├── skills/              # 技能目录 · Skills Directory
│   ├── skill-manager/   # 技能管理 · Skill Management
│   ├── find-skills/     # 技能发现 · Skill Discovery
│   └── skill-creator/   # 技能创建 · Skill Creation
├── scripts/             # 工具脚本 · Scripts
│   ├── sync-skills-repo.py
│   └── skill-recommend.py
└── requirements.txt     # Python 依赖 · Dependencies
```

---

## License

MIT
