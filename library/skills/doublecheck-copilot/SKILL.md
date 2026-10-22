---
name: doublecheck-copilot
description: DoubleCheck（DC）· 快慢机项目的作业规范。任何时候在本仓库做品牌、产品、商业或文档工作，先读本文件。包含口径速查、文件结构、改动流程与验证要求，避免各说各话与资产丢失。
---

# DoubleCheck 作业规范

## 何时启用

在本仓库内做任何与产品、品牌、商业、文档相关的工作时启用。包括：写文案、改标志、更新 BP、加功能定义、做研究、整理文档。

## 第一步：读口径

从 `docs/00-MAP.md` 开始，再按任务读对应编号文档：

| 任务 | 必读 |
|---|---|
| 品牌、标志、配色、文案 | `docs/03-BRAND.md` |
| 产品哲学、功能定义 | `docs/02-VISION.md` |
| 路线、里程碑、验证信号 | `docs/01-ROADMAP.md` |
| 商业、定价、资金 | `docs/05-BUSINESS.md` |
| 获客、渠道、大赛 | `docs/06-GTM.md` |

## 口径速查（不得自创变体）

- 名称：`DoubleCheck（DC）· 快慢机`
- 英文 tagline：`thinking at the right speed.`
- 中文副标：`不徐不疾，得之于手`
- 核心句：`人在回路、按需接入：只在关键时机请你把关，其余时间 AI 全力奔跑`
- 五层：L0 表层交互 / L1 快挡 / L2 直接操作 / L3 慢挡 / L4 长期构思
- 标志：深蓝 `#1E3A8A` 磁贴 + 白鱼（太极逗号）+ 深蓝实心点（左眼=人）+ 白色空心环（右眼=快，压在鱼尾外缘）+ 外圈开口弧（慢，30s 转一圈）
- 两条铁律：**两只眼睛永远都在**（16px 也不许删环）；**只有外圈弧在动**，鱼和两只眼静止

## 铁律：事实纪律

- 不编造用户数、收入、研究履历、市场数据
- 数字必须带来源，或明确标 `[待填]` / `估算`
- 允许写"我们还没做到"，不允许写"即将颠覆"
- 引用外部信息必须给链接

## 改动流程（四步，缺一不可）

1. **快照**：`sh library/scripts/snapshot.sh`
2. **改**：只做定点修改，禁止整页重写；先 Read 再 Edit
3. **校验**：HTML 跑 `python3 library/scripts/check_html.py <file>`；确认旧元素零残留
4. **提交**：`cd docs && git add -A && git -c user.email=dc@local -c user.name=doublecheck commit -m "<说明>"`

## 文件结构

```
docs/        机密文档（独立 git 仓库，推私有远程）
library/     可复用素材（模板 / skills / 脚本 / 外部参考）
README.md    公开主页（不含机密）
```

**禁止**把 `docs/` 内容写进 README、AGENT、TODO 或 library 里——那些会进公开仓库。

## 输出默认要求

- 中文
- 代码零注释（除非用户要求）
- HTML 必须标签闭合
- 表格优先于长段落
- 结论先行，不铺垫
