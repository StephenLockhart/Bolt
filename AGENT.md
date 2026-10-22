# AGENT · 本仓库的作业入口

> 任何新会话、任何 Agent，先读这一页。它定义我们怎么工作，不定义产品做什么（产品在 `docs/`）。

## 项目

**DoubleCheck（DC）· 快慢机** —— 把 AI 的思考速度匹配人的注意力：人在回路、按需接入，其余时间 AI 全力奔跑。

公开主页见 `README.md`；产品哲学、路线、品牌、商业全部在 `docs/`（机密，独立 git 仓库，不进本公开仓库）。

## 目录

```
README.md      公开：产品介绍与标志
AGENT.md       公开：本页，作业规范
TODO.md        公开：路线勾选表

docs/          🔒 机密：编号文档 00–07 + assets（独立 git 仓库）
library/       可复用素材：templates / skills / scripts / references
.local-backups/本地快照（不进仓库）
```

## 记忆分层

| 层 | 位置 | 存什么 | 何时读 |
|---|---|---|---|
| 入口 | `AGENT.md`（本页） | 怎么工作 | 每次会话开头 |
| 地图 | `docs/00-MAP.md` | 文件索引 + 决策记录 | 每次会话开头 |
| 状态 | `docs/STATE.md` | 现在做到哪、下一步、阻塞 | 接手任务前 |
| 详情 | `docs/01`–`07` | 路线 / 哲学 / 品牌 / 产品 / 商业 / 获客 / 学习 | 按任务 |
| 素材 | `library/` | 模板 / skill / 脚本 / 外部参考 | 需要复用或研究时 |

## 工作四步（缺一不可）

1. **快照**：`sh library/scripts/snapshot.sh`
2. **改**：先 Read 再 Edit；只做定点修改，禁止整页重写
3. **校验**：HTML 跑 `python3 library/scripts/check_html.py <file>`；确认旧元素零残留
4. **提交**：`cd docs && git add -A && git -c user.email=dc@local -c user.name=doublecheck commit -m "<说明>"`

## 三条硬规则

1. **事实纪律**：不编造用户数、收入、履历、市场数据；数字带来源或标 `[待填]` / `估算`；引用外部信息给链接
2. **口径唯一**：名称、tagline、五层、标志几何、配色以 `docs/02-VISION.md` 与 `docs/03-BRAND.md` 为唯一权威，不得自创变体
3. **机密不外泄**：`docs/` 内容不得写进 README / AGENT / TODO / library（这些会进公开仓库）

## 输出默认

中文 · 结论先行 · 表格优先 · 代码零注释 · HTML 标签闭合
