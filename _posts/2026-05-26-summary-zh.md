---
layout: default
title: "Horizon Summary: 2026-05-26 (ZH)"
date: 2026-05-26
lang: zh
---

> 从 24 条内容中筛选出 11 条重要资讯。

---

1. [放慢速度，用 AI 写出更好的代码](#item-1) ⭐️ 8.0/10
2. [挪威国家图书馆用 2PB 闪存构建主权大语言模型](#item-2) ⭐️ 8.0/10
3. [Mullvad 推出针对出口 IP 指纹识别的缓解措施](#item-3) ⭐️ 8.0/10
4. [加州提议将 Linux 从年龄验证法中豁免](#item-4) ⭐️ 8.0/10
5. [教皇利奥十四世发布人工智能伦理通谕](#item-5) ⭐️ 8.0/10
6. [研究：步行比坐着更能激发创造力](#item-6) ⭐️ 7.0/10
7. [编程书籍衰落：销售数据与社区见解](#item-7) ⭐️ 7.0/10
8. [Armin Ronacher 批评 AI 生成的错误报告](#item-8) ⭐️ 7.0/10
9. [沙米尔秘密共享原理解析](#item-9) ⭐️ 6.0/10
10. [Datasette 1.0a30 添加可定制‘跳转至’菜单](#item-10) ⭐️ 6.0/10
11. [Claude AI 根据 PDF 重现 1983 年游戏《Mad House》](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [放慢速度，用 AI 写出更好的代码](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/) ⭐️ 8.0/10

文章主张通过缓慢、迭代的过程来使用 AI 编写更好的代码，其中不同的 AI 模型分别负责设计、实现和审查，而不是追求速度。 这挑战了用 AI 快速生成代码的主流范式，强调质量而非速度，可能引导出更审慎可靠的 AI 辅助工程实践。 提议的工作流将职责分配到不同模型：一个负责设计（如 Claude），一个负责实现（如 Claude 4.7 Max），一个负责代码审查（如 Codex GPT 5.5）。社区成员指出，这种迭代过程通常比手动编写代码耗时更长，但能产出更高质量。

hackernews · signa11 · 5月25日 23:16 · [社区讨论](https://news.ycombinator.com/item?id=48272984)

**背景**: AI 代码生成工具传统上强调速度，使用单一提示快速生成代码。迭代提示和多智能体协作是新兴技术，将代码生成视为一个精炼过程，通过反复反馈循环提高准确性和鲁棒性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/compiler-loop-how-we-turned-ai-code-generation-mario-rodriguez-mier-9ziae">The Compiler Loop: How We Turned AI Code Generation into an ...</a></li>
<li><a href="https://arxiv.org/pdf/2404.18496">AI -powered Code Review with LLMs : Early Results</a></li>
<li><a href="https://realpython.com/openrouter-api/">How to Use the OpenRouter API to Access Multiple AI Models via...</a></li>

</ul>
</details>

**社区讨论**: 评论反映了不同体验：有些人认为迭代循环虽然耗时，但能有效发现边缘情况；另一些人则认为审查和指导 LLM 比从头编写代码更费时。有评论者赞赏将 AI 用于审查不会外包思考，这与大规模生成代码不同。

**标签**: `#AI-assisted software development`, `#code quality`, `#code review`, `#LLM`, `#engineering practices`

---

<a id="item-2"></a>
## [挪威国家图书馆用 2PB 闪存构建主权大语言模型](https://www.blocksandfiles.com/flash/2026/05/22/norways-2-petabytes-of-huawei-flash-storage-and-llm-training/5244910) ⭐️ 8.0/10

挪威国家图书馆宣布正在构建一个主权挪威语大语言模型，使用 2PB 的华为闪存和一台配备 448 块 GPU 及 64512 个 CPU 核心的 HPE Cray 超级计算机。 该项目突显了小语种社区追求 AI 主权的趋势，确保本地文化和历史在 AI 模型中得到体现。同时，它也引发了关于如此中等的硬件是否足以训练出有竞争力的 LLM 的讨论。 存储设备来自华为，超级计算机是名为“Olivia”的 HPE Cray EX 系统，图书馆 IT 负责人表示没有商业提供商在开发挪威语 LLM。

hackernews · rbanffy · 5月25日 19:37 · [社区讨论](https://news.ycombinator.com/item?id=48270770)

**背景**: LLM 通常在海量多语言数据集上训练，但像挪威语这样的小语种可能服务不足。主权 LLM 允许国家控制自己的数据和模型，保护语言和文化遗产。挪威图书馆拥有大量的挪威语文本语料库，使其成为自然的数据集来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cray">Cray - Wikipedia</a></li>
<li><a href="https://www.hpe.com/us/en/cray-exascale-supercomputing.html">HPE Cray Supercomputing | HPE</a></li>

</ul>
</details>

**社区讨论**: 评论意见不一：有人质疑 448 块 GPU 是否足以训练一个完整的 LLM，认为在现有开源模型上进行微调可能更高效。其他人则赞赏图书馆现有的搜索界面，并争论在大型公司已经在多语言数据上训练的情况下，主权模型是否必要。

**标签**: `#LLM`, `#AI sovereignty`, `#flash storage`, `#Norway`, `#supercomputing`

---

<a id="item-3"></a>
## [Mullvad 推出针对出口 IP 指纹识别的缓解措施](https://mullvad.net/en/help/exit-ip-vpn-servers-mitigation-rollout) ⭐️ 8.0/10

Mullvad 已开始在其 VPN 服务器上推出缓解措施，以解决 2025 年 5 月 15 日首次报告的出口 IP 指纹识别漏洞。 这项缓解措施至关重要，因为出口 IP 指纹识别可能让网站通过分析 IP 分配模式来追踪 VPN 用户，从而损害隐私。Mullvad 的迅速反应增强了用户信任，并为 VPN 行业树立了良好榜样。 该缓解措施正在逐步部署，Mullvad 的帮助页面提供了已更新服务器的列表。值得注意的是，亚洲服务器尚未包含在此缓解措施中。

hackernews · Cider9986 · 5月25日 17:45 · [社区讨论](https://news.ycombinator.com/item?id=48269580)

**背景**: 出口 IP 指纹识别利用 VPN 提供商分配给用户的 IP 地址中的可预测模式，使网站即使在用户使用 VPN 时也能识别和追踪用户。Mullvad 将用户分配到每个服务器的多个出口 IP 的架构无意中造成了这种模式。缓解措施旨在随机化或掩盖这些模式以防止指纹识别。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mullvad.net/en/help/exit-ip-vpn-servers-mitigation-rollout">Exit IP VPN servers mitigation rollout | Mullvad VPN</a></li>
<li><a href="https://tech.yahoo.com/vpn/articles/mullvad-patch-vpn-fingerprinting-issue-142308257.html">Mullvad to patch VPN fingerprinting issue to stop your activity from...</a></li>
<li><a href="https://www.techradar.com/vpn/vpn-services/some-aspects-are-as-we-intended-and-some-are-not-mullvad-addresses-wireguard-exit-ip-fingerprinting-concern-after-researcher-flags-privacy-risk">'Some aspects are as we intended and some are not' — Mullvad ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 Mullvad 的快速反应表示惊讶和赞赏，一位用户提到他们已经在准备自己解决这个问题。一些人讨论了使用 Mullvad 浏览器或随机 IP 模式作为额外保护。少数用户批评了最初部署中排除亚洲服务器的做法。

**标签**: `#privacy`, `#VPN`, `#security`, `#fingerprinting`, `#Mullvad`

---

<a id="item-4"></a>
## [加州提议将 Linux 从年龄验证法中豁免](https://www.tomshardware.com/software/linux/california-moves-to-exempt-linux-from-its-upcoming-age-verification-law-after-backlash-over-forcing-operating-systems-to-collect-users-ages-amendment-proposed-by-the-same-lawmaker-who-wrote-the-original-law) ⭐️ 8.0/10

面对开源社区的强烈反对，加州立法者提出了一项修正案，旨在将 Linux 发行版从该州的年龄验证法中豁免。 这一政策转变为年龄验证法如何处理开源操作系统树立了先例，可能保护创新和用户隐私。它也展示了社区反对声音对立法决策的影响力。 这项豁免由原法案的同一立法者提出，表明立法机构对批评做出了回应。豁免的具体范围及其对 Linux 发行版的技术影响仍在界定中。

hackernews · rbanffy · 5月25日 18:19 · [社区讨论](https://news.ycombinator.com/item?id=48269961)

**背景**: 加州的年龄验证法最初要求操作系统收集用户年龄，以限制未成年人访问有害内容。批评者认为这会迫使 Linux 发行版实施侵入式追踪，违反开源原则。拟议的修正案旨在缓解这些担忧。

**社区讨论**: 社区评论中既有怀疑也有宽慰：一些人质疑该法律的意图和有效性，而另一些人怀疑豁免可能被用来削弱法律挑战。还有人对法律的复杂性和给消费者带来的负担表示不满。

**标签**: `#age-verification`, `#California law`, `#Linux`, `#open source`, `#tech policy`

---

<a id="item-5"></a>
## [教皇利奥十四世发布人工智能伦理通谕](https://simonwillison.net/2026/May/25/encyclical-on-ai/#atom-everything) ⭐️ 8.0/10

教皇利奥十四世于 2026 年 5 月 25 日发布了首部通谕《壮丽人性》，探讨人工智能伦理融入社会，并引用教宗利奥十三世 1891 年关于劳工的通谕《新事》。 这份通谕标志着宗教界在人工智能讨论中的重要伦理介入，可能通过将人工智能界定为人类尊严与社会正义问题，影响全球政策与公众认知。 文件强调了大语言模型的“可解释性问题”，指出它们“更像被培育而非被构建”，其内部过程仍未知。它还强调真正的发展必须以人为中心，且不能将负担转嫁给他人。

rss · Simon Willison · 5月25日 23:58

**背景**: 通谕是教皇写给天主教会乃至全世界的正式信件。教宗利奥十四世选择此名以纪念教宗利奥十三世，后者曾在工业革命时期的《新事》（1891 年）中探讨社会问题。这份新通谕将类似教义应用于人工智能革命，为维护人类尊严提供伦理指导。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vaticannews.va/en/pope/news/2026-05/pope-leo-xiv-encyclical-magnifica-humanitas-ai.html">Pope Leo’s ‘Magnifica humanitas’: AI must serve humanity not concentrate power - Vatican News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Magnifica_humanitas">Magnifica humanitas - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#Vatican`, `#Religious perspective`, `#Technology and society`

---

<a id="item-6"></a>
## [研究：步行比坐着更能激发创造力](https://www.apa.org/news/press/releases/2014/04/creativity-walk) ⭐️ 7.0/10

美国心理学会 2014 年发表的一项研究发现，步行比坐着能显著提升创造性思维。步行参与者在创造力测试中产生了更多新颖且恰当的想法。 这一发现挑战了关于工作空间设计和生产力的假设，表明融入步行休息有助于提高问题解决能力和创新。社区讨论提供了现实世界的验证，许多人分享了步行时创造力提升的个人经历。 该研究通过实验让参与者在使用跑步机行走或坐着时完成吉尔福德的替代用途测试。步行平均使创造性产出提高 60%，无论步行是在室内还是室外。

hackernews · bilsbie · 5月25日 22:30 · [社区讨论](https://news.ycombinator.com/item?id=48272670)

**背景**: 许多认知过程（包括创造力）受益于轻度身体活动，它能增加大脑血流量。这种现象常被称为“孵化效应”，即暂时离开问题让潜意识继续工作。这项研究为长期存在的关于步行与灵感的传闻提供了实证支持。

**社区讨论**: 评论者普遍证实了该研究的发现，分享了在步行、跑步甚至睡眠中解决问题的个人经历。一些人强调无干扰运动的重要性，而另一些人指出站立式办公桌也能增强专注，但方式更具对抗性。

**标签**: `#creativity`, `#walking`, `#productivity`, `#psychology`, `#problem-solving`

---

<a id="item-7"></a>
## [编程书籍衰落：销售数据与社区见解](https://unix.foo/posts/nobody-cracks-open-a-programming-book/) ⭐️ 7.0/10

一篇题为'没人再翻编程书了'的博文，借助出版商销售数据和社区反思，讨论了编程书籍的衰落以及向在线资源的转变。 这一趋势影响开发者学习方式和编程语言的复杂性，书籍曾约束语言膨胀，同时也影响作者和出版商的收入。 《Learning Go》作者报告每月平装本销量平均约 200-300 本，自 2021 年来总计 2 万本。社区成员指出，有些学习者仍从书籍中受益，尤其是对于像 Rust 这样复杂的语言。

hackernews · zdw · 5月25日 23:21 · [社区讨论](https://news.ycombinator.com/item?id=48273030)

**背景**: 编程书籍传统上是主要学习资源，但在线教程、文档以及 Stack Overflow 等论坛的兴起改变了偏好。这种衰落也可能反映编程语言日益复杂，使全面书籍更难维护。

**社区讨论**: 评论者分享了不同经历：一位作者提供了具体销售数据，显示下降但时有波动；另有人认为书籍缺失解除了对语言复杂度的约束；还有一位赞扬阅读书籍深入学习 Rust。大家一致认为书籍形式不再流行，但某些主题仍具价值。

**标签**: `#programming books`, `#learning`, `#developer culture`, `#software engineering`, `#trend analysis`

---

<a id="item-8"></a>
## [Armin Ronacher 批评 AI 生成的错误报告](https://simonwillison.net/2026/May/24/armin-ronacher/#atom-everything) ⭐️ 7.0/10

Flask 创始人 Armin Ronacher 批评 AI 生成的 bug 报告不准确且充满自信但错误，并建议采用简洁的人工观察格式：运行了什么命令、预期结果、实际结果以及确切的错误信息。 此事很重要，因为 AI 生成的 bug 报告正泛滥于开源项目，浪费维护者时间。Ronacher 的实用建议有助于提高报告质量，减少维护者困扰。 Ronacher 提出的格式包含四个步骤：运行的命令、期望行为、实际行为以及确切的错误/日志。他还批评了那些将观察到的问题重写为冗长不准确报告的 'clanker' AI 工具。

rss · Simon Willison · 5月24日 18:46

**背景**: AI 工具被越来越多地用于生成 bug 报告，但它们常常产生听起来自信但错误的结论。此现象已引起 Linus Torvalds 等知名人物的批评，他表示 AI 生成的 bug 报告使内核邮件列表难以管理。'clanker' 一词已出现，用于描述生成低质量提交的 AI 机器人。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.biggo.com/news/x5n6OZ4BoQmpnl36Ngdg">Torvalds Slams 'Unmanageable' AI Bug Reports as Greg KH's Clanker Bots ...</a></li>
<li><a href="https://cybersecuritynews.com/linus-torvalds-on-ai-bug-reports/">Linus Torvalds says AI Bug Reports Have Made Linux Security Mailing ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Clanker">Clanker - Wikipedia</a></li>

</ul>
</details>

**标签**: `#open source`, `#AI`, `#bug reporting`, `#software engineering`

---

<a id="item-9"></a>
## [沙米尔秘密共享原理解析](https://ente.com/blog/how-shamirs-secret-sharing-works/) ⭐️ 6.0/10

一篇博客文章解释了沙米尔秘密共享，这是一种将秘密拆分成多个份额的密码学技术，只有达到阈值数量的份额才能恢复秘密。社区讨论探讨了其在 DNS 密钥管理中的应用以及与里德-所罗门码的比较。 沙米尔秘密共享是分布式系统中安全密钥分发和备份的基础，允许在不需要所有方都可用的情况下建立信任。该教程使这一概念对更广泛的受众（包括教育者和实践者）变得易于理解。 该方案使用多项式插值：将秘密编码为一个 k-1 次随机多项式的常数项，份额是该多项式上的点。社区指出，对于大秘密，通常结合加密使用沙米尔份额，并将其与缺乏信息论安全性的里德-所罗门码进行比较。

hackernews · subract · 5月25日 22:37 · [社区讨论](https://news.ycombinator.com/item?id=48272715)

**背景**: 秘密共享是一种密码学方法，将秘密分割成多个份额并分发给参与者。沙米尔秘密共享由阿迪·沙米尔于 1979 年提出，利用多项式插值使得任意 k 个份额（共 n 个）可以重构秘密，但少于 k 个则无法获得任何信息。它广泛应用于密钥管理、多方计算和安全备份系统。

**社区讨论**: 评论者称赞该技术可在学校教授，并讨论了诸如根 DNS 密钥管理等实际应用。一些人将其与里德-所罗门码和 par2 恢复进行比较，指出了安全性和性能上的权衡。还分享了一个实现链接作为参考。

**标签**: `#cryptography`, `#secret sharing`, `#shamir`, `#tutorial`

---

<a id="item-10"></a>
## [Datasette 1.0a30 添加可定制‘跳转至’菜单](https://simonwillison.net/2026/May/24/datasette/#atom-everything) ⭐️ 6.0/10

Datasette 1.0a30 引入了一个可定制的“跳转至”菜单，通过按 '/' 键触发，并新增了一个 'jump_items_sql()' 插件钩子，允许插件添加可搜索的项。 此功能增强了 Datasette 的导航性，并通过插件使其更具扩展性，这对于管理大型数据库并希望快速访问的用户来说很重要。 该菜单可以通过新钩子由插件定制；在官方 Datasette 实例上提供了动画演示。它是 alpha 版本 1.0a30 的一部分。

rss · Simon Willison · 5月24日 23:52

**背景**: Datasette 是一个用于探索和发布数据的开源工具。它允许用户加载各种形状的数据，并将其发布为交互式网站和 API。插件可以扩展其功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datasette.io/">Datasette: An open source multi-tool for exploring and publishing data</a></li>
<li><a href="https://docs.datasette.io/en/latest/writing_plugins.html">Writing plugins - Datasette documentation</a></li>

</ul>
</details>

**标签**: `#datasette`, `#data exploration`, `#plugins`, `#release`

---

<a id="item-11"></a>
## [Claude AI 根据 PDF 重现 1983 年游戏《Mad House》](https://simonwillison.net/2026/May/24/usborne-mad-house/#atom-everything) ⭐️ 6.0/10

Simon Willison 使用 Anthropic 的 Claude AI 将 1983 年 Usborne 书籍《Creepy Computer Games》的 PDF 扫描件转换成了可完全运行的 JavaScript 和 HTML 版本游戏《Mad House》。 该项目展示了 AI 如何从扫描文档中快速现代化老旧软件，使经典游戏无需手动转录即可在现代浏览器中运行。 Willison 的提示要求 Claude 创建一个具有复古风格且移动友好的纯 JS 项目，并注明原书来源，链接到 Usborne 的免费 PDF。

rss · Simon Willison · 5月24日 17:14

**背景**: Claude 是 Anthropic 公司开发的一系列大型语言模型，于 2023 年 3 月发布，可用于代码生成等任务。Usborne 出版社免费发布了其 1980 年代的计算机书籍 PDF，读者可以像当年在 Commodore 64 上那样键入并运行《Mad House》等程序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_AI">Claude AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#retro gaming`, `#AI-assisted coding`, `#JavaScript`, `#nostalgia`, `#Claude`

---