---
layout: default
title: "Horizon Summary: 2026-05-24 (ZH)"
date: 2026-05-24
lang: zh
---

> 从 18 条内容中筛选出 6 条重要资讯。

---

1. [16 字节演示程序震撼呈现图形与声音](#item-1) ⭐️ 9.0/10
2. [诈骗者滥用微软内部账户发送垃圾邮件](#item-2) ⭐️ 8.0/10
3. [AMD 取消免费 Vivado 版本的 Linux 支持](#item-3) ⭐️ 8.0/10
4. [内存短缺推高消费电子产品价格](#item-4) ⭐️ 8.0/10
5. [微软开源最早的 DOS 源代码](#item-5) ⭐️ 7.0/10
6. [种子油恐慌危害心脏病人，医生指出](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [16 字节演示程序震撼呈现图形与声音](https://hellmood.111mb.de/wake_up_16b_writeup.html) ⭐️ 9.0/10

一款名为 'Wake up! 16b' 的新 16 字节 PC 演示程序能够实时生成图形和音频，将代码尺寸最小化推向了新的极限。 该演示表明，即使仅有 16 字节，也能实现令人印象深刻的视听效果，为演示场景和代码高尔夫社区带来进一步创新的启发。 该演示是一个 16 字节的 .com 文件，在 PC 硬件上运行，产生彩色动画图案并伴有同步音效，很可能使用了 BIOS 中断和自修改代码。

hackernews · MaximilianEmel · 5月24日 00:30 · [社区讨论](https://news.ycombinator.com/item?id=48253060)

**背景**: 演示场景（demoscene）是一个计算机艺术亚文化，专注于创建称为演示的自包含小型程序，用于制作视听展示。代码高尔夫（code golf）是一种竞赛，旨在为给定任务编写尽可能短的源代码。尺寸受限的演示（如 4K 和 64K 介绍）很常见，但用 16 字节实现图形和声音是汇编编程和优化的极致壮举。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Demoscene">Demoscene</a></li>
<li><a href="https://en.wikipedia.org/wiki/Code_golf">Code golf - Wikipedia</a></li>
<li><a href="https://www.jsalter.tech/posts/deconstruction-of-a-16-byte-demo-part-1">Deconstruction of a 16 byte demo - jsalter.tech</a></li>

</ul>
</details>

**社区讨论**: 社区成员表达了惊叹，有人表示这让他们陷入了长达一小时的探索，最终发现了一个用递归 PowerPoint 构建的谢尔宾斯基三角形。另有人指出，之前的 32 字节演示没有声音，因此这是杰作。还有人感叹行业工作很少允许这样的艺术创作。

**标签**: `#demoscene`, `#low-level programming`, `#minimalism`, `#assembly`, `#code golf`

---

<a id="item-2"></a>
## [诈骗者滥用微软内部账户发送垃圾邮件](https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/) ⭐️ 8.0/10

诈骗者正在利用一个通常用于发送合法账户提醒的微软内部账户，发送垃圾邮件和钓鱼链接。由于邮件来自受信任的微软域，这种滥用绕过了传统的电子邮件安全过滤器。 这种攻击削弱了用户对微软官方通信的信任，并凸显了微软在域管理和电子邮件安全方面的弱点。它可能导致依赖域验证来识别合法邮件的用户更容易遭受钓鱼攻击。 此次滥用涉及从‘microsoftonline.com’域发送垃圾邮件，该域是微软用于发送双因素认证代码等通知的合法域。具体技术漏洞尚未公开，但可能涉及某种形式的域欺骗或配置错误。

hackernews · spike021 · 5月24日 00:51 · [社区讨论](https://news.ycombinator.com/item?id=48253186)

**背景**: 微软使用‘microsoftonline.com’等内部域向用户发送自动账户通知。诈骗者找到了一种方法，让邮件看起来来自这个受信任的域，从而使他们的钓鱼尝试更具说服力。这是攻击者利用合法服务绕过电子邮件安全措施这一更广泛趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/">Scammers are abusing an internal Microsoft account to send spam links ...</a></li>
<li><a href="https://sesamedisk.com/microsoft-internal-account-abuse-2026-cybersecurity/">Microsoft Internal Account Abuse in 2026: Cybersecurity Threats and ...</a></li>
<li><a href="https://mashable.com/tech/scammers-weaponizing-official-microsoft-email-address">Internal Microsoft account being used to send scams, phishing links ...</a></li>

</ul>
</details>

**社区讨论**: 评论者对微软的域管理表示不满，指出公司拥有多个域使得难以判断哪些是合法的。一些人强调 Outlook 字体会使看似相似的域名（如‘rn’和‘m’）难以区分。其他人报告了微软验证器提示未知登录但登录历史为空的问题，暗示存在更广泛的安全问题。

**标签**: `#security`, `#microsoft`, `#phishing`, `#spam`, `#domains`

---

<a id="item-3"></a>
## [AMD 取消免费 Vivado 版本的 Linux 支持](https://adaptivesupport.amd.com/s/question/0D5Pd00001YQLdMKAX/why-is-vivado-20261-dropping-linux-support-for-free-tier-?language=en_US) ⭐️ 8.0/10

从 Vivado 2026.1 版本开始，AMD 取消了免费 Basic（Standard）版本的 Linux 支持，仅保留 Windows 支持，Linux 用户需付费订阅才能使用。 这一变化疏远了依赖 Linux 的学生、爱好者和开发者，可能缩小 FPGA 开发社区并损害 AMD 的生态系统增长，而竞争对手如 Lattice 在 Linux 上仍提供免费工具。 Vivado Standard Edition（免费版本）将不再支持 Linux；仅付费的 Enterprise 和 Core/Pro 订阅包含 Linux 支持。AMD 称这是为了集中资源，但用户批评这是推动付费许可的举措。

hackernews · zdw · 5月24日 04:14 · [社区讨论](https://news.ycombinator.com/item?id=48254309)

**背景**: Vivado 是 AMD（前 Xilinx）的 FPGA 设计套件。免费 Standard Edition 面向低成本器件，而 Enterprise Edition 需要付费许可。Linux 在 FPGA 开发中广泛用于脚本和自动化，因此这一限制构成了重大障碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado/vivado-licensing-options.html">AMD Vivado™ Licensing Options | Flexible Subscription & Perpetual Tiers</a></li>
<li><a href="https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado/vivado-buy.html">AMD Vivado™ Design Suite: Standard & Enterprise Edition</a></li>

</ul>
</details>

**社区讨论**: 社区情绪普遍负面。用户如 akarambir 和 nmaludy 表示沮丧，指出 Linux 用户被疏远并建议转向 Lattice 等竞品。snarfy 称之为“会计逻辑”，jkubic 和 jwrallie 批评了这种不便及其对教育的影响。

**标签**: `#FPGA`, `#AMD`, `#Vivado`, `#Linux`, `#EDA`

---

<a id="item-4"></a>
## [内存短缺推高消费电子产品价格](https://simonwillison.net/2026/May/22/memory-shortage/#atom-everything) ⭐️ 8.0/10

内存制造商正将晶圆产能从 DDR/LPDDR 重新分配给用于 AI 数据中心的 HBM，导致短缺，这将推高使用内存的消费电子产品价格。预计到 2026 年底，HBM 的晶圆产能分配将从 2%升至 20%。 这一转变将显著增加消费设备中内存的成本，尤其影响非洲和南亚等市场的百元以下智能手机。它说明了 AI 基础设施的旺盛需求如何间接影响日常电子产品及全球消费者。 每 GB 的 HBM 消耗的晶圆产能是每 GB 的 DDR 或 LPDDR 的三倍以上。内存公司从过去竞争对手破产中吸取教训，倾向于产能保守而非过度建设，导致未来数年内消费设备内存生产受限。

rss · Simon Willison · 5月22日 22:01

**背景**: 高带宽内存（HBM）是一种与 GPU 配合使用的 3D 堆叠内存接口，用于高性能计算，尤其是 AI 工作负载。晶圆产能是指半导体工厂能加工的硅晶圆数量，该数量固定且需分配给不同类型的内存。目前全球仅有三家主要内存制造商（三星、SK 海力士、美光），它们都在将重心转向利润更丰厚的 HBM 市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wafer_(electronics)">Wafer (electronics) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#memory shortage`, `#HBM`, `#consumer electronics`, `#pricing`, `#AI infrastructure`

---

<a id="item-5"></a>
## [微软开源最早的 DOS 源代码](https://arstechnica.com/gadgets/2026/04/microsoft-open-sources-the-earliest-dos-source-code-discovered-to-date/) ⭐️ 7.0/10

微软于 2026 年 4 月 28 日在其开源博客上宣布，开源了已知最早的 DOS 源代码。这是 MS-DOS 早期版本首次以开源许可证形式公开。 此次发布提供了一个罕见的历史文物，展示了 MS-DOS 的起源——这个操作系统开启了微软在 PC 时代的统治地位。它使开发者、历史学家和复古计算爱好者能够研究早期软件工程实践以及操作系统的演变。 该源代码使用汇编语言编写，代表已知最早的 DOS 版本。微软此前还开源了其早期的 6502 BASIC，这与公司的早期历史密切相关。

hackernews · DamnInteresting · 5月24日 01:21 · [社区讨论](https://news.ycombinator.com/item?id=48253386)

**背景**: MS-DOS（微软磁盘操作系统）是 20 世纪 80 年代初为 IBM PC 开发的基于文本的命令行操作系统。它最初基于 QDOS（快速粗糙操作系统），并成为微软早期成功的基础。开源这些代码让人们能够详细审视开启 PC 革命的软件。

**社区讨论**: 评论者表达了感谢和怀旧之情，许多人强调了 DOS 及相关 BASIC 源代码的历史意义。一些用户指出，几千行汇编代码就足以创办一家成功的软件公司，反映了早期计算的简单性。

**标签**: `#open source`, `#DOS`, `#Microsoft`, `#history`, `#retrocomputing`

---

<a id="item-6"></a>
## [种子油恐慌危害心脏病人，医生指出](https://www.statnews.com/2026/05/22/seed-oils-healthy-fats-tallow-fact-check-cardiac-health/) ⭐️ 6.0/10

一位医学专业人士发表文章指出，对种子油的普遍恐慌是没有根据的，实际上可能会伤害心脏病患者，因为这会阻止他们使用有益心脏健康的不饱和脂肪。 这很重要，因为种子油在流行的健康讨论中被妖魔化，然而科学证据支持它们对心脏健康的益处，背离这些饮食建议可能会导致心脏病患者情况恶化。 种子油包括常见的烹饪油，如大豆油、菜籽油、葵花籽油和玉米油，它们富含多不饱和脂肪，并且已被证明在替代饱和脂肪时可以降低低密度脂蛋白胆固醇。

hackernews · randycupertino · 5月24日 14:27 · [社区讨论](https://news.ycombinator.com/item?id=48257532)

**背景**: 种子油是从种子中提取的植物油。近年来，一些社交媒体影响者和健康倡导者声称种子油有毒或引起炎症，导致公众抵制。然而，美国心脏协会等主要健康组织建议用菜籽油和橄榄油等不饱和脂肪替代饱和脂肪，以降低心脏病风险。

**社区讨论**: 评论显示了分歧：一些用户报告了种子油引起的自身炎症，而另一些人则认为这种广泛恐慌分散了对糖摄入等更大问题的注意力。还有用户指出该话题的政治极化。

**标签**: `#seed oils`, `#nutrition`, `#public health`, `#cardiac health`

---