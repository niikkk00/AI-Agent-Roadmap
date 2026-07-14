# AI-Agent-Roadmap 开发手册（Project Handbook）

**版本：v1.0（2026-07）**

## 一、项目目标

本项目不是单纯学习 AI Agent，而是按照企业开发流程，从零开始完成一套 AI 应用开发路线，最终具备独立开发 AI 产品并获得 AI Agent / AI 应用开发方向实习的能力。

目标岗位包括 AI Agent 开发工程师、AI 应用开发工程师、Python AI 后端工程师和 LLM Application Engineer。路线定位为：

> **AI Agent + Python 后端 + 工程化**

学习重点不止是 Prompt 或 API 调用，还包括系统设计、代码质量、测试、版本管理、部署和项目表达。

## 二、学习原则

整个学习过程采用 Project-Based Learning（项目驱动学习）：

1. 每节课控制在 30～60 分钟。
2. 每节课只学习一个核心工程思想。
3. 先理解设计和验收标准，再编写代码。
4. 不直接复制官方代码，也不由导师一次性提供完整实现。
5. 每节课结束进行 Code Review。
6. 每完成一个 Sprint，整理文档并提交 GitHub。
7. 所有代码遵循企业开发规范。
8. 重点培养工程思维，而不是只会调用 API。

## 三、协作与回答规范

- 使用中文回答，段落紧凑，相近内容放在一起，只在模块之间换行。
- 不一次性给出完整代码；先用问题、设计约束和分级提示引导实现。
- 每个设计都解释原因，并说明它解决的工程问题。
- 学习进度用 Sprint、Feature 和验收结果描述，不只记录“学了什么”。
- Code Review 关注正确性、职责边界、命名、异常处理、安全性、可测试性、文档和 Git 规范。
- 未经过运行验证和 Code Review 的功能，不视为完成。

## 四、当前学习进度

### Sprint 1：ChatBot CLI

#### Day 1：数据结构一致性（Data Consistency）

已完成 Git 初始化、GitHub 仓库建立、Python 虚拟环境、JSON、`list`、`dict`、`messages` 数据结构、`history.json` 和模拟 ChatBot。

核心认识：`messages` 中的元素必须始终保持一致的数据结构：

```python
[
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
]
```

不能混入字符串或其他不符合约定的数据类型，否则调用方需要处理多种输入形态，容易产生运行时错误。

#### Day 2：封装（Encapsulation）

已完成 `while True` 聊天循环、`exit` 退出、多轮聊天和 `send_message()` 的职责设计。

核心认识：模型调用应封装在 `send_message(messages)` 中，而不是直接写在 `main.py`，从而隔离聊天流程和外部模型调用。

#### Day 3：职责单一（Single Responsibility Principle）

已建立以下模块职责：

- `main.py`：只负责 CLI 聊天流程。
- `llm.py`：只负责初始化客户端、调用模型并返回回复内容。
- `config.py`：只负责 API Key、Base URL 和模型等配置。

`llm.py` 已接入 OpenAI SDK 兼容的 DeepSeek API。当前待完成 `main.py` 与 `send_message()` 的集成、运行验证和 Code Review。

## 五、当前系统链路

已完成的核心链路为：

```text
User -> messages -> send_message() -> DeepSeek -> response content
```

下一步将由 `main.py` 串联该链路，形成可运行的 CLI 聊天机器人，通过验收后提交 Git。

## 六、仓库规划

```text
AI-Agent-Roadmap/
├── 01_llm_basic/
│   └── chatbot/
├── 02_prompt/
├── 03_rag/
├── 04_agent/
├── 05_multi_agent/
├── projects/
└── docs/
    ├── Project-Handbook.md
    ├── Roadmap.md
    ├── Sprint1.md
    ├── Sprint2.md
    └── Sprint3.md
```

Sprint 文档按实际进度逐步创建，不预先生成空文档。

## 七、Git Commit 规范

提交信息统一采用 Conventional Commits 风格：

```text
feat(chatbot): support chat loop
feat(chatbot): integrate DeepSeek
fix(chatbot): fix message bug
refactor(chatbot): optimize llm module
docs(chatbot): update README
```

不使用 `update`、`修改`、`第一次提交` 等无法表达变更目的的信息。每次提交只包含一个逻辑完整、可以说明和验证的变更。

## 八、后续学习路线

1. Sprint 1：ChatBot CLI（进行中）
2. Sprint 2：FastAPI ChatBot
3. Sprint 3：Prompt Engineering
4. Sprint 4：RAG
5. Sprint 5：Tool Calling
6. Sprint 6：Multi-Agent
7. Sprint 7：Docker
8. Sprint 8：Linux 部署
9. Sprint 9：完整 AI 助手

预计周期为 3～4 个月，具体进度根据学习节奏和每个 Sprint 的验收结果调整。

## 九、导师职责

导师身份为长期技术导师（Tech Lead），以公司 Mentor 的方式协作：明确目标和约束、引导思考、进行 Code Review、把知识落实到项目，并持续训练软件工程和项目表达能力。

## 十、最终成果

- 一个结构完整、提交记录清晰的 `AI-Agent-Roadmap` GitHub 仓库。
- 8～10 个可运行、可解释、可演示的 AI 项目或阶段性应用。
- FastAPI、RAG、Tool Calling、Multi-Agent、Docker 和 Linux 部署能力。
- 完整的 README、架构说明、运行指南和开发文档。
- 能够写入简历并用于面试讲解的 AI 项目作品集。

## 十一、完成标准（Definition of Done）

一个 Feature 只有同时满足以下条件，才能在 Roadmap 中标记为完成：

1. 功能符合本节课的验收标准。
2. 代码能够在目标环境运行。
3. 关键异常和边界情况已考虑。
4. 已完成 Code Review，并处理阻塞性问题。
5. 相关文档和进度已更新。
6. 已形成职责清晰的 Git 提交。
