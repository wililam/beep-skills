# Audio Announcement Skill 🦊

让 OpenClaw 开口说话，实时播报 AI 的一举一动！

## 概述

这是一个语音播报技能，可以让你的 AI 代理通过语音实时告诉你它在做什么。就像一只爱说话的龙虾，让你更清楚、更安心地知道 AI 的当前状态。

**版本**: 2.0.6  
**状态**: ✅ 生产就绪  
**安装**: `clawhub install audio-announcement`

### 🎯 最新更新 (v2.0.6 - 2026-04-05)
- ✅ **增强防遗忘机制** - 添加验证脚本、heartbeat 自动检查、集成检查清单
- ✅ **快速集成指南** - 提供 announce_helper.py 简化集成
- ✅ **强制规则模板** - 可直接复制到 AGENTS.md 的完整规则
- ✅ **Windows 高可靠性** - 使用 python -m edge_tts 模块调用，不依赖 PATH

### 🎯 最新更新 (v2.0.5 - 2026-04-05)
- ✅ **修复 PATH 依赖问题** - announce_pygame.py 改用 `python -m edge_tts` 模块调用，不依赖 PATH 环境变量
- ✅ **Windows 高可靠性** - 即使 edge-tts 不在 PATH 也能正常工作
- ✅ **配置状态记录** - AGENTS.md 添加语音播报配置状态追踪

### 🎯 最新更新 (v2.0.4 - 2026-03-28)
- ✅ **强化播报规则** - 5 种播报时机，内容原则，检查清单
- ✅ **集成到核心配置** - AGENTS.md / SOUL.md / USER.md / MEMORY.md
- ✅ **强制执行机制** - 每次交互都必须播报，不能遗漏
- ✅ **内容规范** - ≤20 字，口语化，不带名称

### 🎯 历史更新 (v1.5.0-v1.7.4)
- ✅ **Windows 默认使用 pygame** - `announce.sh` 在 Windows 平台自动调用 `announce_pygame.py`
- ✅ **简化 Windows 使用** - 无需手动选择脚本，统一使用 `announce.sh`
- ✅ **清理无用测试脚本** - 移除 `test-integration.sh` 和备份文件

### 📜 历史更新
- **v1.4.0**: Windows 11 完整支持，新增 `announce_pygame.py`，修复新会话语音、macOS 兼容性、跨平台哈希计算
- **v1.3.0**: 新增 workflow-helper.sh，支持自动包装命令
- **v1.2.0**: 新增离线模式支持
- **v1.1.0**: 支持多语言（9种语言）
- **v1.0.0**: 初始版本，支持 macOS/Linux

### 特性

- 🎯 **透明度**：清楚知道 AI 正在执行什么操作
- 🔒 **安全感**：实时听到操作，不用盯着日志看
- 💬 **人性化**：友好的声音，不是冷冰冰的文字
- ⚡ **效率**：专注你的工作，让 AI 用声音告诉你进度
- 🌍 **9种语言**：中文、英文、日文、韩文、西班牙语、法语、德语等
- 🔄 **队列机制**：消息永不丢失，自动重试

### 🦊 语音播报（强制执行）

**每次交互都必须语音播报！**

#### 播报时机与内容
| 时机 | 类型 | 内容要求 | 示例 |
|------|------|----------|------|
| 收到消息 | `receive` | 收到的指令信息 | "收到上传指令" |
| 开始工作 | `task` | 工作规划 | "准备上传到GitHub" |
| 执行中 | `task` | 下一步要处理的内容 | "正在生成文档" |
| 任务完成 | `complete` | 工作总结 | "上传完成" |
| **发送回复** | `complete` | 回复内容的简短总结 | "已发送项目地址" |

#### 内容原则
- **信息丰富**：包含指令/规划/进度/总结
- **简洁**：不超过 20 个字
- **不带名称**：不说用户名、不说"我"
- **口语化**：像朋友随口说一句

#### 安装后配置

安装此技能后，需要将以下内容添加到 OpenClaw 工作区的 `AGENTS.md` 文件中，以确保 AI 代理强制执行语音播报：

```markdown
## 🦊 语音播报（强制执行）

**每次交互都必须语音播报！**

### 播报时机与内容
| 时机 | 类型 | 内容要求 | 示例 |
|------|------|----------|------|
| 收到消息 | `receive` | 收到的指令信息 | "收到上传指令" |
| 开始工作 | `task` | 工作规划 | "准备上传到GitHub" |
| 执行中 | `task` | 下一步要处理的内容 | "正在生成文档" |
| 任务完成 | `complete` | 工作总结 | "上传完成" |
| **发送回复** | `complete` | 回复内容的简短总结 | "已发送项目地址" |

### 内容原则
- **信息丰富**：包含指令/规划/进度/总结
- **简洁**：不超过 20 个字
- **不带名称**：不说用户名、不说"我"
- **口语化**：像朋友随口说一句

### 强制播报场景
- 每次收到用户消息 → 先播报指令内容
- 开始执行任务 → 播报工作规划
- 执行过程中 → 播报下一步要做什么
- 任务完成/失败 → 播报工作总结
- **发送文字回复前 → 播报回复内容的简短总结（1句话）**
- **API/网络异常时 → 播报告警信息**
  - Token 用完 → "额度不足"
  - 网络超时 → "连接超时"
  - 接口异常 → "服务异常"
  - 模型不可用 → "模型繁忙"
```

---

## 🛠️ 使用方法

### macOS / Linux

使用 `announce.sh` 脚本：

```bash
# 收到消息 - 说出指令
./announce.sh receive "收到上传指令" zh

# 开始工作 - 说出规划
./announce.sh task "准备上传文件" zh

# 执行中 - 说出进度
./announce.sh task "正在生成文档" zh

# 任务完成 - 工作总结
./announce.sh complete "任务完成" zh

# 发送回复 - 回复内容总结
./announce.sh complete "已发送项目地址" zh

# 英文播报（任务完成）
./announce.sh complete "Task finished" en

# 日文播报（处理中）
./announce.sh task "処理中です" ja
```

### Windows

使用 `announce_pygame.py` 脚本（推荐）：

```powershell
# 中文播报
python scripts/announce_pygame.py complete "任务完成" zh

# 英文播报
python scripts/announce_pygame.py task "Processing..." en

# 日文播报
python scripts/announce_pygame.py error "エラーが発生しました" ja
```

**Windows 批处理脚本（备用）：**

```cmd
# 使用批处理脚本（需安装 VLC）
scripts\announce.bat complete "任务完成" zh
```

### 脚本参数

所有脚本支持以下参数：

```bash
./announce.sh <type> "<message>" <language>

# type: 消息类型
#   - receive: 收到消息/指令
#   - task: 任务开始/处理中
#   - complete: 任务完成
#   - error: 错误/警告
#   - custom: 自定义消息

# message: 要播报的文字内容

# language: 语言代码
#   - zh: 中文
#   - en: 英文
#   - ja: 日文
#   - ko: 韩文
#   - es: 西班牙语
#   - fr: 法语
#   - de: 德语
```

---

## 🚀 快速集成指南（避免遗漏）

为了让播报功能真正"强制执行"，建议将语音播报直接集成到你的 OpenClaw Agent 响应循环中。

### Python Agent 集成（推荐）

```python
# 在 agent 文件开头添加
import sys
import subprocess
from pathlib import Path

ANNOUNCE_SCRIPT = str(Path.home() / ".openclaw-autoclaw" / "skills" / "audio-announcement" / "scripts" / "announce_pygame.py")

def announce(type_, message, lang="zh"):
    """语音播报 - 同步模式（确保播报完成）"""
    try:
        result = subprocess.run(
            [sys.executable, ANNOUNCE_SCRIPT, type_, message, lang],
            capture_output=True,
            timeout=30
        )
        return result.returncode == 0
    except:
        return False  # 播报失败不影响主流程

# 在你的响应循环中调用
def handle_message(self, message):
    announce("receive", message.content[:20])  # 收到消息播报
    
    # ... 处理消息逻辑 ...
    
    response = self.generate_response(message)
    announce("complete", response[:20])  # 发送回复前播报
    return response
```

### 使用助手模块（更简单）

复制 `scripts/announce_helper.py` 到你的项目，然后：

```python
from announce_helper import announce, receive, task, complete, error

# 一行调用
receive("用户查询天气")
task("正在获取数据")
complete("已发送天气预报")
error("网络超时")
```

### Bash / Shell 集成

在你的脚本中：

```bash
#!/bin/bash
ANNOUNCE="$HOME/.openclaw-autoclaw/skills/audio-announcement/scripts/announce_pygame.py"

announce() {
    python3 "$ANNOUNCE" "$1" "$2" zh &
}

# 使用
announce receive "开始备份"
# ... 执行备份 ...
announce complete "备份完成"
```

### 避免遗漏的最佳实践

1. **模板化**：将播报代码复制到所有 agent 模板中
2. **检查清单**：使用 AGENTS.md 中的清单每次任务后自查
3. **自动验证**：定期运行 `scripts/verify_announcement.py`
4. **异步非阻塞**：如需流畅交互，可使用 `async_=True` 参数

---

## 🔧 高级配置

### 配置播报声音

编辑 `scripts/announce_pygame.py`，修改 `VOLUME` 变量：

```python
VOLUME = 0.8  # 0.0 - 1.0，默认 1.0
```

### 自定义语音

修改 `voices` 字典选择不同的 edge-tts 语音：

```python
voices = {
    "zh": "zh-CN-XiaoxiaoNeural",  # 晓晓
    "en": "en-US-JennyNeural",     # Jenny
    # 更多语音参考: https://learn.microsoft.com/azure/ai-services/speech-service/language-support#text-to-speech
}
```

### 禁用特定类型

若某些播报类型不需要，可以在你的 agent 代码中跳过：

```python
if config.get("announce_receive", True):
    announce("receive", msg)
```

---

## 🧪 测试与调试

### 运行验证脚本

```bash
cd ~/.openclaw-autoclaw/workspace/scripts
python verify_announcement.py
```

该脚本会：
1. 检查 edge-tts 和 pygame 是否安装
2. 逐一测试四种播报类型
3. 报告通过率和修复建议

### 常见问题

**没有声音？**
- 检查系统音量
- 确认 pygame 已安装：`python -c "import pygame; print(pygame.version.ver)"`
- 测试 edge-tts：`edge-tts --text "测试" --voice zh-CN-XiaoxiaoNeural --write-media test.mp3`

**播报延迟？**
- 首次使用会有缓存延迟（下载语音包）
- 考虑使用本地语音合成引擎替代

**PATH 问题？**
-  announce_pygame.py 已改用 `python -m edge_tts` 模块调用
- 不再依赖 PATH 中的 edge-tts 命令

---

## 📊 配置状态追踪

在你的 `AGENTS.md` 和 `MEMORY.md` 中记录配置状态：

```markdown
### ✅ 播报配置状态 (YYYY-MM-DD)

- [x] edge-tts 已安装
- [x] pygame 已安装
- [x] 验证脚本已运行并通过
- [x] 强制规则已集成到 AGENTS.md
- [x] Heartbeat 自动检查已启用
```

---

## 🤝 贡献

欢迎提交 Issue 和 PR！

如果你发现任何遗漏播报的场景，或需要更多集成示例，请告诉我们。

---

## License

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 📞 支持

- **GitHub Issues**: https://github.com/wililam/audio-announcement-skills/issues
- **ClawHub**: `clawhub explore audio-announcement`

---

🦊 让你的 OpenClaw Agent 开口说话，透明化每一步操作！
Make your OpenClaw Agent talk, making every step transparent!

⭐ 如果这个技能对你有帮助，请给它一个 star！⭐
