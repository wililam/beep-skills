# 贡献指南

感谢你对 beep-skills 项目的关注！

## 📋 贡献流程

### 1. Fork 项目

```bash
# Fork 到你的 GitHub 账户
# 然后克隆到本地
git clone https://github.com/your-username/beep-skills.git
cd beep-skills
```

### 2. 创建分支

```bash
git checkout -b feature/your-feature-name
```

### 3. 安装开发依赖

```bash
pip install -e ".[dev]"
```

### 4. 进行修改

- 遵循现有代码风格
- 添加必要的测试
- 更新文档

### 5. 运行测试

```bash
pytest tests/
```

### 6. 提交代码

```bash
git add .
git commit -m "feat: 添加新功能"
git push origin feature/your-feature-name
```

### 7. 创建 Pull Request

- 描述你的修改
- 关联相关 Issue
- 等待代码审查

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

## 🐛 报告问题

### Issue 模板

```markdown
**描述问题**
简要描述遇到的问题

**复现步骤**
1. 执行 '...'
2. 点击 '...'
3. 滚动到 '...'
4. 看到错误

**预期行为**
描述你期望发生的行为

**实际行为**
描述实际发生的行为

**环境信息**
- OS: [e.g., Windows 11]
- Python: [e.g., 3.13.12]
- beep-skills: [e.g., 2.1.0]

**附加信息**
截图或日志
```

## 🎯 开发路线图

查看 [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) 了解未来的开发计划。

## 📞 联系方式

- GitHub Issues: https://github.com/wililam/beep-skills/issues
- Email: uinecn@126.com

---

感谢你的贡献！🎉
