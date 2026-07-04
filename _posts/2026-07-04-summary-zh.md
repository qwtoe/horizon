---
layout: default
title: "Horizon Summary: 2026-07-04 (ZH)"
date: 2026-07-04
lang: zh
---

> 从 20 条内容中筛选出 14 条重要资讯。

---

1. [SearXNG：免费互联网元搜索引擎](#item-1) ⭐️ 8.0/10
2. [欧洲议会议员遭飞马间谍软件入侵](#item-2) ⭐️ 8.0/10
3. [工厂即简单空间：反思制造](#item-3) ⭐️ 8.0/10
4. [Current AI 推出开源 AI 差距地图](#item-4) ⭐️ 8.0/10
5. [Mistral AI 发布 Leanstral 1.5，专用于 Lean 4 定理证明](#item-5) ⭐️ 7.0/10
6. [本地运行顶级大模型指南](#item-6) ⭐️ 7.0/10
7. [Costco 是反亚马逊](#item-7) ⭐️ 7.0/10
8. [Josh Comeau 报告课程销量因 AI 下降超 50%](#item-8) ⭐️ 7.0/10
9. [Simon Willison 2026 年 6 月通讯](#item-9) ⭐️ 7.0/10
10. [使用 DSPy 改进 Datasette Agent 的 SQL 提示](#item-10) ⭐️ 7.0/10
11. [杰弗里·利特提出“理解以参与”理念](#item-11) ⭐️ 7.0/10
12. [AMD MI355X 声称 GLM5.2 成本比 Blackwell 低 2 倍](#item-12) ⭐️ 6.0/10
13. [让 AI 助手自主判断以提高效率](#item-13) ⭐️ 6.0/10
14. [Simon Willison 发布 llm-coding-agent 测试版](#item-14) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [SearXNG：免费互联网元搜索引擎](https://github.com/searxng/searxng) ⭐️ 8.0/10

SearXNG 是一个开源元搜索引擎，能从多个搜索服务聚合结果而不追踪用户。社区讨论强调其越来越多地被用作本地 AI 模型和检索增强生成（RAG）系统的后端。 在隐私问题日益受到关注的今天，SearXNG 提供了一个可自托管、尊重隐私的搜索解决方案。它与本地 AI 和 RAG 工作流的集成，使其对构建私密、离线应用的开发者来说极具价值。 SearXNG 可通过 Docker 自托管，支持 JSON 输出以便程序化访问，并能使用 YaCy 或 Brave Search API 等多种后端。不过，用户反馈其速度可能较慢，偶尔还会遇到来自上游引擎的验证码挑战。

hackernews · theanonymousone · 7月3日 20:15 · [社区讨论](https://news.ycombinator.com/item?id=48779454)

**背景**: 元搜索引擎是一种同时查询多个搜索引擎并整合结果的系统。检索增强生成（RAG）是一种让大语言模型在文本生成过程中检索并整合外部信息的技术。SearXNG 是已停止维护的 Searx 项目的分支，延续了其隐私优先的理念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SearXNG">SearXNG - Wikipedia</a></li>
<li><a href="https://github.com/searxng/searxng">GitHub - searxng/searxng: SearXNG is a free internet metasearch engine ...</a></li>

</ul>
</details>

**社区讨论**: Searx 的原作者 asciimoo 已不再参与开发，转而启动了新项目 Hister（一个全文索引器）。用户反馈 SearXNG 与 TinySearch 等 AI 代理工具以及 Gemma 等本地模型配合良好，但爬取时存在速度和验证码问题。部分用户认为使用 Brave Search API 时较为可靠。

**标签**: `#metasearch engine`, `#privacy`, `#open source`, `#local LLM`, `#RAG`

---

<a id="item-2"></a>
## [欧洲议会议员遭飞马间谍软件入侵](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

公民实验室确认，一名欧洲议会议员的 iPhone 在 2022 年和 2023 年多次感染飞马间谍软件，并与针对欧洲流亡记者的间谍活动有关。 对调查间谍软件的立法者的攻击突显了商业监控威胁的严重性，并引发了对欧盟机构抵御国家支持间谍活动能力的担忧。 感染发生在 2022 年 10 月 21 日和 2023 年 3 月 6 日至 7 日，法医分析确认可信度极高。首次感染与已知的针对俄语和白俄罗斯语流亡记者的飞马行动重叠，表明客户拥有多国授权。

hackernews · ledoge · 7月3日 20:38 · [社区讨论](https://news.ycombinator.com/item?id=48779683)

**背景**: 飞马是由以色列 NSO 集团开发的间谍软件，能够远程隐秘感染移动设备。公民实验室位于多伦多大学，是领先的数字威胁研究机构，曾揭露多起飞马滥用事件。欧洲议会当时正在调查飞马等间谍软件的使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，希腊也曾发生类似间谍活动，据称由政府操控；一些欧盟成员国滥用飞马导致以色列公司切断联系。同一设备同时泄露个人医疗信息和政府文件，引发对欧洲议会设备政策的担忧。

**标签**: `#cybersecurity`, `#Pegasus`, `#espionage`, `#EU`, `#spyware`

---

<a id="item-3"></a>
## [工厂即简单空间：反思制造](https://interconnected.org/home/2026/07/03/factories) ⭐️ 8.0/10

文章反思了工厂可以是简单空间的观念，挑战制造业需要复杂设备和设施的传统看法。 它质疑制造业中自我强加的复杂性，鼓励思维转变，可能影响对小规模生产和创客文化的看法。 社区讨论突出了个人经历，包括一家机械制造公司在没有大量机器的情况下有效运营，以及一个采用手工组装和夹具的小型工厂。

hackernews · arbesman · 7月3日 15:13 · [社区讨论](https://news.ycombinator.com/item?id=48776035)

**背景**: 文章探讨了工厂作为最小空间的概念，与制造业通常是高科技和资本密集型的一般看法形成对比。它借鉴了黑客文化和创客运动，强调许多消费品可以用更简单的设备制造。

**社区讨论**: 评论者分享了经历：一位指出“你可以做到”的心态已经丢失，另一位描述了一家以最小投资成功的小工厂，还有一位指出快餐厨房是高效的工厂。一些人担心没有持续业务就无法维持。

**标签**: `#manufacturing`, `#mindset`, `#making`, `#hacker culture`, `#industry`

---

<a id="item-4"></a>
## [Current AI 推出开源 AI 差距地图](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

当前 AI（Current AI）是一个在 2025 年 2 月巴黎 AI 行动峰会上成立的非营利组织，它发布了开源 AI 差距地图 v0.1，该地图索引了 421 个开源 AI 产品，涵盖模型、工具、数据集和硬件。 该地图提供了对开源 AI 生态系统的系统性概览，帮助开发者、研究人员和资助者识别其中的空白和机遇。 该地图包含来自 228 个组织的 266 个软件工具、85 个模型、50 个数据集和 20 个硬件项目，数据以 MIT 许可证在 GitHub 上发布。

rss · Simon Willison · 7月3日 22:04

**背景**: 'AI 公共选项'的概念借鉴自医疗保健领域，即政府运营的选项与私人保险竞争。当前 AI 是一个资金充足的非营利组织（已承诺 4 亿美元），旨在通过开源构建这样的公共选项。差距地图是他们首个主要成果，用于编录开源 AI 技术栈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">Introducing the Gap Map v0.1 - currentai.org</a></li>
<li><a href="https://map.currentai.org/">Current AI - Open Source AI Gap Map</a></li>
<li><a href="https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/">Open Source AI Gap Map - simonwillison.net</a></li>

</ul>
</details>

**标签**: `#Open Source`, `#AI`, `#Ecosystem Mapping`, `#Non-profit`

---

<a id="item-5"></a>
## [Mistral AI 发布 Leanstral 1.5，专用于 Lean 4 定理证明](https://mistral.ai/news/leanstral-1-5/) ⭐️ 7.0/10

Mistral AI 发布了 Leanstral 1.5，这是一个专门针对 Lean 4 定理证明进行微调的大型语言模型，能够协助形式化证明和错误检测。 此次发布推动了自动化形式验证的发展，使其对开发者更加易用，并可能促进 Lean 4 在构建可靠软件方面的应用。 该模型声称能发现测试遗漏的错误，例如 varinteger 库中的溢出问题，但社区评论指出其对比的是约六个月前的先进模型。

hackernews · programLyrique · 7月3日 22:33 · [社区讨论](https://news.ycombinator.com/item?id=48780801)

**背景**: Lean 4 是一个定理证明器也是通用编程语言，用于形式化验证，通过数学方式证明软件的正确性。形式化验证是一种严谨的方法，尤其在关键应用中确保系统可靠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lean-lang.org/theorem_proving_in_lean4/">Theorem Proving in Lean 4</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification</a></li>
<li><a href="https://octagono.org/blog/lean-four/">Lean 4 : Theorem Proving Meets General-Purpose... — octagono</a></li>

</ul>
</details>

**社区讨论**: 评论对错误发现的说法提出质疑，指出溢出示例是测试通常能发现的已知边界情况，而且模型是与较旧的模型进行比较，降低了结果的令人印象深刻程度。

**标签**: `#LLM`, `#formal verification`, `#Lean 4`, `#AI`, `#programming languages`

---

<a id="item-6"></a>
## [本地运行顶级大模型指南](https://github.com/jamesob/local-llm) ⭐️ 7.0/10

由 jamesob 编写的这份指南全面概述了本地运行顶级大语言模型所需的硬件和成本，涵盖了从预算友好的双 RTX 3090 到超过 4 万美元的四块高端 GPU 配置。 该指南凸显了本地与云端使用大模型之间显著的成本-性能权衡，这对于评估隐私、延迟和长期费用的开发者和组织至关重要。 文章提到一个约 4 万美元的构建方案，但社区评论估计实际成本接近 5 到 5.5 万美元。此外，还指出本地模型通常依赖量化和剪枝技术以适应可用显存，这可能会降低质量。

hackernews · livestyle · 7月3日 15:03 · [社区讨论](https://news.ycombinator.com/item?id=48775921)

**背景**: 像 GPT-4 这样的大语言模型需要大量计算资源，通常通过云端 API 访问。本地运行则需要配备大容量显存（例如 48GB 以上以获得不错性能）的高端 GPU，并且通常涉及量化——一种降低模型精度以适配内存的技术，但会牺牲部分准确性。该指南旨在帮助用户了解这些硬件需求和权衡。

**社区讨论**: 像 Aurornis 这样的评论者警告隐藏成本和降低预期，指出一个 4 万美元的构建方案很容易超过 5 万美元。Jacobgold 指出 4 万美元相当于 16.8 年的 Claude Opus 订阅费，使本地部署更加昂贵。但 GTP 提到了一种折中方案，使用 128GB 统一内存以良好速度运行 DeepSeek V4。

**标签**: `#local-llm`, `#hardware`, `#cost-analysis`, `#AI-infrastructure`, `#community-discussion`

---

<a id="item-7"></a>
## [Costco 是反亚马逊](https://phenomenalworld.org/analysis/the-anti-amazon/) ⭐️ 7.0/10

一篇分析文章指出，Costco 的商业模式刻意避免最后一英里配送的复杂性，专注于店内批量购买，与亚马逊强调送货上门形成鲜明对比。 这种比较凸显了零售业的根本战略选择：优化店内批量销售与优化送货上门的便利性，这对物流、客户体验和城市规划都有影响。 Costco 运营需会员资格的仓储式商店，批量销售商品；而亚马逊依赖庞大的物流网络进行快速、个体的送货上门。文章利用这种对比来阐释工程哲学：“聪明人解决问题，智者回避问题。”

hackernews · bookofjoe · 7月3日 15:14 · [社区讨论](https://news.ycombinator.com/item?id=48776044)

**背景**: 最后一英里配送是指从配送枢纽到最终目的地的最后一程运输，通常是物流中最昂贵、最复杂的部分。Costco 的模式将运输负担转移给顾客，他们自己开车到商店并将批量购买的商品运回家。这与亚马逊等处理送货上门的电商公司形成对比，后者需要庞大的基础设施。文章利用这种差异来讨论工程权衡和文化影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Last_mile_delivery">Last mile delivery</a></li>
<li><a href="https://www.britannica.com/money/Costco">Costco | History, Growth, Products, & Facts | Britannica Money</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了 Costco 模式和亚马逊模式之间的权衡，有人赞扬 Costco 的效率，也有人指出其以汽车为中心的特性。一条评论强调了回避问题的工程智慧，另一条提供了英国视角，指出 Costco 在电子产品和大件家电上的特别优惠。

**标签**: `#Costco`, `#Amazon`, `#logistics`, `#engineering philosophy`, `#business model`

---

<a id="item-8"></a>
## [Josh Comeau 报告课程销量因 AI 下降超 50%](https://simonwillison.net/2026/Jul/3/josh-w-comeau/#atom-everything) ⭐️ 7.0/10

知名课程创作者 Josh W. Comeau 报告，其新课程《Whimsical Animations》的销量预计仅为正常发布水平的三分之一，现有课程的销量也较去年大幅下滑。 这突显了一个更广泛的趋势：AI——包括工作不确定性以及基于 LLM 的辅导——正在颠覆开发者教育市场，可能减少创作者的收入和生产优质内容的动力。 Comeau 提到双重打击：一是工作不安全感使人们犹豫是否投入时间和金钱学习新技能；二是 LLM 提供免费个性化辅导，降低了对付费课程的需求。他指出，多位课程创作者报告收入下降 50%以上。

rss · Simon Willison · 7月3日 21:25

**背景**: Josh W. Comeau 是知名的 Web 开发教育者，以交互式 CSS 和 React 课程闻名。他的课程销售数据反映了创作者经济中普遍存在的模式：AI 工具（如 ChatGPT）越来越多地被用于学习。许多开发者担心 AI 可能取代工作，从而降低了提升技能的价值感。

**标签**: `#AI`, `#education`, `#software engineering`, `#industry trends`

---

<a id="item-9"></a>
## [Simon Willison 2026 年 6 月通讯](https://simonwillison.net/2026/Jul/3/june-newsletter/#atom-everything) ⭐️ 7.0/10

Simon Willison 发布了他的 2026 年 6 月赞助人专属通讯，内容涵盖 Claude Fable 5、GPT-5.6、GLM-5.2、美国出口限制、Datasette Apps 以及 WASM 项目。 该通讯提供了最新 AI 模型发布和开源工具更新的精选概述，帮助开发者和研究人员及时了解快速发展的技术和监管变化。 该通讯仅向 GitHub 赞助人开放，月费 10 美元，内容包括 tokenmaxxing 趋势、sqlite-utils、shot-scraper 和 Datasette 等部分。文中附带了 5 月通讯的预览链接。

rss · Simon Willison · 7月3日 14:50

**背景**: Datasette 是一个用于探索和发布表格数据的开源工具，常与 SQLite 数据库一起使用。sqlite-utils 是一个用于管理 SQLite 数据库的 Python 库。WASM（WebAssembly）是一种可移植的二进制格式，用于高性能 Web 应用。Simon Willison 是知名开发者兼 AI 评论员，他每月策划一份通讯总结 AI 和开源新闻。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Datasette">Datasette</a></li>
<li><a href="https://sqlite-utils.datasette.io/">sqlite - utils</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly - Wikipedia</a></li>

</ul>
</details>

**标签**: `#newsletter`, `#AI`, `#open source`, `#Datasette`, `#WASM`

---

<a id="item-10"></a>
## [使用 DSPy 改进 Datasette Agent 的 SQL 提示](https://simonwillison.net/2026/Jul/2/dspy-datasette-agent-prompts/#atom-everything) ⭐️ 7.0/10

Simon Willison 使用 DSPy 框架自动评估并改进 Datasette Agent 的 SQL 系统提示，发现由于缺少架构细节导致列名猜测等问题。 这展示了一种用于 AI 代理提示优化的新颖工作流，表明 DSPy 可以系统性地识别并提出 LLM 提示的改进建议，从而可能使 AI 代理更可靠、更准确。 该实验通过 Claude Fable 5 使用 GPT-4.1 mini 和 nano 模型，发现将列名包含在架构列表中或软化关于不要调用 describe_table 的建议可以减少错误重试循环。

rss · Simon Willison · 7月2日 18:25

**背景**: DSPy (声明式自我改进 Python) 是一个通过组合 Python 代码而非编写脆弱提示来构建 AI 系统的框架。Datasette Agent 是一个将 LLM 集成到 Datasette 中帮助用户探索和查询数据的 AI 助手。提示工程对 LLM 性能至关重要，DSPy 提供了自动评估和优化的工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dspy.ai/">DSPy</a></li>
<li><a href="https://agent.datasette.io/">Datasette Agent: an AI assistant for Datasette to help explore and ...</a></li>
<li><a href="https://github.com/stanfordnlp/dspy">GitHub - stanfordnlp/dspy: DSPy: The framework for programming—not prompting—language models</a></li>

</ul>
</details>

**标签**: `#DSPy`, `#prompt engineering`, `#SQL`, `#AI agents`, `#Datasette`

---

<a id="item-11"></a>
## [杰弗里·利特提出“理解以参与”理念](https://simonwillison.net/2026/Jul/2/understand-to-participate/#atom-everything) ⭐️ 7.0/10

研究员杰弗里·利特在 2026 年 7 月 1 日的 AIE 大会上提出了“理解以参与”概念，主张开发者在与 AI 编码代理协作时必须保持对代码的深度理解，以避免累积认知债务。 这一框架揭示了 AI 辅助软件工程中的关键挑战：随着 AI 代理生成越来越复杂的代码变更，开发者面临失去对系统理解的风险，从而产生认知债务。该概念为开发者提供了宝贵的思维模型，帮助其保持主动参与并维护代码质量。 利特在 AI 工程师世博会（AIE）2026 上发表了演讲，所有 300 多场演讲将在随后三周内通过 YouTube 发布。他还在 Twitter 上发布了演讲内容要点串。

rss · Simon Willison · 7月2日 17:07

**背景**: 认知债务指的是开发者对代码的理解与实际代码工作方式之间的差距，这是随着 AI 编码代理生成大量代码而日益突出的问题。与存在于代码本身的技术债务不同，认知债务影响开发者的心智模型和有效参与能力。“理解以参与”概念强调，为了与 AI 代理进行有意义的协作，开发者必须投入精力理解生成的代码，才能保持创造力和流畅性，成为项目的积极贡献者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://devtoollab.com/blog/cognitive-debt-ai-coding">What Is Cognitive Debt ? How AI Coding Tools Are... | DevToolLab Blog</a></li>

</ul>
</details>

**标签**: `#AI-assisted coding`, `#cognitive debt`, `#software engineering`, `#code comprehension`, `#developer tools`

---

<a id="item-12"></a>
## [AMD MI355X 声称 GLM5.2 成本比 Blackwell 低 2 倍](https://www.wafer.ai/blog/glm52-amd) ⭐️ 6.0/10

AMD 声称其 MI355X GPU 以每节点每秒 2626 个 token 的速度运行 GLM5.2 模型，成本比 NVIDIA 的 Blackwell GPU 低 2 倍以上。该基准测试使用了 FP4 量化来达到这些性能数据。 如果得到验证，这可能会使 AMD 成为大规模 AI 推理中 NVIDIA 的有力替代品，尤其是对于那些难以获得 NVIDIA 硬件的组织。然而，FP4 量化的使用引发了对模型质量的担忧，这可能会限制其在需要高准确度场景中的实际采用。 GLM5.2 模型是 Z.ai 的旗舰开源 LLM，AMD MI355X GPU 配备 288 GB HBM3E 内存并原生支持 FP4 数据类型。社区评论者指出，与 FP8 相比，FP4 量化通常会导致明显的精度下降，从而对报告的速度提升提出质疑。

hackernews · latchkey · 7月3日 21:49 · [社区讨论](https://news.ycombinator.com/item?id=48780417)

**背景**: FP4 量化将模型权重和激活值的数值精度降低到 4 位，从而在潜在精度损失的情况下实现更快的推理和更低的内存使用。GLM5.2 模型是一个最先进的开源 LLM，专为编码和智能体任务设计，性能与顶级专有模型相当。AMD 的 MI355X GPU 基于 CDNA 4 架构，以高内存容量和带宽瞄准 AI 推理，并支持 FP4 格式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html">AMD Instinct™ MI355X GPUs</a></li>
<li><a href="https://www.datacamp.com/blog/glm-5-2">GLM - 5 . 2 : Features, Setup, Benchmarks, and Model ... | DataCamp</a></li>
<li><a href="https://www.spheron.network/blog/fp4-quantization-blackwell-gpu-cost/">FP4 Quantization on Blackwell GPUs: Throughput, Cost, and When It's Worth It | Spheron Blog</a></li>

</ul>
</details>

**社区讨论**: 评论者表示怀疑，有人指出 FP4 量化‘实际上从来不是无损的’，模型变得‘功能上被切除了脑叶’。另一个人指出从 FP8 到 MXFP4 有明显的精度下降。还有人呼吁在标题中包含每瓦性能并明确说明量化方式。

**标签**: `#hardware`, `#AI inference`, `#AMD`, `#benchmark`, `#quantization`

---

<a id="item-13"></a>
## [让 AI 助手自主判断以提高效率](https://simonwillison.net/2026/Jul/3/judgement/#atom-everything) ⭐️ 6.0/10

Simon Willison 分享了 Claude Code 团队的建议：让 Fable 自行判断测试和模型选择，而不是硬性规定；通过提示词将编码任务委托给低功耗子代理。 这条实用建议帮助开发者在昂贵的高端 AI 模型上优化 token 消耗和成本，在保证质量的同时提高效率。 Willison 使用提示词'让你的判断力决定合适的低功耗模型并在子代理中运行'，这保存了一个记忆文件，据报道减少了 Fable 的 token 消耗同时保持了生产力。

rss · Simon Willison · 7月3日 18:51

**背景**: Claude Code 是 Anthropic 的 AI 编码助手。Fable（Claude Fable 5）是顶级模型，针对 UI 设计和游戏编码等任务优化。这条建议的核心是避免在琐碎任务上使用最强大的模型，让 AI 自行委托给更便宜的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://www.ai.engineer/worldsfair/2026">AI Engineer World's Fair 2026: June 29 - July 2, San Francisco</a></li>

</ul>
</details>

**标签**: `#AI coding assistants`, `#Fable`, `#Claude Code`, `#developer tools`, `#best practices`

---

<a id="item-14"></a>
## [Simon Willison 发布 llm-coding-agent 测试版](https://simonwillison.net/2026/Jul/2/llm-coding-agent/#atom-everything) ⭐️ 6.0/10

Simon Willison 发布了 llm-coding-agent 0.1a0 版本，这是一个基于他 LLM 框架构建的代码代理，能够读取文件、编辑代码和执行 shell 命令。该 alpha 版本本身主要是通过 Claude Code 的两个提示生成的。 此次发布展示了 LLM 框架如何演变为一个代理平台，支持新的编程助手。同时也展示了 AI 辅助开发的强大能力，因为该代理的初始实现是由另一个 AI 代理构建的。 该代理包含工具如 edit_file、execute_command、list_files、read_file 和 search_files。可通过 `uvx --prerelease=allow --with llm-coding-agent llm code` 运行，并提供基于 CodingAgent 类的 Python API。

rss · Simon Willison · 7月2日 19:33

**背景**: Simon Willison 的 LLM 库是一个用于与各种语言模型交互的 Python 命令行工具。llm-coding-agent 是一个新插件，增加了类似 Claude Code 的代码代理功能，Claude Code 是 Anthropic 的一个产品，可以自主执行编码任务。该代理是使用 python-lib-template-repository 和 Claude Code 本身构建的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://code.claude.com/docs/en/sub-agents">Create custom subagents - Claude Code Docs</a></li>
<li><a href="https://github.com/simonw/python-lib-template-repository">GitHub - simonw/ python - lib - template - repository : GitHub template...</a></li>

</ul>
</details>

**标签**: `#llm`, `#coding agent`, `#AI`, `#open source`, `#Python`

---