---
layout: default
title: "Horizon Summary: 2026-09-07 (ZH)"
date: 2026-09-07
lang: zh
---

> 从 21 条内容中筛选出 11 条重要资讯。

---

1. [OpenAI 高管称尚无实验室解决 AI 对齐问题，呼吁放慢发展](#item-1) ⭐️ 9.0/10
2. [GPT-6 Astra 开发者版发布，展示先进 3D 建模能力](#item-2) ⭐️ 9.0/10
3. [坎特里尔：用 LLM 代笔而不披露等于“智识的拉链没拉”](#item-3) ⭐️ 8.0/10
4. [Asahi Linux 正式支持 M3 芯片](#item-4) ⭐️ 8.0/10
5. [OpenAI 揭开递归自我改进与编码智能体采用内幕](#item-5) ⭐️ 8.0/10
6. [将 Python 解释器压缩进 1024 字节 C 代码](#item-6) ⭐️ 7.0/10
7. [Anubis 作者回顾耗时一年集成 WebAssembly 的历程](#item-7) ⭐️ 7.0/10
8. [Nitter 与 XCancel 在获得法律意见后恢复服务](#item-8) ⭐️ 7.0/10
9. [GrapheneOS Overhauled Default Apps and Secure Clipboard](#item-9) ⭐️ 7.0/10
10. [报告：每五个新注册的通用顶级域中约有一个可能用于诈骗](#item-10) ⭐️ 7.0/10
11. [Simon Willison：彻底重写遗留软件很少成功](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI 高管称尚无实验室解决 AI 对齐问题，呼吁放慢发展](https://openai.com/index/an-alien-mind/) ⭐️ 9.0/10

在一篇名为《An Alien Mind》的新 OpenAI 博文中，一位 OpenAI 领导层成员表示，目前没有任何实验室在 AI 对齐与监控方面达到足以负责任地继续以最大速度扩张的程度。文章呼吁行业主动减速，并希望各国政府将未来 AI 发展的国际协调列为最高优先事项。 这一表态意义重大，因为它来自一家正在快速扩张强大模型的顶级 AI 实验室内部，凸显出越来越多的人意识到对齐研究已落后于能力发展。它可能影响 AI 安全讨论，并推动各国政府将国际协调视为紧迫任务而非可有可无的选项。 文中还承认，继续快速训练更智能模型的最强理由是需要构建防御系统，以应对其他 AI 带来的危险，这是一种军备竞赛逻辑。作者还表示，预计在建立“共同安全标准”之前，自愿减速将变得普遍。

hackernews · tosh · 9月6日 16:27 · [社区讨论](https://news.ycombinator.com/item?id=49588080)

**背景**: AI 对齐（AI alignment）是 AI 安全的一个子领域，目标是让 AI 系统朝着符合人类意图和价值观的方向运行，避免奖励作弊（reward hacking）、策略性欺骗或追求权力等失当行为。已有实证研究发现，高级大语言模型有时会表现出欺骗性行为，许多研究者认为这些风险会随能力增强而上升。这篇文章参与了一场更广泛的讨论：各国政府和实验室是否应放慢 AI 能力发展的步伐，以及如何建立有效的国际治理机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有人强调这篇文章核心信息的重要性，也有人以讽刺回应，想象“外星博物馆”会如何注解人类未能放慢脚步的失败。有评论指责这篇博文是上市前的造势——一个以拯救人类为宗旨的慈善机构，如今却把“末日机器”的一部分拿到纳斯达克上市。另一些评论者认真讨论了军备竞赛论点，担心中国开源模型会在缺乏协调约束的情况下持续进步。

**标签**: `#AI alignment`, `#AI safety`, `#OpenAI`, `#policy`, `#arms race`

---

<a id="item-2"></a>
## [GPT-6 Astra 开发者版发布，展示先进 3D 建模能力](https://simonwillison.net/2026/Sep/5/introducing-gpt-6-astra-for-developers/) ⭐️ 9.0/10

西蒙·威利森重点介绍了 OpenAI 面向开发者发布的 GPT-6 Astra，指出该模型在细节关注度和生成复杂 3D 模型（如花园、造船厂、戴森球）方面表现出色。他还提到一个反复出现的视觉梗：Astra 总是生成一只戴着红领巾、骑着自行车的鹈鹕。 这是 OpenAI 下一代旗舰模型首次面向开发者发布的重要举措，表明其正大力推进多模态生成和 3D 资产生成能力。依赖生成式 AI 进行设计、游戏开发和可视化的开发者，可能会从 Astra 改进的 3D 建模能力中获得显著收益。 GPT-6 Astra 于 2026 年 9 月 3 日作为有限预览向可信合作伙伴发布，支持从低到极高的推理力度设置。根据 OpenAI API 文档，它是该公司目前最强的模型，专为复杂推理、编程、计算机操作、研究和文档生成而设计。

rss · Simon Willison · 9月5日 23:27

**背景**: GPT-6 Astra 是 OpenAI 最新的大型语言模型，延续了之前的 GPT 系列，与全面公开发布不同，它以有限预览形式提供给可信合作伙伴。西蒙·威利森是知名开发者兼博主，经常分析新 AI 发布动态；他的文章突出介绍了一个有趣且有启发性的怪现象——该模型总会生成一只系红领巾、骑自行车的鹈鹕。这个反复出现的模式说明，即使是先进的模型也会从训练数据中形成某种特性，为这篇技术性公告增添了一丝趣味。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT - 6 Astra - Wikipedia</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-6-astra">GPT - 6 Astra Model | OpenAI API</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT - 6 Astra : A new generation of intelligence | OpenAI</a></li>

</ul>
</details>

**标签**: `#GPT-6`, `#AI`, `#3D modeling`, `#developers`, `#OpenAI`

---

<a id="item-3"></a>
## [坎特里尔：用 LLM 代笔而不披露等于“智识的拉链没拉”](https://bcantrill.dtrace.org/2025/12/05/your-intellectual-fly-is-open/) ⭐️ 8.0/10

Bryan Cantrill 在 2025 年 12 月的一篇文章中提出，在未披露的情况下用 LLM 代笔发表文章，就像“智识的拉链没拉”：那种千篇一律的 AI 文字暴露了作者缺乏真实的个人思考与声音。 这一论点触及了 AI 辅助写作中关于真实性、作者身份与披露规范的关键争论。由于 Cantrill 是一位受人尊敬的技术专家，而文章在 Hacker News 上引发了 392 条评论，它很可能影响技术作者和博主对是否披露 LLM 使用的思考。 Cantrill 的核心比喻是，未披露的 LLM 代笔如同裤子拉链没拉——一种作者自己可能意识不到的明显难堪。他强调 LLM 不仅写得糟糕，而且“最关键的是：它们不是你”，因此让 LLM 代笔会抹掉使文字值得阅读的个人风格和怪癖。

hackernews · cyb0rg0 · 9月6日 11:56 · [社区讨论](https://news.ycombinator.com/item?id=49585644)

**背景**: 对许多专业人士而言，写作不只是把成熟的想法传达出来，它本身就是一种思考方式：动笔的过程会迫使你把模糊的念头逐条展开、厘清和修正。LLM 让人能快速生成漂亮的文字，但这不禁让人怀疑，最终的作品是否仍代表作者真正的观点和推理过程。Cantrill 此文刻意把未披露的 AI 代笔定义成一种伦理和智识层面的失败，而不只是一个文风问题。

**社区讨论**: 评论者大多赞同“写作就是思考”的观点，不少人警告说，让 LLM 代笔相当于跳过了写作过程中自我澄清的重要环节。也有人质疑这种论证框架：如果 LLM 的写作能力大幅提升，反对不披露的理由可能就不在于“写得差”了。jgrahamc 和 ericbarrett 等用户则强调，读者真正珍视的往往是作者真实的声音和个人风格。

**标签**: `#LLM`, `#AI ethics`, `#technical writing`, `#authenticity`

---

<a id="item-4"></a>
## [Asahi Linux 正式支持 M3 芯片](https://asahilinux.org/2026/09/m2-episode-1/) ⭐️ 8.0/10

Asahi Linux 在一篇新博文中宣布正式支持苹果 M3 系列芯片，这是其持续通过逆向工程将 Linux 带到 Apple Silicon Mac 上的最新进展。 这将为那些希望在 Mac 硬件上运行 Linux 而非 macOS 的用户扫除又一个障碍，也表明独立开发者通过逆向工程也能支持苹果较新的自研芯片。 官方 M3 支持是一个里程碑，但社区仍反馈存在 HDMI 输出缺失、睡眠支持不完整等缺口。用户还指出，在相同硬件上，苹果专有的 Metal 后端的 GPU 计算仍比当前 Linux 图形栈更快，这影响了像 llama.cpp 这样的工作负载。

hackernews · mdp2021 · 9月6日 14:08 · [社区讨论](https://news.ycombinator.com/item?id=49586698)

**背景**: Apple Silicon Mac 采用自研的 ARM 架构处理器，其图形、显示和电源管理硬件并未向第三方系统提供文档支持。Asahi Linux 是一个开源项目，通过逆向工程这些组件，在 M1 至 M3 及更新的芯片上提供成熟的 Linux 体验。由于芯片较新，驱动程序的开发和测试通常是分阶段推进的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Asahi_Linux">Asahi Linux - Wikipedia</a></li>
<li><a href="https://asahilinux.org/">Asahi Linux</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论总体上很积极，评论者称赞该团队的逆向工程工作。然而，一些用户表示仍然缺少 HDMI 和睡眠支持，阻碍了日常使用；还有一位开发者指出，在相同的 M1 Ultra 硬件上，运行 llama.cpp 时 Linux 下的性能远不如苹果 Metal 后端。

**标签**: `#linux`, `#apple-silicon`, `#asahi-linux`, `#reverse-engineering`, `#hardware`

---

<a id="item-5"></a>
## [OpenAI 揭开递归自我改进与编码智能体采用内幕](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/) ⭐️ 8.0/10

OpenAI 发布了两篇文章——《Research acceleration: The view inside OpenAI》和首席科学家 Jakub Pachocki 的《An Alien Mind》——将递归自我改进（RSI）定为核心主题，并披露了其研究人员如今如何依赖编码智能体。报告中的图表显示，研究人员每日 AI 支出中位数从 2026 年 2 月的接近零，飙升至 2026 年 8 月底的约 600 美元，且自 7 月下旬起急剧加速。 这是智能体工程（agentic engineering）已在一线 AI 实验室内部达到生产规模的具体证据，而不仅仅局限于外部开发者社区。这也表明 OpenAI 正在公开地将自己的路线图与递归自我改进挂钩，而这一概念具有重大的安全与战略影响。 文章中直接使用缩写 RSI 而未展开解释，Simon Willison 指出这或许有些脱离外界认知，因为该缩写尚未在 OpenAI 圈子之外普及。他推测，7 月下旬人均研究 AI 支出的飙升恰好与内部员工获得后来以 GPT-6 Astra 名义发布的模型访问权限的时间吻合。

rss · Simon Willison · 9月6日 23:57

**背景**: 递归自我改进是一种假设性过程：通用人工智能（AGI）系统通过改写自己的代码来增强能力，理论上可能导致智能爆炸。在实践中，现有系统大多仍处于“有界自我改进（bounded self-refinement）”阶段，而开放式 RSI 仍受制于锚定（grounding）要求和计算资源限制。与此同时，2026 年的编码智能体已从简单的自动补全发展为能自主驱动“编辑—测试—修复”循环的工具，这有助于解释 OpenAI 研究人员智能体使用量的急剧上升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://arxiv.org/abs/2607.07663">Recursive Self-Improvement in AI: From Bounded Self ...</a></li>
<li><a href="https://agentic.ai/best/coding-agents">20 Best AI Coding Agents in 2026 — Agentic.ai</a></li>

</ul>
</details>

**社区讨论**: 评论者的态度不一：有人对 OpenAI 所谓“为防御危险 AI 而必须推进 AI”的框架表示怀疑，也有人认为内部使用数据最为有趣。Simon Willison 批评文中未解释“RSI”这一缩写，hedgehog 则表示自己也有类似的工作流加速体验，但认为 OpenAI 每位研究员每天约 8000 美元的支出令人震惊。Jeff_Brown 提出了一个尚未得到解答的问题：如果早期某代模型未正确对齐，是否可能已经把风险传递给了后续模型。

**标签**: `#OpenAI`, `#Recursive Self-Improvement`, `#AI research`, `#coding agents`, `#AGI`

---

<a id="item-6"></a>
## [将 Python 解释器压缩进 1024 字节 C 代码](https://austinhenley.com/blog/python1024.html) ⭐️ 7.0/10

奥斯汀·亨利发布了一篇博客文章，展示了一个只有 1024 字节的 C 源文件，能够解释执行 Python 语言的一个极小部分。这个解释器依靠假设单个字母“f”“w”和“i”分别代表 for、while 和 if 来解析代码。 作为代码高尔夫和极小化语言工程的杰作，它能激发人们对解释器工作原理以及源码能压缩到多小的好奇心。它还引发了社区讨论：与 Snek 这类面向生产的微型语言相比，这种高度简化、依赖假设的解释器是否有价值。 这里的 1024 字节是指 C 源码大小，而不是编译后的可执行文件，后者要大得多。实现中循环的处理方式是每次迭代都跳回源码并重新解析，这让人想起 DOS 批处理文件的做法；同时它完全不进行语法检查。

hackernews · azhenley · 9月6日 23:14 · [社区讨论](https://news.ycombinator.com/item?id=49591876)

**背景**: 代码高尔夫是一种休闲编程竞赛，参赛者比拼用最短的源码解决给定问题。编写极小的编译器和解释器是经典的代码高尔夫挑战，知名例子包括小巧的 C 编译器 C4，以及面向仅有几 KB 闪存和内存的微控制器的可嵌入类 Python 语言 Snek。Snek 的设计目标是让程序能在完整的 Python 3 实现中运行，从而让所学知识可以直接迁移到真正的 Python 编程中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Code_golf">Code golf</a></li>
<li><a href="https://sneklang.org/">sneklang</a></li>
<li><a href="https://lwn.net/Articles/810201/">A tiny Python called Snek [LWN.net]</a></li>

</ul>
</details>

**社区讨论**: 读者反应不一：有人为这个巧妙的手工黑客技巧感到高兴，也有人批评它盲目假设任何“f”都是 for 且缺乏错误检查。有评论者推荐在内存受限设备上使用时选择 Snek，还有人称 1024 字节是 C 源码大小，不是编译后程序的体积。这篇帖子也让大家关注到作者之前的“teeny tiny compiler”项目。

**标签**: `#python`, `#interpreter`, `#code-golf`, `#minimalism`, `#c`

---

<a id="item-7"></a>
## [Anubis 作者回顾耗时一年集成 WebAssembly 的历程](https://anubis.techaro.lol/blog/2026/anubis-wasm/) ⭐️ 7.0/10

Anubis 项目的作者发布了一篇工程回顾，讲述了为集成 WebAssembly 支持并保持向后兼容性而进行的长达一年的努力。文章详细介绍了发布过程中遇到的权衡和约束。 Anubis 是一个被许多 Git 托管平台和自由软件项目采用的开源反爬虫防火墙，因此其验证挑战的可靠性和兼容性对大量网站都很重要。这篇回顾以坦诚的视角展示了维护者如何在引入 WebAssembly 等新能力与兼容旧浏览器和用户期望之间取得平衡。 向后兼容性深刻影响了这项工作，旧浏览器（如 Chrome 66）和许多智能电视被视为关键边缘情况。评论者还指出，Rust 的 wasm32v1-none target 可用于生成不带扩展的基线 WebAssembly，并提到这一改动收窄了类似“CUDA Anubis 求解器”的 AI 辅助破解路径。

hackernews · xena · 9月6日 20:32 · [社区讨论](https://news.ycombinator.com/item?id=49590611)

**背景**: Anubis 是一个开源工具，会向进入的 HTTP 请求发放工作量证明挑战，充当抵御爬虫机器人的防火墙；它常见于 Git 托管平台和自由软件项目。WebAssembly 是一种低级的、类似汇编的语言，可在浏览器中以接近原生的速度运行，并可作为 C/C++、Rust 等语言的编译目标，从而让更复杂或对性能敏感的代码在网页上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/TecharoHQ/anubis">GitHub - TecharoHQ/anubis: Weighs the soul of incoming HTTP ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anubis_(software)">Anubis (software) - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/WebAssembly">WebAssembly | MDN</a></li>

</ul>
</details>

**社区讨论**: 评论者赞赏作者关于开源维护者处境的诙谐语气，并感谢其在向后兼容性上投入的努力。一些人提到他们在 Firefox 中禁用了 WebAssembly，希望有回退提示；另一些人则建议为兼容性而使用与时代匹配或演进较慢的工具链，例如 ClojureScript。

**标签**: `#WebAssembly`, `#backward-compatibility`, `#open-source`, `#security`, `#engineering`

---

<a id="item-8"></a>
## [Nitter 与 XCancel 在获得法律意见后恢复服务](https://github.com/zedeus/nitter/commit/1428b4c2b4246f92a7e5b2673438e5fb39fcc4a3) ⭐️ 7.0/10

Nitter 与 XCancel.com 宣布在收到法律建议后恢复服务，逆转了之前因 X Corp 发出的停止并终止函而导致的关停。这两个项目于 2026 年 8 月 26 日暂停运营，目前表示很快会公布更多细节。 恢复服务使得一条保护隐私、访问 X/Twitter 内容的关键通道继续存在，这对不想被追踪或被迫登录的用户和记者尤为重要。这也表明，开源替代前端面对大型平台运营商施压时仍可能找到合法的运营方式。 Nitter 是一个免费开源的替代前端，允许用户在不看广告、不被追踪或无需账户的情况下浏览 X 的个人资料、时间线和搜索结果，并支持 RSS 订阅。XCancel 依赖 Nitter 在其他网站上嵌入 X 帖子；这两个项目此前都曾在 GitHub 和 XCancel.com 上发布过停止并终止通知。

hackernews · zImPatrick · 9月6日 17:49 · [社区讨论](https://news.ycombinator.com/item?id=49588988)

**背景**: 以 Nitter 为代表的替代前端充当代理，去除主流平台上的追踪、广告和登录要求，提供一种注重隐私的内容浏览方式。X Corp 曾发出停止并终止函，指控这些项目抓取和镜像推文，导致它们暂时关闭。获得的法律建议显然使维护者相信这些项目可以继续运营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nitter">Nitter - Wikipedia</a></li>
<li><a href="https://github.com/zedeus/nitter">GitHub - zedeus/nitter: Alternative Twitter front-end · GitHub</a></li>
<li><a href="https://www.forbes.com/sites/siladityaray/2026/08/26/cease-and-desist-from-x-shuts-down-nitter-and-xcancel-sites-that-scraped-and-mirrored-tweets/">Nitter And XCancel Shutdown After ‘Cease And Desist’ From ...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍对这一消息表示欢迎，称 Nitter 在读取仅在 X 上发布的紧要信息时很有价值，并对替代前端表示赞赏。有人担忧小型项目面对大公司时承受的法律和资金压力，另一些人则指出当前网络更广泛的问题：匿名浏览日益受阻，内容集中在少数几个平台上。

**标签**: `#Nitter`, `#privacy`, `#open-source`, `#legal`, `#Twitter`

---

<a id="item-9"></a>
## [GrapheneOS Overhauled Default Apps and Secure Clipboard](https://grapheneos.social/@GrapheneOS/117225539756835649) ⭐️ 7.0/10

GrapheneOS announces plans to overhaul or replace default AOSP apps, including a secure clipboard and new SMS/RCS app, sparking community discussion about the project's direction.

hackernews · Cider9986 · 9月6日 20:24 · [社区讨论](https://news.ycombinator.com/item?id=49590512)

**标签**: `#GrapheneOS`, `#Android`, `#Privacy`, `#Security`, `#Mobile OS`

---

<a id="item-10"></a>
## [报告：每五个新注册的通用顶级域中约有一个可能用于诈骗](https://simonwillison.net/2026/Sep/6/the-purpose-of-dns-is-to-spread-scams/) ⭐️ 7.0/10

Terence Eden 引用 2026 年 Interisle 报告指出，2025 年新增的 8500 万个通用顶级域（gTLD）注册中，到 2025 年 5 月已有 850 万个被列入黑名单。他认为真实滥用率可能在 10% 到 20% 之间，使 DNS 成为诈骗的主要途径。 这一统计数字表明域名治理正面临持续危机，新注册域名中有相当比例被用于诈骗。它促使 ICANN 和安全专业人员把 DNS 滥用视为系统性问题，而非个别现象。 Interisle 报告聚焦于 gTLD 新增注册，并以被列入黑名单作为下限衡量。Eden 估计实际比例可能接近 20%，并指出 ICANN 多年来一直在讨论该问题，却未得到有效解决。

rss · Simon Willison · 9月6日 14:40

**背景**: 通用顶级域（gTLD）是不与国家或地区绑定的域名类别，例如 .com、.org、.io、.dev，以及 .blog、.shop 等较新的后缀。DNS 黑名单是记录滥用域名或 IP 地址的数据库，通常用于过滤垃圾邮件或恶意流量。ICANN 负责协调全球 DNS 并管理新顶级域的审批，但并不控制内容。该报告凸显了域名注册政策与实际犯罪使用之间的差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains">List of Internet top - level domains - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Domain_Name_System_blocklist">Domain Name System blocklist - Wikipedia</a></li>
<li><a href="https://www.icann.org/resources/pages/what-2012-02-25-en">What Does ICANN Do? - ICANN</a></li>

</ul>
</details>

**标签**: `#DNS`, `#security`, `#domain abuse`, `#ICANN`, `#scams`

---

<a id="item-11"></a>
## [Simon Willison：彻底重写遗留软件很少成功](https://simonwillison.net/2026/Sep/6/theres-no-limit-to-how-bad-code-can-get/) ⭐️ 7.0/10

Simon Willison 在 Lobste.rs 上发表评论指出，从头重写遗留系统很少成功，因为旧系统仍会作为业务核心不断变化，而新团队难以完全把握其行为和范围。他建议优先用自动化测试加固旧系统，并做有针对性的重构，而不是启动全新重写。 这一观点对软件工程中常见的“推倒重来”策略提出了务实警示，可能影响团队面对大量技术债务时的决策。它为全新项目的吸引力提供了一种现实的反驳，促使企业认真考虑更温和的替代方案。 Willison 特别指出两个风险：留在旧系统上的开发者没有动力付出超出最小限度的努力，而新系统最终可能只交付一部分功能，导致两套系统同时运行。他推荐阅读 Will Larson 的文章《Migrations: the sole scalable fix to tech debt》，认为这是负责任地完成这类迁移的最佳指南。

rss · Simon Willison · 9月6日 09:08

**背景**: 遗留系统是指仍在运行使用的旧软件，通常由过时的语言、框架或架构写成，且缺少自动化测试，导致重构风险很高。技术债务（technical debt）一词由 Ward Cunningham 于 1992 年提出，用来描述为了短期快速交付而牺牲代码质量所产生的未来返工成本。当债务大到难以承受时，完全替换系统看似很有吸引力，但旧系统长期运行导致其行为往往缺乏文档记录，这正是替换计划容易失败的原因之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Technical_debt">Technical debt</a></li>
<li><a href="https://en.wikipedia.org/wiki/Legacy_software">Legacy software</a></li>

</ul>
</details>

**标签**: `#technical-debt`, `#software-engineering`, `#rewrites`, `#legacy-systems`

---