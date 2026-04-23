# 项目结构

## 📁 目录结构

```
beep-skills/
├── 📄 项目文件
│   ├── README.md              # 项目说明文档
│   ├── LICENSE                 # MIT 许可证
│   ├── CHANGELOG.md           # 更新日志
│   ├── CONTRIBUTING.md        # 贡献指南
│   ├── PROJECT_STRUCTURE.md   # 项目结构说明（本文件）
│   ├── SKILL.md               # OpenClaw 技能文档
│   ├── HOOK.md                # 钩子配置文档
│   ├── setup.py               # 传统安装脚本
│   ├── pyproject.toml         # 现代项目配置
│   ├── requirements.txt       # 依赖列表
│   └── MANIFEST.in            # 打包清单
│
├── 📦 核心代码
│   ├── audio_announcement/    # 主包目录
│   │   ├── __init__.py       # 包初始化
│   │   ├── announce_helper.py # 核心帮助类
│   │   ├── cli.py            # 命令行接口
│   │   └── scripts/          # 脚本目录
│   │       ├── announce_pygame.py    # pygame 播放器
│   │       ├── announce.sh           # Linux/macOS 脚本
│   │       ├── announce-offline.sh   # 离线播放脚本
│   │       └── workflow-helper.sh    # 工作流助手
│   │
│   └── scripts/              # 顶层脚本
│       ├── announce.py       # 主播报脚本
│       └── startup_check_announcement.py  # 启动检查
│
├── 🧪 测试
│   └── tests/                # 测试目录
│       ├── __init__.py       # 测试包初始化
│       ├── conftest.py       # pytest 配置
│       ├── test_announce_helper.py  # 帮助类测试
│       ├── test_cli.py       # CLI 测试
│       └── test_integration.py      # 集成测试
│
├── 📚 文档
│   └── docs/                 # 文档目录
│       └── announcement-anti-forgetting.md  # 防遗忘机制文档
│
├── 🔧 GitHub 配置
│   └── .github/              # GitHub 配置
│       ├── workflows/
│       │   └── ci.yml        # CI/CD 工作流
│       ├── ISSUE_TEMPLATE/
│       │   ├── bug_report.md # Bug 报告模板
│       │   └── feature_request.md  # 功能请求模板
│       └── PULL_REQUEST_TEMPLATE.md  # PR 模板
│
├── 📊 元数据
│   ├── _meta.json            # 技能元数据
│   └── .clawhub/             # ClawHub 配置
│       └── origin.json       # 来源信息
│
└── ⚙️ 配置文件
    └── .gitignore            # Git 忽略文件
```

## 📋 文件说明

### 项目文件

| 文件 | 说明 |
|------|------|
| `README.md` | 项目主文档，包含安装、使用、特性说明 |
| `LICENSE` | MIT 许可证 |
| `CHANGELOG.md` | 版本更新日志 |
| `CONTRIBUTING.md` | 贡献指南 |
| `SKILL.md` | OpenClaw 技能文档 |
| `HOOK.md` | 钩子配置文档 |
| `setup.py` | 传统 Python 安装脚本 |
| `pyproject.toml` | 现代 Python 项目配置（PEP 518） |
| `requirements.txt` | Python 依赖列表 |
| `MANIFEST.in` | 打包时包含的文件清单 |

### 核心代码

| 目录/文件 | 说明 |
|-----------|------|
| `audio_announcement/` | 主 Python 包 |
| `audio_announcement/__init__.py` | 包初始化，导出主要类 |
| `audio_announcement/announce_helper.py` | 核心帮助类，处理播报逻辑 |
| `audio_announcement/cli.py` | 命令行接口实现 |
| `audio_announcement/scripts/` | 播放器脚本 |
| `scripts/announce.py` | 主播报脚本，供外部调用 |

### 测试

| 文件 | 说明 |
|------|------|
| `tests/conftest.py` | pytest 配置和 fixtures |
| `tests/test_announce_helper.py` | AnnouncementHelper 类测试 |
| `tests/test_cli.py` | CLI 功能测试 |
| `tests/test_integration.py` | 集成测试 |

### GitHub 配置

| 文件 | 说明 |
|------|------|
| `.github/workflows/ci.yml` | CI/CD 工作流（测试、构建、发布） |
| `.github/ISSUE_TEMPLATE/bug_report.md` | Bug 报告模板 |
| `.github/ISSUE_TEMPLATE/feature_request.md` | 功能请求模板 |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR 模板 |

## 🚀 快速开始

### 安装依赖

```bash
# 开发模式安装
pip install -e ".[dev]"
```

### 运行测试

```bash
# 运行所有测试
pytest tests/

# 运行特定测试
pytest tests/test_announce_helper.py

# 带覆盖率报告
pytest tests/ --cov=audio_announcement --cov-report=html
```

### 代码格式化

```bash
# 使用 black 格式化
black audio_announcement/ tests/

# 使用 flake8 检查
flake8 audio_announcement/ tests/
```

## 📦 打包发布

### 构建分发包

```bash
# 清理旧构建
rm -rf build/ dist/ *.egg-info

# 构建
python -m build

# 检查构建结果
ls -lh dist/
```

### 发布到 PyPI

```bash
# 安装 twine
pip install twine

# 上传到 PyPI
twine upload dist/*
```

### 发布到 ClawHub

```bash
# 使用 ClawHub CLI
clawhub publish
```

## 🔧 开发工作流

### 1. 创建功能分支

```bash
git checkout -b feature/new-feature
```

### 2. 编写代码和测试

- 在 `audio_announcement/` 中添加代码
- 在 `tests/` 中添加测试

### 3. 运行测试

```bash
pytest tests/ -v
```

### 4. 提交代码

```bash
git add .
git commit -m "feat: 添加新功能"
git push origin feature/new-feature
```

### 5. 创建 Pull Request

在 GitHub 上创建 PR 并等待审查

## 📝 代码规范

### Python 代码风格

- 使用 4 个空格缩进
- 行长度限制 88 字符
- 使用 type hints
- 添加 docstrings

### 提交信息格式

```
<type>: <description>

类型：
- feat: 新功能
- fix: 修复 bug
- docs: 文档更新
- style: 代码格式调整
- refactor: 重构
- test: 测试相关
- chore: 构建/工具相关
```

## 🎯 版本管理

### 版本号位置

版本号需要在以下文件中保持一致：

1. `setup.py` - `version="2.2.0"`
2. `_meta.json` - `"version": "2.2.0"`
3. `SKILL.md` - `**版本**: 2.2.0`
4. `README.md` - 版本徽章
5. `pyproject.toml` - `version = "2.2.0"`

### 更新版本号

```bash
# 使用脚本更新版本号
./scripts/update_version.py 2.2.0
```

## 📞 获取帮助

- 📖 [README.md](README.md) - 项目说明
- 🤝 [CONTRIBUTING.md](CONTRIBUTING.md) - 贡献指南
- 📝 [CHANGELOG.md](CHANGELOG.md) - 更新日志
- 🐛 [GitHub Issues](https://github.com/wililam/beep-skills/issues) - 问题反馈

---

*最后更新: 2026-04-23*
