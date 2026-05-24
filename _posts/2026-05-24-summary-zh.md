---
layout: default
title: "Horizon Summary: 2026-05-24 (ZH)"
date: 2026-05-24
lang: zh
---

> 从 17 条内容中筛选出 6 条重要资讯。

---

1. [微软开源已知最早的 DOS 源代码](#item-1) ⭐️ 8.0/10
2. [Wake Up! 16 字节演示：演示场景的极致极简](#item-2) ⭐️ 8.0/10
3. [Vivado 2026.1 取消免费版 Linux 支持](#item-3) ⭐️ 8.0/10
4. [格雷格·布罗克曼采访引发关于 OpenAI 治理的辩论](#item-4) ⭐️ 8.0/10
5. [内存短缺推高消费电子产品价格](#item-5) ⭐️ 8.0/10
6. [诈骗者滥用微软内部账户发送垃圾邮件](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [微软开源已知最早的 DOS 源代码](https://arstechnica.com/gadgets/2026/04/microsoft-open-sources-the-earliest-dos-source-code-discovered-to-date/) ⭐️ 8.0/10

微软开源了已知最早的 MS-DOS 源代码版本，该代码从纸质打印输出中通过 OCR 和人工转录精心恢复。 此次发布保存了计算史上的基础篇章，并为开发者和历史学家提供了了解这一开启 PC 革命的操作系统起源的宝贵机会。 源代码来自原始开发者 Tim Paterson 提供的纸质打印输出，数字副本已不复存在。由 Yufeng Gao 和 Rich Cini 领导的“DOS 反汇编小组”团队进行了恢复，克服了针对数十年历史打印件的 OCR 困难。

hackernews · DamnInteresting · 5月24日 01:21 · [社区讨论](https://news.ycombinator.com/item?id=48253386)

**背景**: MS-DOS 是早期 IBM PC 及其兼容机的操作系统，在 20 世纪 80 年代至 90 年代初占据主导地位。微软最初从西雅图计算机产品公司收购了 QDOS 并适配给 IBM。最早的版本使用汇编语言编写，以现代标准看体积极小。

**社区讨论**: 评论者表达了感激和怀旧之情，其中一位指出同时开源的早期 Microsoft BASIC 同样意义重大。另一位强调了从纸质打印输出中恢复源代码所需的繁琐 OCR 过程。

**标签**: `#open-source`, `#history`, `#DOS`, `#Microsoft`, `#software preservation`

---

<a id="item-2"></a>
## [Wake Up! 16 字节演示：演示场景的极致极简](https://hellmood.111mb.de/wake_up_16b_writeup.html) ⭐️ 8.0/10

一篇关于 16 字节演示“Wake Up!”的详细分析发布，解释了如何仅用 16 字节的可执行文件实现令人惊叹的图形和声音。 这个演示突破了尺寸编码的极限，展示了极端优化，激励了演示场景社区，并彰显了极简主义的艺术和技术价值。 该演示在 16 字节内包含视觉和音频输出，使用了自修改代码和 x86 指令特性；在 Hacker News 上获得 331 分和 24 条评论，备受赞誉。

hackernews · MaximilianEmel · 5月24日 00:30 · [社区讨论](https://news.ycombinator.com/item?id=48253060)

**背景**: 演示场景是一个专注于制作自包含音视频程序（称为演示）的亚文化。尺寸编码挑战程序员将令人印象深刻的效果塞进极小（如 4K 或 64K）的可执行文件中。16 字节演示处于这一挑战的前沿，需要深厚的硬件知识和创造力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Demoscene">Demoscene</a></li>
<li><a href="http://viznut.fi/texts-en/16-byte_frontier.html">The 16 - byte frontier: extreme results from extremely small programs.</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了敬畏和赞赏，有人称其为“可以退休的杰作”，还有人表示它引发了一场深入的探索。有人将其与其他小型演示对比，强调包含声音是一个重大成就。

**标签**: `#demoscene`, `#optimization`, `#demo`, `#assembly`, `#minimalism`

---

<a id="item-3"></a>
## [Vivado 2026.1 取消免费版 Linux 支持](https://adaptivesupport.amd.com/s/question/0D5Pd00001YQLdMKAX/why-is-vivado-20261-dropping-linux-support-for-free-tier-?language=en_US) ⭐️ 8.0/10

AMD 的 Vivado 2026.1 版本移除了免费 Basic 层级对 Linux 的支持，Windows 成为唯一的免费选项。该变更通过 AMD 支持论坛帖子公布，引发社区广泛反对。 这一决定疏远了依赖 Linux 进行 FPGA 开发的学生、爱好者和开发者，可能将他们推向 Lattice 或开源工具等竞争对手。这也表明 AMD 在收购 Xilinx 后战略发生转变，优先考虑短期收入而非生态系统增长。 免费 Basic 层级此前同时支持 Windows 和 Linux；付费层级（Standard 和 Enterprise）仍支持 Linux。社区指出，Windows 无法完全替代 Linux 进行交叉编译和 CI 工作流，因此这一变更对教育和研究领域尤其痛苦。

hackernews · zdw · 5月24日 04:14 · [社区讨论](https://news.ycombinator.com/item?id=48254309)

**背景**: Vivado 是 AMD（原 Xilinx）的 FPGA 设计套件，用于综合 HDL 设计并编程 FPGA。免费 Basic 版本提供核心功能，付费版本增加高级功能。FPGA 是可配置集成电路，广泛应用于电信、航空航天和研究领域；Linux 因其灵活性和工具链支持成为 FPGA 开发的首选操作系统。AMD 于 2022 年收购 Xilinx，此后用户观察到政策逐渐向商业导向转变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vivado">Vivado - Wikipedia</a></li>
<li><a href="https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado/vivado-buy.html">AMD Vivado ™ Design Suite: Standard & Enterprise Edition</a></li>
<li><a href="https://en.wikipedia.org/wiki/Field-programmable_gate_array">Field-programmable gate array - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区成员表达强烈不满，指责 AMD 采用会计思维，优先考虑许可收入而非生态系统增长。多位用户威胁转向 Lattice，称其免费工具和数据手册更优。一位教育工作者指出，这一变更将使学生远离 AMD FPGA。

**标签**: `#FPGA`, `#AMD`, `#Xilinx`, `#Vivado`, `#Linux`

---

<a id="item-4"></a>
## [格雷格·布罗克曼采访引发关于 OpenAI 治理的辩论](https://fs.blog/knowledge-project-podcast/greg-brockman/) ⭐️ 8.0/10

OpenAI 联合创始人兼总裁格雷格·布罗克曼在《知识项目》播客上接受采访，引发了关于 OpenAI 公司结构、道德方向以及依赖其 API 风险的广泛讨论。 这次对话之所以重要，是因为它暴露了人们对 OpenAI 是否偏离其最初非营利使命的深切担忧，并凸显了基于其 API 构建的 AI 产品栈的脆弱性。 采访涵盖了 OpenAI 复杂的公司结构——一个非营利母公司加上一个利润上限的有限责任公司——以及最近董事会危机中暴露出的技术和治理上的脆弱性。

hackernews · prakashqwerty · 5月24日 08:29 · [社区讨论](https://news.ycombinator.com/item?id=48255593)

**背景**: OpenAI 最初是一家非营利性 AI 研究组织，但后来设立了营利性部门（OpenAI LP）以吸引资本，同时仍宣称保有非营利使命。这种混合结构因允许私人获利而受到批评。此外，许多公司直接在 OpenAI 的 API 上构建应用程序，这使得它们高度依赖 OpenAI 的稳定性和治理决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/our-structure/">Our structure | OpenAI</a></li>
<li><a href="https://www.mida.so/blog/why-ab-testing-is-the-missing-infrastructure-layer-for-llm-products">Why A/B Testing Is the Missing Infrastructure Layer for LLM Products</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了强烈不满，有人称 OpenAI 背叛了其起源，认为非营利组织不应被允许转型为营利实体。其他人则强调基于 OpenAI API 构建产品的实际风险，称这种依赖关系“可怕”，使得整个技术栈变得脆弱。

**标签**: `#OpenAI`, `#AI governance`, `#interview`, `#technology ethics`

---

<a id="item-5"></a>
## [内存短缺推高消费电子产品价格](https://simonwillison.net/2026/May/22/memory-shortage/#atom-everything) ⭐️ 8.0/10

人工智能对高带宽内存（HBM）的需求正在将晶圆分配从传统 DDR/LPDDR 转向 HBM，而每 GB HBM 消耗的晶圆容量是 DDR 或 LPDDR 的三倍以上。预计这将减少消费级内存的供应，推高智能手机等设备的价格，尤其是 100 美元以下的机型。 消费电子产品的重新定价将对非洲和南亚等价格敏感市场产生不成比例的影响，这些地区的廉价智能手机至关重要。这也凸显了 AI 基础设施投资间接推高了日常科技产品的成本。 目前仅剩三家主要内存制造商，它们有意控制晶圆产能以避免过剩。HBM 利润率更高，导致制造商优先生产 HBM 而非消费级 RAM，这将使后者的供应受限数年。

rss · Simon Willison · 5月22日 22:01

**背景**: 高带宽内存（HBM）是一种 3D 堆叠 DRAM 技术，用于 AI 加速器，可提供高数据带宽并降低功耗。内存制造商的晶圆处理能力固定，不同内存类型（DDR、LPDDR、HBM）的分配决定了市场供应。历史上 HBM 仅占 2%的晶圆产能，但 AI 数据中心的发展正推动其在 2026 年前达到 20%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2024–present_global_memory_supply_shortage">2024–present global memory supply shortage - Wikipedia</a></li>
<li><a href="https://www.formfactor.com/blog/2026/high-bandwidth-memory-testing-why-early-test-strategies-are-critical-for-yield-cost-and-performance/">High-Bandwidth Memory Testing – Why Early Test Strategies Are...</a></li>
<li><a href="https://luna3.ai/what-is-hbm-memory">What Is HBM Memory ? The Bottleneck Behind Every AI Chip</a></li>

</ul>
</details>

**标签**: `#memory`, `#hardware`, `#AI`, `#supply chain`, `#consumer electronics`

---

<a id="item-6"></a>
## [诈骗者滥用微软内部账户发送垃圾邮件](https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/) ⭐️ 7.0/10

数月来，诈骗者一直在利用一个漏洞，从通常用于发送合法账户警报的微软内部电子邮件地址发送垃圾邮件。 这种滥用行为削弱了用户对微软自有域的信任，并突显了持续的域管理和钓鱼风险，可能欺骗那些依赖发件人地址识别合法邮件的用户。 垃圾邮件看似来自合法的微软内部账户，由于域受信任而绕过典型的垃圾邮件过滤器。微软尚未公开披露具体账户或滥用的全部范围。

hackernews · spike021 · 5月24日 00:51 · [社区讨论](https://news.ycombinator.com/item?id=48253186)

**背景**: 组织通常使用内部电子邮件地址发送自动通知，这些账户通常被电子邮件安全系统列入白名单。如果诈骗者获得从这些地址发送邮件的能力，其消息可以绕过 SPF、DKIM 和 DMARC 检查。此事件反映了微软域蔓延的更广泛问题，即许多子域和账户难以追踪和保护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/">Scammers are abusing an internal Microsoft account to send spam links | TechCrunch</a></li>
<li><a href="https://news.ycombinator.com/item?id=48253186">Scammers are abusing an internal Microsoft account to send spam links | Hacker News</a></li>

</ul>
</details>

**社区讨论**: 评论者对微软混乱的域组合表示沮丧，指出即使是内部账户也无法免于滥用。一些人指出了其他服务的类似钓鱼问题，而另一些人则批评缺乏一个用于验证的微软官方域综合列表。

**标签**: `#security`, `#phishing`, `#Microsoft`, `#spam`, `#domain management`

---