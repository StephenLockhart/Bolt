# 早期 AI 创业融资模板、内容渠道与脑机接口前景研究报告

检索与交叉验证日期：2026-10-21。证据等级标注：`[CONFIRMED]`（≥3 个独立来源一致）/ `[MAJORITY]`（多数来源一致）/ `[SINGLE-SOURCE]`（单源）/ `[unverified]`（无法核实）。引用格式 `[cite:N]` 对应文末 Sources。

## 执行摘要

1. 融资叙事存在跨市场共识结构：10~14 页、每页只回答一个判断问题、证据优先于形容词、首页只有 20~30 秒机会。中美模板的差异主要在团队页位置与市场分析权重，骨架高度一致。`[CONFIRMED]`
2. 2026 年 AI 创业的门槛发生了反转：纯 deck 与纯原型（Figma）已不足以融资，投资人要的是可交互的 MVP、付费试点或 LOI；行业口号是"Pre-revenue is fine. Pre-signal is not."。`[MAJORITY]`
3. 对"装配层"产品有一条专门的检验："LLM Wrapper Test"——大模型厂商能否在短时间内把它做成免费功能。护城河必须回答"拥有什么大厂没有的东西"。`[MAJORITY]`
4. 公众号没有死，但流量逻辑已重构：公域算法推荐占主导、完读率成为第一权重、搜索与 AI 搜索带来长尾。它适合高客单、深信任、私域转化的定位，不适合泛流量打法。`[MAJORITY]`
5. 脑机接口的现实是分裂的：侵入式已在医疗场景达到接近甚至超过手鼠的意念输入速度（8~11.32 BPS），但消费级植入被业界创始人估为 15~20 年；非侵入式仍在 TRL 3，离线、高错误率。BCI 是愿景页素材，不是近期路线图。`[MAJORITY]`

---

## 1 融资叙事模板的主流结构

### 1.1 两大经典框架：Sequoia 与 Y Combinator

两大框架的骨架高度一致，差异在强调顺序。Sequoia 框架按投资人评估机会的逻辑展开：一句话定位 → 问题 → 方案 → 为什么是现在 → 市场 → 竞争 → 商业模式 → 团队 → 财务 → 愿景。`[cite:1][cite:2]` 其中"Why now（为什么是现在）"是 Sequoia 模板的标志性页面，强迫回答时间窗口问题——这也是资深投资人最先问的问题之一。`[cite:1]`

YC 的 seed deck 在同一 DNA 上把牵引（Traction）提前到第 4 页，其顺序为：标题页 → 问题 → 方案 → 牵引 → 补充指标 → 洞察/为什么是你们 → 商业模式 → 市场 → 团队 → 融资请求。`[cite:1]` YC 对团队页的态度很明确："只写创始人，没人在意你的顾问"；Ask 页要求写清融资额和这笔钱在一年内买到的里程碑。`[cite:1]` YC 建议总页数约 15 页以内，单个主题最多扩展到 2~3 页。`[cite:1]`

### 1.2 投资人注意力的量化证据

多份来源给出一致的量化画面：投资人首次阅读一份 deck 的平均时长约 2 分 45 秒至 3 分 44 秒，约 58% 的 deck 会被完整读完，第一页只有约 20~25 秒来争取下一页。`[cite:4][cite:6][cite:10]` DocSend 的分析显示团队页平均停留约 46 秒，而最终被投资的 deck 在商业模型页上多花了约 94% 的时间。`[cite:1]` 由此派生出可执行的版式约束：60 秒法则（一页要点在 60 秒内讲不清就要简化）、正文 28pt 以上字号、一页一个观点。`[cite:4][cite:5]`

| 量化指标 | 数值 | 来源 |
|---|---|---|
| 首次阅读总时长 | 2 分 45 秒 ~ 3 分 44 秒 | [cite:4][cite:6][cite:10] |
| deck 完整读完率 | 约 58% | [cite:10] |
| 首页停留 | 20~25 秒 | [cite:10] |
| 团队页停留 | 约 46 秒 | [cite:1] |
| 被投 deck 商业模型页额外耗时 | +94% | [cite:1] |

### 1.3 阶段差异与页面取舍

不同阶段的叙事目标不同：pre-seed 讲"问题巨大、团队是解题的人"（8~10 页）；seed 讲"问题真实、方案可行、已有早期牵引"（10~12 页）；Series A 讲"模型可复制、能规模化"（12~15 页 + 附录）。`[cite:4]` pre-seed 投资人的评估顺序是团队不公平优势（领域专长、既往退出、独特渠道）、市场楔子（够小能赢、够大值得）、反共识洞察；此阶段指标权重低，但每个数字都要经得起天使级别的核查。`[cite:6]`

通用共识是 10~14 页核心内容，细节进附录。`[cite:3][cite:5][cite:8]` 页数本身不是标准，"判断问题不缺失"才是标准。`[cite:13]`

### 1.4 中国 BP 的习惯差异

中国投资人语境下的模板与美式骨架一致，但有四个显著差异。第一，团队页位置大幅提前：早期项目"投资人投的就是团队"，天使轮 BP 常把团队放在最前部，强调 2~3 个能力互补的创始合伙人与股权结构（创始人 CEO 控股 51% 以上）。`[cite:11][cite:15]` 第二，注意力假设更苛刻："投资人的注意力也就开头 3 分钟"，反对一上来做大篇幅市场分析。`[cite:11]` 第三，市场分析极度压缩：只给两三个数据说明市场是百亿、千亿还是万亿，不需要图表与琐碎分析。`[cite:11]` 第四，融资额有具体算法：一期运营计划预算加约 20% 余量；天使轮出让 10%~25% 股份；常见融资额 100~500 万人民币，并要求给出 12 个月里程碑。`[cite:11][cite:15]`

| 维度 | 美式（Sequoia/YC） | 中国习惯 |
|---|---|---|
| 团队页位置 | 偏后（第 8~10 页） | 偍前（早期项目首位要素）[cite:11][cite:15] |
| 市场页 | TAM/SAM/SOM 自下而上 | 两三个数据点到为止 [cite:11] |
| 核心页数 | 10~15 页 | 10 页左右，20 页以内 [cite:11] |
| 融资额依据 | Ask + 12 个月里程碑 | 6 个月预算 + 20% 余量，出让 10%~25% [cite:11] |
| 文件格式 | PDF 转发 | PDF（"千万别用 Word"），路演转 PDF 不做动画 [cite:11] |

中国本土的 12 页 BP 基础结构为：封面、客户问题、解决方案、产品与交付、市场、商业模式、竞争、获客、验证数据、团队、财务与现金、融资计划，要求"把形容词换成证据"——"领先/巨大/颠覆/刚需"都不是证据，要用客户数量、客单价、使用频次、留存、具体经历替代。`[cite:13]` 轻资产项目的极简版是"5 页纸"：一句话介绍、痛点+方案（附 demo 截图或视频）、初期数据验证、团队、融资需求与用途。`[cite:15]`

### 1.5 2026 年 AI 创业的门槛反转（关键反面证据）

这是本次检索最重要的发现，它直接约束"先有模有样装起来"的策略边界：

1. **原型的定义变了。** 2026 年的投资人筛选中，Figma 原型不再算数；期望是运行在真实客户环境中的可交互产品，最好有真金白银的承诺。行业口号是"Pre-revenue is fine. Pre-signal is not."（没收入可以，没信号不行）。`[cite:7]` deck 只是获得第一次会议的入场券，能被投资人亲手操作的产品才推进决策。`[cite:9]`
2. **五大过滤器。** 可运行原型或付费试点；数据护城河（核心问题："你有什么是 OpenAI 没有的？"）；垂直而非通用（通用 agent 是功能，垂直 agent 是生意）；评测框架（数百个边界用例的成功率数据，有证据的 95% 成功率可融资，无证据是红旗）；可信单位经济（AI 算力进 COGS 压毛利，投资人要看 70%+ 毛利路径与模型路由策略）。`[cite:7]`
3. **LLM Wrapper Test。** 每次见投资人前自问："OpenAI 能不能在下周把它做成免费功能？"答案是"能"或"也许"，叙事就需要重做。`[cite:7]` 这对架构层/交互层创新的产品是最尖锐的一问。
4. **指标与结构。** 低净收入留存（NDR）是 AI 应用轮次被拒的头号指标原因；AI 公司的 deck 用 AI 生成又正在被 AI 初筛过滤；AI seed 中位 pre-money 估值约 1790 万美元（约为非 AI seed 的两倍多），但 AI 创业公司融资额比 2021 年同类公司小 20%~35%、更快到达有意义收入，"资本效率"本身是卖点。`[cite:7][cite:10]`（估值数字为行业二手统计 `[unverified]`。）

### 1.6 合成：早期 AI 创业 BP 骨架（10~14 页）

综合上述模板，一套不缺判断问题的骨架如下：

| 页 | 判断任务 | 证据要求 | 依据 |
|---|---|---|---|
| 1 封面 | 这家公司一句话是什么 | 一句话说清"为谁解决什么"，可被复述 | [cite:6][cite:8] |
| 2 问题 | 坏在哪里、谁疼 | 带数字的场景 + 用户原话 | [cite:6][cite:8] |
| 3 解决方案与楔子 | 凭什么是结构不同 | 一张图/三句话，先讲楔子不讲五年平台 | [cite:6] |
| 4 Why now | 为什么是现在 | 技术/行为/监管拐点 | [cite:1][cite:2] |
| 5 产品/演示 | 东西存在吗 | 可交互 MVP、demo 视频或截图流 | [cite:5][cite:9] |
| 6 市场 | 楔子能赢、奖赏够大吗 | 自下而上 TAM/SAM/SOM | [cite:3][cite:5] |
| 7 商业模式与单位经济 | 一块钱怎么进来 | 谁付费/多少/多久 + 毛利路径 | [cite:1][cite:7] |
| 8 牵引与验证 | 有人要吗 | 付费试点、LOI、留存、评测数据 | [cite:4][cite:7][cite:13] |
| 9 竞争与护城河 | 客户今天怎么解决、凭什么选你 | 替代方案清单 + Wrapper Test 回答 | [cite:5][cite:7] |
| 10 团队 | 为什么是这群人 | 不公平优势、既往交付 | [cite:4][cite:11][cite:15] |
| 11 Ask | 多少钱、买什么里程碑 | 金额、用途、12 个月里程碑 | [cite:1][cite:11][cite:13] |

常见失败模式（各家来源高度一致）：埋没牵引数据（有势头要放前面）、问题陈述含糊、市场自上而下吹大数、只有累计用户没有留存口径、融资用途只写"市场推广"不写里程碑、隐藏明显风险导致尽调崩盘。`[cite:5][cite:13]`

---

## 2 公众号作为创业公司渠道的评估

### 2.1 流量结构已重构，而非消失

行业运营者提供的数据显示打开率确实在降：十万级大号打开率从约 10% 降到 3%~5%，但数千至万级精准小号打开率可达 8%~10%——精准粉丝的价值上升，泛流量的价值下降。`[cite:16]` `[MAJORITY]` 平台层面发生了三轮规则地震：2024Q4 服务号折叠使触达率腰斩；2025Q4 阅读口径从"次数"改为"人数"挤掉刷量水分；2026 年完读率权重升至约 35% 成为算法第一指标，同时微信接入 AI 搜索，公众号文章成为 AI 回答的核心引用源。`[cite:17]` 行业评测称公域算法推荐占比已超 70%，粉丝量不再决定流量上限，千粉新号也可能靠单篇跑出高阅读。`[cite:20]`（占比数字为行业评测口径 `[unverified]`。）

流量入口的迁移有官方数据佐证方向：微信搜一搜月活超 8 亿、日均搜索请求约 15 亿次，约 40% 新增关注来自搜索入口，42% 的搜索流量流向公众号内容。`[cite:17]` 这意味着内容的长尾复利价值（发布数月后仍被搜索到、被 AI 引用）在上升，而订阅推送的即时触达价值在下降。`[cite:17][cite:18][cite:20]`

### 2.2 适配判据：什么时候该做

对创业公司，投放前的判据可归纳为五问：`[cite:19]`

1. 行业里有没有高质量对标账号（近一年周更以上、ToB 均阅 1000+/ToC 5000+、趋势平稳或上升）？找不到对标要慎重，找得到说明这条路有人走通。
2. 是否已有高客单产品的 1.0？公众号获客拼的是精准度而非线索数量，认知层次高的读者适合高客单转化。
3. 内容是否做了分层：引流型（拉新）、留存型（建信任）、获客型（带精准线索）？
4. 更新频率是否能稳定维持（周更/隔日更均可，关键是规律，实操建议先坚持三个月不断更）。
5. 产品露出策略是什么（独立推文还是文中自然露出），顺序上先分层再设计广告。

公众号的结构性优势是私域中枢（连接社群、企业微信、小程序的闭环）与深度信任（长内容建立认知，适合转化），结构性劣势是泛流量红利结束、用户耐心变短、竞争密集、平台规则持续变化。`[cite:16][cite:18][cite:20]`

### 2.3 决策矩阵

| 目标 | 公众号适合度 | 说明 |
|---|---|---|
| 泛流量涨粉、品牌曝光 | 低 | 泛流量时代已结束 [cite:16][cite:18] |
| 高客单/高信任转化（ToB、知识付费） | 高 | 精准读者 + 私域闭环 + 长尾搜索 [cite:18][cite:19] |
| 投资人与行业背书（创始人 IP） | 中高 | 深度内容建立专业信任，但见效慢、需持续输出 [cite:16][cite:19] |
| 冷启动获客（无产品期） | 中 | 可先用内容验证需求，但须有对标账号与内容分层 [cite:19] |
| 与搜索/AI 搜索的长尾占位 | 高 | 搜索入口迁移 + AI 引用源红利 [cite:17][cite:20] |

运营要点若做：窄定位（"某细分领域的深度"优于"某大领域"）、完读率导向写作（结构化、高信息密度、开头即结论——同时适配算法与 AI 搜索抓取）、稳定更新至少三个月再评估、读者互动沉淀为私域。`[cite:16][cite:17]`

---

## 3 脑机接口作为"快思考"输入通道的现实检验

### 3.1 侵入式：医疗场景已达"接近手速"

Neuralink 的 Telepathy 项目两年内全球累计 21 名临床试验参与者，官方称零严重器械相关不良事件。`[cite:22][cite:25]` 信息传输率（BPS）是关键指标：健全人用鼠标操作约为 8~10 BPS，多名 Neuralink 参与者达到或超过该区间（参与者 Nick 首周即超 10 BPS）；2026 年 10 月，利用 5 万小时无标注神经数据做自监督预训练后，单人最高纪录达 11.32 BPS，且把解码器校准负担从平均每周约 55 分钟降到部分用户每周约 10 分钟。`[cite:21][cite:22][cite:25]` 学术侧的 BrainGate 于 2026 年 3 月在 Nature Neuroscience 发表双手 QWERTY 解码研究，打字速度达 110 字符/分钟、词错率 1.6%。`[cite:25]` 手术侧，Neuralink 第二代植入机器人将单根电极植入时间从 17 秒缩到 1.5 秒，1024 通道，理论可达皮层下 50mm 以上区域。`[cite:24]`

证据纪律需要保留：截至 2026 年 10 月，Neuralink 设备尚无同行评审的人体数据，11.32 BPS 等纪录来自公司博客；学术团队（如 UC Davis 的 ALS 患者居家语音解码近 3800 小时）提供了更强的同行评审证据。`[cite:25]` 植入式 BCI 在美欧均未获完全商业批准。`[cite:25]`

时间表是分歧最大的地方：马斯克称 2026 年开启"大规模量产"、2028 年实现"全脑接口"；而 Synchron 创始人的估计是医疗应用获批还需 3~5 年，消费级植入设备需要 15~20 年。`[cite:31]` 两个口径的分歧根源是立场差异（愿景叙事 vs 监管现实），报告并列呈现。新入局者包括采用超声路径的 Merge Labs（山姆·奥特曼参与），中国方面有华山医院全植入式临床试验与强脑科技的非侵入产品线。`[cite:31]` 据中国信通院报告口径，2025 年全球 BCI 企业超 800 家、市场规模数十亿美元，预计 2030 年破百亿美元。`[cite:31]`（市场规模为预测口径 `[unverified]`。）

### 3.2 非侵入式：仍在 TRL 3

Meta 与 ENS 等机构的 Brain2Qwerty 研究（2026 年 6 月发表于 Nature Neuroscience）代表非侵入式解码的最新上限：MEG 设备平均字符错误率约 32%（最佳参与者 19%），EEG 约 65%~67%。`[cite:26][cite:27][cite:30]` 但细读实验条件会大幅降温：强结果只来自房间级、不可移动、造价约 100~300 万美元的 MEG 设备；输出是离线的（整句打完才解码）；受试者实际在键盘上打字（并非纯"意念默读"）；词汇量约 372 词，且语言模型会按先验补错误，脑信号与模型贡献无法分离。`[cite:27][cite:29][cite:30]` 流传的"61% 词准确率、实时"数字来自另一个未同行评审的预印本，与正式论文不应混淆。`[cite:30]`

消费级硬件的泛化鸿沟更触目：一项跨 5 款 EEG 设备的 P300 拼写研究显示，样本内准确率 94.7% 对字符留出评估仅 31.3%；最优消费设备的解码 AUC 约 0.72——统计可检出，但离临床可用很远。`[cite:28]` 综合判断，非侵入式脑对文的近期场景是重度运动障碍患者，健康人的消费级应用"最早也要 2030 年代"。`[cite:29][cite:30]`

### 3.3 对"快慢机"产品定位的含义

1. **输入通道的带宽瓶颈在 5~10 年内不变。** 快挡的人机交互仍由语音、键盘、眼动主导；BCI 只在医疗场景达到手速水平。`[cite:22][cite:25][cite:31]` 因此 BCI 应放在愿景页（pitch 最后一页"未来"），不进入产品路线图与 PRD 范围。
2. **叙事彩蛋真实存在。** Neuralink 参与者的体验描述是"它有时比你思考快一点，预判你接下来要做什么"。`[cite:22]` 这与"快挡预判意图、慢挡提前铺垫"的产品概念形成呼应，可作为愿景页的一句引语，但不应据此承诺任何功能。
3. **战略重心的反向推论。** 即使 BCI 未来成熟，被商品化的也是"输入通道"，而人的注意力预算、任务的跨天调度、快慢两轨的交接协议并不因输入变快而消失。产品价值应锚定慢挡（长思考调度与状态管理）与耦合层（交接协议），输入通道（含未来的 BCI）按可插拔处理。这一推论与本企划 PRD 1.4 的"耦合层差异点"一致。

---

## 4 风险与信息缺口

- **来源等级风险**：融资门槛与公众号运营类结论多来自从业者内容平台（P2 级），其中 AI 融资门槛（付费试点、评测框架等）经多个独立来源交叉 `[MAJORITY]`，但缺乏一手融资数据库佐证；AI seed 估值、公众号公域推荐占比等数字均为二手统计口径 `[unverified]`。
- **模板页数冲突**：5 页（轻资产）/10 页（YC 简版）/11 页（elev-x）/12 页（leofund）/14 页不等。分歧根源是项目类型与阶段不同，不应取单一数字；正确用法是保证判断问题不缺失、核心 10~14 页、细节进附录。`[cite:4][cite:13][cite:15]`
- **BCI 证据冲突**：公司博客纪录（11.32 BPS、量产时间表）与同行评审证据之间存在明显缺口，学术界提醒每次看纪录都要记住这一差距。`[cite:25]` 时间表分歧（2028 全脑接口 vs 消费级 15~20 年）按立场差异并列保留。`[cite:31]`
- **信息缺口**：中国 AI 创业（尤其 agent 赛道）的最新融资统计、开发者工具类产品的公众号获客转化数据、以及"演示造假（vaporware）"在当前监管与舆论环境下的声誉风险，本次检索未获得可靠数据，标注 `[INSUFFICIENT DATA]`。

---

## 5 结论与行动含义

1. **模板是共识而非创意**：按 1.6 的骨架填空即可达到市场标准，页数不重要，"每页一个判断问题 + 证据代替形容词"才重要。中国语境下把团队与数据验证前置、市场分析压缩到两三个数据。
2. **"装起来"的边界被证据收紧**：可演示的 demo 是必要的，但 2026 年的门槛是"可交互、可验证信号"。纯 deck、纯原型会被初筛淘汰；装的目标应是"能跑起来、能给投资人亲手操作、有一两个真实信号（哪怕是候补名单或设计伙伴）"，而非视觉完善。
3. **护城河叙事要先过 Wrapper Test**：竞品分析（PRD 1.4）已定位差异点在耦合层，BP 的竞争页必须正面回答"OpenAI/大厂为什么不做/做不好这个"——交接协议、跨天状态、注意力调度、宿主嵌入四选一作为主打。
4. **公众号可做，但定位决定成败**：若目标是行业背书与高信任转化（创始人 IP + 细分深度），值得做，先找对标账号验证、内容分层、坚持三个月；若目标是泛流量获客，则不应投入。
5. **BCI 放愿景页**：作为"人机带宽终局"的叙事收尾，配 Neuralink 参与者引语；产品价值锚定慢挡与耦合层，输入通道可插拔——这条推论同时是愿景，也是对"快思考加脑机接口"的诚实回应。

---

## Sources

[cite:1] What's the Right Slide Order for a Pitch Deck? — https://climbtheladder.com/whats-the-right-slide-order-for-a-pitch-deck/
[cite:2] Sequoia Capital Investor Deck: A Guide — https://www.brandatlas.com/investor-decks/sequoia-capital
[cite:3] How to create a 10-slide pitch deck (Sequoia structure) — https://academy.billionideas.co/tutorial/create-pitch-deck-10-slides
[cite:4] Pitch Deck Structure by Stage — https://knowledgelib.io/business/fundraising/pitch-deck-structure-by-stage/2026
[cite:5] The Seed Pitch Deck: The 11 Slides That VCs Expect — https://elev-x.com/news-insights/article-seed-pitch-deck/
[cite:6] Pre-Seed Pitch Deck Template: The 10 Slides Investors Actually Read — https://valueaddvc.com/blog/pre-seed-pitch-deck-template-the-10-slides-investors-actually-read
[cite:7] How to Raise Money for Your AI Startup in 2026: What Investors Actually Want — https://aifirstfounders.com/blog/raise-money-ai-startup-2026.html
[cite:8] Free Investor Pitch Deck Template for 2026 Fundraising — https://aidocx.ai/en/blog/investor-pitch-deck-template-free-download-2026
[cite:9] AI Startup Funding in 2026: Why Investors Want to See a Working AI MVP First — https://www.sortresume.ai/ai-startup-funding-in-2026-why-investors-want-to-see-a-working-ai-mvp-first/
[cite:10] AI Startup Pitch Decks — What Gets Funded Right Now — https://www.venturemage.com/ai-startup-pitch-deck
[cite:11] 投资人真正想看的是这样的BP！ — https://finance.sina.com.cn/wm/2026-03-18/doc-inhrkfux7609128.shtml
[cite:12] 创业项目天使轮融资计划书ppt模板 — https://max.book118.com/html/2026/1016/8022046076010134.shtm
[cite:13] 融资BP模板：商业计划书逐页写法与检查清单 — https://leofund.cn/guides/funding-bp-template
[cite:14] 创业商业融资计划书框架完整模板 — https://m.book118.com/try_down/557042165136010040.pdf
[cite:15] 天使轮商业计划书：轻资产项目快速融资模板 — https://www.cniplan.com/news/detail/tian-shi-lun-shang-ye-ji-hua-shu-qing-zi-chan-xiang-mu-kuai-su-rong-zi-mo-ban.html
[cite:16] 2026年做公众号还有流量吗？晚不晚？我说点大实话 — https://a.jzl.com/exp/2026%E5%B9%B4%E5%81%9A%E5%85%AC%E4%BC%97%E5%8F%B7%E8%BF%98%E6%9C%89%E6%B5%81%E9%87%8F%E5%90%97%EF%BC%9F%E6%99%9A%E4%B8%8D%E6%99%9A%EF%BC%9F%E6%88%91%E8%AF%B4%E7%82%B9%E5%A4%A7%E5%AE%9E%E8%AF%9D
[cite:17] 微信公众号流量去哪了？不是被AI抢走了，是被微信自己"平分"了 — https://www.codingtech.cn/?p=40057
[cite:18] 公众号没凉，但确实不像以前那么好做了 — http://melon.xkwl.net/html/471.html
[cite:19] 公众号引流，创业公司到底做不做？先想清楚这五点！ — http://m.toutiao.com/group/7577250411392942592/
[cite:20] 2026年微信公众号运营全面评测：现状、优劣、变现与实操建议 — https://m.book118.com/html/2026/1009/8056120050010133.shtm
[cite:21] Pretraining on 50,000 Hours of Unlabeled Brain Data — https://neuralink.com/updates/pretraining-on-50000-hours/
[cite:22] Two Years of Telepathy — https://neuralink.com/updates/two-years-of-telepathy/
[cite:23] Neuralink Updates — https://neuralink.com/updates/
[cite:24] 5轴联动直插大脑，马斯克大招：90亿美元估值，20余人已植入 — https://36kr.com/p/3799098062036225
[cite:25] Brain Computer Interfaces: How the Technology Is Advancing in 2026 — https://dev.to/the_daily_flare/brain-computer-interfaces-how-the-technology-is-advancing-in-2026-8
[cite:26] Noninvasive decoding of typing-related brain activity opens a new route for communication brain-computer interfaces — https://www.the-innovation.org/data/article/neurology/preview/pdf/TINE-2026-0044.pdf
[cite:27] Brain-to-Text Decoding: A Non-invasive Approach via Typing (Brain2Qwerty) — https://arxiv.org/abs/2502.17480
[cite:28] P300 Speller Pipeline Tested Across 5 EEG Headsets — https://bciintel.com/news/p300-speller-brainflow-lsl-five-eeg-platforms-2026/
[cite:29] Brain-computer interface typing: is Meta Brain2Qwerty actually useful for everyday people? — https://jakeinsight.com/tech-economy/2026-06-30-brain-computer-interface-typing-meta-brain2qwerty/
[cite:30] How far has noninvasive "brain-to-text" really come? Reading the headlines against the fine print — https://uthandonethemba.com/2026/07/06/how-far-has-noninvasive-brain-to-text-really-come-reading-the-headlines-against-the-fine-print/
[cite:31] 马斯克：2026年，Neuralink开启"大规模量产" — https://digital.gmw.cn/2026-01/04/content_38517384.htm
