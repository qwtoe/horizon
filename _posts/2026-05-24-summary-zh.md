---
layout: default
title: "Horizon Summary: 2026-05-24 (ZH)"
date: 2026-05-24
lang: zh
---

> 从 17 条内容中筛选出 6 条重要资讯。

---

1. [微软开源已知最早的 DOS 源代码](#item-1) ⭐️ 8.0/10
2. [骗子利用微软内部账户发送垃圾邮件](#item-2) ⭐️ 8.0/10
3. [16 字节演示《Wake Up!》打破尺寸记录](#item-3) ⭐️ 8.0/10
4. [Greg Brockman 讲述差点毁掉 OpenAI 的 72 小时](#item-4) ⭐️ 8.0/10
5. [Vivado 2026.1 移除 Linux 免费版](#item-5) ⭐️ 7.0/10
6. [AI 对 HBM 的需求推高消费电子价格](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [微软开源已知最早的 DOS 源代码](https://arstechnica.com/gadgets/2026/04/microsoft-open-sources-the-earliest-dos-source-code-discovered-to-date/) ⭐️ 8.0/10

微软开源了已知最早的 DOS 源代码以及其早期的 BASIC 解释器，保护了计算史上的关键部分。 此次发布使开发者和历史学家能够研究微软操作系统业务的起源以及个人计算的早期发展。 该源代码是从纸质打印件通过 OCR 恢复的，因为没有数字副本；一个名为 DOS 反汇编小组的团队主导了这项工作。

hackernews · DamnInteresting · 5月24日 01:21 · [社区讨论](https://news.ycombinator.com/item?id=48253386)

**背景**: MS-DOS 是 20 世纪 80 年代和 90 年代初 IBM PC 兼容机上的主流操作系统。微软最初从西雅图计算机产品公司获得 DOS，并授权给 IBM，这导致了微软的成功。早期代码的开源提供了对当时技术和商业决策的洞察。

**社区讨论**: 社区成员表达了感谢，指出了微软 BASIC 的历史重要性，并分享了 IBM 在 Digital Research 拒绝签署 NDA 后转向微软的故事。一些人评论了涉及从纸质打印件进行 OCR 的艰苦恢复过程。

**标签**: `#open-source`, `#DOS`, `#Microsoft`, `#history`, `#retrocomputing`

---

<a id="item-2"></a>
## [骗子利用微软内部账户发送垃圾邮件](https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/) ⭐️ 8.0/10

骗子正在利用一个微软内部账户（很可能通过 Microsoft 365 Direct Send）发送垃圾邮件链接，这些邮件看似来自微软内部，从而绕过邮件过滤。 这凸显了微软邮件基础设施中的一个严重安全缺陷：即使是内部账户也可能被伪造，从而削弱了对邮件安全的信任，并可能助长更有效的钓鱼攻击。 该滥用行为利用了允许通过 Direct Send 进行内部伪造的配置，此功能本应用于内部邮件中继。微软在 2026 年 1 月警告称，错误配置的邮件路由可能引发伪造攻击。

hackernews · spike021 · 5月24日 00:51 · [社区讨论](https://news.ycombinator.com/item?id=48253186)

**背景**: SPF、DKIM 和 DMARC 等电子邮件认证协议旨在通过验证发件人身份来防止伪造。然而，内部邮件系统通常对受信任域有例外规则，若配置不当则可能被利用。Microsoft 365 的 Direct Send 功能在错误设置时，允许外部发件人伪造内部地址。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/microsoft-365-direct-send-abuse-enables-internal-email-spoofing-bsnic">Microsoft 365 Direct Send Abuse Enables Internal Email Spoofing</a></li>
<li><a href="https://www.inceptionsecurity.com/post/microsoft-365-direct-send-phishing-how-internal-looking-emails-bypass-defenses-and-what-smbs-can">Microsoft 365 Direct Send Phishing: How Internal -Looking Emails ...</a></li>
<li><a href="https://www.captaindns.com/en/blog/email-routing-spoofing-microsoft-warning">Email Routing Spoofing : Microsoft 's January 2026 Warning</a></li>

</ul>
</details>

**社区讨论**: 评论者对微软域名管理的复杂性表示沮丧，指出即使是内部人员也难以列出所有官方域名。有人分享了类似的伪造攻击经历，还有人批评微软未使用子域名以及 Microsoft Authenticator 存在糟糕的安全默认设置。

**标签**: `#security`, `#phishing`, `#Microsoft`, `#spam`, `#domain management`

---

<a id="item-3"></a>
## [16 字节演示《Wake Up!》打破尺寸记录](https://hellmood.111mb.de/wake_up_16b_writeup.html) ⭐️ 8.0/10

一款名为《Wake up! 16b》的 16 字节演示程序发布，以极小的二进制体积实现了视听演示效果。这是底层编程和尺寸优化领域的一项了不起成就。 该演示将 16 字节所能实现的效果推向了新极限，激励了演示场景社区，并展示了编程中极简主义的美学。它凸显了演示场景社区持续的创造力和技术功底。 该演示是一个自包含的可执行文件，尽管只有 16 字节，却能生成图像和声音。它延续了尺寸受限的片头演示（如 64k 和 4k 片头）的传统，但达到了前所未有的压缩水平。

hackernews · MaximilianEmel · 5月24日 00:30 · [社区讨论](https://news.ycombinator.com/item?id=48253060)

**背景**: 演示场景是一个计算机艺术亚文化，创作自包含的实时视听程序（演示），通常有严格的尺寸限制，如 64KB 或 4KB。尺寸优化涉及压缩代码、重用数据、利用硬件特性等技术，以最小化二进制体积。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Demoscene">Demoscene</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了惊叹和怀旧之情，一位用户花了一小时探索相关演示。另一用户指出，之前 32 字节演示似乎已是极限，因此这个 16 字节的成就更令人印象深刻。

**标签**: `#demo scene`, `#size optimization`, `#low-level programming`, `#hacker news`, `#minimal binary`

---

<a id="item-4"></a>
## [Greg Brockman 讲述差点毁掉 OpenAI 的 72 小时](https://fs.blog/knowledge-project-podcast/greg-brockman/) ⭐️ 8.0/10

前 OpenAI 总裁 Greg Brockman 详细描述了那场 72 小时的董事会政变，其中罢免了 CEO Sam Altman，随后员工和高管共同努力使其复职，避免了公司崩溃。 这一内部描述揭示了 AI 治理的脆弱性以及少数董事会成员的巨大影响力，凸显了依赖 OpenAI API 运营的初创公司和企业面临的风险。 这场危机在一个周末内展开：Sam Altman 在周五被解雇，在员工和投资者（包括集体辞职威胁）的压力下，于周二复职。

hackernews · prakashqwerty · 5月24日 08:29 · [社区讨论](https://news.ycombinator.com/item?id=48255593)

**背景**: OpenAI 最初以非营利组织形式成立，使命是安全地开发 AI，但后来创建了封顶利润的子公司以筹集资金。董事会解雇 Altman 的决定引发了关于非营利结构是否可能被利用谋取私利的治理辩论。

**社区讨论**: 评论者表达了不同意见：有人认为政变会修复 OpenAI，有人觉得这背叛了其初衷，还有许多人担心依赖其 API 的业务的稳定性。也有人质疑 Ilya Sutskever 的动机，他最初支持解雇 Altman，后来却签署了团结信。

**标签**: `#OpenAI`, `#AI governance`, `#leadership`, `#tech drama`, `#startups`

---

<a id="item-5"></a>
## [Vivado 2026.1 移除 Linux 免费版](https://adaptivesupport.amd.com/s/question/0D5Pd00001YQLdMKAX/why-is-vivado-20261-dropping-linux-support-for-free-tier-?language=en_US) ⭐️ 7.0/10

AMD 的 Vivado 2026.1 从免费版 WebPACK 中移除了 Linux 支持，Linux 用户只能使用付费的 Standard 或 Enterprise 版本。 这一决定提高了依赖 Linux 的学生、爱好者和开发者的入门门槛，可能缩小 FPGA 生态系统，并将用户推向 Lattice 等竞争对手。 免费的 Vivado Standard 版继续仅支持 Windows，而付费版本仍为多平台。这一变化从 2026.1 版本开始影响所有使用免费版的 Linux 用户。

hackernews · zdw · 5月24日 04:14 · [社区讨论](https://news.ycombinator.com/item?id=48254309)

**背景**: Vivado 是 AMD 的 FPGA 设计套件，用于 Xilinx 器件的综合、分析和编程。历史上，免费的 WebPACK 版同时支持 Windows 和 Linux，为教育和原型设计提供了广泛访问。付费的 Standard 和 Enterprise 版解锁更多功能并支持所有平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vivado">Vivado - Wikipedia</a></li>
<li><a href="https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado/vivado-buy.html">AMD Vivado ™ Design Suite : Standard & Enterprise Edition</a></li>
<li><a href="https://forum.digikey.com/t/xilinx-vivado-design-suite-getting-started/13253">Xilinx Vivado Design Suite - Getting Started - Logic Design - DigiKey...</a></li>

</ul>
</details>

**社区讨论**: 社区情绪普遍负面，用户指责 AMD 的财务逻辑和疏远 Linux 开发者基础。一些人将 Lattice 更慷慨的免费许可政策与之对比，另一些人则抱怨 AMD 管理下许可流程带来的麻烦。

**标签**: `#FPGA`, `#AMD`, `#Vivado`, `#Linux`, `#ecosystem`

---

<a id="item-6"></a>
## [AI 对 HBM 的需求推高消费电子价格](https://simonwillison.net/2026/May/22/memory-shortage/#atom-everything) ⭐️ 7.0/10

内存制造商正在将晶圆产能从 DDR 和 LPDDR 转向 HBM，导致消费级内存价格大幅上涨，特别是 100 美元以下的智能手机。 消费电子的重新定价将影响数十亿用户，尤其是在新兴市场，并标志着 AI 基础设施投资挤占主流设备的结构性转变。 HBM 每 GB 消耗的晶圆容量是 DDR 或 LPDDR 的三倍以上，其分配比例预计从 2%上升到 2026 年底的 20%。

rss · Simon Willison · 5月22日 22:01

**背景**: HBM（高带宽内存）是一种垂直堆叠的内存，可实现高带宽和低功耗，对 AI GPU 至关重要。内存制造商的晶圆制造能力有限，且因以往竞争对手破产的教训而倾向于供应不足。当 AI 需求激增时，它们优先生产高利润的 HBM，留给 PC 和智能手机所用 DDR 和 LPDDR 的产能减少。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://intuitionlabs.ai/articles/hbm-vs-ddr-memory-comparison">HBM vs. DDR: Key Differences in Memory Technology Explained | IntuitionLabs</a></li>

</ul>
</details>

**标签**: `#memory shortage`, `#consumer electronics`, `#AI infrastructure`, `#semiconductor industry`

---