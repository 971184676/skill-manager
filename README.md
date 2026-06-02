# Skill Manager

AI 技能管理与推荐系统，用于管理和推荐 Claude Code 技能。

## 功能特性

- 自动扫描并分类已安装的技能
- 智能技能推荐（根据项目类型推荐合适的技能）
- 技能组合管理
- Excel 技能仓库可视化
- 同一任务后续步骤的技能选择

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 同步技能仓库

```bash
python scripts/sync-skills-repo.py
```

### 推荐技能

```bash
python scripts/skill-recommend.py --project .
```

## 项目结构

```
├── skills/              # 技能目录
│   ├── skill-manager/   # 技能管理
│   ├── find-skills/     # 技能发现
│   └── skill-creator/   # 技能创建
├── scripts/             # 工具脚本
│   ├── sync-skills-repo.py
│   └── skill-recommend.py
└── requirements.txt     # Python 依赖
```

## License

MIT
