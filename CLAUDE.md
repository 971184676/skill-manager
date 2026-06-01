# 蟹老板工作区配置 · Xielaoban Workspace Config

---

## 语言声明 · Language

**中文** | 请始终使用中文（简体）回复。代码注释和文档优先使用中文，必要时附带英文说明。

**English** | Please always respond in Simplified Chinese. Code comments and documentation should prefer Chinese, with English translations when necessary.

---

## Skill 管理系统 · Skill Management System

**中文** | 本工作区使用 skill-manager 系统管理所有已安装的 AI 技能。这是核心工作流，请严格遵守。

**English** | This workspace uses the **skill-manager** system to manage all installed AI skills. This is the core workflow — please follow strictly.

### 推荐流程 · Recommendation Flow

**中文** | 在**任何编程/开发任务的计划阶段**，必须先运行技能推荐流程：

1. 运行 `python scripts/skill-recommend.py --project .` 分析项目
2. 展示推荐的技能组合给用户
3. 询问用户是否使用此组合
4. 允许用户替换/添加/移除组合中的任意技能
5. 用户确认后才开始编码

**English** | During the **planning phase of ANY programming/development task**, you MUST run the skill recommendation process:

1. Run `python scripts/skill-recommend.py --project .` to analyze the project
2. Present the recommended skill combo to the user
3. Ask if the user wants to use this combo
4. Allow the user to swap/add/remove any skill in the combo
5. Only start coding after the user confirms

### 同步流程 · Sync Flow

**中文** | 安装新技能后，系统会自动同步（通过 `.claude/settings.json` 中的 PostToolUse hook）。也可手动运行：

**English** | After installing new skills, the system auto-syncs (via PostToolUse hook in `.claude/settings.json`). You can also run manually:

```bash
python scripts/sync-skills-repo.py
```

### 数据库文件 · Database Files

| 文件 File | 用途 Purpose |
|---|---|
| `Skill仓库.xlsx` | 可视化 Excel 技能总表 · Visual Excel skill database |
| `skills-index.json` | JSON 技能索引（推荐引擎使用）· JSON index (used by recommender) |
| `scripts/skill-recommend.py` | 推荐引擎 · Recommendation engine |
| `scripts/sync-skills-repo.py` | 同步脚本 · Sync script |
| `scripts/skill-classifier.json` | 分类规则 · Classification rules |
| `.skill-preferences.json` | 用户偏好（自动生成）· User preferences (auto-generated) |
