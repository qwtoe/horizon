---
layout: default
title: "Horizon Summary: 2026-09-04 (ZH)"
date: 2026-09-04
lang: zh
---

> 从 15 条内容中筛选出 11 条重要资讯。

---

1. [OpenAI 发布 GPT-6 Astra，ARC-AGI-3 得分达 99.9%](#item-1) ⭐️ 9.0/10
2. [ICANN 与威瑞信拟终止 .name 三级域名](#item-2) ⭐️ 8.0/10
3. [开发者用 LLM 将 1993 年 Amiga 汇编游戏移植到 Godot](#item-3) ⭐️ 8.0/10
4. [AI 编程代理会选哪些工具？17,000 次运行实测给出答案](#item-4) ⭐️ 8.0/10
5. [Paint.NET 开发者借助 Claude 为 WINE 重写 Direct2D（18 万行代码）](#item-5) ⭐️ 8.0/10
6. [Qwen 3.8 27B available on Cerebras at 1500 tokens/s](#item-6) ⭐️ 7.0/10
7. [IFM 发布 K2 Horizon，推出六个完全开放的 AI 模型](#item-7) ⭐️ 7.0/10
8. [围棋大师申真谞让两子击败 AI KataGo](#item-8) ⭐️ 7.0/10
9. [Claude's new system prompt really doesn't want to reproduce song lyrics](#item-9) ⭐️ 7.0/10
10. [美国遭遇前所未有 GPS 故障，误差高达 33 英尺](#item-10) ⭐️ 6.0/10
11. [从所有人类历史中随机抽取一个人生并生成简介的应用](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 GPT-6 Astra，ARC-AGI-3 得分达 99.9%](https://openai.com/index/gpt-6-astra/) ⭐️ 9.0/10

OpenAI 发布了新旗舰模型 GPT-6 Astra，公布了系统卡并开始逐步推出。该模型在 ARC-AGI-3 上获得 99.9% 的成绩，在 Artificial Analysis Coding Agent Index 上也有大幅提升。 作为一次重大旗舰发布，它可能重新定义前沿模型的能力预期，尤其是在超越静态问答的交互式推理基准上。极高的 ARC-AGI-3 得分可能加剧关于该结果是体现通用智能还是特定基准技能习得的争论。 该模型的系统卡托管在 OpenAI 的部署安全门户上，表明经过了完整的安全评估。社区分析指出 ARC-AGI-3 对比可能不一致：GPT-6 Astra 使用了 Responses API 评估框架，而页面上的 GPT-5.6 Sol 得分为 7.8%，并未按该框架估算，其对应分数约为 30%。

hackernews · kibae · 9月3日 18:41 · [社区讨论](https://news.ycombinator.com/item?id=49554643)

**背景**: ARC-AGI-3 是一个交互式推理基准，要求 AI 智能体实时探索新环境、临时获取目标并解决问题，而不是回答静态问题。OpenAI 的系统卡是部署前说明模型能力、局限与风险缓解措施的安全文档。此前 GPT-5.5、GPT-5.6 Sol 等模型在 ARC-AGI-3 上得分很低，因此 GPT-6 Astra 的 99.9% 标志着大幅跃升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/">How enabling two settings tripled our scores on the ARC-AGI-3 benchmark | OpenAI</a></li>
<li><a href="https://artificialanalysis.ai/agents/coding-agents">AI Coding Agent Benchmarks & Leaderboard | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者意见不一：有人认为 ARC-AGI-3 记分卡具有误导性，因为它把使用 Responses API 评估框架的 GPT-6 Astra 与在另一设置下运行的旧模型比较。也有人质疑大幅基准提升是否代表 AGI，并指出其他多数基准仅有小幅改进；还有人呼应 François Chollet 的观点，认为前沿模型的进展仍像是技能习得。

**标签**: `#OpenAI`, `#GPT-6`, `#AI`, `#large language models`, `#benchmarks`

---

<a id="item-2"></a>
## [ICANN 与威瑞信拟终止 .name 三级域名](https://neil.fraser.name/news/2026/09/03/) ⭐️ 8.0/10

ICANN 与威瑞信提出终止所有现有的 .name 三级域名注册（形如 x.y.name），并释放相应的 y.name 二级域名。该提案将取消注册者多年持有的名称，且未提及任何“祖父条款”或对父级域名的保留措施。 终止现有注册将打破 .name 用户长期以来的预期，并可能为域名抢注甚至劫持打开大门——这些域名可能正被用于网站和邮箱。此举也与 ICANN 所宣称的“确保互联网唯一标识系统稳定安全运行”的使命相冲突。 该提案并未删除 .name 顶级域名本身，受影响的只是 x.y.name 形式的三级域名注册；相关的 y.name 二级域名会被释放，而不会被继续保留。评论者还指出，提案没有建议保留二级父级域名以防止域名抢注。

hackernews · pavel_lishin · 9月3日 14:54 · [社区讨论](https://news.ycombinator.com/item?id=49550772)

**背景**: 三级域名是 DNS 层级中位于二级域名之下的子域名，形如 x.y.name。.name 这个顶级域名最初被设计为面向个人的域名空间，目前由威瑞信在 ICANN 的监管下运营。域名劫持指未经域名所有者许可擅自变更域名注册归属；突然释放域名可能使注册者面临被他人抢注或劫持的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Third-level_domain">Third-level domain</a></li>
<li><a href="https://en.wikipedia.org/wiki/Domain_hijacking">Domain hijacking</a></li>
<li><a href="https://www.icann.org/en/contracted-parties/registry-operators/resources/list-of-top-level-domains">List of Top - Level Domains</a></li>

</ul>
</details>

**社区讨论**: 评论者强调，.name 顶级域名本身并未终止，受影响的只是三级域名。不少人认为该提案不公平且违背 ICANN 的使命，主张应继续承认既有注册并保留父级域名；也有人指出域名本质上是租赁的，本就可能随时消失。

**标签**: `#DNS`, `#ICANN`, `#domain names`, `#internet governance`

---

<a id="item-3"></a>
## [开发者用 LLM 将 1993 年 Amiga 汇编游戏移植到 Godot](https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/) ⭐️ 8.0/10

一位开发者记录了自己如何用 Claude 在一个晚上把 1993 年用 MC68000 汇编语言在巴格达编写的 Amiga 游戏移植到 Godot 引擎。过程中，LLM 用 vasm 汇编代码，直到与原始二进制字节完全一致，只除了一段神秘的 108 字节差异。 这是 LLM 辅助逆向工程和代码翻译的一个引人注目的例子，表明现代 AI 能够读懂并移植几十年前的汇编代码到当代引擎中。这可能让复古游戏保存和重制对独立开发者来说变得容易得多。 作者指出，他原始发布的二进制文件是游戏运行后的内存快照，因为 AsmOne 在内存中汇编，游戏将那段内存保存到磁盘；这解释了 108 字节的差异。该文章本身也先由 Claude 起草，再由作者花了一周逐行编辑。

hackernews · rabahs · 9月3日 14:28 · [社区讨论](https://news.ycombinator.com/item?id=49550375)

**背景**: MC68000 是摩托罗拉推出的一款 16/32 位处理器，用于 Amiga、Atari ST 以及早期 Macintosh 和 Genesis 等设备；用汇编写程序需要直接操作硬件寄存器。vasm 是一个可移植、可重定向的汇编器，在给定正确选项时可以逐字节重现输出，而 AsmOne 则是当时流行的 Amiga 汇编器/IDE，直接在内存中工作。Godot 是现代的开放源代码游戏引擎，因此要把 1993 年的汇编代码搬过去，通常意味着重写大量代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://sun.hasenbraten.de/vasm/">vasm portable and retargetable assembler</a></li>
<li><a href="https://en.wikipedia.org/wiki/Amiga_programming_languages">Amiga programming languages - Wikipedia</a></li>
<li><a href="https://en.wikibooks.org/wiki/68000_Assembly">68000 Assembly - Wikibooks, open books for an open world</a></li>

</ul>
</details>

**社区讨论**: 评论者对这个 1993 年汇编游戏表示惊叹，指出在互联网出现之前开发难度极大。还有人分享了类似实验，比如用 Claude 把 ZX81 内存转储转换成 Go 语言，以及为 NES、SNES、GBA 和 Sega Genesis 构建可复用的移植框架；还有人将这款游戏与《Gods: Into the Wonderful》作比较。

**标签**: `#LLM`, `#Godot`, `#reverse engineering`, `#retro gaming`, `#assembly`

---

<a id="item-4"></a>
## [AI 编程代理会选哪些工具？17,000 次运行实测给出答案](https://armature.tech/blog/which-tools-coding-agents-install) ⭐️ 8.0/10

Armature 实测了 Claude、Codex 和 Cursor 三类编码代理的 17,000 次运行，并分析了这些代理会选择安装或调用哪些开发工具。这项研究以量化方式呈现了编码代理的工具偏好。 AI 编码代理正成为开发者工具的重要分发渠道，了解它们会选择哪些工具，对开发者和供应商都很有价值。这些数据既有助于团队配置对代理友好的开发环境，也有助于工具厂商让自家产品更容易被代理发现。 该分析基于 17,000 次运行，关注的是 Claude、Codex 和 Cursor 的工具选择行为，而不是基准测试准确率。文章摘要没有列出完整的被测工具清单或环境配置细节。

hackernews · screm · 9月3日 21:20 · [社区讨论](https://news.ycombinator.com/item?id=49557206)

**背景**: Claude 是 Anthropic 推出的 AI 助手；Codex 最初是 OpenAI 的编程模型，后来也以 Codex CLI 形式作为本地终端编码代理发布；Cursor 则是基于 Visual Studio Code 分支构建的 AI 代码编辑器。这类代理工具可以编写和修改代码、执行命令并与文件交互，因此它们实际挑选的命令行工具至关重要。类似的研究正是在追踪“代理会选择哪些工具”这一新兴行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude ( AI ) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(code_editor)">Cursor (code editor)</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为这项研究有价值，并补充了自己的观察。有人把“让代理选择你的产品”比作面向人类的营销，还有人分享了自己的开源追踪项目 preseason.ai；另几位评论者则注意到 Claude Code 的工具行为不稳定。一位评论者担心，当前“AI 工具黄金时代”的开放性终将被追求利润和锁定用户的做法取代。

**标签**: `#AI agents`, `#coding assistants`, `#empirical analysis`, `#developer tools`, `#Claude`

---

<a id="item-5"></a>
## [Paint.NET 开发者借助 Claude 为 WINE 重写 Direct2D（18 万行代码）](https://simonwillison.net/2026/Sep/2/rick-brewster/) ⭐️ 8.0/10

Paint.NET 开发者 Rick Brewster 宣布，他使用 Anthropic 的 Claude 从零开始、以“洁净室”逆向工程方式重写了微软的 Direct2D API。这部分约 18 万行的 AI 生成代码位于 PaintDotNet.Windows.Direct2D1.Managed.dll，在 WINE 下通过 /wine 命令行参数启用。 这是一个引人注目的现实案例，表明大语言模型能够完成规模巨大、此前几乎无法解决的逆向工程任务，对通过 WINE 在 Linux 上运行 Windows 应用有直接影响。同时，由于 Brewster 承认自己无法逐行审查全部 18 万行 AI 代码，这件事也加剧了围绕“vibe coding（随性编码）”的争论。 Direct2D 一直是 Paint.NET 在 WINE 上最大的兼容性障碍，而且不能简单地禁用它。Brewster 表示他需要持续“照看”Claude，例如纠正它早期没有对 COM 对象执行 AddRef() 引用计数的问题；同时，Claude 对 Direct2D 内置效果所用公式的逆向工程能力也令他印象深刻。作为规模对比，Paint.NET 其余代码约 70 万行，是作者花了 20 多年写成的。

rss · Simon Willison · 9月2日 05:50

**背景**: Direct2D 是微软为 Windows 提供的硬件加速、即时模式 2D 图形 API，用于高性能渲染几何图形、位图和文本。WINE 是一个兼容层，通过重新实现 Windows API 让 Windows 应用程序能够在 Linux 等操作系统上运行。“洁净室”逆向工程是一种注重法律风险的方法：不直接复制专有源码，而是根据规格说明独立重新实现；这正是 Brewster 称 Claude 的重写为“从零开始的洁净室实现”的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Direct2D">Direct2D</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/win32/direct2d/direct2d-portal">Direct2D - Win32 apps | Microsoft Learn</a></li>
<li><a href="https://en.wikipedia.org/wiki/Clean-room_reverse_engineering">Clean-room reverse engineering</a></li>

</ul>
</details>

**标签**: `#AI-generated code`, `#reverse engineering`, `#WINE`, `#Direct2D`, `#Paint.NET`

---

<a id="item-6"></a>
## [Qwen 3.8 27B available on Cerebras at 1500 tokens/s](https://inference-docs.cerebras.ai/models/overview) ⭐️ 7.0/10

Qwen 3.8 27B is now available on Cerebras at 1500 tokens/s, though users report rate limits and cost issues that limit practical use.

hackernews · altertable · 9月3日 18:32 · [社区讨论](https://news.ycombinator.com/item?id=49554520)

**标签**: `#qwen`, `#cerebras`, `#inference`, `#llm`, `#performance`

---

<a id="item-7"></a>
## [IFM 发布 K2 Horizon，推出六个完全开放的 AI 模型](https://ifm.ai/blog/k2/) ⭐️ 7.0/10

IFM 推出了 K2 Horizon，一个包含六个开源模型的系列，并称其为 AI 史上规模最大的完全开源模型发布。这次发布开放了模型权重、训练代码和训练数据的访问权限。 完全开放的 AI 系统非常少见，许多所谓“开放”模型只开放权重，却隐藏训练数据和代码。像 K2 Horizon 这样的完整开放技术栈，让大型实验室之外的开发者能够审查、定制并信任他们部署的模型。 这个包含六个模型的系列定位覆盖推理、编程、智能体工作流、边缘设备和企业部署等应用场景。早期社区测试已对部分性能声明提出质疑，有评测者报告 3.7B 模型会生成错误代码并凭空捏造不存在的 API。

hackernews · karimf · 9月3日 15:36 · [社区讨论](https://news.ycombinator.com/item?id=49551760)

**背景**: 在 AI 行业中，“开源”与“开放权重”经常被混为一谈，但真正完全开放的系统必须同时公开模型、代码和训练数据。Open Source Initiative 也强调训练数据是真正开源 AI 模型的关键要素。正如有评论者指出，完全开放也被视为防范封闭提供商进行社会操纵的一种制衡手段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ifm.ai/blog/k2">Introducing K2 Horizon: Frontier Performance, Radically Open</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-source_artificial_intelligence">Open-source artificial intelligence - Wikipedia</a></li>
<li><a href="https://bipartisanpolicy.org/article/the-open-or-closed-ai-dilemma/">The Open or Closed AI Dilemma</a></li>

</ul>
</details>

**社区讨论**: 许多评论者欢迎又一个完全开放模型家族的出现，并认为此前只有英伟达的 Nemotron 等少数项目可比。主要争议集中在性能上：有基准对比显示 32B 模型落后于 Qwen3 27B，另有测试者发现 3.7B 模型在编程上不可靠，会臆造 API 并重复无效检查。还有评论者表示，模型发布速度过快已经让人产生“模型疲劳”。

**标签**: `#open models`, `#LLM`, `#AI`, `#machine learning`, `#open source`

---

<a id="item-8"></a>
## [围棋大师申真谞让两子击败 AI KataGo](https://www.kedglobal.com/artificial-intelligence/newsView/ked202607210007) ⭐️ 7.0/10

围棋大师申真谞在让两子的情况下击败了人工智能系统 KataGo。这场比赛是人类罕见地战胜顶级围棋 AI 之一。 这一结果表明，在让子条件下，最强的人类棋手仍然能与领先的 AI 较量，并凸显了申真谞模仿 AI 下法的非凡能力。它也引发了关于如何利用让子棋局来评估和改善人类与 AI 在围棋中的互动的问题。 让两子被认为是一个巨大优势；据估计，AI 在分先对局中的实力大约比人类强 400-600 ELO。评论者指出，申真谞刻意选择了一种复杂的定式变化，并制定了针对让子局面的策略，而 KataGo 据报道只是一味下高概率的招法，没有主动引诱他进入复杂战斗。

hackernews · gmays · 9月3日 01:11 · [社区讨论](https://news.ycombinator.com/item?id=49544762)

**背景**: 围棋是一种古老的棋盘游戏，为了让水平较弱的棋手有机会与强者对弈，可以设置让子——让两子意味着较弱的棋手在开局前先在棋盘上放两颗棋子。KataGo 是一款领先的开源围棋 AI，其水平早已超过最优秀的人类棋手。申真谞被普遍认为是这一代最强的人类围棋棋手，其等级分远超此前任何棋手。

**社区讨论**: 评论者大多称赞申真谞的成绩，指出他的实力远超历史上其他人类棋手，并且比任何人都更接近 AI 的下法。也有人提出保留意见：让两子是一个很大的优势，人类在分先对局中不可能赢 KataGo。还有评论指出标题可能具有误导性，因为接受让子意味着申真谞仍被视为较弱的一方。

**标签**: `#Go`, `#AI`, `#KataGo`, `#Human vs AI`, `#Strategy`

---

<a id="item-9"></a>
## [Claude's new system prompt really doesn't want to reproduce song lyrics](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/) ⭐️ 7.0/10

Anthropic's updated Claude system prompts now explicitly instruct the model not to reproduce song lyrics, reflecting ongoing copyright concerns.

rss · Simon Willison · 9月2日 14:16

**标签**: `#AI`, `#Anthropic`, `#Claude`, `#system prompts`, `#copyright`

---

<a id="item-10"></a>
## [美国遭遇前所未有 GPS 故障，误差高达 33 英尺](https://www.sciencealert.com/gps-glitched-across-the-us-by-as-much-as-33-feet-scientists-have-never-seen-this-before) ⭐️ 6.0/10

科学家在美国各地记录到一次前所未有的 GPS 故障，定位误差高达 33 英尺，他们表示这种现象从未被观测到过。此次事件扰乱了全美卫星导航系统的精度，而非仅局限于个别地区。 这种规模的 GPS 误差对依赖高精度的技术非常危险，例如自动驾驶汽车、精准农业和电子监控，这些技术通常需要厘米级精度。这也凸显了现代基础设施面对太空天气和信号干扰时的脆弱性。 文章报道称，2024 年 5 月的太阳风暴据估计因扰乱精准导航，给美国农业造成了约 5 亿美元损失。普通消费级 GPS 的精度只有数米，而精准农业依赖实时动态（RTK）定位等修正技术来达到厘米级精度。

hackernews · thread_id · 9月3日 00:49 · [社区讨论](https://news.ycombinator.com/item?id=49544618)

**背景**: GPS（全球定位系统）通过测量来自卫星星座的信号时间来计算接收机的位置。太阳风暴和电离层扰动等太空天气会延迟这些信号，导致定位误差。精准农业是一种利用 GPS 引导机械进行播种、喷药和收割的农业管理方式，它通常依赖 RTK（实时动态）定位，这是一种可将卫星信号误差降低到厘米级的修正技术。这一背景解释了为何约 33 英尺的大规模定位故障意义重大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Space_weather">Space weather</a></li>
<li><a href="https://en.wikipedia.org/wiki/Precision_agriculture">Precision agriculture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Real-time_kinematic_positioning">Real-time kinematic positioning</a></li>

</ul>
</details>

**社区讨论**: 评论者提出了若干现实担忧，指出电子监控设备可能误报人们离开住所，自动驾驶汽车若偏移 33 英尺也可能非常危险。还有人将该事件与廉价 GPS 干扰器的泛滥联系起来，并回顾美国曾利用“选择性可用性”故意降低 GPS 精度的历史。一位评论者质疑了 5 亿美元农业损失估算的可信度，称其难以置信。

**标签**: `#GPS`, `#space weather`, `#navigation`, `#precision agriculture`, `#systems reliability`

---

<a id="item-11"></a>
## [从所有人类历史中随机抽取一个人生并生成简介的应用](https://anyhumanever.com/) ⭐️ 6.0/10

一款名为 Any Human Ever 的网页应用会从全部人类历史中随机抽取一个人生，并显示由 AI 撰写的生平简介和相关历史统计。该应用可在 anyhumanever.com 访问。 它把抽象的人口历史变成一个能引起情感共鸣的具体个人故事，吸引了写作者和历史爱好者。不过评论显示其数据与方法不够严谨，因此它的价值更多在于创意新颖性，而非作为精确的数据工具。 生成的生平会引用类似“Hajnal (RH31)”和“Kaplan (RH03)”的资料，但用户发现链接失效或与内容无关。评论还指出抽样方法有问题：年份选择似乎没有充分代表较晚近的出生，而且有例子同时给出婚姻率和儿童死亡率，导致统计上自相矛盾。

hackernews · thinkingemote · 9月3日 14:51 · [社区讨论](https://news.ycombinator.com/item?id=49550698)

**背景**: Any Human Ever 属于一类把大规模数据变得有个人色彩的创意 AI 与数据可视化项目。它背后的关键人口学概念是：由于近几世纪人口快速增长，从“所有曾生活过的人”中随机抽取一个，往往更可能出生在离现代较近的时期；这也意味着项目必须小心处理所采用的概率分布。

**社区讨论**: 反响褒贬不一：有人觉得它令人感动，或很适合“Thousand Year Old Vampire”这类角色扮演游戏；也有人指出统计数字不真实、抽样分布错误，以及引用可能存在 AI 幻觉。总的来说，大家认为它发人深省且有趣，但如果当作真实数据来看则会误导人。

**标签**: `#visualization`, `#history`, `#data-quality`, `#simulation`, `#statistics`

---