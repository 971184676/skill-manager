"""
Skill 推荐引擎 v1.0
====================
在编程任务的计划阶段调用，分析项目上下文并推荐技能组合。

用法:
  python scripts/skill-recommend.py --project <项目路径> [--list-all]
  python scripts/skill-recommend.py --project . --output json
  python scripts/skill-recommend.py --add skill_name
  python scripts/skill-recommend.py --remove skill_name
"""
import os
import sys
import json
import re
import argparse
from pathlib import Path

# ── 路径配置 ────────────────────────────────────────────────
CWD = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CWD)
INDEX_PATH = os.path.join(PROJECT_ROOT, 'skills-index.json')
# 用户技能偏好配置
USER_PREFS_PATH = os.path.join(PROJECT_ROOT, '.skill-preferences.json')


def load_index():
    """加载技能索引"""
    if not os.path.exists(INDEX_PATH):
        print(f'[!] 未找到技能索引文件，请先运行 sync-skills-repo.py')
        return None
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_preferences():
    """加载用户偏好"""
    if os.path.exists(USER_PREFS_PATH):
        with open(USER_PREFS_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        'always_include': [],  # 用户指定的始终包含的技能
        'always_exclude': [],  # 用户指定的始终排除的技能
        'last_combo': {},       # 上一次使用的组合
        'history': [],          # 历史记录
    }


def save_preferences(prefs):
    """保存用户偏好"""
    with open(USER_PREFS_PATH, 'w', encoding='utf-8') as f:
        json.dump(prefs, f, ensure_ascii=False, indent=2)


def analyze_project(project_path):
    """分析项目目录，识别项目类型、技术栈等信息"""
    project_info = {
        'project_name': os.path.basename(os.path.abspath(project_path)),
        'project_type': 'unknown',
        'languages': [],
        'frameworks': [],
        'tools': [],
        'has_frontend': False,
        'has_backend': False,
        'has_database': False,
        'has_tests': False,
        'is_ai_project': False,
        'is_web_project': False,
        'is_cli_project': False,
        'is_library': False,
        'confidence': 0,
    }

    if not os.path.isdir(project_path):
        return project_info

    # 扫描项目中的关键文件
    files = list(Path(project_path).rglob('*'))
    filenames = [f.name for f in files]
    ext_to_lang = {
        '.py': 'Python', '.js': 'JavaScript', '.ts': 'TypeScript',
        '.tsx': 'TypeScript', '.jsx': 'JavaScript', '.java': 'Java',
        '.go': 'Go', '.rs': 'Rust', '.rb': 'Ruby', '.php': 'PHP',
        '.swift': 'Swift', '.kt': 'Kotlin', '.vue': 'Vue',
        '.svelte': 'Svelte', '.c': 'C', '.cpp': 'C++',
    }

    for f in files:
        ext = f.suffix.lower()
        if ext in ext_to_lang:
            lang = ext_to_lang[ext]
            if lang not in project_info['languages']:
                project_info['languages'].append(lang)

    # 通过关键文件判断项目类型
    if 'package.json' in filenames:
        project_info['is_web_project'] = True
        project_info['frameworks'].append('Node.js/npm')
        # 尝试读取 package.json 获取更多信息
        try:
            pkg_path = os.path.join(project_path, 'package.json')
            with open(pkg_path, 'r', encoding='utf-8') as f:
                pkg = json.load(f)
            deps = {**pkg.get('dependencies', {}), **pkg.get('devDependencies', {})}
            framework_map = {
                'react': 'React', 'vue': 'Vue', 'angular': 'Angular',
                'next': 'Next.js', 'nuxt': 'Nuxt', 'express': 'Express',
                'fastify': 'Fastify', 'nest': 'NestJS', 'svelte': 'Svelte',
                'tailwindcss': 'Tailwind CSS', 'vite': 'Vite',
                'jest': 'Jest', 'vitest': 'Vitest',
                'playwright': 'Playwright', 'cypress': 'Cypress',
                'prisma': 'Prisma', 'typeorm': 'TypeORM',
            }
            for dep in deps:
                for key, fw in framework_map.items():
                    if key in dep.lower():
                        if fw not in project_info['frameworks']:
                            project_info['frameworks'].append(fw)
        except Exception:
            pass

    if 'requirements.txt' in filenames or 'Pipfile' in filenames:
        project_info['is_web_project'] = True
        project_info['frameworks'].append('Python')
        try:
            req_path = os.path.join(project_path, 'requirements.txt')
            if os.path.exists(req_path):
                with open(req_path, 'r', encoding='utf-8') as f:
                    reqs = f.read().lower()
                fw_map = {
                    'django': 'Django', 'flask': 'Flask', 'fastapi': 'FastAPI',
                    'pytorch': 'PyTorch', 'tensorflow': 'TensorFlow',
                    'pandas': 'Pandas', 'numpy': 'NumPy',
                    'pytest': 'pytest', 'celery': 'Celery',
                }
                for key, fw in fw_map.items():
                    if key in reqs and fw not in project_info['frameworks']:
                        project_info['frameworks'].append(fw)
        except Exception:
            pass

    if 'Cargo.toml' in filenames:
        project_info['frameworks'].append('Rust')
    if 'go.mod' in filenames or 'go.sum' in filenames:
        project_info['frameworks'].append('Go')

    # 判断项目具体类型
    if project_info['is_web_project']:
        has_frontend_fw = any(f in project_info['frameworks']
                             for f in ['React', 'Vue', 'Angular', 'Svelte', 'Next.js', 'Nuxt'])
        has_backend_fw = any(f in project_info['frameworks']
                            for f in ['Django', 'Flask', 'FastAPI', 'Express', 'NestJS', 'Fastify'])
        if has_frontend_fw:
            project_info['has_frontend'] = True
            project_info['project_type'] = '前端项目'
            project_info['confidence'] = 70
        if has_backend_fw:
            project_info['has_backend'] = True
            project_info['project_type'] = '后端项目' if not has_frontend_fw else '全栈项目'
            project_info['confidence'] = 80
        if has_frontend_fw and has_backend_fw:
            project_info['project_type'] = '全栈项目'
            project_info['confidence'] = 90

    # AI项目检测
    ai_keywords = ['pytorch', 'tensorflow', 'llm', 'langchain', 'openai', 'transformers',
                   'huggingface', 'onnx', 'mlx', 'ggml', 'llama']
    for fw in project_info['frameworks']:
        if any(k in fw.lower() for k in ai_keywords):
            project_info['is_ai_project'] = True
            project_info['project_type'] = 'AI/ML项目'
            project_info['confidence'] = 85
            break

    # CLI工具检测
    if any(f in filenames for f in ['cli.py', 'main.py', 'index.js', 'bin/']) or \
       any(f.endswith('.command') for f in filenames):
        project_info['is_cli_project'] = True
        if project_info['project_type'] == 'unknown':
            project_info['project_type'] = 'CLI工具'
            project_info['confidence'] = 60

    # 测试检测
    test_patterns = ['test_', '_test', '__tests__', 'spec.', 'test.', 'jest.config', 'vitest.config', 'pytest.ini']
    for f in filenames:
        if any(p in f for p in test_patterns):
            project_info['has_tests'] = True
            break

    # 数据库检测
    db_files = ['schema.prisma', 'migrations/', 'alembic.ini', 'db.sqlite3', 'database.yml']
    for f in filenames:
        if any(db in f for db in db_files):
            project_info['has_database'] = True
            break
    db_deps = ['prisma', 'typeorm', 'sqlalchemy', 'mongoose', 'redis', 'postgres']
    if any(d in str(project_info['frameworks']).lower() for d in db_deps):
        project_info['has_database'] = True

    return project_info


def recommend_skills(project_info, index, prefs):
    """
    根据项目信息推荐技能组合
    返回: { category: [skills], ... }
    """
    now_include = set(prefs.get('always_include', []))
    now_exclude = set(prefs.get('always_exclude', []))
    skills = index['skills']

    # ── Skill-Project 匹配规则 ──
    recommendations = {
        'core': {
            'reason': '无论项目类型，建议启用以下核心技能',
            'skills': []
        },
        'frontend': {
            'reason': '',
            'skills': []
        },
        'backend': {
            'reason': '',
            'skills': []
        },
        'testing': {
            'reason': '',
            'skills': []
        },
        'ai_ml': {
            'reason': '',
            'skills': []
        },
        'devops': {
            'reason': '',
            'skills': []
        },
        'utility': {
            'reason': '',
            'skills': []
        },
    }

    for skill in skills:
        name = skill['name']
        cat = skill['category']
        desc = skill['description'].lower()
        tags = [t.lower() for t in skill['tags']]

        # 排除用户明确不想要的
        if name in now_exclude:
            continue

        # 核心技能：一些通用管理技能始终推荐
        if name in ('find-skills', 'skill-creator', 'skill-manager'):
            recommendations['core']['skills'].append({
                'name': name,
                'desc': skill['description'][:80],
                'required': name == 'skill-manager',
            })
            continue

        # 前端项目
        if project_info['has_frontend'] or project_info['is_web_project']:
            if cat == '前端开发' or any(t in ('react', 'vue', 'web', '设计') for t in tags):
                if not recommendations['frontend']['reason']:
                    recommendations['frontend']['reason'] = f'检测到 {project_info["project_type"]}，推荐前端开发技能'
                recommendations['frontend']['skills'].append({
                    'name': name,
                    'desc': skill['description'][:80],
                    'category': cat,
                })
                continue

        # AI项目
        if project_info['is_ai_project']:
            if cat == 'AI/机器学习':
                if not recommendations['ai_ml']['reason']:
                    recommendations['ai_ml']['reason'] = '检测到 AI/ML 项目，推荐 AI 开发技能'
                recommendations['ai_ml']['skills'].append({
                    'name': name,
                    'desc': skill['description'][:80],
                    'category': cat,
                })
                continue

        # 后端项目
        if project_info['has_backend'] or project_info['has_database']:
            if cat in ('后端开发', '数据库'):
                if not recommendations['backend']['reason']:
                    recommendations['backend']['reason'] = f'检测到后端/数据库依赖，推荐后端开发技能'
                recommendations['backend']['skills'].append({
                    'name': name,
                    'desc': skill['description'][:80],
                    'category': cat,
                })
                continue

        # 有测试的项目
        if project_info['has_tests']:
            if cat == '测试':
                if not recommendations['testing']['reason']:
                    recommendations['testing']['reason'] = '检测到测试文件，推荐测试相关技能'
                recommendations['testing']['skills'].append({
                    'name': name,
                    'desc': skill['description'][:80],
                    'category': cat,
                })
                continue

        # 通用开发技能兜底
        if cat in ('文档写作', '代码质量/安全', '设计/UI/UX', '性能优化', 'DevOps/部署'):
            if not recommendations['utility']['reason']:
                recommendations['utility']['reason'] = '推荐的通用开发技能'
            recommendations['utility']['skills'].append({
                'name': name,
                'desc': skill['description'][:80],
                'category': cat,
            })

    # 清理空分组
    recommendations = {k: v for k, v in recommendations.items() if v['skills']}

    return recommendations


def format_recommendation(recommendations, project_info):
    """格式化为用户友好的文字描述"""
    lines = []
    lines.append('=' * 65)
    lines.append('  >> Skill 组合推荐 <<')
    lines.append(f'  项目: {project_info["project_name"]}')
    lines.append(f'  类型: {project_info["project_type"]}')
    if project_info['frameworks']:
        lines.append(f'  技术栈: {", ".join(project_info["frameworks"])}')
    lines.append('=' * 65)

    group_labels = {
        'core': '[核心技能]',
        'frontend': '[前端开发]',
        'backend': '[后端开发]',
        'testing': '[测试]',
        'ai_ml': '[AI/ML]',
        'devops': '[DevOps]',
        'utility': '[通用工具]',
    }

    skill_index = 1
    for group_key, group in recommendations.items():
        label = group_labels.get(group_key, group_key)
        lines.append(f'\n  {label}')
        if group.get('reason'):
            lines.append(f'    -> {group["reason"]}')
        for s in group['skills']:
            required_tag = ' [必选]' if s.get('required') else ''
            lines.append(f'    {skill_index}. {s["name"]}{required_tag}')
            lines.append(f'       {s["desc"][:70]}')
            skill_index += 1

    lines.append('\n' + '-' * 65)
    lines.append('是否使用以上技能组合？可以执行以下操作：')
    lines.append('  1. 直接开始 - 使用该组合')
    lines.append('  2. 替换技能 - 从组合中移除或添加技能')
    lines.append('  3. 自定义 - 重新选择')
    lines.append('-' * 65)

    return '\n'.join(lines)


def format_json(recommendations, project_info):
    """JSON 格式输出"""
    return json.dumps({
        'project': project_info,
        'recommendations': recommendations,
        'total_skills': sum(len(g['skills']) for g in recommendations.values()),
    }, ensure_ascii=False, indent=2)


def interactive_adjust(recommendations, prefs):
    """交互式调整技能组合"""
    print('\n[?] 是否调整技能组合？ (y/n, 默认 n): ', end='')
    sys.stdout.flush()

    response = sys.stdin.readline().strip().lower()
    if response not in ('y', 'yes'):
        return recommendations

    print('\n可用操作:')
    print('  add <skill_name>   - 加入技能')
    print('  remove <skill_name> - 移除技能')
    print('  list               - 列出所有可用技能')
    print('  save               - 保存偏好并退出')
    print('  done               - 完成调整')
    print('  quit               - 放弃调整')

    available_skills = {s['name']: s for s in load_index()['skills']}

    while True:
        print('\n> ', end='')
        sys.stdout.flush()
        cmd = sys.stdin.readline().strip()
        if not cmd:
            continue

        parts = cmd.split(maxsplit=1)
        action = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ''

        if action == 'done':
            break
        elif action == 'quit':
            return None
        elif action == 'list':
            print('\n所有可用技能:')
            for name, info in sorted(available_skills.items()):
                print(f'  {name:30s} [{info["category"]}]')
        elif action == 'add' and arg:
            if arg in available_skills:
                # 添加到 always_include
                if arg not in prefs['always_include']:
                    prefs['always_include'].append(arg)
                    print(f'  [OK] 已添加: {arg}')
                else:
                    print(f'  [!] {arg} 已在偏好列表中')
            else:
                print(f'  [X] 未找到技能: {arg}')
        elif action == 'remove' and arg:
            if arg in available_skills:
                if arg not in prefs['always_exclude']:
                    prefs['always_exclude'].append(arg)
                    print(f'  [OK] 已移除: {arg}')
                else:
                    print(f'  [!] {arg} 已在排除列表中')
            else:
                print(f'  [X] 未找到技能: {arg}')
        elif action == 'save':
            save_preferences(prefs)
            print('  [OK] 偏好已保存')
        else:
            print('  [!] 未知命令')

    return recommendations


def main():
    parser = argparse.ArgumentParser(description='Skill 推荐引擎')
    parser.add_argument('--project', '-p', default='.', help='项目路径')
    parser.add_argument('--output', choices=['text', 'json'], default='text', help='输出格式')
    parser.add_argument('--list-all', action='store_true', help='列出所有可用技能')
    parser.add_argument('--interactive', '-i', action='store_true', help='交互模式（允许调整组合）')
    parser.add_argument('--add', help='将技能添加到始终包含列表')
    parser.add_argument('--remove', help='将技能添加到始终排除列表')

    args = parser.parse_args()

    # 加载数据
    index = load_index()
    if index is None:
        sys.exit(1)

    # 加载用户偏好
    prefs = load_preferences()

    # 处理 --add / --remove
    if args.add:
        skill_name = args.add
        found = any(s['name'] == skill_name for s in index['skills'])
        if found:
            if skill_name not in prefs['always_include']:
                prefs['always_include'].append(skill_name)
                save_preferences(prefs)
                print(f'[OK] 已添加 "{skill_name}" 到始终包含列表')
            else:
                print(f'[!] "{skill_name}" 已在始终包含列表中')
        else:
            print(f'[X] 未找到技能 "{skill_name}"')
        return

    if args.remove:
        skill_name = args.remove
        if skill_name not in prefs['always_exclude']:
            prefs['always_exclude'].append(skill_name)
            save_preferences(prefs)
            print(f'[OK] 已添加 "{skill_name}" 到始终排除列表')
        else:
            print(f'[!] "{skill_name}" 已在始终排除列表中')
        return

    # 列出所有技能
    if args.list_all:
        print(f'\nSkill 仓库 - 共 {index["total"]} 个技能\n')
        for skill in index['skills']:
            tags = ', '.join(skill['tags']) if skill['tags'] else '-'
            print(f'  {skill["name"]:30s} | {skill["category"]:12s} | 标签: {tags}')
        return

    # 分析项目并推荐
    project_path = os.path.abspath(args.project)
    if not os.path.exists(project_path):
        print(f'[X] 项目路径不存在: {project_path}')
        sys.exit(1)

    project_info = analyze_project(project_path)
    recommendations = recommend_skills(project_info, index, prefs)

    if args.output == 'json':
        print(format_json(recommendations, project_info))
    else:
        print(format_recommendation(recommendations, project_info))

        if args.interactive:
            result = interactive_adjust(recommendations, prefs)
            if result is None:
                print('\n[!] 已放弃调整')
                sys.exit(1)
            print('\n[OK] 组合已确认!')


if __name__ == '__main__':
    main()
