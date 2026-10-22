# 独立开发者赚钱真实案例库

> 服务对象：DoubleCheck（DC）· 快慢机。目的不是仰望，是抄作业。
> 核实日期：**2026-10-22**。所有链接当天做过访问检查。
> 口径：收入数字为**公开自述或第三方估算，非审计数据**；找不到就写「未公开」，不猜。
> 汇率：保留原币种；人民币换算只作直觉参考，按 1 USD ≈ 7.1 CNY（2026-10，估算）。

## 先给五条结论

| # | 结论 | 证据 |
|---|---|---|
| 1 | 最早赚到钱的动作，几乎都不是「做产品」，而是「先找到一个具体的人，手工解决一次」 | Tally 前 344 个用户是手动找的；AudioPen 是一周做 4 个、只加码有反应的那个；白描是给女朋友做的；打工人小组件是和朋友／插画师一起做的 |
| 2 | 「被使用」和「被付费」经常背离 | Tailwind 每周安装 1.1 亿次，2026 年收入却跌近 80%；打工人小组件上了 App Store 首页、月留存 50%+，月入仍只有 ¥3,000 |
| 3 | 两人团队最现实的可复制增长只有三种：免费工具／水印、深度内容 SEO、设计伙伴预付款 | Bannerbear + Tally + 沉浸式翻译；ScrapingBee + Starter Story + Plausible；Tally + 打工人小组件 |
| 4 | 专业创作者市场，买断／非自动续费年付比月订阅好卖 | TypingMind 买断起家；AudioPen $99/年不自动续费；白描永久会员；ShipFast 一次性 |
| 5 | 收入会衰减，第二件产品要在第一件还赚钱时就开始 | ShipFast 从峰值 $143,280/月跌到 $3,537/月（−97%）；Tailwind 收入跌近 80%；Marc Lou 靠组合补位 |

> 读法：赶时间只看 **§三（三件可抄的事）**；要论证再看 §二；案例卡是证据，不是故事。

---

## 一、16 个案例

### 1.1 速览表

> 口径图例：**官方**＝公司／创始人公开披露；**自述**＝创始人在 X、博客、访谈中的说法；**第三方**＝外部估算或转述；**未公开**＝找不到可靠数字。所有数字都不是审计数据。

| # | 产品 | 类型 | 公开收入（年份／口径） | 第一个用户／第一笔钱 | 适用度 |
|---|---|---|---|---|---|
| 1 | Nomad List／Nomads.com | 社区 + 数据库 | 单产品未公开；全组合 $200K–$250K/月（2026，创始人自述）；累计付费会员 43,252（自述） | 2014 年先做公开城市对比表，再做成网站 | 中 |
| 2 | PhotoAI | AI 写真订阅 | $105K–$138K/月（2025–2026，创始人自述／第三方转述） | 一条 AI 照片推文爆了，第二天上线 | 中 |
| 3 | ShipFast | SaaS 模板买断 | 峰值 $143,280/月（2024-06）；2026-08 近 30 天 $3,537（−97%）；全组合 $89.9K/月（2026-10 官网） | 二十多个产品后，把重复脚手架抽出来卖（$199–$299） | 高 |
| 4 | HeadshotPro | AI 头像 B2C/B2B | 官网累计 $10M+（2026）；第三方估 $300K/月（2025–2026） | 30 天做出，SEO + 联盟 | 中 |
| 5 | TypingMind | AI 聊天前端 | 上线 7 天 $22K（2023）；20 个月做到过去 12 个月 $1M（2024-11 自述）；2026 全组合约 $45K/月（第三方） | OpenAI API 开放后几天做出，Twitter + PH #1 | 高 |
| 6 | Bannerbear | 图片 API | $10K→$20K→$50K MRR（官方）；2026 约 $79K MRR（第三方转述） | 7 个产品 0 收入后全押 API，用免费工具引流 | 高 |
| 7 | Plausible | 开源分析 | $1M ARR（2022，官方）；21,000+ 付费；10 人；无融资无广告 | 一个人做，靠「GA 替代品」内容 + 开源 | 高 |
| 8 | Tailwind UI | 开源 + 付费模板 | 首日 $400K；5 个月 $2M；2020 年 mid-seven figures/年；2026 收入 −80%、裁员 75% | 9 年开源 + 直播写代码，文档即分发 | 高（反面教材） |
| 9 | Starter Story | 内容 + 会员 | $79,342/月（2022-09 自述）；约 $1.1M/年（2024 第三方）；2026 自述 multi-million | 免费访谈 + SEO，再上付费墙 | 高 |
| 10 | ScrapingBee | 抓取 API | 约 $5M ARR（收购时，第三方估）；6–7 人；99% 收入来自 SEO（第三方） | 3 周做出，每月 3–4 篇 30 小时长文 | 高 |
| 11 | Tally | 免费表单 | $5M ARR（2026-04 官方）；$6M ARR + 250 万用户（2026-09 官方）；10 人 | 手动找前 344 个用户；免费层 + 水印 | 高 |
| 12 | AudioPen | 语音转文字 | $15K/月（2025–2026，第三方）；12 小时 MVP | 一周做 4 个，只加码有反应的那个 | 高 |
| 13 | 白描 | OCR 工具 | 未公开；用户 200 万→1000 万+；永久会员 ¥30/¥50 | 给女朋友做读书摘抄工具，上架后被推荐 | 高 |
| 14 | 沉浸式翻译 | 浏览器扩展 | 未公开；3000 万用户；Pro ¥69/月、Max ¥199/月 | 免费扩展 + 四个浏览器商店 + 口碑 | 高 |
| 15 | 打工人小组件 | iOS 小组件 | 月均 ¥3,000+（2025-03 自述）；两人五五分 | 设计差异化 + App Store 首页推荐 | 高（警告） |
| 16 | NuxtPro | 开源模板 + 商业版 | ¥1–3 万/月（2026-07 创始人受访自述） | X 公开构建 + 社群 + 联合宣发 | 高 |

> 中国案例说明：1c7 的 [chinese-independent-developer](https://github.com/1c7/chinese-independent-developer) 清单收录项目很多，但绝大多数不公开收入。本文只选有公开数字或官方用户数的 4 个：白描、沉浸式翻译、打工人小组件、NuxtPro。

---

### 1.2 案例卡

#### 1. Nomad List／Nomads.com（Pieter Levels）

| 项 | 内容 |
|---|---|
| 做什么 | 数字游民城市数据库 + 付费社区，后来改名 Nomads.com；2026-09 起改为 $1 注册 + 赞助模式 |
| 公开收入 | 单产品收入未公开。创始人 2026-09 自述：全组合营收稳定在 **$200K–$250K/月**，利润率约 **94.5%**；Nomads 累计付费会员 **43,252**（2014–2026，自述） |
| 起步 | 2014 年为了解决自己「去哪座城市住」的问题，先做一个「最便宜城市排行榜」；上线第一天就盈利，而且商业模式是上线后才发现的——有人要在上面挂招聘广告。它诞生于「12 个月做 12 个产品」挑战期间（2014-07） |
| 最值得抄的一个做法 | 下周做一张「直播交接断点表」：10 行，列是 时间点／谁在说话／AI 该做什么／人该做什么／断在哪。发到 3 个创作者群，请每人补 3 行。有人补＝刚需；没人补＝换场景。补表的人直接进访谈名单 |
| 对我们的适用度 | **中** —— 「先公开一张表」零成本、下周可做；但社区＋赞助模式依赖 12 年品牌，不能抄 |
| 来源 | [levels.io 全组合收入](https://levels.io/passed-10m-revenue-investment-gains)｜[Nomads 转免费](https://levels.io/nomads-com-free-after-a-decade)｜[MVP 方法](https://levels.io/how-i-build-my-minimum-viable-products)｜[项目总表](https://levels.io/projects)｜[Wired 2014 报道（排行榜、首日盈利）](https://www.wired.com/2014/08/12-startups-in-12-months/) |

#### 2. PhotoAI（Pieter Levels）

| 项 | 内容 |
|---|---|
| 做什么 | AI 写真／头像生成，订阅制；从高开低走的 AvatarAI 转向更聚焦的「真人照片」 |
| 公开收入 | **$105K–$138K/月**（2025–2026 不同月份，创始人自述／第三方转述）；2026-03 转述其 X 简介为 **$112K/月** |
| 起步 | 2022-09 先用模型给自己生成照片，发推文爆了；第二天就上线产品。先有传播，再有产品 |
| 最值得抄的一个做法 | 下周用 DC 真跑一场 30 分钟直播复盘，把「介入前／介入后」两版简报截图（脱敏）做成一条对比贴；文末只放一个「我也想要一场」的预约入口，不放功能列表 |
| 对我们的适用度 | **中** —— 「成品即广告」可抄；但它依赖模型出片效果和现成受众，不是纯流程能补 |
| 来源 | [第三方收入转述 $112K](https://www.thestartupstorys.com/2026/03/ai-headshot-business-startup-story.html)｜[VibeCoderHQ 榜单 $105K](https://vibecoderhq.com/success-stories/pieter-levels-photo-ai)｜[第三方估算 $132–138K](https://getburnrate.io/blog/solo-developer-ai-superpowers-one-person-startups)｜[项目总表](https://levels.io/projects) |

#### 3. ShipFast（Marc Lou）

| 项 | 内容 |
|---|---|
| 做什么 | Next.js + Stripe + Auth 的 SaaS 脚手架，一次性买断（$199–$299） |
| 公开收入 | 峰值 **$143,280/月**（2024-06，公开自述／第三方引用）；2026-08 近 30 天 **$3,537**，较峰值 **−97%**；2026-10 官网显示 **$1.7K/月**；Marc 全组合 **$89.9K/月**（2026-10 官网实时） |
| 起步 | 先公开做了二十多个产品、多数没赚到钱，把反复重搭的脚手架抽出来卖；买家是看了他两年发布的人 |
| 最值得抄的一个做法 | 下周把 DC 内部已在用的「交接协议 v0.1」整理成一页 PDF + 3 个模板（直播前／直播中／直播后），定价 **¥299 一次买断**，只卖给访谈过的 10 个人；不建站，先用微信／邮件人工交付 |
| 对我们的适用度 | **高** —— 我们已经有内部工具，打包即可卖；但要接受它会衰减，别把它当终局 |
| 来源 | [marclou.com 实时收入](https://marclou.com/)｜[2026 衰减报道](https://greyjournal.net/hustle/grow/how-much-do-indie-hackers-make-2026/)｜[ShipFast 拆解](https://www.ideaindex.so/case-studies/shipfast) |

#### 4. HeadshotPro（Danny Postma）

| 项 | 内容 |
|---|---|
| 做什么 | AI 职业头像，个人套餐 + 团队／企业版 |
| 公开收入 | 官网：**累计收入 $10M+**（2026）；第三方估算 **约 $300K/月**（2025–2026） |
| 起步 | 2023 上线，30 天做出；前两周收入 $100K（第三方）；增长主要靠 SEO 和联盟，不靠投放 |
| 最值得抄的一个做法 | 下周写 **1 篇**「直播参谋台替代方案」对比页：提词器／真人助理／剪辑师／DC 四栏，写清价格、延迟、谁做决定、出错谁兜底；文末放设计伙伴 CTA。先写 1 篇，不要建 20 篇 |
| 对我们的适用度 | **中** —— SEO／联盟是 12 个月工程，两人团队只能先做 1 篇验证，不能当 30 天救命稻草 |
| 来源 | [HeadshotPro 官方 About](https://www.headshotpro.com/about)｜[第三方收入估算](https://vibecoderhq.com/success-stories/danny-postma-headshotpro)｜[Starter Story 拆解](https://www.starterstory.com/stories/headshotpro-breakdown)｜[前两周 $100K（第三方）](https://www.epirus.vc/blog/how-ai-is-creating-the-next-generation-of-founders) |

#### 5. TypingMind（Tony Dinh）

| 项 | 内容 |
|---|---|
| 做什么 | 自带 API Key 的多模型聊天前端；个人买断 + 团队订阅（TypingMind Custom 白标） |
| 公开收入 | 上线 **7 天 $22K**（2023，创始人自述）；**20 个月做到过去 12 个月累计 $1M**（2024-11 创始人 newsletter）；2026 第三方快照全组合约 **$45K/月** |
| 起步 | OpenAI API 开放后几天做出，Twitter + Product Hunt 第一；先卖 $39／$79／$99 买断，后加团队订阅，拿到 3,000 席大单 |
| 最值得抄的一个做法 | 下周把 Pro 改成「**买断 ¥999/年 + 不自动续费**」，报价单上写「到期前 7 天提醒，不自动扣款」；只对前 10 个设计伙伴试，记录接受率 |
| 对我们的适用度 | **高** —— 买断降低首单决策，适合大陆创作者；团队版等有 3 家设计伙伴后再加 |
| 来源 | [创始人 $1M newsletter](https://news.tonydinh.com/p/nov-2024-my-first-million)｜[2026 全组合快照](https://tycoon.us/one-person-company/tony-dinh)｜[买断页拆解](https://aihustlepath.com/typingmind-business-model-case-study/) |

#### 6. Bannerbear（Jon Yongfook）

| 项 | 内容 |
|---|---|
| 做什么 | 图片／视频／PDF 自动生成 API + 模板编辑器，服务营销与电商 |
| 公开收入 | 官方里程碑：**$10K MRR** → **$20K MRR** → **$50K MRR**（2023-07 官方博客）；2026 自述约 **$79K MRR**（第三方转述其 X 简介） |
| 起步 | 辞职后 12 个月做 7 个产品、0 收入；聚焦图片生成；2020-03 全押 API；用自家 API 做免费工具引流；在 Indie Hackers／Product Hunt 公开每一步 |
| 最值得抄的一个做法 | 下周上线一个免费「交接简报生成器」：8 个问题 → 一页 PNG；页脚固定「Made with DoubleCheck · 交接协议 v0.1」；不登录、不收费、留邮箱拿模板 |
| 对我们的适用度 | **高** —— 免费工具是我们唯一不花钱的分发，而且工具本身就是协议演示 |
| 来源 | [官方 Open Startup](https://www.bannerbear.com/open/)｜[0→$10K MRR 复盘](https://www.bannerbear.com/journey-to-10k-mrr/)｜[7 条做到 $50K MRR](https://www.bannerbear.com/blog/7-lessons-growing-a-bootstrapped-saas-to-50k-mrr/)｜[2026 约 $79K MRR（第三方转述）](https://m.zhiding.cn/article/3186405.htm) |

#### 7. Plausible Analytics（Uku Taht）

| 项 | 内容 |
|---|---|
| 做什么 | 开源、无 Cookie、隐私友好的网站分析；自托管免费，云托管订阅 |
| 公开收入 | **$1M ARR**（2022 跨过，官方）；**21,000+ 付费订阅**；团队 **10 人**；无融资、无广告、无联盟（官方） |
| 起步 | 2018-12 一个人开始做，2019 上线付费；2020 加营销合伙人；靠「Google Analytics 替代品」内容、开源透明和口碑增长 |
| 最值得抄的一个做法 | 下周把 DC 的一句话定位改成「×× 的替代品」句式，写 3 个候选：提词器替代／直播助理替代／会后剪辑替代；拿 10 个创作者做二选一，把赢的那个放到官网首屏 |
| 对我们的适用度 | **高** —— 「替代品」是最省力的搜索入口；但我们的品类搜索量还很小，需要内容造需求 |
| 来源 | [Plausible 官方 About](https://plausible.io/about)｜[官方首页数据](https://plausible.io/)｜[早期开源 SaaS 复盘](https://plausible.io/blog/open-source-saas) |

#### 8. Tailwind UI／Tailwind Plus（Adam Wathan）

| 项 | 内容 |
|---|---|
| 做什么 | 开源 CSS 框架 + 付费组件／模板库；2026-09 加入 Shopify，停止新付费用户 |
| 公开收入 | 首发日 **$400K**；5 个月 **$2M**；2020 年 **mid-seven figures/年**（创始人年复盘）；2026-01 自述收入跌近 **80%**、文档流量较 2023 初跌 **40%**、裁掉 **75%** 工程团队；2026-09 官方宣布加入 Shopify |
| 起步 | 2017 起开源 + 长期直播写代码；文档就是分发渠道；2020-02 上线付费模板，首日 $400K |
| 最值得抄的一个做法 | 下周盘点 DC 的分发资产：邮箱列表／微信群／B站／小红书／GitHub star，各写一个数字。一个都没有，就先别做付费墙；先做 4 周内容攒 100 个邮箱 |
| 对我们的适用度 | **高（反面教材）** —— 不能把「被使用」当「被付费」；必须自建直接渠道，不能把文档／平台推荐当唯一入口 |
| 来源 | [2020 年复盘](https://adamwathan.me/journal/2020/12/29/2020-year-in-review/)｜[5 个月 $2M](https://adamwathan.me/tailwindcss-from-side-project-byproduct-to-multi-mullion-dollar-business/)｜[加入 Shopify 官方公告](https://tailwindcss.com/blog/tailwind-is-joining-shopify)｜[裁员与 −80% 报道](https://36kr.com/p/3630336479183876) |

#### 9. Starter Story（Pat Walls）

| 项 | 内容 |
|---|---|
| 做什么 | 创始人访谈案例库 + 付费会员／课程／赞助；把别人的收入数字做成内容 |
| 公开收入 | **$79,342/月**（2022-09 创始人 Reddit 自述）；约 **$1.1M/年**（2024 第三方拆解）；2026 自述「multi-million」；250K newsletter、10K+ 付费会员（自述） |
| 起步 | 2017 起步，先免费访谈 + SEO；内容本身是营销循环，后来加付费墙、赞助、课程 |
| 最值得抄的一个做法 | 下周把 3 个访谈做成 3 张「案例卡」：背景／原来怎么做／用了 DC 后／数字／原话，每张 300 字，发同一个专栏；每张末尾放「你也可以被写进这个专栏」的预约链接 |
| 对我们的适用度 | **高** —— 两人团队可做；案例既是内容又是销售材料，还能反向换来更多访谈 |
| 来源 | [第三方拆解与 $79K 出处](https://growthinreverse.com/starter-story/)｜[VibeCoderHQ 收入页](https://vibecoderhq.com/success-stories/pat-walls-starter-story)｜[Starter Story 官网](https://www.starterstory.com/) |

#### 10. ScrapingBee（Pierre de Wulf / Kevin Sahin）

| 项 | 内容 |
|---|---|
| 做什么 | 网页抓取 API，处理 headless 浏览器、代理轮换、反爬 |
| 公开收入 | 收购时约 **$5M ARR**（第三方估算）；团队 **6–7 人**；**99% 收入来自 SEO**（第三方拆解）；已并入 Oxylabs（ScrapingBee 官方公告，2026-01-19） |
| 起步 | 3 周做出 MVP；每月 3–4 篇深度 SEO 长文，每篇约 30 小时，坚持多年，做成「网页抓取」领域第二大的博客 |
| 最值得抄的一个做法 | 下周定一个「每月 3 篇、每篇 30 小时」的排期，只写一个母题：「直播时 AI 该闭嘴还是该说话」；3 个角度：翻车复盘／交接清单／工具对比。写完第 1 篇再排第 2 篇 |
| 对我们的适用度 | **高** —— 两人可执行；但起量要 12 个月，不能当 30 天救命稻草 |
| 来源 | [ScrapingBee 被收购官方公告](https://www.scrapingbee.com/blog/scrapingbee-acquisition/)｜[收购与 $5M ARR 拆解](https://www.ideaindex.so/case-studies/scrapingbee) |

#### 11. Tally（Marie Martens / Filip Minev）

| 项 | 内容 |
|---|---|
| 做什么 | 免费表单 builder；免费层极慷慨，另有 Pro 订阅 |
| 公开收入 | **$5M ARR**（2026-04 官方）；**$6M ARR + 250 万用户 + 10 人**（2026-09 官方）；完全 bootstrapped |
| 起步 | 2020 从失败的旅行项目转做表单；手动去 Product Hunt、Twitter、社区找前 344 个用户，2020-11 只有 **$119 MRR**；免费层 + 「Made with Tally」水印形成循环；2025 年起 ChatGPT 推荐激增，2026 年成为最大来源（第三方） |
| 最值得抄的一个做法 | 下周给免费版加一个不能关的水印：「由 DoubleCheck 交接协议生成 · 15 分钟搭一场」；每份导出带可追踪链接；先测 20 份导出里有多少人点回官网 |
| 对我们的适用度 | **高** —— 水印是零成本分发；但我们的产品不是天然病毒，别期待 Tally 的循环 |
| 来源 | [$6M ARR 官方](https://blog.tally.so/6-years-in-6-million-far/)｜[$5M ARR 官方](https://blog.tally.so/the-road-from-4m-to-5m-arr/)｜[早期 344 用户与 $119 MRR 拆解](https://okara.ai/blog/tally-revenue-growth) |

#### 12. AudioPen（Louis Pereira）

| 项 | 内容 |
|---|---|
| 做什么 | 语音笔记 → 结构化文字；$99/年 或 $159/2 年，**非自动续费** |
| 公开收入 | **$15K/月**（2025–2026，Starter Story／第三方）；MVP 在 **12 小时**内做出 |
| 起步 | 一周做 4 个小产品，发 Twitter；只有 AudioPen 有反应，就加码它；12 小时做出 MVP，边做边公开，beta 用户当场付费 |
| 最值得抄的一个做法 | 下周把「直播后 10 分钟出简报」做成一个 1 页固定模板（不是功能），用 3 场真实直播手动跑；记录「从下播到拿到简报」的分钟数，把分钟数写进报价单 |
| 对我们的适用度 | **高** —— 极窄场景 + 非自动续费，正对大陆创作者；12 小时 MVP 也适合我们两人节奏 |
| 来源 | [Starter Story 数据转述（含 12 小时视频与定价原话）](https://www.betterlaunch.co/playbooks/lewis-audiopen-5) |

#### 13. 白描（陶新乐）

| 项 | 内容 |
|---|---|
| 做什么 | 拍照 OCR、表格识别、文件扫描、翻译；多平台；永久会员 |
| 公开收入 | **未公开**。用户 **200 万**（2019 爱范儿专访）→ **1000 万+**（2022 华为云案例）；永久会员 **¥18→¥30、¥40→¥50**（官方调价公告，年份未标注） |
| 起步 | 为女朋友读书摘抄做的小工具；上架 App Store 后被首页推荐、获多个应用市场年度奖；靠口碑和商店推荐 |
| 最值得抄的一个做法 | 下周把 DC 砍到只剩一个动词：「把一场直播变成一份能带走的简报」；官网只留 3 屏：输入（直播链接／录音）／输出（简报样例）／价格（买断）；其他全删 |
| 对我们的适用度 | **高** —— 单场景 + 买断 + 低客服；但收入上限低，别指望它养两人 |
| 来源 | [爱范儿 2019 专访（200 万用户）](https://www.ifanr.com/app/1257045)｜[华为云 2022 案例（1000 万+ 用户）](https://juejin.cn/post/7156431429780865032)｜[官方调价公告](https://baimiao.uzero.cn/article_detail/id/5.html) |

#### 14. 沉浸式翻译（Owen）

| 项 | 内容 |
|---|---|
| 做什么 | 双语网页／PDF／电子书／视频字幕翻译浏览器扩展；免费 + Pro／Max 订阅 |
| 公开收入 | **未公开**。官方称 **3000 万用户**；Pro **¥69/月**、Max **¥199/月**；年付 **¥588／¥1599**；联盟佣金 20% |
| 起步 | 免费扩展，主打「双语对照」；上 Chrome／Edge／Safari／Firefox 四个商店；发布 5 个月 40 万用户；创始人推文 + 口碑 |
| 最值得抄的一个做法 | 下周做一个「直播交接」浏览器插件最小版：直播后台侧边栏显示「当前该人接管／AI 继续跑」两色状态条 + 一键生成简报；先只支持一个平台（B站或抖音），上架商店 |
| 对我们的适用度 | **高** —— 商店分发 + 免费 + Pro 是两人可复制的；但需要 3000 万级用户才成立，早期只能当获客入口 |
| 来源 | [官方定价页（3000 万用户）](https://immersivetranslate.com/zh-Hans/pricing/)｜[会员条款（价格）](https://immersivetranslate.com/zh-Hans/docs/MEMBERSHIP-TERMS/)｜[官方介绍](https://immersivetranslate.com/zh-TW/docs/) |

#### 15. 打工人小组件（lacklock／富贵 + 大点）

| 项 | 内容 |
|---|---|
| 做什么 | iOS 下班倒计时小组件 + 插画主题；永久会员 ¥24（最初） |
| 公开收入 | **月均 ¥3,000+**（2025-03 创始人 V2EX 自述）；两人五五分，每人约 ¥1,000+；全职两年；上过 App Store 首页推荐；月留存 50%+ |
| 起步 | 选 iOS 新特性 + 设计差异化；与插画师合作；上架后被 App Store 本周精选／首页推荐；但几乎没有运营推广 |
| 最值得抄的一个做法 | 下周把「设计差异化」换成「交付差异化」：给每个设计伙伴做一份带她名字／直播间封面的简报模板，而不是通用模板；同时第一天就收费（哪怕 ¥99 定金），用付费筛真需求 |
| 对我们的适用度 | **高（作为警告）** —— 被推荐 ≠ 能赚钱；我们不能只靠产品好，必须同时有定价和获客 |
| 来源 | [V2EX 两年复盘原文](https://v2ex.com/t/1121385) |

#### 16. NuxtPro（Kevin）

| 项 | 内容 |
|---|---|
| 做什么 | Nuxt3 SaaS 出海模板；开源版免费，商业版解锁完整功能 |
| 公开收入 | **¥1–3 万/月**（2026-07 创始人受访自述）；MVP **1 周**；GitHub **120 star**；DR 26 |
| 起步 | 为学 Nuxt 而做，发现 Next.js 模板多、Nuxt 少；在 X 上 build in public + 社群运营；与非竞品独立开发者联合宣发；付费版卖完整功能 |
| 最值得抄的一个做法 | 下周把「交接协议 v0.1」开源到 GitHub（只放 spec + 3 个模板），商业版卖「直播参谋台 + 复盘 + 30 天陪跑」；README 顶部放设计伙伴申请表 |
| 对我们的适用度 | **高** —— 与 DC「协议公开、产品收费」最像；但 ¥1–3 万/月是天花板提醒，不是目标 |
| 来源 | [独立开发前线 2026-07 专访](https://indiefront.cn/articles/cmrhtlq0q001b9zthgsjkjd7x/) |

---

## 二、模式归纳（8 条）

| # | 模式 | 具体做法 | 证据（2–3 个案例） | 对我们的意思 |
|---|---|---|---|---|
| 1 | **先卖再建** | 先用一张表、一次手工交付、一份报价单换到真钱，再决定要不要写代码 | Nomad List 先做公开的城市排行榜；AudioPen 一周做 4 个、只加码有反应的那个；Tally 手动找前 344 个用户，先有 $119 MRR | 我们先卖「一场直播的参谋台」服务，不卖 SaaS；预付款到账再写功能 |
| 2 | **单一场景做到极窄** | 一个产品只回答一个问题，官网只留一个动词 | 白描＝拍照取字；AudioPen＝说话变文字；PhotoAI＝职业头像；TypingMind＝更好的聊天前端 | DC 只做「直播时什么时候该人接管」；五层光谱是解释，不是功能清单 |
| 3 | **免费层／免费工具自带分发** | 免费版可用，但每一份产出都带水印或回链 | Tally 的「Made with Tally」；Bannerbear 用自家 API 做免费工具；沉浸式翻译免费扩展 + 商店；Plausible 开源可自托管 | 免费简报生成器 + 不可关水印，是我们唯一零成本的分发 |
| 4 | **公开构建换流量（有条件）** | 把失败、数字、决策过程公开，形成「追更」关系，再卖产品 | Marc Lou 公开二十多个产品、多数失败后才卖 ShipFast；Levels 公开 12 年、100+ 项目；NuxtPro 在 X 日更 + 社群 | 我们没有受众，公开构建只能当「记录」，不能当「渠道」；先攒 100 个真实读者 |
| 5 | **买断 vs 订阅要混搭** | C 端／专业个人卖买断或非自动续费年付；团队／企业卖订阅 | TypingMind 买断起家后加团队订阅；AudioPen $99/年不自动续费；白描永久会员；ShipFast 一次性 | Pro 卖买断／年付不自动续费，Team 卖席位订阅；先别做自动续费月付 |
| 6 | **按「替代什么」定价，不按功能定价** | 锚定用户现在付的那笔钱：摄影师、ChatGPT Plus、翻译公司、助理 | HeadshotPro 锚专业摄影师；TypingMind 锚 ChatGPT Plus；白描锚昂贵 OCR 会员 | DC 锚「提词器 + 直播助理 + 剪辑师」三项月支出，不锚「AI 功能多少个」 |
| 7 | **收入会衰减，靠组合续命** | 第一件产品见顶前就上第二件；或从个人客群换到团队客群 | ShipFast 峰值后 −97%，Marc 靠 DataFast／TrustMRR 补位；Tailwind 收入 −80% 后加入 Shopify；Levels 靠组合稳定在 $200K–$250K/月 | 直播参谋台见顶前，就要准备「团队版／交接协议授权」第二条收入 |
| 8 | **开源核心 + 商业版／托管收费** | 协议／核心公开换信任和分发，钱收在托管、团队协作、陪跑上 | Plausible 开源自托管 + 云订阅；NuxtPro 开源版 + 商业版；Tailwind 开源框架 + 付费模板 | 交接协议 spec 公开，参谋台产品收费；这正好是我们的叙事 |

> 一条反模式：**只靠「产品好」**。打工人小组件有 App Store 首页推荐、50%+ 月留存、两年全职，月入仍只有 ¥3,000。产品好是入场券，不是收入。

---

## 三、对我们能直接抄的三件事（30 天）

> 约束：两人、无收入、大陆主体、不追盈利但必须先拿到钱。三件事只围绕「能收到钱」和「能拿到用户」，不扩产品功能。

### 3.1 谈 3 个、成 1 个「直播参谋台设计伙伴包」

| 项 | 内容 |
|---|---|
| 做什么 | 不卖 SaaS 试用，卖一次**人工交付**：一场直播的参谋台 + 一份交接复盘。报价 **¥3,000／场** 或 **¥8,000／3 场**，预付 50%。目标 10 个直播／口播创作者访谈，出 3 份报价，至少 1 笔到账 |
| 参考哪个案例 | **Tally**（手动找前 344 个用户，先有 $119 MRR）＋ **打工人小组件**（第一天就收费）＋ **TypingMind**（买断降低决策） |
| 验收标准 | ① 10 份访谈摘要（每份 5 行以内，含「上次直播卡在哪」原话）；② 3 份报价单；③ **≥1 笔预付款到账 ≥¥3,000**；④ 1 份可公开的匿名案例，含「介入次数／下播到出简报分钟数」前后对比 |
| 不做什么 | 不做免费试用、不做 7 天无条件退款、不做「先做出来再找客户」；不承诺全自动 |
| 为什么是这件事 | 设计伙伴预付款是最硬的验证：客户在没成品时先给钱；这也是所有案例里最不依赖受众、最不依赖 SEO、30 天内就能验证的路径 |

### 3.2 上线「交接简报」免费生成器，导出带水印

| 项 | 内容 |
|---|---|
| 做什么 | 一个不登录的网页工具：8 个问题（谁在回路／何时介入／交接物／验收标准／最坏情况／回滚方式／记忆归谁／下次怎么复用）→ 一页 PNG 简报。页脚固定「Made with DoubleCheck · 交接协议 v0.1」，留邮箱领 3 个直播模板 |
| 参考哪个案例 | **Bannerbear**（用自家 API 做免费工具引流）＋ **Tally**（Made with Tally 水印）＋ **白描**（一个动词：拍照取字） |
| 验收标准 | ① 7 天内上线；② 30 天内 **100 次真实导出**（不是访问量）；③ ≥5 个留下联系方式；④ ≥3 个导出者愿意接 15 分钟访谈；⑤ 水印回链可追踪，能说出带来多少官网点击 |
| 不做什么 | 不做账号体系、不做付费墙、不做多平台适配；只做一个页面、一个导出格式 |
| 为什么是这件事 | 免费工具是两人团队唯一不花钱的分发；而且工具本身就是「交接协议」的可感知演示，比 3 分钟视频更容易被转发 |

### 3.3 用「五层光谱」做 4 篇公开诊断 + 1 张可截图诊断表

| 项 | 内容 |
|---|---|
| 做什么 | 连续 4 周、每周 1 篇，对象是直播／口播创作者。固定结构：一场真实直播的 5 个断点 → 用 L0–L4 标注 → 如果重来怎么交接 → 附一张可截图的诊断表。发 2 个主阵地（B站 + 公众号／小红书二选一），每篇结尾 CTA「预约 15 分钟诊断」 |
| 参考哪个案例 | **ScrapingBee**（每月 3–4 篇、每篇 30 小时）＋ **Starter Story**（案例即 SEO）＋ **Plausible**（「替代品」定位） |
| 验收标准 | ① 4 篇按时发布；② 至少 1 篇被 3 个创作者转发或引用；③ 30 天内带来 **30 个诊断预约**（或 10 个访谈）；④ 每篇带 UTM，能说出哪一篇带来第一笔预付款；⑤ 诊断表被下载／保存 ≥50 次（用短链或下载事件统计） |
| 不做什么 | 不写「AI 思考速度」概念文、不做行业综述、不追求涨粉；只写「某场直播的具体断点」 |
| 为什么是这件事 | 五层光谱是我们的解释框架，但创作者不会为框架付费，只会为「我这场直播怎么不翻车」点进来；内容是把框架变成询盘的最低成本方式 |

### 3.4 一页带走

| 如果只记三件事 | 具体动作 |
|---|---|
| **先收钱** | 30 天内谈 3 个、成 1 个 ¥3,000 的直播参谋台设计伙伴包，预付 50%；到账再写功能 |
| **做窄** | 官网只回答一个问题：「直播时，AI 什么时候该闭嘴、什么时候该叫人」 |
| **留水印** | 免费简报生成器，每份导出带「Made with DoubleCheck · 交接协议 v0.1」和回链 |

---

## 四、抄不了的

| 案例 | 它依赖的条件 | 我们没有 | 硬抄会怎样 |
|---|---|---|---|
| Pieter Levels／Nomad List | 数十万级 X 受众（2026 年第三方转述约 84 万）、12 年公开构建、100+ 项目试错、欧美支付通道、个人品牌 | 没有受众、没有 12 年、没有海外收款 | 「一条推文上线」会变成 0 阅读；社区＋赞助模式更无从谈起 |
| Marc Lou／ShipFast | 二十万级 Twitter、十万级 YouTube（第三方拆解）、27+ 个产品且多数失败、Product Hunt Maker of the Year、两年公开演示同一套代码 | 没有受众、没有两年公开代码史 | 做同样的模板，卖不出第一单；而且它本身已从峰值跌 97%，抄的是正在退潮的品 |
| Danny Postma／HeadshotPro | 20+ AI 产品经验、早期 OpenAI 访问、成熟 SEO 域名、联盟网络、巴厘岛成本结构 | 没有 SEO 权重、没有联盟军团、没有模型优势 | 写 20 篇 SEO 也起不来；联盟没人愿意推冷产品 |
| Tailwind UI | 110M 次/周安装、9 年文档分发、完整工程团队 | 没有开源用户、没有文档流量 | 把「被使用」当「被付费」，做完发现没人买；而且 AI 正在吃掉这条文档漏斗 |
| Starter Story | 4,000+ 访谈、160 万粉丝、25 万 newsletter、2017 年开始的内容复利 | 没有内容资产、没有 8 年 | 做 4 篇案例就期待订阅，会饿死 |
| ScrapingBee | 99% 收入来自 SEO、每篇 30 小时、多年域名权重 | 没有域名权重、没有 12 个月现金流 | 写 3 篇没排名就放弃，或把 SEO 当 30 天救命稻草 |
| Tally | 表单天然病毒（每张表单都是广告）、250 万用户、10 人团队 | 产品没有天然病毒循环 | 以为加个水印就能自增长；实际水印只能带来少量回链 |
| Plausible | 「Google Analytics 替代品」巨大搜索需求、隐私监管顺风、开源社区 | 品类搜索量接近 0、没有监管顺风 | 写「DC 替代品」没人搜；需要先造需求，不能只做 SEO |
| 白描／沉浸式翻译 | App Store／Chrome 商店海量分发、1000 万／3000 万用户、消费级市场 | 没有商店推荐、没有海量 C 端 | 用消费级免费策略做 B2B 窄市场，付费率会低到无法覆盖成本 |
| 打工人小组件 | App Store 编辑推荐（含运气）、3 人设计团队、50%+ 留存 | 没有编辑推荐、没有插画师全职 | 抄它＝抄一个「月入 ¥3,000、两年后放弃」的结果 |
| NuxtPro | Vue 生态、X 受众、¥1–3 万/月的低客单 | 没有 Vue 生态受众、没有模板货架 | 把「月入 1–3 万」当目标，会低估 DC 需要的交付深度 |
| 所有用 Stripe／Paddle／App Store 收款的案例 | 海外主体、Stripe 账户、应用商店开发者账号 | 大陆主体、收款路径待确认 | 直接照抄定价页会卡在收款；必须先确认收款路径再谈增长 |

> 一句话：**能抄的是动作，不是条件。** 动作＝先收钱、做窄、加水印、写案例；条件＝受众、域名权重、平台推荐、海外收款。

---

## 五、数据来源与核实日期

> 核实日期：**2026-10-22**。以下链接当天逐条检查；收入数字为公开自述或第三方估算，**非审计数据**。
> 少数站点（V2EX、Grey Journal、The Startup Storys、Tally 博客）对脚本请求偶发返回 000，但用浏览器或抓取工具可正常打开；相关页面已用 WebFetch／搜索抓取实际读取内容后才引用。

| # | 来源 | 链接 | 支撑 |
|---|---|---|---|
| 1 | Pieter Levels：全组合收入与利润率（2026-09-23） | https://levels.io/passed-10m-revenue-investment-gains | 案例 1 |
| 2 | Pieter Levels：Nomads 转免费、43,252 付费会员（2026-09-05） | https://levels.io/nomads-com-free-after-a-decade | 案例 1 |
| 3 | Pieter Levels：MVP 方法（2014-09-02） | https://levels.io/how-i-build-my-minimum-viable-products | 案例 1 |
| 4 | Pieter Levels：项目总表（更新 2026-10-03） | https://levels.io/projects | 案例 1、2 |
| 5 | PhotoAI 收入转述（2026-03） | https://www.thestartupstorys.com/2026/03/ai-headshot-business-startup-story.html | 案例 2 |
| 6 | VibeCoderHQ：PhotoAI 榜单 | https://vibecoderhq.com/success-stories/pieter-levels-photo-ai | 案例 2 |
| 7 | Marc Lou 实时收入页 | https://marclou.com/ | 案例 3 |
| 8 | 2026 独立开发者收入与 ShipFast 衰减（2026-10-15） | https://greyjournal.net/hustle/grow/how-much-do-indie-hackers-make-2026/ | 案例 3 |
| 9 | ShipFast 拆解（$1.23M 累计等） | https://www.ideaindex.so/case-studies/shipfast | 案例 3 |
| 10 | HeadshotPro 官方 About（累计 $10M+） | https://www.headshotpro.com/about | 案例 4 |
| 11 | HeadshotPro 第三方收入估算 | https://vibecoderhq.com/success-stories/danny-postma-headshotpro | 案例 4 |
| 12 | Starter Story 官方拆解（HeadshotPro） | https://www.starterstory.com/stories/headshotpro-breakdown | 案例 4 |
| 13 | Tony Dinh：$1M/12 个月（2024-11-22） | https://news.tonydinh.com/p/nov-2024-my-first-million | 案例 5 |
| 14 | Tony Dinh：2026 全组合快照（2026-04-17） | https://tycoon.us/one-person-company/tony-dinh | 案例 5 |
| 15 | TypingMind 买断模式拆解 | https://aihustlepath.com/typingmind-business-model-case-study/ | 案例 5 |
| 16 | Bannerbear 官方 Open Startup | https://www.bannerbear.com/open/ | 案例 6 |
| 17 | Bannerbear：0→$10K MRR 复盘 | https://www.bannerbear.com/journey-to-10k-mrr/ | 案例 6 |
| 18 | Bannerbear：7 条做到 $50K MRR | https://www.bannerbear.com/blog/7-lessons-growing-a-bootstrapped-saas-to-50k-mrr/ | 案例 6 |
| 19 | Plausible 官方 About（$1M ARR、21k 付费、10 人） | https://plausible.io/about | 案例 7 |
| 20 | Plausible 官方首页数据 | https://plausible.io/ | 案例 7 |
| 21 | Plausible 早期开源 SaaS 复盘 | https://plausible.io/blog/open-source-saas | 案例 7 |
| 22 | Adam Wathan 2020 年复盘（$400K 首日、mid-seven figures） | https://adamwathan.me/journal/2020/12/29/2020-year-in-review/ | 案例 8 |
| 23 | Tailwind UI：5 个月 $2M | https://adamwathan.me/tailwindcss-from-side-project-byproduct-to-multi-mullion-dollar-business/ | 案例 8 |
| 24 | Tailwind Labs 加入 Shopify（官方，2026-09-09） | https://tailwindcss.com/blog/tailwind-is-joining-shopify | 案例 8 |
| 25 | Tailwind 裁员 75%、收入 −80% 报道（2026-01-08） | https://36kr.com/p/3630336479183876 | 案例 8 |
| 26 | Starter Story 第三方拆解（$79,342/月、$1.1M/年） | https://growthinreverse.com/starter-story/ | 案例 9 |
| 27 | Starter Story 收入页（$83,333/月口径） | https://vibecoderhq.com/success-stories/pat-walls-starter-story | 案例 9 |
| 28 | ScrapingBee 被收购官方公告 | https://www.scrapingbee.com/blog/scrapingbee-acquisition/ | 案例 10 |
| 29 | ScrapingBee：$5M ARR、99% SEO、6 人 | https://www.ideaindex.so/case-studies/scrapingbee | 案例 10 |
| 30 | Tally：$6M ARR、250 万用户（2026-09-22） | https://blog.tally.so/6-years-in-6-million-far/ | 案例 11 |
| 31 | Tally：$5M ARR（2026-04-15） | https://blog.tally.so/the-road-from-4m-to-5m-arr/ | 案例 11 |
| 32 | Tally：344 用户、$119 MRR 等早期拆解 | https://okara.ai/blog/tally-revenue-growth | 案例 11 |
| 33 | AudioPen：$15K/月、12 小时、非自动续费定价 | https://www.betterlaunch.co/playbooks/lewis-audiopen-5 | 案例 12 |
| 34 | 白描：200 万用户（2019 爱范儿） | https://www.ifanr.com/app/1257045 | 案例 13 |
| 35 | 白描：1000 万+ 用户（2022 华为云） | https://juejin.cn/post/7156431429780865032 | 案例 13 |
| 36 | 白描：永久会员调价公告 | https://baimiao.uzero.cn/article_detail/id/5.html | 案例 13 |
| 37 | 沉浸式翻译：官方定价页（3000 万用户） | https://immersivetranslate.com/zh-Hans/pricing/ | 案例 14 |
| 38 | 沉浸式翻译：会员条款（¥69／¥199 等） | https://immersivetranslate.com/zh-Hans/docs/MEMBERSHIP-TERMS/ | 案例 14 |
| 39 | 沉浸式翻译：官方介绍 | https://immersivetranslate.com/zh-TW/docs/ | 案例 14 |
| 40 | 打工人小组件：两年复盘（¥3,000/月） | https://v2ex.com/t/1121385 | 案例 15 |
| 41 | NuxtPro：创始人专访（¥1–3 万/月） | https://indiefront.cn/articles/cmrhtlq0q001b9zthgsjkjd7x/ | 案例 16 |
| 42 | PhotoAI：$132–138K/月（第三方，2026-03） | https://getburnrate.io/blog/solo-developer-ai-superpowers-one-person-startups | 案例 2 |
| 43 | Wired 2014：NomadList 是排行榜、首日盈利 | https://www.wired.com/2014/08/12-startups-in-12-months/ | 案例 1 |
| 44 | Bannerbear 2026 约 $79K MRR（第三方转述其 X 简介） | https://m.zhiding.cn/article/3186405.htm | 案例 6 |
| 45 | 中国独立开发者清单（项目多、公开收入少） | https://github.com/1c7/chinese-independent-developer | 中国案例选取说明 |

### 核实中发现的口径差异（必须保留）

| 事项 | 核实结果 | 本文怎么处理 |
|---|---|---|
| Nomad List 单产品收入 | 第三方快照口径差异较大，且 2026-09 已转免费，前后不可比 | 不采用单产品数字；只用创始人全组合 $200K–$250K/月 + 43,252 付费会员 |
| PhotoAI 收入 | 不同月份、不同来源的数字不一致（约 $105K 到 $138K） | 写成区间 $105K–$138K/月，标注自述／转述 |
| Marc Lou 全组合 | 第三方口径差异极大，且统计的产品组合不同 | 只采用官网实时 $89.9K/月 + ShipFast 峰值／衰减两个可追溯数字 |
| Starter Story | $79,342/月（2022 自述）与 $83,333/月（$1M ARR 折算）不同 | 两个都列，注明口径 |
| ScrapingBee 收购时间 | 官方公告日期与第三方数据库记录不一致 | 只写「已并入 Oxylabs」，不写具体成交日 |
| Tailwind 收入 −80%、裁员 75% | 创始人 GitHub 评论／播客自述，非审计 | 明确标「创始人自述」，不写成财报 |
| 白描、沉浸式翻译收入 | 官方从未公布 | 写「未公开」，只列用户数与公开定价 |
| 所有收入数字 | 公开自述或第三方估算，非审计数据 | 全文统一口径，不据此做精确预测 |

> 最后提醒：本库所有案例都是别人的「结果」。能抄的只有他们「第一周做了什么」——找人、收钱、发一张表、写一篇复盘。其余都是条件。
