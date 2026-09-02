# 贡献指南

感谢你帮助维护 12306。项目正在进行维护重启，优先处理可测试性、依赖升级、文档和与当前公开接口的兼容性。

## 开始之前

1. 在 Issue 中确认问题尚未被处理；较大改动请先讨论设计。
2. 日志和截图必须移除账号、手机号、身份证号、Cookie、Token、订单信息等敏感数据。
3. 不提交规避平台验证、访问控制或风控机制的实现。

## 本地验证

```bash
python -m compileall -q run.py agency config init inter myException myUrllib tests
python -m unittest discover -s tests -v
```

不依赖网络的逻辑应附带单元测试。调用外部服务的测试必须使用 mock，不能在 CI 中访问真实账号或生产接口。

## Pull Request

- 每个 PR 聚焦一个问题，并关联对应 Issue。
- 清楚说明行为变化、兼容性和回滚方式。
- 保持提交信息简洁；推荐使用 `fix:`、`feat:`、`docs:`、`test:`、`chore:` 前缀。
- 维护者会检查测试、敏感信息、依赖风险和文档完整性。
