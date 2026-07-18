---
layout: default
title: "Horizon Summary: 2026-07-18 (ZH)"
date: 2026-07-18
lang: zh
---

> 从 24 条内容中筛选出 13 条重要资讯。

---

1. [Moonshot AI 发布 2.8T 参数开源权重模型 Kimi K3](#item-1) ⭐️ 9.0/10
2. [凯撒护士称 AI 和监控工具使工作和护理恶化](#item-2) ⭐️ 8.0/10
3. [在宜居带岩石系外行星上首次探测到大气层](#item-3) ⭐️ 8.0/10
4. [SQLite 实用技巧：.expert、限定 AWS 凭证与备份](#item-4) ⭐️ 8.0/10
5. [Firefox 通过 WebAssembly 在另一个浏览器中运行](#item-5) ⭐️ 8.0/10
6. [Inkling：Thinking Machines Lab 发布 975B 参数开源 MoE 模型](#item-6) ⭐️ 8.0/10
7. [林纳斯·托瓦兹支持 AI 用于 Linux 开发](#item-7) ⭐️ 8.0/10
8. [Recurse Center 创始人感谢 HN 社区 15 年支持](#item-8) ⭐️ 7.0/10
9. [LLM 陈词滥调高亮工具帮助识别 AI 写作模式](#item-9) ⭐️ 7.0/10
10. [将高尔夫球场改为公园抵消数据中心用水](#item-10) ⭐️ 7.0/10
11. [GPT-5.6 Codex 漏洞可删除 $HOME 目录](#item-11) ⭐️ 7.0/10
12. [Zilog Z80 迎来 50 周年](#item-12) ⭐️ 6.0/10
13. [通过 WebAssembly 实现带颜色的 Mermaid 转 ASCII 艺术图](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Moonshot AI 发布 2.8T 参数开源权重模型 Kimi K3](https://simonwillison.net/2026/Jul/16/kimi-k3/#atom-everything) ⭐️ 9.0/10

Moonshot AI 发布了 Kimi K3，一个拥有 2.8 万亿参数的开源权重模型，并承诺在 2026 年 7 月 27 日前开放权重。该模型在自报基准上表现优于 Claude Opus 4.8 和 GPT-5.5。 此次发布标志着首个“开源 3T 级模型”的重大里程碑，可能使前沿 AI 能力更加普及。社区围绕基准可靠性的高度参与和辩论凸显了评估此类强大模型面临的持续挑战。 Kimi K3 在鹈鹕测试中使用的输出 token 数远多于之前的模型（16,658 个），并发现了一个约 85 token 的隐藏系统提示。定价为每百万输入 token 3 美元、输出 15 美元，是目前最贵的中国 AI 模型。

rss · Simon Willison · 7月16日 20:19 · [社区讨论](https://news.ycombinator.com/item?id=48947717)

**背景**: “骑自行车的鹈鹕”测试是由开发者 Simon Willison 创建的非正式基准测试，要求 LLM 生成一只骑自行车的鹈鹕的 SVG 图。根据斯坦福 HAI 的定义，开源权重模型公开释放核心模型参数，允许下载和使用。尽管有局限性，该基准测试常用于比较模型能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Pelican_on_a_bicycle_AI_benchmark">Pelican on a bicycle (AI benchmark)</a></li>
<li><a href="https://huggingface.co/spaces/victor/pelican-benchmark">Pelican Benchmark - a Hugging Face Space by victor</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**社区讨论**: 评论者指出鹈鹕测试可能受到污染，因为网上已有很多骑自行车的鹈鹕图片，一位用户指出 Simon 自己的博客可能就是来源。其他人指出该测试未评估代理工具调用能力，并建议对每个模型进行多次运行以进行更好的比较。

**标签**: `#AI`, `#Large Language Models`, `#Open Source`, `#Benchmarking`, `#Moonshot AI`

---

<a id="item-2"></a>
## [凯撒护士称 AI 和监控工具使工作和护理恶化](https://localnewsmatters.org/2026/07/15/kaiser-nurses-say-ai-workplace-surveillance-are-making-their-jobs-and-patient-care-worse/) ⭐️ 8.0/10

凯撒医疗集团的护士报告称，AI 和工作场所监控工具（包括呼叫中心指标和共情评估软件）增加了压力、降低了自主性，并对患者护理产生负面影响。 这凸显了医护人员与用于绩效监控的 AI 之间日益紧张的关系，可能影响员工士气、患者信任以及有益 AI 工具在医疗领域的采用。 文章指出，AI 共情工具是 2024 年的试点项目，现已停止，但护士仍面临指标驱动监控的压力。社区评论显示，一些员工认为医学 LLM 工具在翻译、笔记总结和决策支持方面很有价值。

hackernews · gnabgib · 7月17日 22:26 · [社区讨论](https://news.ycombinator.com/item?id=48952880)

**背景**: 护理领域的 AI 包括跟踪患者结果和用药准确性等指标的绩效监控系统，以及用于临床文档和翻译的医学大语言模型（LLM）等工具。电子健康记录（EHR）数据也可用于医疗实践监控。护士们担心，过度依赖指标可能优先考虑效率而非共情和以患者为中心的护理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11675209/">Artificial Intelligence in Nursing: Technological Benefits to Nurse’s Mental Health and Patient Care Quality - PMC</a></li>
<li><a href="https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2025.1666005/full">Frontiers | Artificial intelligence in nursing: a systematic review of attitudes, literacy, readiness, and adoption intentions among nursing students and practicing nurses</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映出分歧：有人认为投诉集中在指标滥用而非 AI 本身，而另一些人反对用机器评估共情。也有人分享了积极体验，比如一位医生喜欢 AI 笔记减轻压力。有评论者警告护士行为问题，但总体情绪是对监控和指标滥用保持谨慎。

**标签**: `#AI`, `#healthcare`, `#workplace surveillance`, `#ethics`

---

<a id="item-3"></a>
## [在宜居带岩石系外行星上首次探测到大气层](https://www.bbc.com/news/articles/cy4kdd1e0ejo) ⭐️ 8.0/10

天文学家利用 JWST 的透射光谱技术，在位于宜居带的岩石系外行星 LHS 1140b 上探测到了大气层。这是首次在可能支持生命的轨道上的类地行星上确认大气层。 这一发现是表征类地系外行星并评估其宜居性的重要一步。它展示了 JWST 研究岩石行星大气层的能力，最终可能有助于识别地球以外的生命迹象。 LHS 1140b 距离地球约 48 光年，围绕一颗红矮星运行。大气层的探测是通过 JWST 发射光谱在行星经过其恒星背后时进行的，排除了迷你海王星的可能性。

hackernews · neversaydie · 7月17日 14:06 · [社区讨论](https://news.ycombinator.com/item?id=48947560)

**背景**: 宜居带是恒星周围液态水可能存在于行星表面的区域。透射光谱分析恒星光线穿过行星大气层后的光谱，以揭示其成分。此前系外行星大气层的探测主要集中在气态巨行星上，这是首次在宜居带的岩石行星上实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Transmission_spectroscopy">Transmission spectroscopy</a></li>
<li><a href="https://en.wikipedia.org/wiki/Habitable_zone">Habitable zone</a></li>

</ul>
</details>

**社区讨论**: 一些评论者质疑 LHS 1140b 是否真正类地，指出红矮星不稳定且可能剥离大气。其他人则讨论未来推进技术以访问这类近邻系外行星，以及费米悖论的影响。JWST 数据似乎排除了迷你海王星，支持岩石成分。

**标签**: `#exoplanets`, `#astronomy`, `#atmosphere`, `#JWST`, `#habitable zone`

---

<a id="item-4"></a>
## [SQLite 实用技巧：.expert、限定 AWS 凭证与备份](https://jvns.ca/blog/2026/07/17/learning-about-running-sqlite/) ⭐️ 8.0/10

Julia Evans 的博文分享了运行 SQLite 的实用技巧，包括使用.expert 命令获取索引建议、生成限定范围的 AWS 凭证用于备份，以及使用.dump 和 zstd 压缩的高效备份命令。 这些技巧帮助开发者提升 SQLite 查询性能并简化备份流程，解决了索引调优和凭证管理等常见痛点，使 SQLite 更易于在生产环境中使用。 SQLite CLI 中的.expert 命令会分析查询并建议索引以提升性能；s3-credentials 工具生成仅限特定 S3 桶的读写、只读或只写凭证；备份命令`sqlite3 -readonly file.db .dump | zstd --fast --rsyncable`生成压缩转储，在使用 WAL 模式时不会阻塞写入操作。

hackernews · surprisetalk · 7月17日 17:45 · [社区讨论](https://news.ycombinator.com/item?id=48950122)

**背景**: SQLite 是广泛使用的嵌入式数据库引擎。.expert 命令自 SQLite 3.30.0 起可用，提供自动索引建议。管理 AWS 凭证可能繁琐且易出错；s3-credentials 工具通过生成限定桶的凭证简化这一过程。备份 SQLite 数据库可以使用.dump 生成可移植的 SQL 脚本，并通过管道传输到 zstd，提供高效压缩且适合 rsync 的输出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sqlite.org/cli.html">Command Line Shell For SQLite</a></li>
<li><a href="https://news.ycombinator.com/item?id=48950122">Learning a few things about running SQLite | Hacker News</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的社区讨论补充了更多技巧：分批删除、使用 SELECT 预加载行 ID 以避免阻塞，以及在备份时使用 WAL 模式允许并发读取。总体情绪积极，用户欣赏其实用价值，并结合自身经验进一步扩展了建议。

**标签**: `#sqlite`, `#databases`, `#backup`, `#command-line`, `#practical-tips`

---

<a id="item-5"></a>
## [Firefox 通过 WebAssembly 在另一个浏览器中运行](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 8.0/10

Puter 将 Mozilla Firefox（Gecko 引擎）编译为 WebAssembly，使得整个浏览器能通过使用 Wisp 协议的 WebSocket 代理在另一个浏览器中运行。演示展示了在 Chrome 内运行的完全可用的 Firefox 浏览网页。 该项目展示了使用 WebAssembly 在另一个浏览器中运行完整复杂浏览器的可行性，为跨浏览器测试、沙箱浏览和新的云计算模式开辟了可能性。它也凸显了 AI 辅助编程的潜力，因为大型语言模型帮助降低了开发成本。 编译后的 WebAssembly 二进制文件大小为 233 MB，另有一个 18 MB 的压缩资源包。所有网络流量均通过 Wisp 协议经过 Puter 的服务器代理，因为浏览器代码无法直接打开任意网络连接。支持端到端加密，并且已验证 HTTPS 流量会被加密。

rss · Simon Willison · 7月16日 23:34

**背景**: WebAssembly (WASM) 是一种低级二进制指令格式，能够在现代网络浏览器中以接近原生的速度运行。将像 Gecko 这样的完整浏览器引擎编译为 WASM 在技术上具有挑战性，因其规模和复杂性。该项目使用了 Claude Opus 和 Fable 等 AI 编程助手，估计 token 成本为 25,000 美元，但订阅计划降低了实际支出。类似项目 WebKitWasm 也将 WebKit 编译为 WASM，但目前没有在线演示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low-overhead, easy to implement protocol for proxying multiple TCP/UDP sockets over a single websocket. · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wire_protocol">Wire protocol</a></li>
<li><a href="https://puter.com/">Puter</a></li>

</ul>
</details>

**标签**: `#WebAssembly`, `#Firefox`, `#browser`, `#WebSocket`, `#demo`

---

<a id="item-6"></a>
## [Inkling：Thinking Machines Lab 发布 975B 参数开源 MoE 模型](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 8.0/10

Mira Murati 创立的 Thinking Machines Lab 发布了 Inkling，这是一个拥有 9750 亿参数的开放权重 MoE 多模态模型，采用 Apache-2.0 许可证，在 45 万亿 token 的文本、图像、音频和视频数据上训练。 此发布通过一个大规模、开放许可的模型增强了美国开源 AI 生态系统，与中国的模型竞争，为微调和定制提供了坚实基础。 Inkling 采用 MoE 架构，总参数量 975B，但每个 token 仅激活 41B；还承诺推出更小的变体 Inkling-Small（276B 总参数，12B 激活）。模型卡缺乏详细的训练数据文档。

rss · Simon Willison · 7月16日 15:35

**背景**: MoE（混合专家）是一种神经网络设计，每个输入只激活部分参数，使模型在保持推理效率的同时拥有大容量。在 MoE 模型中，“激活参数”指每个 token 激活的专家子集，远小于总参数量。这使得模型可以扩展到数千亿参数而计算成本不会成比例增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datanorth.ai/blog/what-is-mixture-of-experts-moe-and-why-does-it-matter">What is mixture of experts ( MoE ) and why does it matter?</a></li>
<li><a href="https://www.automataai.com.au/blog/moe-architecture-active-vs-total-parameters-explained">MoE Architecture: Active vs Total Parameters Explained | Automata AI...</a></li>
<li><a href="https://medium.com/ramses-engineering/not-one-brain-but-many-how-mixture-of-experts-moe-makes-ai-smarter-and-faster-568f41220852">Not One Brain, But Many: How Mixture of Experts ( MoE )... | Medium</a></li>

</ul>
</details>

**标签**: `#open-weights`, `#multimodal`, `#mixture-of-experts`, `#AI model release`

---

<a id="item-7"></a>
## [林纳斯·托瓦兹支持 AI 用于 Linux 开发](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linux 最高维护者林纳斯·托瓦兹在 Linux 媒体邮件列表上表示，AI 是 Linux 开发中一个明确有用的工具，该项目并非反 AI，并邀请反对者分叉或离开。 托瓦兹的这一明确公开表态在 Linux 社区中具有重大分量，标志着内核开发中向接纳 AI 工具的转变，可能影响开源软件工程的未来。 托瓦兹强调 AI 的有用性已不再是问题，尽管其他问题如经济影响仍存在，他并驳斥了那些实际上未使用过 AI 的批评者。

rss · Simon Willison · 7月16日 13:26

**背景**: 林纳斯·托瓦兹于 1991 年创建了 Linux 内核，并仍是其主要维护者。AI 工具，特别是大型语言模型（LLM），最近已在软件开发中被用于代码生成和调试等任务，但其在内核开发中的使用一直存在争议。托瓦兹的立场公开使 Linux 与开源界中支持 AI 的阵营保持一致。

**标签**: `#Linux`, `#Linus Torvalds`, `#AI`, `#open source`, `#kernel`

---

<a id="item-8"></a>
## [Recurse Center 创始人感谢 HN 社区 15 年支持](https://news.ycombinator.com/item?id=48949551) ⭐️ 7.0/10

Recurse Center（原 Hacker School）创始人近日在 Hacker News 上发表回顾文章，感谢社区 15 年来的支持，并指出 2011 年的一条 HN 帖子启动了该项目的起飞。 Recurse Center 已成为编程社区中备受喜爱的机构，为 3000 多名参与者提供了深度学习与协作的机会；其成功故事凸显了社区驱动、专注教育型项目的巨大潜力。 该 retreat 对参与者免费，资金来源于内置的招聘机构；在纽约或远程开展为期六或十二周的自我导向式批次。PG 在 HN 上的早期评论指出，虽然这不是一个十亿美元级别的生意，但这是一项善举。

hackernews · nicholasjbs · 7月17日 16:57

**背景**: Recurse Center 是一个为程序员设立的自我导向、社区驱动的教育性 retreat，源自 2010 年一个失败创业项目的转型（最初想做“求职版 OkCupid”）。起初名为 Hacker School。参与者在此进行项目开发、贡献开源并相互帮助提升。中心通过内置的招聘机构为毕业生推荐工作，从而让 retreat 对所有人免费。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.recurse.com/">The Recurse Center</a></li>
<li><a href="https://www.ycombinator.com/companies/recurse-center">Recurse Center : The retreat where curious programmers recharge...</a></li>
<li><a href="https://www.crunchbase.com/organization/hacker-school">Recurse Center - Crunchbase Company Profile & Funding</a></li>

</ul>
</details>

**社区讨论**: 评论主要为过往参与者的感谢与美好回忆，许多人表示 RC 改变了他们的人生。一名用户提出经济可及性问题，指出虽然学费免费，但纽约的生活费用仍需自理，这可能限制了那些无法承担脱产开销的人参与。

**标签**: `#Recurse Center`, `#programming retreat`, `#community`, `#YC`, `#lifelong learning`

---

<a id="item-9"></a>
## [LLM 陈词滥调高亮工具帮助识别 AI 写作模式](https://simonwillison.net/2026/Jul/17/llm-cliche-highlighter/#atom-everything) ⭐️ 7.0/10

Simon Willison 发布了一款名为 LLM 陈词滥调高亮器的 Web 应用，可自动高亮 LLM 生成文本中的十种常见陈词滥调模式，例如“is real and”和“worth naming”。 该工具解决了人们对公式化 AI 生成文本的普遍不满，帮助写作者、编辑和内容审核者快速识别并避免过度使用的表达，从而提升 AI 辅助内容的质量和自然度。 该应用可直接分析粘贴的文本或通过 r.jina.ai 代理加载 URL 内容，并支持链式模式（如“no X, no Y”）并显示计数徽章。它使用 Fable 5 通过“vibe coding”方式构建，即开发者描述目标后由 AI 生成代码。

rss · Simon Willison · 7月17日 12:11

**背景**: 像 ChatGPT 这样的 LLM 经常依赖某些陈词滥调（如“delve into”或“it's worth noting”），使得文本显得机械。Vibe coding 由 Andrej Karpathy 在 2025 年提出，是一种 AI 辅助编程实践，开发者通过提示词生成代码而几乎不做人工审查。r.jina.ai 服务可将任意 URL 转换为 LLM 友好的纯文本，便于分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tools.simonwillison.net/llm-cliche-highlighter">LLM cliché highlighter</a></li>
<li><a href="https://github.com/nanxstats/llm-cliches">GitHub - nanxstats/llm-cliches: A curated collection of commonly used clichés and phrases in Large Language Models outputs · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>

</ul>
</details>

**标签**: `#LLM`, `#cliché detection`, `#writing tools`, `#AI-generated text`, `#quality assurance`

---

<a id="item-10"></a>
## [将高尔夫球场改为公园抵消数据中心用水](https://simonwillison.net/2026/Jul/17/spot-birds-not-golf/#atom-everything) ⭐️ 7.0/10

谷歌等超大规模云服务商因数据中心用水面临压力；Simon Willison 建议他们购买高档高尔夫球场，将其改为公共公园，并推广观鸟活动，以抵消用水量。 这一想法突出了人工智能基础设施增长与环境可持续性之间的张力，并提供了一种创造性的、受公众欢迎的解决方案，可能重塑土地利用和企业水资源管理。 谷歌在 2025 年使用了 109 亿加仑水（日均 3000 万加仑），而科切拉谷的每个高尔夫球场每年约消耗 800 英亩-英尺水（日均约 75 万加仑）。Willison 计算，购买该地区 40 个球场（占三分之一）即可抵消谷歌的用水量。

rss · Simon Willison · 7月17日 02:58

**背景**: 超大规模云服务商（hyperscaler）是指谷歌、微软、亚马逊等运营超大型数据中心的云提供商，其冷却过程需要大量水。英亩-英尺（acre-foot）是美国水资源管理中常用的体积单位，约等于 325,851 加仑（足以让一英尺深的水覆盖一个足球场）。随着人工智能工作负载的扩展，数据中心的用水问题日益受到关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hyperscale_computing">Hyperscale computing - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Acre-foot">Acre-foot - Wikipedia</a></li>
<li><a href="https://brazos.org/about-us/education/water-school/articleid/249/what-is-an-acre-foot">What is an acre-foot? - Water School - Brazos River Authority</a></li>

</ul>
</details>

**标签**: `#ai-energy-usage`, `#water sustainability`, `#data centers`

---

<a id="item-11"></a>
## [GPT-5.6 Codex 漏洞可删除 $HOME 目录](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 7.0/10

Thibault Sottiaux 报告称，GPT-5.6 Codex 在启用完全访问模式且无沙盒保护时，可能因尝试覆盖 $HOME 环境变量时出错而意外删除用户的 $HOME 目录。 此漏洞对部署具有完全系统访问权限的 AI 编码代理的用户构成严重安全风险，凸显了需要强大的沙盒和自动审查保护以防止灾难性数据丢失。 该漏洞特定发生在启用完全访问模式、禁用沙盒保护（包括自动审查）时，模型尝试通过覆盖 $HOME 环境变量设置临时目录，但错误地删除了 $HOME。

rss · Simon Willison · 7月16日 17:45

**背景**: Codex 是 OpenAI 的一款 AI 编码代理，可在用户本地计算机上运行，能够执行 shell 命令和操作文件。沙盒是一种安全技术，将代理的操作隔离在受限环境中，防止其影响关键系统路径。此漏洞突显了在没有任何防护措施的情况下授予 AI 代理无限制文件系统访问权限的危险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/codex/">Codex in ChatGPT | AI Coding Agents for Software... | OpenAI</a></li>
<li><a href="https://www.firecrawl.dev/blog/ai-agent-sandbox">AI Agent Sandbox: How to Safely Run Autonomous Agents in 2026</a></li>
<li><a href="https://northflank.com/blog/how-to-sandbox-ai-agents">How to sandbox AI agents in 2026: MicroVMs, gVisor & isolation strategies | Blog — Northflank</a></li>

</ul>
</details>

**标签**: `#codex`, `#coding-agents`, `#generative-ai`, `#AI safety`, `#file deletion`

---

<a id="item-12"></a>
## [Zilog Z80 迎来 50 周年](https://goliath32.com/blog/z80.html) ⭐️ 6.0/10

Zilog Z80 微处理器迎来了它的 50 周年纪念，一篇博文详细介绍了其技术历史并汇集了社区回忆。 Z80 是家用计算机兴起的关键处理器，并仍在嵌入式系统中广泛使用，其长寿是对其设计和影响力的证明。 虽然 Z80 与 Intel 8080 二进制兼容，但在某些操作上标志寄存器的行为存在差异。它驱动了 TRS-80、ZX Spectrum 等标志性机器以及许多游戏机。

hackernews · st_goliath · 7月17日 19:41 · [社区讨论](https://news.ycombinator.com/item?id=48951461)

**背景**: Z80 由 Zilog 于 1976 年推出，是一款 8 位微处理器，因其低成本且功能强大的指令集，成为家用计算机、游戏机和嵌入式设备的主力。它拥有众多寄存器，并与 Intel 8080 向上兼容。Z80 至今仍在生产，用于嵌入式应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zilog">Zilog - Wikipedia</a></li>
<li><a href="https://codedocs.org/what-is/zilog-z80">Zilog Z 80 - CodeDocs</a></li>
<li><a href="https://ohagan.medium.com/long-live-the-z80-the-chip-that-quietly-changed-everything-6e4c8f8850f4">Long Live the Z 80 : The Chip That Quietly Changed Everything | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了在 Z80 上学习汇编、搭建套件以及使用它在家中电脑（如 Timex Sinclair）的怀旧回忆。一些人指出了 Z80 与 8080 之间的技术差异，例如标志寄存器的行为。

**标签**: `#z80`, `#cpu history`, `#retrocomputing`, `#microprocessors`, `#vintage computing`

---

<a id="item-13"></a>
## [通过 WebAssembly 实现带颜色的 Mermaid 转 ASCII 艺术图](https://simonwillison.net/2026/Jul/16/mermaid-ascii/#atom-everything) ⭐️ 6.0/10

Simon Willison 使用 Claude Fable 5 将 Go 库 AlexanderGrooff/mermaid-ascii 编译为 WebAssembly，创建了一个可将 Mermaid 图表转换为彩色 ASCII 艺术图的网页工具。相较于之前基于 Grok Build 的 Rust 工具，此工具增加了颜色支持。 这使得 Mermaid 图表在终端、邮件或文档等纯文本环境中可用，且新增颜色支持提升了可读性。它展示了将 Go 库编译为 WebAssembly 供客户端使用的便捷性，拓宽了图表渲染的可能性。 该工具支持流程图、子图、颜色和多种链接类型，并提供填充和仅 ASCII 模式选项。它通过 WebAssembly 完全在浏览器中运行，无需服务器端依赖。

rss · Simon Willison · 7月16日 14:57

**背景**: Mermaid 是一种基于文本的图表工具，可通过简单语法渲染图表。ASCII 艺术图使用文本字符代表图像。WebAssembly 允许在浏览器中以接近原生速度运行编译后的代码。Go 和 Rust 均可编译为 WebAssembly，从而在 Web 应用中复用现有库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Grok_Build">Grok Build</a></li>

</ul>
</details>

**标签**: `#mermaid`, `#ascii-art`, `#webassembly`, `#go`, `#tool`

---