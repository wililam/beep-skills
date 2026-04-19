# beep-skills Skill 🔔

<div align="center">

![Version](https://img.shields.io/badge/version-2.1.0--dev-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)
![Command](https://img.shields.io/badge/command-beep-ff6600.svg)

# 🔔 Beep · 小喇叭 | 让电脑会说话

**一键集成验证，让 AI 开口告诉你它在做什么。**

不再是冷冰冰的日志，而是一个贴心的小喇叭，实时播报每一步操作。

*"收到消息"* • *"正在处理"* • *"任务完成"* • *"遇到问题"*

---

[English](#english) | [中文](#中文)

</div>

---

<a name="english"></a>
## 🇺🇸 English

### Why Beep?

Your AI agent shouldn't be silent. With **Beep · 小喇叭**, OpenClaw becomes a talkative companion that keeps you informed in real-time:

- 🎯 **One-Click Verification**: `beep verify-integration` confirms everything works
- 🔔 **Clear Audio Cues**: Hear exactly what the AI is doing
- 💬 **Human-Friendly**: A friendly voice, not cold logs
- ⚡ **Non-Blocking**: Async by default, won't slow you down

### Features

- ✅ **One-Click Integration Verify**: Install → run `beep verify-integration` → hear test sounds
- ✅ **4 Platform Support**: Windows, macOS, Linux (pygame-based, reliable)
- ✅ **9 Languages**: Chinese, English, Japanese, Korean, Spanish, French, German, and more
- ✅ **Smart Retry**: Network issues? 3 retries with exponential backoff
- ✅ **Graceful Degradation**: pygame → system player → log-only fallback
- ✅ **Hot Reload**: Change config without restarting
- ✅ **LRU Cache**: Auto-cleanup old audio files (keep last 100)
- ✅ **Structured Logging**: Timestamp, level, message for easy debugging

### Installation

```bash
# Method 1: PyPI (Recommended)
pip install beep-announcement pygame

# Method 2: ClawHub
clawhub install beep

# Method 3: GitHub
git clone https://github.com/wililam/beep-announcement.git
cd beep-announcement && pip install -e .
```

### Quick Start

```bash
# 1️⃣ 一键验证集成（强烈推荐！）
beep verify-integration
# → 听到4种测试声音，看到完整报告

# 2️⃣ 配置
beep config async_default=true volume=0.25

# 3️⃣ 测试
beep test

# 4️⃣ 在你的 Agent 中使用
from beep import receive, task, complete, error

receive("用户查询天气")
task("正在获取数据")
complete("已发送天气预报")
error("网络超时")
```

### Commands

| Command | Description |
|---------|-------------|
| `beep test` | Test all 4 announcement types |
| `beep config` | View/set configuration |
| `beep verify-integration` | **One-click integration verify** (new!) |
| `beep stats` | Show statistics |
| `beep enable` / `disable` | Enable/disable announcements |
| `beep check` | Run environment check |

**Backward Compatible**: `audio-announce` command still works (same functionality).

### Configuration

Config file: `~/.config/audio-announcement/config.json`

```json
{
  "enabled": true,
  "default_lang": "zh",
  "volume": 0.25,
  "async_default": true,
  "log_level": "WARNING"
}
```

Change at runtime:
```python
from beep import set_config
set_config(volume=0.8, async_default=False)
```

---

<a name="中文"></a>
## 🇨🇳 中文

### 为什么选择 Beep · 小���叭？

- 🔔 **品牌上口**：Beep（4字母）+ 小喇叭（3个字），小学生都能读
- ✅ **一键验证**：安装后运行 `beep verify-integration`，听到声音就成功
- 🎯 **功能完整**：重试、降级、热重载、LRU缓存、结构化日志
- 🛡️ **防遗忘机制**：启动自检 + 强制规则，永远不会漏播

### 核心特性

| 特性 | 说明 |
|------|------|
| 🎉 一键集成验证 | `beep verify-integration` 播放4种测试音，输出完整报告 |
| 🔄 智能重试 | 网络失败自动重试3次（指数退避 1s→2s→4s） |
| ⬇️ 播放降级 | pygame → 系统播放器 → 仅日志（保证核心功能） |
| 🔄 热重载配置 | 修改配置无需重启，`beep config reload` 立即生效 |
| 🗑️ 自动清理 | LRU 缓存策略，自动删除旧文件（保留最新100个） |
| 📊 结构化日志 | 时间戳+级别+消息，支持 DEBUG/INFO/WARNING/ERROR |
| 📈 运行时统计 | 缓存大小、成功率、运行时间一目了然 |
| 🐛 异常追踪 | `exc_info=True`，完整堆栈便于调试 |

### 安装与验证

```bash
# 1. 安装
pip install beep-announcement pygame

# 2. 一键验证（最重要的一步！）
beep verify-integration

# 预期输出：
# ============================================================
# Beep · 小喇叭 集成验证 v2.1.0-dev
# ============================================================
# 📦 依赖检查
#   ✅ pygame 2.6.1
#   ✅ edge-tts 7.2.8
#   ✅ Python 3.13.12
#
# 🔊 功能测试
#   ▶️  测试 receive... ✅ 成功
#   ▶️  测试 task... ✅ 成功
#   ▶️  测试 complete... ✅ 成功
#   ▶️  测试 error... ✅ 成功
#
# 🎉 所有检查通过！语音播报系统已成功集成。
# ============================================================
```

听到测试声音 + 看到成功消息 = 集成成功！

### 命令速查

```bash
# 测试
beep test                           # 测试所有类型
beep verify-integration             # 一键验证（新增！）

# 配置
beep config                         # 查看当前配置
beep config volume=0.5              # 设置音量
beep config async_default=true      # 设置异步播放
beep config reload                  # 热重载配置

# 统计与检查
beep stats                          # 查看统计
beep check                          # 环境自检

# 启用/禁用
beep enable                         # 启用播报
beep disable                        # 禁用播报
```

### Python 集成

```python
from beep import receive, task, complete, error

# 最简单的方式（一行调用，异步非阻塞）
receive("用户提交报告")
task("正在分析数据")
complete("分析完成")
error("网络连接失败")

# 高级控制
from beep import AnnouncementHelper
helper = AnnouncementHelper()
helper.config.volume = 0.8
helper.config.async_default = False  # 同步播放
helper.receive("重要消息")
```

### 强制播报规则

**每次交互都必须播报！** 这是 OpenClaw 的核心要求。

| 时机 | 类型 | 内容示例（≤20字） |
|------|------|-------------------|
| 收到消息 | receive | "收到上传指令" |
| 开始工作 | task | "准备生成报告" |
| 执行中 | task | "正在下载文件" |
| 完成任务 | complete | "上传完成" |
| 发送回复 | complete | "已发送项目地址" |
| 遇到异常 | error | "网络超时" |

**内容原则**：简洁、口语化、不带用户名、信息丰富。

---

## 📁 项目结构

```
beep/                          # 技能目录（新名称）
├── SKILL.md                   # 详细使用文档
├── README.md                  # 本文件（品牌已更新）
├── _meta.json                 # 技能元数据（已更新）
├── package.json
├── version.txt                # 当前版本：2.1.0-dev
├── requirements.txt
├── setup.py                   # PyPI 打包配置
│
├── audio_announcement/        # Python 包（保持原名，向后兼容）
│   ├── __init__.py
│   ├── __main__.py            # CLI 入口（已更新支持 verify-integration）
│   ├── announce_helper.py     # 核心逻辑（已优化 v2.1.0）
│   ├── announce_pygame.py     # pygame 播放器（已修复配置读取）
│   └── scripts/
│       ├── announce.py        # 统一包装脚本
│       ├── announce_pygame.py  # Windows  pygame 方案
│       ├── startup_check_announcement.py  # 启动自检
│       └── verify_integration.py  # 新增：一键验证脚本
│
├── docs/                      # 文档
│   └── audio-announcement-learning.md
│
└── scripts/                   # 工作区脚本
    └── verify_announcement.py # 完整验证脚本
```

---

## 🔧 故障排除

### 没有声音？

1. 检查系统音量
2. 确认 pygame 安装：`python -c "import pygame; print(pygame.version.ver)"`
3. 测试 edge-tts：`edge-tts --text "测试" --voice zh-CN-XiaoxiaoNeural --write-media test.mp3`
4. 手动播放 test.mp3

### 播报延迟？

- 首次使用有缓存延迟（下载语音包）
- 使用 `async_default=true` 异步播放
- 检查网络连接

### /RESET 后失效？

- 确认 `startup_check_announcement.py` 已配置自动运行
- 手动运行：`python scripts/startup_check_announcement.py`
- 检查 AGENTS.md 和 IDENTITY.md

---

## 📈 版本历史

### v2.1.0-dev（开发中）
- 🎉 新增 `verify-integration` 一键验证命令
- 🔧 稳定性增强（重试、降级、热重载、LRU 缓存）
- 📝 结构化日志与运行时统计
- 🐛 修复多个 bug（配置读取、方法缺失等）
- 🎨 品牌升级：Beep · 小喇叭

### v2.0.8（生产稳定）
- ✅ 播报本地化（不发送语音文件到聊天）
- ✅ 统一包装脚本（announce.py）
- ✅ 默认音量 10%
- ✅ 防遗忘两重保障

### v2.0.6-v2.0.7
- ✅ PyPI 发布
- ✅ 配置文件系统
- ✅ 异步默认化
- ✅ CLI 工具

---

## 🤝 贡献

欢迎提交 Issue 和 PR！

发现漏播场景？需要更多集成示例？告诉我们！

---

## 📄 License

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 👤 Author

**miaoweilin** - [GitHub](https://github.com/wililam)

---

<div align="center">

# 🔔 **Beep · 小喇叭** - 让电脑会说话！

**安装 → 验证 → 使用，三步搞定！**

```bash
pip install beep-announcement pygame
beep verify-integration
from beep import receive, task, complete, error
```

**你的 AI，现在有声音了！** 🎉

⭐ 如果这个工具对你有帮助，请给我们一个 Star！ ⭐

</div>
