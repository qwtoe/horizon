---
layout: default
title: "Horizon Summary: 2026-11-09 (ZH)"
date: 2026-11-09
lang: zh
---

> 从 14 条内容中筛选出 8 条重要资讯。

---

1. [高盛从银行家和交易员电脑上撤下 Claude Code](#item-1) ⭐️ 8.0/10
2. [llama-modchip 声称在 64GB 内存、无 GPU 环境下运行 284B DeepSeek-V4-Flash](#item-2) ⭐️ 8.0/10
3. [英伟达董事会调查针对 CEO 黄仁勋的情报行动](#item-3) ⭐️ 8.0/10
4. [Outlook.com 悄然拒收未配置 DMARC 域名的邮件](#item-4) ⭐️ 7.0/10
5. [博主主张写作是思考工具，而非仅仅记录成果](#item-5) ⭐️ 7.0/10
6. [开发者弃用 Claude Code 转投 Pi，引发智能体框架大讨论](#item-6) ⭐️ 7.0/10
7. [Simon Willison 用 C 与 Rust 分别实现 parse_number() SQLite 扩展并做性能对比](#item-7) ⭐️ 7.0/10
8. [Dux（原 Dank Material Shell）发布 v2.0，新增对原子发行版的支持](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [高盛从银行家和交易员电脑上撤下 Claude Code](https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers) ⭐️ 8.0/10

高盛正在从自家银行家和交易员的电脑上移除 Anthropic 的 Claude Code，相当于撤回了这款智能体编程工具在华尔街顶级投行内部的一次部署。此举背后是对在敏感金融工作站上运行半自主智能体的安全顾虑，以及计费与合规方面的摩擦。 这是一个极具标志性的信号：在开发者中迅速普及的智能体编程工具，可能在数据授权和可审计性属于硬性要求的受监管行业里遭遇天花板。其他正在评估类似部署的银行和金融机构，很可能会把高盛的这次撤回当作一个警示案例。 有评论者注意到时机耐人寻味——消息出现在 Anthropic 预期 IPO 前不久，而据称高盛正是承销方之一；还有人推测只有拥有下单权限的交易员被收回访问权，这暗示背后可能发生了运营或安全事件，而非一刀切的政策调整。另一些评论者提到 Claude Code 的按量计费模式造成预算长期超支，而 Anthropic 无法提供标准化的费率，从而把部分团队推向了定价更平稳的 Gemini。

hackernews · TheWiggles · 11月8日 18:16 · [社区讨论](https://news.ycombinator.com/item?id=50415628)

**背景**: Claude Code 是 Anthropic 推出的智能体编程工具，运行在终端和 IDE 中，能读取代码库、编辑文件并代替用户执行 shell 命令——这些能力让它在工程师手中非常强大，但也赋予了它广泛的机器级访问权限。安全研究者用“致命三要素”来形容一种危险组合：同时拥有访问私有数据的能力、接触不可信内容、以及对外通信的能力，三者叠加就为提示注入攻击和数据外泄打开了大门。在交易大厅里，一台工作站往往同时存放客户与自营交易数据、电子邮件、内网访问和互联网连接。此外，大模型 API 通常按 token 消耗量计费而非按席位收费，因此企业成本波动大、难以预测，与传统的 SaaS 定价模式截然不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI coding agent and assistant</a></li>
<li><a href="https://github.com/anthropics/claude-code">GitHub - anthropics/ claude - code : Claude Code is an agentic coding ...</a></li>
<li><a href="https://www.kinde.com/learn/billing/pricing/billing-for-ai-and-llm-based-apis-cost-control-strategies/">Billing for AI and LLM-Based APIs: Cost Control Strategies</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（557 分、329 条评论）基本聚焦于安全：评论者认为真正原因是“致命三要素”——无人值守的智能体与客户/交易数据、电子邮件和互联网访问共处同一台工作站。另一些人强调那些看似平淡却更具决定性的因素：长期的账单超支把团队推向 Gemini 的固定定价，以及银行业沉重的合规、权限与可审计要求，而这些往往被非技术人员写的概念验证所忽视。还有人质疑消息相对 Anthropic IPO 的时机，并推测触发撤回的是一次具体的运营损失，而非主动出台的政策。

**标签**: `#AI coding agents`, `#enterprise AI adoption`, `#security`, `#financial services`, `#LLM cost/billing`

---

<a id="item-2"></a>
## [llama-modchip 声称在 64GB 内存、无 GPU 环境下运行 284B DeepSeek-V4-Flash](https://github.com/synchopate/llama-modchip) ⭐️ 8.0/10

一个名为 llama-modchip 的 GitHub 项目（开发者 synchopate，目前已发布 v2.4.0）声称可以在仅有 64GB 内存、完全没有 GPU 的机器上运行 DeepSeek 的 284B 参数 V4-Flash 模型，依靠的是打了补丁、支持 AVX-512/AVX2 或 Apple Metal 的 llama.cpp 引擎。仓库提供了零动态库依赖的单文件预编译服务端二进制，并警告该模型使用的自定义张量类型 40 在未打补丁的 llama.cpp、Ollama 或 LM Studio 中会加载失败。 如果这一说法成立，那么在内存与 GPU 价格持续上涨的背景下，运行前沿规模 MoE 模型的硬件门槛就被拉低到了普通消费级工作站的水平。这也为“激进的量化究竟能走多远、何时会牺牲模型质量”这一更广泛的争论添了一把火。 DeepSeek-V4-Flash 是一个 MoE 模型，总参数 284B，但每个 token 仅激活 13B，这正是纯 CPU 推理在理论上可行的原因；项目还宣称支持 256K 上下文窗口、1.64MB 的 Stockfish-PVS 加 RouteCrack L3 草稿器（drafter）以及 2MB 大页内存。代价是整个模型必须以高度压缩的位宽常驻内存，因此输出质量和速度高度依赖量化选择；批评者还指出，默认流程实际只启动了一个小得多的 Nemotron-3.5-30B-A3B（Q4_0）模型。

hackernews · joshcsimmons · 11月8日 10:22 · [社区讨论](https://news.ycombinator.com/item?id=50411961)

**背景**: 大语言模型的权重通常以 16 位或 8 位数值存储；量化把这些权重压缩到 4 位、3 位甚至更低精度，使模型能塞进小得多的内存里，但会付出一定的精度代价。像 DeepSeek 使用的 MoE（混合专家）架构会把模型拆成许多专家子网络，每个 token 只激活其中少数几个，因此一个 284B 参数的模型每次计算可能只用到约 13B 参数——这减少了算力需求，但全部参数仍需驻留在内存中。llama.cpp 是广受欢迎的开源 C/C++ 推理引擎，用于在 CPU 和消费级 GPU 上本地运行此类模型，而类似本项目的工作通常会对其进行分支改造，加入自定义算子和张量格式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/synchopate/llama-modchip">GitHub - synchopate/llama-modchip: Run 284B DeepSeek-V4 ...</a></li>
<li><a href="https://github.com/synchopate/llama-modchip/tree/main">GitHub - synchopate/llama-modchip: ♟️ llama-modchip v2.1: Run ...</a></li>
<li><a href="https://arxiv.org/html/2508.16712v1">Systematic Characterization of LLM Quantization: A ...</a></li>

</ul>
</details>

**社区讨论**: 评论区意见明显分成热情与质疑两派。armcat 提醒说量化的性能表现是非线性的，经验上“体积-性能比”的最佳点在 4 位附近，再低就会显著掉质量；antirez 则指出 128GB 统一内存已经足以让这类模型快到可以承接编码智能体的程度。质疑最激烈的是 aappleby，他在 16 核 Ryzen 7945HX 加 96GB DDR5 的机器上实测发现，除 prefill 更快之外，该仓库在 CPU 上的表现与原生 llama.cpp 差不多，而且根本找不到可以选中 DeepSeek“modchip 配置”的选项。

**标签**: `#local AI`, `#quantization`, `#LLM inference`, `#DeepSeek`, `#hardware`

---

<a id="item-3"></a>
## [英伟达董事会调查针对 CEO 黄仁勋的情报行动](https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors) ⭐️ 8.0/10

英伟达董事会确认正在调查一起针对 CEO 黄仁勋的情报行动，而不是在对黄仁勋本人展开调查——这一区别被新闻标题所掩盖，令不少读者产生误解。社区成员还引用彭博社的报道《Nvidia Board to Probe Spying Case After CEO Admits Infidelity》，该报道称此次调查是在黄仁勋承认婚外情之后启动的。 英伟达处于全球 AI 硬件供应链的核心位置，因此任何涉及这位创始人兼 CEO 的治理或安全争议，其影响都会远超公司本身，波及投资者、客户和监管机构。此事也凸显出地缘政治如今已直接触及半导体高管的私人生活，因为对华先进芯片出口管制涉及数十亿美元级别的决策。 董事会声明发布在英伟达自家的企业新闻室页面上，但公开细节仍然很少；目前流传的许多说法——包括婚外情这一角度以及所谓与一家新加坡公司的关联——都来自二手报道和评论者的推测，而非已确认的事实。评论者强调，目前没有任何证据表明黄仁勋或英伟达存在不当行为。

hackernews · vincentchau · 11月8日 20:26 · [社区讨论](https://news.ycombinator.com/item?id=50416801)

**背景**: 黄仁勋是英伟达的联合创始人及长期担任的 CEO，该公司设计的 GPU 和 AI 加速器是绝大多数大规模机器学习训练与推理的基础。所谓“情报行动”在此语境下指的是间谍式活动，通常由国家情报机构或其代理人实施，目的在于对高价值目标获取把柄、情报或影响力。英伟达的业务深受美国出口管制的塑造，这些管制限制其最先进芯片对华销售，因此公司领导层的个人行为与社会关系不仅关乎公司治理，也涉及监管层面的关切。

**社区讨论**: 最主要的反应是对误导性标题的不满，最高票评论澄清说，英伟达调查的是发生在黄仁勋身上的某件事，而不是在调查他本人。其他人则给出了地缘政治层面的分析——有评论者认为，掌握如此巨大经济权力的人必然会被外国情报机构长期研究；也有人猜测存在试图对英伟达施加杠杆的图谋，并提醒目前并未证实任何不当行为。还有评论把事件的重要性与出口管制法律联系起来，指出如果黄仁勋明知一家新加坡合作方实为中国企业的代理，就会引发关于尽职调查与是否共谋的质疑。

**标签**: `#nvidia`, `#corporate-governance`, `#espionage`, `#semiconductors`, `#geopolitics`

---

<a id="item-4"></a>
## [Outlook.com 悄然拒收未配置 DMARC 域名的邮件](https://mailroute.net/blog/outlook-rejecting-email-without-dmarc) ⭐️ 7.0/10

据 MailRoute 报道，自 2026 年 11 月 5 日起，微软的消费级邮件服务开始拒收部分来自未发布 DMARC 记录的域名所发送的邮件，而微软并未发布任何公开公告。该变化影响发往 outlook.com、hotmail.com、live.com 和 msn.com 地址的邮件，发送方目前可能已经在对这些收件人投递时遇到退信。 对于任何自建邮件服务器或大规模发送事务性邮件的人来说，这是一次实质性的运营变化：缺少一条 DNS 记录，就可能导致邮件无法投递到这家庞大的消费级邮箱服务商。这也表明，长期被视为最佳实践的 DMARC 正逐渐成为大型邮箱服务商的硬性准入要求。 报道给出的解决办法只是在 DNS 中添加一条 DMARC TXT 记录，而且这种拒收看起来是策略层面的过滤，而非基于垃圾邮件评分的判定。有评论者不认同“悄然”这一说法，指出 Outlook 确实会返回 5xx 永久性投递失败，但也有人反映邮件在 SMTP 阶段被正常接收，随后却被静默丢弃。

hackernews · xmddmx · 11月8日 19:20 · [社区讨论](https://news.ycombinator.com/item?id=50416158)

**背景**: DMARC（基于域的消息认证、报告与一致性）是一种通过 DNS 发布的策略，它建立在 SPF 和 DKIM 之上，用于告知接收方服务器在邮件认证失败时应如何处理——不采取动作、隔离还是拒收。未发布 DMARC 记录的域名等于没有向接收方声明策略，因此大型服务商越来越倾向于把这类发件人视为不可信。“静默丢弃”则是一个长期存在的独立问题：接收服务器以 SMTP 250 OK 接受邮件，却从未真正投递，导致发送方连可用于排查的退信都收不到。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mailroute.net/blog/outlook-rejecting-email-without-dmarc">Outlook.com Is Quietly Rejecting Email From Domains Without ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者普遍认为要求 DMARC 是合理的，多人表示发件方多年前就该部署，但最主要的抱怨是缺乏透明度：一位管理员称其 VPS 服务商被非公开的黑名单封禁且申诉渠道无效，另一位则反映多年来尽管 SPF、DKIM 和 DMARC 都配置正确，邮件仍被接收后静默丢弃。也有人对报道的表述提出反驳，指出 Outlook 实际上会返回 5xx 永久失败。

**标签**: `#email`, `#dmarc`, `#deliverability`, `#self-hosting`, `#infrastructure`

---

<a id="item-5"></a>
## [博主主张写作是思考工具，而非仅仅记录成果](http://muratbuffalo.blogspot.com/2026/11/writing-as-thinking-tool.html) ⭐️ 7.0/10

文章将写作从被动的输出环节重新定义为一种主动的思考方式，评论者则进一步把这一观点延伸到设计与编程等类似的思考工具上。 这篇文章触及了工程师、研究者和设计师的普遍痛点：他们往往把写作、绘图或写代码视为额外负担，而不是工作本身的一部分。它的热度表明，人们越来越关注手工过程如何塑造思维质量，尤其是在 AI 工具承诺可以完全跳过这些步骤的当下。 这一论点主要依靠社区中的个人经历而非正式研究来支撑：一位博士生的经历说明，反复起草论文迫使自己理清思路；其他人则指出，手写代码和在纸上画草图能揭示事先并不明确的需求。讨论也隐含地质疑：基于提示词的 AI 工作流能否复制“思考与动手”之间的紧密循环。

hackernews · jruohonen · 11月8日 10:41 · [社区讨论](https://news.ycombinator.com/item?id=50412067)

**背景**: “写作是思考工具”这一观念可追溯到关于写作的经典论述，常被概括为“在说出想法之前，我怎么知道自己想的是什么”。在知识工作中，这种观点把起草、修改和把想法外化视为推理的必要环节，而非最后的汇报步骤。Hacker News 的讨论把同样的逻辑扩展到其他技艺，将设计稿、原型和代码都看作外化的思考。

**社区讨论**: 评论者总体上表示赞同，并进一步拓展而非反驳这一观点：有人谈到读博期间意识到表达想法本身就在塑造科学研究；有人认为 Figma 式的设计过程依然重要，因为手工创作带来的洞察是提示词难以替代的；还有人补充了编程、纸上画草图乃至石雕等领域，认为动手制作能澄清问题。整体情绪积极，主要担忧在于 AI 辅助的捷径可能绕过手工劳动所产生的思考过程。

**标签**: `#writing`, `#productivity`, `#cognition`, `#software-engineering`, `#design`

---

<a id="item-6"></a>
## [开发者弃用 Claude Code 转投 Pi，引发智能体框架大讨论](https://caleb.software/posts/claude-to-pi.html) ⭐️ 7.0/10

一位开发者发表了题为《Goodbye Claude, hello Pi》的博客文章，解释自己为何从 Anthropic 的 Claude Code 转向 Pi——一个极简、可扩展的终端编码智能体框架。该文章登上 Hacker News 首页，获得 684 分和 424 条评论，演变成一场关于框架设计、模型行为与服务条款风险的大范围讨论。 这场讨论反映出开发者对 AI 编码工具认知的转变：包裹在模型之外的框架——包括提示词、工具、上下文管理和界面的整套脚手架——正被视为与底层模型同等重要。对于使用大模型的团队而言，这意味着工具选型与定制化的重要性可能不亚于选择哪个模型。 据描述，Pi 是一个极简的终端框架，系统提示词很短以节省 token，支持 skills 和 AGENTS.md 文件，并可在运行中按 Enter 立即干预、按 Alt+Enter 排队后续指令。评论者提醒，将第三方框架与 Anthropic 模型搭配使用可能因违反服务条款而面临封号风险，还可能错过 Claude Code 所依赖的未公开 API 行为。

hackernews · karagenit · 11月8日 03:11 · [社区讨论](https://news.ycombinator.com/item?id=50410107)

**背景**: 编码智能体框架（harness）是大模型外层的软件层，负责把模型变成能自主干活的执行者：它管理智能体循环、工具调用、文件访问、沙箱、记忆以及终端或图形界面。Claude Code 是 Anthropic 为其 Claude 模型提供的官方框架，而 Pi 是一个开放、极简的替代品，意在让开发者按自己的工作流重塑工具。由于框架决定了模型能看到什么、如何行动，同一个模型在不同框架下往往表现差异明显。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pi.dev/">A terminal-based coding agent</a></li>
<li><a href="https://github.com/earendil-works/pi">GitHub - earendil-works/ pi : AI agent toolkit: unified LLM API, agent ...</a></li>
<li><a href="https://silenceper.com/en/article/2026-05-27-pi-coding-agent-harness/">Pi : A Coding Agent Harness You Can Reshape Around Your Workflow</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Pi 总体持肯定态度，有人称其为最好的框架，因为完全本地可控才能从“驾驶智能体”迈向“编排智能体”。也有人反对将替代框架与 Anthropic 模型搭配使用，理由是封号风险、缺失官方私有的通信机制、上下文压缩效果较差，并认为模型效能的大头如今在框架而非模型本身。还有用户表示，随着跨多个项目的 LLM 使用量激增，自己已从终端界面转向图形界面客户端。

**标签**: `#AI coding agents`, `#LLM tooling`, `#Claude Code`, `#developer workflow`, `#agent harness`

---

<a id="item-7"></a>
## [Simon Willison 用 C 与 Rust 分别实现 parse_number() SQLite 扩展并做性能对比](https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust/) ⭐️ 7.0/10

Simon Willison 借助 Claude Opus 5.5，分别用 C 和 Rust 实现了一个 parse_number() SQLite 扩展，用于把 "-$1,234.56" 或 "12.5%" 这类字符串转换成可排序、可求和的数值。最初的 Rust 版本体积远大于 14 KB 的 C 版本（使用 Rusqlite 为 321 KB，使用 sqlite-loadable-rs 为 298 KB），但运行更快，因为 Rust 的浮点解析速度约为 C 的 strtod 的两倍；在提示模型手写自定义 C 解析函数后，新版 C 实现降至每行 16–19 纳秒，在 200 万行的测试中全面胜过两个 Rust 版本（32–55 纳秒）。 这项实验量化了许多开发者在扩展 SQLite 时面临的权衡：C 能产出极小的二进制文件，并且在手工优化解析逻辑后拥有最好的原始性能；Rust 则带来内存安全和对 crates.io 生态的访问能力，代价是共享库体积大约增加到 20 倍。由于整项调研——代码、基准测试以及 simonw/research 仓库中的书面报告——都是在一次 AI 辅助会话中完成的，它也说明 AI 结对编程如今能多快地把一个遛狗时冒出的想法变成可复现的技术对比。 基准测试覆盖 200 万行数据的三类负载：混合数据（新 C 版 19 纳秒，Rusqlite 46 纳秒，sqlite-loadable-rs 41 纳秒）、纯整数（16 纳秒对 36/32 纳秒）和纯小数（18 纳秒对 55/47 纳秒），其中最初的 C 版本最慢，达到 106 纳秒。这些只是单机上的微基准测试，代码属于探索性原型而非已发布打包的扩展，而且实现由大语言模型生成，因此真实场景表现与正确性验证仍是未解问题。

rss · Simon Willison · 11月8日 22:26

**背景**: SQLite 支持运行时加载扩展：这些共享库可以加载进一个数据库连接（在命令行中通过 .load，在 API 中通过 sqlite3_load_extension()），并暴露诸如 sqlite3_extension_init 的入口点，再通过 sqlite3_create_function() 注册新的标量函数。用 C 编写是原生路径，能生成非常小的 .so 文件；Rust 开发者则可以在广泛使用的 rusqlite 库和 asg017 的 sqlite-loadable-rs 框架之间选择，后者对 SQLite C API 做了封装（大量使用 unsafe 代码），并把 Rust 运行时静态链接进产物中。parse_number() 函数可用于清洗杂乱的抓取数据——去掉货币符号、逗号和百分号——从而直接在 SQL 中求和与排序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/asg017/sqlite-loadable-rs">GitHub - asg017/sqlite-loadable-rs: A framework for writing ...</a></li>
<li><a href="https://sqlite.org/loadext.html">Run-Time Loadable Extensions - SQLite</a></li>
<li><a href="https://docs.rs/sqlite-loadable/latest/sqlite_loadable/">sqlite_loadable - Rust - Docs.rs</a></li>

</ul>
</details>

**标签**: `#sqlite`, `#rust`, `#c`, `#performance`, `#extensions`

---

<a id="item-8"></a>
## [Dux（原 Dank Material Shell）发布 v2.0，新增对原子发行版的支持](https://duxlabs.dev/) ⭐️ 6.0/10

原名 Dank Material Shell（DMS）的 Wayland 桌面 shell 现更名为 Dux，并在几周前完成品牌替换后发布了 v2.0 版本。此次发布内置了文件管理器和主题系统，并正式支持 Bazzite 等原子（不可变）发行版，填补了此前在这类热门发行版上安装不便的空白。 Dux 是构建在 niri 可滚动平铺合成器之上的较为精致的 shell 之一，长期用户认为它足以帮助 niri 走向主流用户群体。支持原子发行版之所以重要，是因为像 Bazzite 这样的不可变系统是 Linux 桌面增长最快的细分领域之一，而无法干净地叠加到这类系统上的桌面 shell 就会被排除在这部分用户之外。 Dux 是运行在 Wayland 合成器之上的 shell 层，本身并非合成器，主要支持目标是 niri，并采用 `curl | sh` 脚本方式安装——有评论者指出这在信任与安全层面令人担忧。也有用户认为它正变得越来越“大而全”，因而转向更轻量的替代方案，例如 Noctalia 搭配基于 River 的 triad 合成器。

hackernews · indigodaddy · 11月8日 19:08 · [社区讨论](https://news.ycombinator.com/item?id=50416053)

**背景**: Wayland 是旨在取代 X Window System 的现代显示服务器协议，在 Wayland 中显示服务器与合成器被合并为同一个组件。niri 这类用 Rust 编写的可滚动平铺合成器会把窗口排列在一条可无限横向滚动的窗口列上，而不是依赖传统工作区。像 Dux 这样的桌面 shell 则叠加在合成器之上，提供面板、启动器、通知和文件管理等功能。Fedora Silverblue、Bazzite 等原子或不可变发行版将根文件系统保持只读并以事务方式应用更新，回滚很方便，但安装桌面 shell 这类系统级组件会更麻烦。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wayland_(display_server_protocol)">Wayland (display server protocol)</a></li>
<li><a href="https://github.com/niri-wm/niri">GitHub - niri-wm/niri: A scrollable-tiling Wayland compositor.</a></li>
<li><a href="https://itsfoss.com/immutable-linux-distros/">12 Future-Proof Immutable Linux Distributions - It's FOSS 5 atomic Linux distros I trust for stress-free OS updates ... Home, RakuOS Best Future-Proof Immutable Linux Distributions 3 atomic Linux distros I trust for a stress free PC Best immutable Linux distro in 2026: 9 picks ranked</a></li>

</ul>
</details>

**社区讨论**: 长期用户评价非常正面：有人已把 DMS 与 niri 搭配使用近一年，称其“顺滑得没完没了”，并打趣说已经不打算再换回去；另一位用户则表示这是他第一次稳定到停止频繁更换桌面环境的 shell。质疑者则认为它外观很像 Android，并对 `curl | sh` 安装方式提出疑问，认为这类项目应先由发行版打包并经过审查，才值得无条件信任；另有讨论转向 XFCE 的 Wayland 路线图以及更轻量的替代方案。

**标签**: `#linux`, `#wayland`, `#desktop-environment`, `#open-source`, `#niri`

---