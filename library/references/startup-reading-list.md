# 创业学习库 · 按「此刻卡在哪」组织

> 服务对象：DoubleCheck（DC）· 快慢机。当前状态：原型可演示，尚未真用、尚未收费。
> 本清单不追求穷举，只回答一个问题：**读哪一条，能让我们这周少犯一个错。**
> 核实日期：2026-10-22。所有链接逐条做过 HTTP 检查；对脚本返回 403 但浏览器可开的站点标 `⚠️CF`。
> 图例：必读 = 两周内就该读完；选读 = 卡到具体问题时再读。免费栏写「免费」指正文可公开阅读，不含付费书。

## 0. 一页速览

| 卡点 | 对应章节 | 先读这三条 | 读完 7 天内应交出的东西 |
|---|---|---|---|
| 不知道创作者到底痛在哪 | §1 | The Mom Test / YC《How to talk to users》/ YC《First 10 customers》 | 5 份访谈摘要 + 3 句重复出现的原话 |
| 定价只有假设，没有证据 | §2 | Growth Unhinged 2026 报告 / a16z GenAI 定价 / 《Monetizing Innovation》 | 3 档价格卡 + 1 份设计伙伴报价单 |
| 3 分钟讲不清产品 | §3 §6 | Shape Up / Getting Real / B站 AI 创造公开赛规则 | 1 条不剪辑的 3 分钟视频 + 10 页 BP 骨架 |
| 两人团队排不出节奏 | §3 | MicroConf Video Vault / Indie Hackers / Shape Up | 90 天切两个 6 周 cycle 的排期表 |
| 资金材料不会写 | §4 | 奇绩申请页 / 深创赛 / HICOOL | 一页 one-pager + 1 分钟手机视频 |
| 开源/协议怎么变生意 | §5 | Plausible / Dify / awesome-indie | 公开 spec 的范围与收费边界一页纸 |

---

## 1. 找需求与验证

| # | 名称 | 作者 / 来源 | 形式 | 免费 | 链接 | 读它能解决我们的哪个具体问题 | 优先级 |
|---|---|---|---|---|---|---|---|
| 1.1 | The Mom Test | Rob Fitzpatrick（YC S07 校友） | 书（138 页，约 2 小时） | 付费（官网有试读与课程） | https://www.momtestbook.com/ | 让我们停止问「你觉得这个想法好吗」，改问「你上次卡住是什么时候、当时怎么解决的」，避免访谈全变成好评 | 必读 |
| 1.2 | How to talk to users | Gustaf Alströmer / YC Startup School | 课程视频（17 分钟） | 免费 | https://www.ycombinator.com/library/Iq-how-to-talk-to-users | 给出五个可直接照抄的访谈问题，并说明哪些问题一问就污染数据 | 必读 |
| 1.3 | How to Get Your First 10 Customers | Max Kolysh / YC Startup School | 课程视频 | 免费 | https://www.ycombinator.com/library/SF-how-to-get-your-first-10-customers | 解决「去哪找前 10 个直播创作者」：先一度人脉、再去他们真实聚集的地方，而不是冷邮件群发 | 必读 |
| 1.4 | Do Things that Don't Scale | Paul Graham | 文章 | 免费 | https://www.paulgraham.com/ds.html | 允许我们用手工方式服务前几个设计伙伴（代配置、代跑任务），把「不规模化」当成学习手段 | 必读 |
| 1.5 | Startup = Growth | Paul Graham | 文章 | 免费 | https://www.paulgraham.com/growth.html | 校准什么叫「增长」：先看每周新增的真实使用，而不是注册数；防止我们拿演示次数自我安慰 | 选读 |
| 1.6 | Starter Story 收入拆解案例库 | Pat Walls / Starter Story | 案例库（以 Morning Brew 拆解为例） | 部分免费 | https://www.starterstory.com/stories/morning-brew-breakdown | 给我们一个可照抄的「案例卡」格式：想法来源、启动成本、团队人数、定价、获客渠道，五栏就能把设计伙伴讲清楚 | 选读 |

> 读完马上做：把 1.1 的三条规则写成访谈提纲的「禁问句」清单，贴进访谈模板。

---

## 2. 定价与单位经济

| # | 名称 | 作者 / 来源 | 形式 | 免费 | 链接 | 读它能解决我们的哪个具体问题 | 优先级 |
|---|---|---|---|---|---|---|---|
| 2.1 | Pricing & Packaging（专栏） | a16z Growth | 文章合集 | 免费 | https://a16z.com/pricing-packaging/ | 建立定价词汇表（价值指标、分层、超额、可预测性），让我们讨论「按任务小时还是按席位」时不说外行话 | 必读 |
| 2.2 | Pricing and Packaging Your B2B or Prosumer Generative AI Feature | Sarah Wang / Tugce Erten / Alex Immerman，a16z | 文章 | 免费 | https://a16z.com/pricing-packaging-ai-b2b-prosumer/ | 直接对应我们的困境：AI 功能有推理成本，不能照抄纯 SaaS 席位价；给出「价值 / 成本 / 打包」三角 | 必读 |
| 2.3 | The state of B2B monetization in 2026 | Kyle Poyar / Growth Unhinged（230 家公司问卷） | 报告 + newsletter | 摘要免费，全文部分付费 | ⚠️CF · https://www.growthunhinged.com/p/the-state-of-b2b-monetization-in-2026 | 用真实样本纠正「AI 产品该按结果收费」的想象：混合定价才是主流，早期团队仍偏固定费 | 必读 |
| 2.4 | Pricing 专题索引（含 How to run a pricing project） | Kyle Poyar / Growth Unhinged | 文章索引 | 免费 | ⚠️CF · https://www.growthunhinged.com/pricing | 给出一条可执行的定价项目流程（策略→客户验证→系统上线），我们只需跑「客户验证」这一段 | 选读 |
| 2.5 | Monetizing Innovation | Madhavan Ramanujam & Georg Tacke / Simon-Kucher | 书（Wiley，256 页） | 付费（官网页面标「Order your free copy」，赠阅库存待核实） | https://www.simon-kucher.com/en/insights/beating-inflation-monetizing-innovation-book-order-landing-page | 逼我们在做功能前先做「付费意愿对话」，避免做出没人愿意加价的功能；书里的「功能冲击 / 低价化」四类失败可直接对照我们 | 选读 |

> 读完马上做：把 2.2 的「价值 / 成本 / 打包」三问，改写成给设计伙伴的 5 句话报价说明。

---

## 3. 两人 / 极简团队怎么起步

| # | 名称 | 作者 / 来源 | 形式 | 免费 | 链接 | 读它能解决我们的哪个具体问题 | 优先级 |
|---|---|---|---|---|---|---|---|
| 3.1 | Indie Hackers | Courtland Allen 创办，现独立运营 | 社区 + 访谈库 | 免费 | ⚠️CF · https://www.indiehackers.com/ | 看同类小团队如何用真实收入数字说话；也给我们「公开构建」的发布格式与节奏参考 | 必读 |
| 3.2 | MicroConf Video Vault | Rob Walling / MicroConf | 视频库（170+ 小时） | 免费 | https://microconf.com/latest/microconf-video-vault | 补「两人公司怎么分工、怎么定价、怎么不融资活下去」的实操，不用飞去美国参会 | 必读 |
| 3.3 | Turning side projects into profitable startups | Pieter Levels（levels.io） | 演讲文字稿 + 视频 | 免费 | https://levels.io/startups | 用「12 个产品 12 个月、先发布再迭代」治我们的完美主义；也提醒单人产品靠的是极窄场景 | 必读 |
| 3.4 | Shape Up | Ryan Singer / 37signals | 在线书（免费全文） | 免费 | https://basecamp.com/shapeup | 解决两人团队「需求越做越大」：固定时间、可变范围、6 周一个 cycle、到点就砍 | 必读 |
| 3.5 | Getting Real | Jason Fried / 37signals | 在线书（免费全文） | 免费 | https://basecamp.com/gettingreal | 给「少做、做小、先上线」提供一整套话术，适合拿来对抗我们自己想加功能的冲动 | 选读 |

> 读完马上做：用 3.4 的 pitch 五要素（问题 / 胃口 / 方案 / 兔子洞 / 不做什么）写一页「快挡 MVP」提案。

---

## 4. 中国语境下的早期融资与政府资助

| # | 名称 | 作者 / 来源 | 形式 | 免费 | 链接 | 读它能解决我们的哪个具体问题 | 优先级 |
|---|---|---|---|---|---|---|---|
| 4.1 | 奇绩创坛 2027 春季创业营（申请页） | 奇绩创坛 MiraclePlus | 官网 | 免费 | https://www.miracleplus.com/en/apply/ | 明确「30 万美元换 7%、3 个月、北京/华东/深圳/线上面谈、申请截止 2026-12-12」；并给出申请写法：一句话说清用户与价值 | 必读 |
| 4.2 | 奇绩创业营说明（投资与资源） | 奇绩创坛 | 官网 | 免费 | https://www.miracleplus.com/batch/ | 判断我们是否需要这笔钱、能换来什么（Office Hour、路演日、校友网络），而不是只看估值 | 必读 |
| 4.3 | 深创赛（中国深圳创新创业大赛）官网专栏 | 深圳市科技创新局 | 政府官网 | 免费 | https://stic.sz.gov.cn/xxgk/ztzl/cxcyds/ | 看清赛制（国/市/区三级）、奖金与「鲲鹏青年」资助衔接；2026 届报名 6/3–7/15 已结束，用来倒推 2027 届准备 | 必读 |
| 4.4 | HICOOL 全球创业大赛 | 北京海外高层次人才协会 | 官网 | 免费 | https://www.hicool.com/ | 看清「200 个获奖名额、一等奖 200 万、面向在京落地」的取舍；2026 届报名 2/27–4/15，2027 届时间需以官网复核 | 选读 |
| 4.5 | B站 AI 创造公开赛 活动规则 | 哔哩哔哩 | 赛事规则页 | 免费 | https://m.bilibili.com/opus/1210076034617049096 | 直接对齐我们的演示物料：产品必须「可运行、可交互」、横屏视频 ≥1 分钟、以连载形式公开过程；投币数决定入围，评审团定名次 | 必读 |
| 4.6 | 快手 AI 创作者大赛（200 万奖金池报道） | 成都日报 / 快手光合大会 | 新闻报道 | 免费 | https://m.xinminweekly.com.cn/content/51088.html | 判断是否值得为「12 周征集、单项最高 50 万」调整内容节奏；官方报名入口与截止日待核实 | 选读 |

> 读完马上做：把 4.1 的申请问题逐条回答一遍（用户是谁 / 解决什么 / 一句话类比 / 团队三格），不超过 300 字。

---

## 5. 开源项目如何变成生意

| # | 名称 | 作者 / 来源 | 形式 | 免费 | 链接 | 读它能解决我们的哪个具体问题 | 优先级 |
|---|---|---|---|---|---|---|---|
| 5.1 | awesome-indie | mezod / GitHub | 仓库（清单） | 免费 | https://github.com/mezod/awesome-indie | 一次性拿到独立开发者赚钱的渠道、案例、工具清单，用来补我们「除了大赛还能怎么活」的选项 | 必读 |
| 5.2 | chinese-independent-developer | 1c7 / GitHub | 仓库（清单） | 免费 | https://github.com/1c7/chinese-independent-developer | 看中国独立开发者真实在做什么、怎么定价、怎么推广；比英文案例更贴近大陆支付与渠道 | 必读 |
| 5.3 | Plausible Analytics | Plausible / GitHub | 仓库 + 官网 | 免费（开源，云服务付费） | https://github.com/plausible/analytics | 一个可照抄的「开源核心 + 云托管收费」模型：AGPL 自托管免费，订阅收入养 10 人团队，21k 付费用户，不投广告 | 必读 |
| 5.4 | Dify | langgenius / GitHub | 仓库 + 定价页 | 免费（社区版开源，企业版付费） | https://github.com/langgenius/dify | 展示「社区版免费、企业版卖合规/SSO/支持」的开源商业化边界，帮我们想清楚 spec 公开到哪一层 | 选读 |
| 5.5 | build-your-own-x | codecrafters-io / GitHub | 仓库（技术练习清单） | 免费 | https://github.com/codecrafters-io/build-your-own-x | 只用来补底层理解、提升技术可信度；**不是商业清单**，别把它当产品方向（见 §7 勘误） | 选读 |

> 读完马上做：写一页「我们公开什么、不公开什么、什么收费」——spec 公开、产品源码不公开、托管与团队协作收费。

---

## 6. AI 产品与 Agent 的公开设计经验

| # | 名称 | 作者 / 来源 | 形式 | 免费 | 链接 | 读它能解决我们的哪个具体问题 | 优先级 |
|---|---|---|---|---|---|---|---|
| 6.1 | Building effective agents | Anthropic Engineering | 长文 | 免费 | https://www.anthropic.com/engineering/building-effective-agents | 给我们交接协议的骨架：优先用简单可组合的 workflow，而不是一上来堆多 agent；并强调显式展示计划步骤 | 必读 |
| 6.2 | A practical guide to building agents | OpenAI | PDF | 免费 | https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf | 提供「什么时候该用 agent、护栏怎么设、human-in-the-loop 怎么放」的清单，可直接改成交接协议检查表 | 必读 |
| 6.3 | Effective context engineering for AI agents | Anthropic Engineering | 长文 | 免费 | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | 解释长任务为什么会「越跑越糊涂」：上下文要压缩、要分层、要有可恢复的状态，对应我们的记忆 v1 | 必读 |
| 6.4 | Building monday.com Sidekick | Omri Bruchim / LangChain 博客 | 案例复盘 | 免费 | https://www.langchain.com/blog/building-monday-com-sidekick-why-capable-agents-need-more-than-just-tools | 真实失败复盘：工具越多、单 agent 越差；他们改成有界职责 + 沙箱 + 子 agent。正好反驳我们「功能全塞一个循环」的冲动 | 必读 |
| 6.5 | Building effective agent automations | Lance Martin / CJ Avilla，Anthropic | 工程文章 + 参考实现 | 免费 | https://claude.dev/blog/building-effective-agent-automations/ | 列出定时 Agent 的常见失效：源失联、偏好漂移、缺预算上限；对应我们慢挡的「可中断、可恢复、可审计」 | 选读 |
| 6.6 | 老板花 50 万搞了个 AI Agent，上线一周就关了 | 枫叶冰澜 / dbaplus 社群 | 中文复盘 | 免费 | https://dbaplus.cn/news-73-7450-1.html | 最贴近我们的失败样本：幻觉、延迟、上下文污染三杀；给出「先 AI 辅助人工，再谈全自动」的顺序 | 必读 |

> 读完马上做：把 6.6 的三个死因（幻觉、延迟、上下文污染）各写一条我们产品里的对应风险与拦截点。

---

## 7. 核实记录与勘误（重要）

| 事项 | 核实结果 |
|---|---|
| 链接可用性 | 除标注 `⚠️CF` 的站点（Indie Hackers、Growth Unhinged 对脚本返回 403）外，本清单所有链接在 2026-10-22 返回 200；403 站点浏览器可正常打开 |
| OpenView 的 UBP 报告 | OpenView 已不再以原形态运营，原报告入口不可依赖；其原合伙人 Kyle Poyar 在 Growth Unhinged 持续发布更新数据，故 §2 改用后者 |
| `awesome-bootstrap` | GitHub 上这个名字实际指 Bootstrap 主题清单（如 StartBootstrap），**不是**独立开发者创业清单；对应的真清单是 `awesome-indie`。按名字找会走错 |
| `build-your-own-x` | 是编程练习清单（重写数据库/编译器/编辑器等），不是商业案例库；只适合补技术基本功 |
| HICOOL 时间 | 2026 届报名为 2026-02-27 至 2026-04-15（港中大转载官网公告）。`06-GTM` 里「2027 届 8 月起报名」与我们检索到的官方节奏不一致，提交前必须以 hicool.com 复核，暂标 `待核实` |
| 快手赛事 | 2026 光合大会宣布「AI 创作者大赛」12 周征集、200 万+ 奖金池；公开报道多，官方报名入口在快手 App 内，截止日 `待核实`。另有面向在校生的「AI 未来创造者挑战赛」，我们不符合资格 |
| 奇绩条款 | 「30 万美元或等值人民币换 7%」已在官网核实；2027 春季批申请截止 2026-12-12（官网英文页） |

## 8. 怎么读（7 天，每天 ≤60 分钟）

| 天 | 读什么 | 时长 | 当天产出 |
|---|---|---|---|
| D1 | 1.1 The Mom Test（前半） | 60 分 | 访谈提纲 v1，含 10 个禁问句 |
| D2 | 1.2 + 1.3 | 45 分 | 20 人访谈名单（每人一句「为什么找他」） |
| D3 | 2.1 + 2.2 | 45 分 | 三档价格卡草稿（只写价值与计量单位，不写数字） |
| D4 | 2.3 + 2.5（第 4 章） | 60 分 | 付费意愿四问，插入访谈末尾 |
| D5 | 3.4 Shape Up（第 1–3 章） | 60 分 | 6 周 cycle 排期表 + 砍功能清单 |
| D6 | 4.1 + 4.6 | 45 分 | 申请/参赛材料对照表（缺什么一目了然） |
| D7 | 6.1 + 6.6 | 60 分 | 交接协议 v1 的 5 个字段 + 3 个风险拦截点 |

> 纪律：读完不产出，就等于没读。任何一条读完 48 小时没有动作，先标「暂缓」，不要继续囤链接。
