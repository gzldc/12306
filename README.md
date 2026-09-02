# 12306

[![CI](https://github.com/gzldc/12306/actions/workflows/ci.yml/badge.svg)](https://github.com/gzldc/12306/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/gzldc/12306)](https://github.com/gzldc/12306/stargazers)

一个使用 Python 编写的 12306 购票流程研究项目，源自 [testerSunshine/12306](https://github.com/testerSunshine/12306)，本仓库曾针对当时的登录、查询、候补与通知流程进行二次开发。

> [!IMPORTANT]
> **项目正在维护重启。** 现有核心实现和依赖主要来自 2020–2021 年，12306 的接口与验证流程已经变化；当前版本不应被视为可用的生产工具。请勿使用它规避平台验证、访问控制或风控机制，并遵守 12306 的服务规则与适用要求。

## 当前状态

| 范围 | 状态 |
| --- | --- |
| 代码语法与离线冒烟测试 | CI 持续验证 |
| 依赖升级 | 规划中 |
| 当前登录/查询接口兼容性 | 待验证 |
| 真实购票流程 | 未承诺可用 |
| 安全与隐私审计 | 规划中 |

维护工作的优先级与进展会通过 [Issues](https://github.com/gzldc/12306/issues) 和 Pull Requests 公开记录。

## 代码结构

```text
agency/       CDN 与代理相关逻辑
config/       配置、日志、通知和接口地址
init/         登录与流程编排
inter/        业务接口封装
myUrllib/     HTTP 客户端封装
verify/       历史验证码识别代码
tests/        不访问生产服务的离线测试
run.py        命令行入口
```

## 本地开发

维护者当前先保证无需真实账号和生产接口的离线检查可运行：

```bash
git clone https://github.com/gzldc/12306.git
cd 12306
python -m compileall -q run.py agency config init inter myException myUrllib tests
python -m unittest discover -s tests -v
```

历史依赖包含停止维护或无法在新版本 Python 上安装的组件。请先关注依赖升级 Issue，不建议直接在主机环境安装 `requirements.txt`；如需研究旧版行为，请使用隔离的容器或虚拟环境。

## 维护路线图

- [x] 恢复最小 CI 与离线测试
- [x] 补充贡献、安全和 Issue/PR 模板
- [ ] 将配置模板与运行时秘密彻底分离
- [ ] 升级并拆分核心、可选机器学习依赖
- [ ] 为 HTTP 层增加 mock 测试和明确超时
- [ ] 评估当前公开接口兼容性，移除失效功能
- [ ] 发布经过验证的维护版本

## 参与贡献

欢迎提交可复现的 Issue 和小而清晰的 Pull Request。开始前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 和 [SECURITY.md](SECURITY.md)。提交日志时务必移除账号、手机号、身份证号、Cookie、Token 和订单信息。

## 历史资料

- 原项目：[testerSunshine/12306](https://github.com/testerSunshine/12306)
- 历史视频教程：[bilibili/BV1mK4y1V7cd](https://www.bilibili.com/video/BV1mK4y1V7cd)
- 历史更新说明：[Update.md](Update.md)

历史文档和配置仅用于理解旧版实现，不代表当前仍然可用。

## 许可证

本项目采用 [MIT License](LICENSE)。
