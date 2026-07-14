# AI-Agent-Roadmap

本文件只维护 Sprint 和 Feature 的验收进度。功能需满足《Project Handbook》中的 Definition of Done 后，才能标记为完成。

## Sprint 1：ChatBot CLI

**状态：进行中（约 70%）**

- [x] JSON 基础
- [x] `list` / `dict` 基础
- [x] `messages` 数据结构
- [x] Chat Loop
- [x] `send_message()` 职责封装
- [x] DeepSeek API 调用模块
- [ ] 在 `main.py` 中集成真实模型调用
- [ ] CLI 端到端运行验证
- [ ] Stream Output
- [ ] Memory / 历史记录
- [ ] 异常处理与安全配置
- [ ] README 完善
- [ ] Sprint 1 Code Review
- [ ] Sprint 1 GitHub 提交

### 当前 Feature

**集成 DeepSeek CLI ChatBot**

验收标准：用户可在终端连续输入消息；每轮调用 DeepSeek 并显示回复；上下文保持统一的 `messages` 结构；输入 `exit` 后正常退出；代码职责符合 `main.py`、`llm.py`、`config.py` 的模块边界。

## Sprint 2：FastAPI ChatBot

**状态：未开始**

- [ ] FastAPI 基础
- [ ] REST API 设计
- [ ] Chat 接口
- [ ] 请求与响应模型
- [ ] 错误处理
- [ ] API 测试

## Sprint 3：Prompt Engineering

**状态：未开始**

- [ ] 待 Sprint 2 验收后拆分 Feature

## Sprint 4：RAG

**状态：未开始**

- [ ] 待前置 Sprint 验收后拆分 Feature

## Sprint 5：Tool Calling

**状态：未开始**

- [ ] 待前置 Sprint 验收后拆分 Feature

## Sprint 6：Multi-Agent

**状态：未开始**

- [ ] 待前置 Sprint 验收后拆分 Feature

## Sprint 7：Docker

**状态：未开始**

- [ ] 待前置 Sprint 验收后拆分 Feature

## Sprint 8：Linux 部署

**状态：未开始**

- [ ] 待前置 Sprint 验收后拆分 Feature

## Sprint 9：完整 AI 助手

**状态：未开始**

- [ ] 待前置 Sprint 验收后拆分 Feature
