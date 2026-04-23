# 更新日志

所有值得注意的版本变更都会记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，并且本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [2.2.0] - 2026-04-23

### 新增
- ✅ **防遗忘机制（6层防线）**：确保 Agent 永远不会忘记播报
  - openclaw.json hooks：每次会话启动自动运行自检脚本
  - BOOTSTRAP.md：新会话自动加载播报规则
  - 6层防线：Session Hook → 自检脚本 → BOOTSTRAP → AGENTS → MEMORY → IDENTITY
- ✅ **文件集成规则**：SKILL.md 中明确说明需要在哪些文件中加入什么播报规则
  - AGENTS.md：播报时机表、内容原则、强制播报场景、播报脚本路径
  - MEMORY.md：强制播报规则表
  - IDENTITY.md：强制播报声明、启动播报自检
  - TOOLS.md：语音播报系统说明
  - USER.md：播报偏好设置
- ✅ **SKILL.md 重构**：精简为纯技能文档，移除非技能内容

### 改进
- ✅ SKILL.md 从 354 行精简到 ~450 行（内容更聚焦）
- ✅ 新增防遗忘流程图和配置说明
- ✅ 新增自检清单（5项检查）

## [2.1.0] - 2026-04-23

### 新增
- ✅ **一键集成验证** `beep verify-integration` - 完整验证命令
  - 依赖检查（pygame, edge-tts, Python 版本）
  - 配置验证（音量、语言、异步设置）
  - 环境自检（7项系统检查）
  - 播放4种测试语音（receive, task, complete, error）
  - 输出结构化报告 + 返回码（0=成功，1=失败）

### 改进
- ✅ **重试机制**：网络调用 3 次重试 + 指数退避（1s→2s→4s）
- ✅ **播放降级**：pygame → 系统播放器 → 仅日志（保证核心功能）
- ✅ **配置热重载**：`beep config reload` 无需重启应用
- ✅ **LRU 缓存**：自动清理旧文件，默认保留最新100个
- ✅ **结构化日志**：时间戳 + 级别 + 消息，支持 DEBUG/INFO/WARNING/ERROR
- ✅ **运行时统计**：缓存大小、成功率、运行时间
- ✅ **异常堆栈**：`exc_info=True`，调试更清晰
- ✅ **路径容错**：中文/空格路径安全处理

### 修复
- ✅ 修复配置读取 bug（配置文件路径错误）
- ✅ 修复方法缺失问题（AnnouncementHelper 类同步）
- ✅ 修复函数名错误（`cleanup_old_cache` → `cleanup_temp_files`）
- ✅ 修复重复定义（移除重复的 `clear_cache` 和 `reload_config`）
- ✅ 删除多余文件（误创建的 `core.py`）

### 品牌升级
- 🎨 英文名：Beep
- 🎨 中文名：小喇叭
- 🎨 Slogan：让电脑会说话

## [2.0.8] - 2026-04-11

### 改进
- ✅ 播报本地化 - 所有播报仅在本机后台播放，不发送语音文件到聊天
- ✅ 统一包装脚本 - scripts/announce.py 自动解析 skill 路径
- ✅ 默认音量优化 - 配置文件默认 volume=0.1（10%）
- ✅ CLI 工具修复 - 修复 pygame 导入问题，提升 Windows 稳定性
- ✅ 文档全面升级 - MEMORY.md / AGENTS.md / TOOLS.md 统一管理

## [2.0.7] - 2026-04-08

### 新增
- ✅ PyPI 支持 - pip install beep-announcement
- ✅ 配置文件系统 - ~/.config/audio-announcement/config.json
- ✅ 异步默认化 - 默认后台播放，减少阻塞
- ✅ CLI 工具 - audio-announce 命令支持测试、配置、统计

## [2.0.6] - 2026-04-05

### 新增
- ✅ 防遗忘机制 - 启动自检 + 身份绑定
- ✅ 快速集成指南 - announce_helper.py 简化集成
- ✅ 强制规则模板 - 可直接复制到 AGENTS.md

## [2.0.5] - 2026-04-01

### 初始版本
- ✅ 基础语音播报功能
- ✅ 支持 9 种语言
- ✅ 支持 4 个平台（macOS, Linux, Windows, Android）
- ✅ 队列系统 - 消息不丢失，失败自动重试

---

## 版本说明

### 语义化版本

格式：`MAJOR.MINOR.PATCH`

- **MAJOR**: 不兼容的 API 变更
- **MINOR**: 向后兼容的功能性新增
- **PATCH**: 向后兼容的问题修复

### 支持平台

- ✅ Windows 10/11
- ✅ macOS 10.15+
- ✅ Linux (Ubuntu, Debian, CentOS, etc.)
- ✅ Android (Termux)

### Python 版本支持

- ✅ Python 3.9+
- ✅ Python 3.10
- ✅ Python 3.11
- ✅ Python 3.12
- ✅ Python 3.13
