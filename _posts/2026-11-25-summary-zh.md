---
layout: default
title: "Horizon Summary: 2026-11-25 (ZH)"
date: 2026-11-25
lang: zh
---

> 从 16 条内容中筛选出 12 条重要资讯。

---

1. [Ternary Bonsai 2.5 27B：把接近前沿的编程能力塞进消费级硬件](#item-1) ⭐️ 8.0/10
2. [OpenAI 称 GPT-6 无需专用模型即可设计蛋白质结合体](#item-2) ⭐️ 8.0/10
3. [泄露的 GTA 6 Xbox 版本正通过 Wine 式项目在 Windows 上运行](#item-3) ⭐️ 8.0/10
4. [Quad9 因法院命令停止在法国提供公共 DNS 服务](#item-4) ⭐️ 8.0/10
5. [Simon Willison 谈十二个月内 LLM 的三个拐点](#item-5) ⭐️ 8.0/10
6. [GPT-6.2 Astra 自主破解 1808 年匿名素描本的作者之谜](#item-6) ⭐️ 8.0/10
7. [Z.ai 发布 GLM-5.4，首个循环 Transformer 模型，一周内第二例](#item-7) ⭐️ 8.0/10
8. [Ladybird 发布首个 Alpha 版本，独立浏览器引擎终于可直接安装](#item-8) ⭐️ 8.0/10
9. [GreyNoise 披露针对 Check Point 安全管理服务器的持续入侵活动](#item-9) ⭐️ 7.0/10
10. [Jetty Pro：取代 Dock 的 Mac 新应用引发订阅模式争议](#item-10) ⭐️ 7.0/10
11. [Songe：用闲置算力训练本地模型的开源训练引擎](#item-11) ⭐️ 7.0/10
12. [爱丁堡大学研究：心脏病发作与中风风险可提前数十年预测](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Ternary Bonsai 2.5 27B：把接近前沿的编程能力塞进消费级硬件](https://prismml.com/news/bonsai-2-5-27b) ⭐️ 8.0/10

Ternary Bonsai 2.5 27B 是一个 270 亿参数的模型，以三值量化（ternary）的 Q2 GGUF 形式发布，据称在 SWE-bench Verified 上取得了接近前沿模型的成绩，同时能在 24GB 内存的 Mac Mini 上流畅运行。社区用户实测生成速度约为每秒 22 至 25 个 token，并且在一台 24GB 内存的 M5 Pro Mac Mini 上可轻松容纳最高 128K 的上下文。 如果这些报告的数据经得起检验，那么一个能在笔记本级设备上运行的 27B 模型，就可能把过去依赖云端 API 或数据中心 GPU 的智能体编程工作流带到本地消费级硬件上。这也强化了一个趋势：经过激进量化的小模型正在真实软件工程任务上缩小与前沿系统的差距。 三值量化把权重压缩为 -1、0、+1 三个取值，每个权重理论上约 1.58 比特，这正是 27B 模型能够塞进很小内存占用的原因；代价是模型质量高度依赖具体的量化格式，而且提示词处理速度可能落后于生成本身。其核心卖点建立在 SWE-bench Verified 之上，这是一个经人工筛选、包含 500 个实例的基准，评论者指出它虽然有用，但并不能完全代表真实的编程能力。

hackernews · b0m · 11月24日 20:08 · [社区讨论](https://news.ycombinator.com/item?id=50633922)

**背景**: 三值量化通常被称为 1.58 比特量化，它只用三个取值来表示每个模型权重，而不是标准格式所用的 16 比特，从而大幅缩小模型体积和内存带宽需求，但会付出一定的精度代价。GGUF 是 llama.cpp 及相关本地推理工具使用的文件格式，其中 Q2 系列属于压缩力度最大的档位之一。SWE-bench Verified 是经过人工验证的 500 个 GitHub issue 任务子集，模型必须写出能通过项目测试套件的补丁，因此它被视为衡量 AI 编程智能体在真实代码仓库上表现的最常被引用的指标之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://runaihome.com/blog/ternary-llm-1-58-bit-quantization-home-lab-2026/">Breaking the 1.58-Bit Barrier: What Ternary LLM Quantization Means...</a></li>
<li><a href="https://www.swebench.com/verified.html">SWE-bench Verified</a></li>
<li><a href="https://canitrun.dev/guides/quantization-explained/">GGUF Quantization Explained: Q4, Q5, Q6, Q8 Compared</a></li>

</ul>
</details>

**社区讨论**: 讨论气氛热烈但带有怀疑：一位用户在 24GB 的 Mac Mini 上实测到 22.3 tok/s 和 128K 上下文，认为对小模型而言相当惊艳；另一位则追问这一结果究竟反映真实能力、基准“刷分”，还是仅仅说明前沿能力会以约六个月的滞后期出现在小模型上。还有人希望看到与同尺寸、同等量化程度的模型（如 Qwen 系列）的直接对比，另有一位用户分享了在 MacBook Air M3 上用 7–8GB 内存运行 1 比特模型画出的、意外像样的“鹈鹕”测试结果。

**标签**: `#llm`, `#quantization`, `#local-inference`, `#small-models`, `#swe-bench`

---

<a id="item-2"></a>
## [OpenAI 称 GPT-6 无需专用模型即可设计蛋白质结合体](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/) ⭐️ 8.0/10

OpenAI 发布报告称，他们向 GPT-6.2 提供了五个靶标蛋白的三维结构并标注了希望结合的位置，随后该模型自行编写代码生成了三维 minibinder（微型结合蛋白）设计方案，全程未依赖专门的蛋白质 AI 模型。为了让这些设计能在实验室中测试，OpenAI 又用专用模型 SolubleMPNN 为每个设计推荐氨基酸序列，并用其他蛋白质模型筛选候选分子，实验室测试在全部五个靶标上都发现了结合的证据。 这一说法意味着通用大语言模型或许能承担起此前专属蛋白质设计模型（如 RFdiffusion、ProteinMPNN）负责的那部分工作，从而降低计算生物学的入门门槛。如果该结论站得住脚，通用推理模型与专用结构/序列模型之间如何分工、生物科技 AI 的价值由谁获取，都将成为开放问题。 核心结果比表面看起来要窄：GPT-6.2 产出的是骨架层面的三维设计，而真正决定蛋白质本质的序列设计交给了 SolubleMPNN，候选筛选也依赖其他专用预测模型。OpenAI 报告的只是在五个靶标上“出现了结合的证据”，并未给出解析结构或亲和力数据，因此这些设计尚未与成熟的计算流程做基准对比。

hackernews · acossta · 11月24日 21:02 · [社区讨论](https://news.ycombinator.com/item?id=50634658)

**背景**: 从头蛋白质设计通常分为两步：先生成能贴合靶标位点的三维骨架形状（过去依赖 RFdiffusion 等工具），再找出能折叠成该形状的氨基酸序列（由 ProteinMPNN 及其优化溶解度的变体 SolubleMPNN 等逆折叠模型完成）。Minibinder 是能紧密附着在特定位点上的小型工程蛋白，被视为抗体在治疗和诊断领域的替代方案。OpenAI 的主张是，通用推理模型可以通过自行编写设计代码来完成第一步，而不需要专门针对蛋白质结构训练的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/">GPT - 6 models demonstrate intrinsic protein - design capabilities</a></li>
<li><a href="https://proteiniq.io/app/soluble-mpnn">SolubleMPNN Online - ProteinIQ</a></li>
<li><a href="https://www.nature.com/articles/s41467-025-56369-w">De novo design of protein minibinder agonists of TLR3 - Nature</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论普遍对这套叙事持怀疑态度：一条高票回复追问 GPT-6.2 究竟设计出了什么，因为真正定义蛋白质的是氨基酸序列，而这部分交给了 SolubleMPNN。也有人认为真正的看点在于写代码是通用模型的“超能力”——任何能归结为写出更好代码的任务都会被自动化；一位 Baker 实验室的博士则表示，这一思路与实验室多年前的预期一致，当时把蛋白质模型与语言模型融合还被认为荒诞可笑。

**标签**: `#AI`, `#protein-design`, `#LLM`, `#computational-biology`, `#OpenAI`

---

<a id="item-3"></a>
## [泄露的 GTA 6 Xbox 版本正通过 Wine 式项目在 Windows 上运行](https://twitter.com/raul_bs3/status/2125213756238291075) ⭐️ 8.0/10

一份泄露的《侠盗猎车手 6》（GTA 6）Xbox 版本——据称由名为 "Cyberleek" 的泄露者先发布资源、后发布游戏可执行文件——正被 xcl 和 VIctory 等社区项目设法在 Windows 上运行，这些项目采用类似 Wine 的兼容层思路，而不是完整的反编译再原生移植流程。该话题在 Hacker News 上获得约 290 分和 370 条评论，此前还有关于 "Leonida" GTA 6 重编译项目被 GitHub 封禁的相关讨论。 这一成果说明，由于现代 Xbox 主机在架构上非常接近 Windows PC，爱好者可以在官方 PC 版发布之前很久就把一款重量级主机游戏搬上 PC，这引发了关于 DRM、平台控制权以及游戏保存边界的尖锐问题。它也让一场持续中的争论更加激烈：在 GTA 6 已被视为史上最昂贵创作之一的情况下，此类泄露与重编译项目究竟是在帮助还是在伤害这个行业。 根据社区解释，该 Xbox 二进制文件没有特别的 DRM 或混淆保护，因此难点不在于执行代码，而在于解决兼容性和图形层问题，xcl 与 VIctory 项目正是用 Wine 式的系统调用转换来应对这些难点。此前该领域的尝试——尤其是 Leonida 重编译项目——已被从 GitHub 下架，因此真正的瓶颈在于分发渠道和法律风险，而非纯粹的技术可行性。

hackernews · andrem · 11月24日 13:19 · [社区讨论](https://news.ycombinator.com/item?id=50627783)

**背景**: 兼容层是一种软件，它把为某一系统编译的二进制程序所发起的调用翻译成宿主系统的原生调用，从而让这些程序在另一系统上运行；Wine 是最著名的例子，它不是模拟器，却能让 Windows 游戏在类 Unix 系统上运行。现代 Xbox 主机与 Windows 及 DirectX 图形栈共享大量组件，微软的 Game Development Kit（GDK）同时面向 Xbox 和 Windows，这就是为什么 Xbox 版本比 PlayStation 版本更接近 PC 版本。重编译项目走的是另一条路，通过静态翻译或反编译把原始游戏代码转换为原生可执行文件——这一技术因《塞尔达传说：王国之泪》等游戏的社区移植而广为人知。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Compatibility_layer">Compatibility layer - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wine_(software)">Wine (software) - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/en-us/gaming/gdk/?view=gdk-2604">Game Development Kit (GDK) documentation</a></li>

</ul>
</details>

**社区讨论**: 评论者更多是好奇而非恐慌：有人主张这类项目并不会对游戏生产构成生存威胁，因为 GTA 6 已经利润丰厚，并且还会通过 DLC 和官方 PC 版赚得更多；另一位则梳理了技术图景——先泄露资源再泄露二进制文件、没有 DRM、剩下的主要是兼容性和图形工作。还有人整理了相关 Hacker News 讨论帖的脉络，一位持怀疑态度的评论者则追问为何必须要靠泄露的 Xbox 版本才能实现，并警告此类成功可能促使发行商转向永远在线的云端组件，使其无法被反编译。

**标签**: `#game-preservation`, `#reverse-engineering`, `#windows`, `#xbox`, `#hacker-news`

---

<a id="item-4"></a>
## [Quad9 因法院命令停止在法国提供公共 DNS 服务](https://quad9.net/news/blog/quad9-service-deactivation-in-france/) ⭐️ 8.0/10

非营利公共 DNS 解析服务 Quad9 已于 2026 年 11 月 24 日起停止向法国用户提供服务，起因是法国法院要求其封锁被指侵犯版权的域名。如今从法国网络发往 9.9.9.9 的查询会返回 REFUSED 响应，并附带 EDNS 扩展 DNS 错误码 18（Prohibited），说明该服务因法国法律限制而不可用。 这是大型全球公共解析器首次选择退出整个国家、而非服从站点封锁命令，为 DNS 过滤义务与跨境基础设施之间的冲突树立了先例。它影响法国用户的隐私与安全状况，也表明版权执法正日益瞄准域名解析层，而非托管方或 ISP。 Quad9 同时提供未过滤与过滤（拦截恶意软件）两种版本，支持 DoH、DoT 和传统 DNS；此次停用仅针对法国用户，其他地区服务照常。由于免费的全球任播解析器难以把封锁限制在一国司法辖区内，Quad9 选择退出而非过滤，社区成员随后发布了可直连的 DoH/DoT 代理，从法国境外转发查询至 Quad9。

hackernews · farrokhi · 11月24日 08:33 · [社区讨论](https://news.ycombinator.com/item?id=50625384)

**背景**: Quad9 是由总部位于瑞士的非营利基金会运营的免费递归 DNS 解析器，以拦截恶意软件和钓鱼域名、同时尽量少记录用户数据而闻名。DNS 解析器相当于互联网的通讯录，负责把域名翻译成 IP 地址，因此谁掌握了域名解析，谁就能决定用户能访问哪些网站。法国法院与版权方（尤其是体育转播商 beIN Sports）此前已获得要求中间商封锁盗版相关域名的命令，如今这类命令正从接入服务商扩展到公共解析器。REFUSED 响应（RCODE 5）表示域名服务器出于策略原因刻意拒绝作答，Quad9 正是用这种方式表明法律封锁，而不是返回一个虚假的“域名不存在”结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eff.org/deeplinks/2026/10/french-courts-site-blocking-orders-drive-quad9-out-france">French Court’s Site-Blocking Orders Drive Quad9 Out Of France</a></li>
<li><a href="https://techstackups.com/articles/quad9-leaves-france-dns-blocking/">Quad9 Is Leaving France: Why DNS Resolvers Are the Wrong ...</a></li>

</ul>
</details>

**社区讨论**: 评论者的反应兼有实用变通方案与公民自由担忧：一位用户公开了支持 DoH、DoT 以及 IPv4/IPv6 上 Do53 的 Quad9 代理作为近似无缝的替代，另一位则用 dig 输出确认了停服，显示 REFUSED 状态与 EDE 18 信息。其他人贴出了此前两个大型 Hacker News 讨论帖以及 TorrentFreak 的报道，也有评论者质疑：如果 Quad9 在法国没有办公室和人员，为何还要遵守该命令。

**标签**: `#DNS`, `#privacy`, `#internet-freedom`, `#France`, `#legal-policy`

---

<a id="item-5"></a>
## [Simon Willison 谈十二个月内 LLM 的三个拐点](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) ⭐️ 8.0/10

在 2026 年 11 月 24 日的一篇文章中，Simon Willison 进一步阐述了自己在 AI Engineer Code Summit 主题演讲中的观点，认为 LLM 与编程智能体的能力在过去十二个月里跨过了三个重要拐点。他把第一个拐点锚定在 2025 年 11 月发布的 Claude Opus 4.5，把第二个拐点锚定在 2026 年 6 月至 7 月出现的“Fable 级模型”，例如 Claude Fable 5。 Willison 是编程智能体领域最受关注的观察者之一，因此他的阶段划分让工程师有了共同语言，用来区分常规模型升级与真正改变日常开发流程的变化。如果这一判断成立，团队评估编程智能体工具时，将更少看基准演示，更多看它们能否可靠完成真实代码库任务。 文章把 Fable 级模型定义为：只要给定目标和必要工具，就能以蛮力方式解决问题的系统；Willison 举的例子是 Claude Fable 为调试 Safari 显示故障，自行搭建了基于 pyobjc-framework-Quartz 的截图机制和启用 CORS 的本地日志服务器。所提供的摘录在第三个拐点被完整描述之前就中断了。

rss · Simon Willison · 11月24日 23:02

**背景**: Simon Willison 是一名开发者兼写作者，以记录 LLM 工具链和智能体工作流而知名；AI Engineer Code Summit 是面向编程智能体开发者和 AI 工程师的会议，2026 年会议于 11 月 10 日至 12 日在旧金山举行。编程智能体是由 LLM 驱动的系统，能够在有限人工指导下读取代码、调用工具并修改代码库，而 Claude Code 是 Anthropic 推出的智能体编程工具。文章以 Anthropic 于 2025 年 11 月发布的 Claude Opus 4.5 的周年纪念为参照点，衡量这些工具进步得有多快。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.engineer/code/2026">AI Engineer Code Summit 2026: AI Engineering Conference, Nov...</a></li>
<li><a href="https://www.anthropic.com/research/building-effective-agents">Building effective AI agents \ Anthropic</a></li>

</ul>
</details>

**标签**: `#LLM`, `#coding-agents`, `#AI-engineering`, `#model-capabilities`, `#industry-analysis`

---

<a id="item-6"></a>
## [GPT-6.2 Astra 自主破解 1808 年匿名素描本的作者之谜](https://simonwillison.net/2026/Nov/24/astra-historical-mystery/) ⭐️ 8.0/10

历史学教授 Mark Humphries 报告称，在仅有极少提示的情况下，GPT-6.2 Astra 仅用 22 分钟就利用公开的一手与二手资料，自主确认了耶鲁大学拜内克图书馆所藏一部 1808 年匿名素描本的创作者身份。该模型找到了一条鲜为人知的日记记载：德沙博子爵（vicomte de Chabot）曾到访附近一条河流，其日期比素描本中提到的日期早五天，并推断沙博的旅行日记（只能从克利夫兰州立大学订购获取）可证实这一归属，最终果然得到印证。 这是一个大语言模型作为自主研究代理而非文本助手的具体案例，其产生的档案发现本身，据 Humphries 所说，将对加拿大史与毛皮贸易史研究者具有重要价值。这也引出一个类似国际象棋“深蓝时刻”的问题：当代理式系统能够完成人类难以复制的研究任务时，各个专业领域将如何应对。 关键线索是一次时间上的对应关系——一则关于沙博到访的日记记载，其日期比素描本在河边记录的某个日期早五天——再加上“那份难以获取的日记能定论”的预测。值得注意的是，这并不是一篇技术深度分析：内容来自一位实践者的博客文章以及 Simon Willison 的链接博客，并未提供基准测试或可复现性细节。

rss · Simon Willison · 11月24日 16:53

**背景**: GPT-6.2 Astra 属于 OpenAI 的 GPT-6.2 系列，于 2026 年 11 月 17 日与更小、更高效的 GPT-6.2 Sol 一同发布，定位为面向艰难、长周期任务的前沿模型，能力涵盖浏览与计算机操作。正是这种浏览与多步规划能力，使得“自主代理”（即在极少人工批准下规划并执行多步工作流的系统）能够自行追查档案线索。耶鲁大学的拜内克珍本与手稿图书馆是全球最重要的珍本与手稿收藏机构之一，涉事素描本已在耶鲁的馆藏系统中数字化。Humphries 的文章明确将此刻比作 1997 年“深蓝”击败卡斯帕罗夫的国际象棋时刻，但他认为历史学受到的冲击会更温和，因为历史写作是解释性的，而非追求单一普世真理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-2-astra-sol/">Introducing GPT-6.2 Astra and Sol | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6.2_Astra">GPT-6.2 Astra</a></li>
<li><a href="https://en.wikipedia.org/wiki/Autonomous_agent">Autonomous agent - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM applications`, `#AI research`, `#historical research`, `#autonomous agents`, `#GPT-6.2`

---

<a id="item-7"></a>
## [Z.ai 发布 GLM-5.4，首个循环 Transformer 模型，一周内第二例](https://simonwillison.net/2026/Nov/23/glm-54/) ⭐️ 8.0/10

中国 AI 实验室 Z.ai 发布了 GLM-5.4，这是其首个采用循环（权重共享、迭代）Transformer 架构的模型，公告题为《GLM-5.4：以我们的首个循环 Transformer 迈向通用编码》。该发布距 Thinking Machines Lab 于 11 月 20 日推出同样采用循环 Transformer 设计的 Inkling 2 Mini 仅三天。 两家独立实验室在一周内先后采用循环 Transformer，说明该技术正成为「单纯堆参数」之外的一条严肃路线，可能改变前沿模型的训练方式与推理成本。若循环设计能在固定参数规模下带来更强的推理深度，将显著降低高性能编码与智能体模型的硬件和显存门槛。 据相关报道，GLM-5.4 将 GLM-5 基座模型的 28 层运行两遍，在不增加参数的情况下获得更深的网络，Z.ai 称这一思路可追溯到 2018 年的 Universal Transformer。该模型尚未开放权重——Z.ai 表示将在完成「必要的安全加固」后开源——目前只能通过 Coding Plan 订阅访问，而非常规 API，不过两者共用同一个兼容 OpenAI 的接口 https://api.z.ai/api/v1。

rss · Simon Willison · 11月23日 23:40

**背景**: 在标准 Transformer 中，每一层在每次前向传播中只执行一次，因此要讓模型「更深」通常意味着增加层数，也就是增加参数量。循环 Transformer 则选取一组权重共享的层，对每个 token 反复运行该层组多次，在每次迭代中精炼隐藏状态——在不增加权重显存开销的前提下换取更多计算量与推理步骤。这一概念并不新（Universal Transformer 可追溯到 2018 年），但近期在小体量开放模型上重新流行，例如 Thinking Machines Lab 的 Inkling 2 Mini 就将中间的 12 层对每个 token 运行三遍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thenextweb.com/news/zai-glm-5-4-loop-transformer-coding-model">Z . ai ’s GLM - 5 . 4 runs its layers twice to rival 2T-parameter models</a></li>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/looped-depth-sharing/">Looped Transformer | Sebastian Raschka, PhD</a></li>
<li><a href="https://thinkingmachines.ai/news/inkling-2-mini/">Introducing Inkling 2 Mini - Thinking Machines Lab</a></li>

</ul>
</details>

**标签**: `#LLM`, `#looped-transformer`, `#GLM`, `#model-release`, `#AI-research`

---

<a id="item-8"></a>
## [Ladybird 发布首个 Alpha 版本，独立浏览器引擎终于可直接安装](https://simonwillison.net/2026/Nov/23/ladybird/) ⭐️ 8.0/10

Ladybird 项目于 2026 年 11 月 23 日发布首个 Alpha 版本，提供了 macOS 和 Linux 的可下载安装包，用户不再需要自行从源码编译。这是这个从零自研的浏览器引擎首次以可直接安装的产品形态交付，而不再只是一个需要自行构建的开发者项目。 从零构建一个全新的浏览器引擎是软件工程中最困难的任务之一，而推出可安装的 Alpha 版本意味着开放网络在 Chromium、Gecko、WebKit 之外多了一个罕见的独立选择——尤其是在浏览器引擎多样性不断萎缩的当下。如果 Ladybird 逐渐成熟，它将能对 Web 标准的实现形成真正的竞争压力，并减少对少数几家大公司主导引擎的依赖。 在实际测试中，Simon Willison 发现 Ladybird 能正常运行依赖 WebAssembly 的工具，例如基于 ffmpeg 的视频压缩工具和 Pyodide（用 Wasm 运行的 Python）REPL；但 Datasette Lite 无法运行，因为 Service Worker 支持尚不完整——LibWeb 中的 `navigator.serviceWorker.startMessages` 仍标注为 FIXME。该浏览器采用多进程架构，由一个 Hub 父进程加上独立的 WebContent、RequestServer、Compositor、MediaServer 和 VideoDecoderServer 进程组成；目前内存占用偏高，单个 WebContent 进程峰值约达 819 MB。

rss · Simon Willison · 11月23日 21:46

**背景**: Ladybird 脱胎于 SerenityOS——Andreas Kling 从零编写的类 Unix 桌面操作系统，该系统自带基于 LibWeb 渲染引擎和 LibJS JavaScript 引擎的浏览器。如今大多数“新”浏览器其实只是 Google Blink（Chromium）、Apple WebKit 或 Mozilla Gecko 的外壳，而 Ladybird 则自行实现了 HTML 解析器、CSS 引擎、布局和 JavaScript 运行时，只借用少数外部库：HarfBuzz 用于文本整形（把 Unicode 文本转换为位置正确的字形）、Skia 用于 2D 图形（一个开源 C++ 绘图库，最初由 Skia 公司开发，2005 年被 Google 收购）、ffmpeg 用于视频解码，SQLite 用于存储。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SerenityOS">SerenityOS - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/HarfBuzz">HarfBuzz - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Skia_Graphics_Library">Skia Graphics Library</a></li>

</ul>
</details>

**标签**: `#browsers`, `#Ladybird`, `#open-source`, `#web-engines`, `#alpha-release`

---

<a id="item-9"></a>
## [GreyNoise 披露针对 Check Point 安全管理服务器的持续入侵活动](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign) ⭐️ 7.0/10

GreyNoise 记录了一场仍在进行中的入侵活动，目标是 Check Point 安全管理服务器，已确认的攻击活动发生在 2026 年 10 月 17 日至 11 月 2 日之间，至少波及全球 22 家不同的组织。在观察到的攻击链中，攻击者连续收集了 "sid" 值取自 JavaScript 的 Math.random() 的会话 Cookie，据此重建了 V8 伪随机数生成器的内部状态，恢复了会话 Cookie 的签名密钥，随后伪造出已签名的管理员会话 Cookie。 安全管理服务器是防火墙策略、访问规则与网关配置的中央控制平面，因此攻击者一旦在该系统上取得管理员权限，就等于掌控了整个组织的安全边界。单一活动即波及 22 家以上组织，说明这类管理接口在互联网上的暴露面相当广，也说明一个会话伪造漏洞足以把非加密安全的伪随机数生成器问题升级为完整的最高权限沦陷。 该攻击在技术上有其看点：V8 的 Math.random() 是一种快速的非加密安全生成器，其内部状态可以从数量不多的连续输出中还原出来，而且报告指出这只是多种攻击向量之一，并非唯一入口。Rejetto HFS 中相关的会话伪造漏洞被编号为 CVE-2026-61500，CVSS 评分为 9.3；社区成员则推测 CVE-2026-16232 才是最初的入侵入口，这意味着许多受害者的管理服务器很可能直接暴露在互联网上。

hackernews · louiereederson · 11月24日 16:32 · [社区讨论](https://news.ycombinator.com/item?id=50630594)

**背景**: Check Point 安全管理服务器是 Check Point 防火墙体系背后的管理中枢：管理员通过它向网关下发策略、读取日志，因此其中保存着整个环境的凭据与信任关系。Node.js 所用 V8 引擎中的 Math.random() 是为速度和模拟场景设计的，并不以保密性为目标，它并非加密安全的伪随机数生成器，只要观察到足够多的输出，就能预测后续取值。这类“用弱随机数生成安全令牌”的缺陷（CWE-338）已多次让攻击者伪造会话 Cookie、彻底绕过身份认证，因此安全令牌必须使用密码学安全的随机数生成器产生。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign">An Active Intrusion Campaign Against Check Point Security ...</a></li>
<li><a href="https://thehackernews.com/2026/10/attackers-target-rejetto-hfs-flaw-that.html">Attackers Target Rejetto HFS Flaw That Enables Admin Session ...</a></li>
<li><a href="https://tech.yahoo.com/cybersecurity/articles/control-tower-left-unguarded-check-094326324.html">The Control Tower Left Unguarded: Check Point ’s Management ...</a></li>

</ul>
</details>

**社区讨论**: 评论者的情绪夹杂着黑色幽默与担忧：有人以“你好啊，我的老朋友 PRNG”来形容这类缺陷存在之久，也有人主张应当直接修复 Math.random() 本身，而不是责怪数以百计误用它的应用。还有读者担心，借助大模型辅助的攻击很快会让水平低得多的犯罪群体也能大规模冲击在线服务与关键基础设施；另有一些人对报告中关于初始入侵途径的含糊表述提出疑问，怀疑是 CVE-2026-16232 叠加管理服务器暴露在互联网上所致。

**标签**: `#security`, `#vulnerability-exploitation`, `#prng`, `#nodejs`, `#check-point`

---

<a id="item-10"></a>
## [Jetty Pro：取代 Dock 的 Mac 新应用引发订阅模式争议](http://hypercritical.co/2026/11/23/jetty-pro) ⭐️ 7.0/10

John Siracusa 于 2026 年 11 月 23 日在 hypercritical.co 上发布了 Jetty Pro，这是一款能在 Mac 各显示器边缘创建可自定义、类似 Dock 的浮动面板的 Mac 应用，面板中可放入文件、文件夹、磁盘卷、应用、快捷指令、间隔、分隔线乃至废纸篓的任意组合。该发布在 Hacker News 上引发强烈反响（277 分、120 条评论），讨论很快转向定价模式以及用户自建替代方案。 这一反响说明 Mac 与独立软件用户群体对订阅制已相当敏感：即便出自口碑良好的开发者、产品打磨精致，也会因原则性问题而非价格遭到抵触。同时它也凸显出一个趋势——用户开始借助 AI 助手“氛围编程”（vibe coding）出小型原生 Mac 应用来替代商业软件，这可能重塑专注型独立工具的市场格局。 Jetty Pro 采用直接分发而非通过 Mac App Store 上架，并且在不启用沙盒的情况下运行，以获得所需的更深层系统访问权限；据俄语媒体报道，最初的普通版 Jetty 本计划登陆 Mac App Store，但相关工作在不到两周后便被放弃。评论者还指出，产品页面从未明确说明它是对 macOS Dock 界面的替代方案，而且用一段演示视频来展示功能会清楚得多。

hackernews · zdw · 11月24日 16:23 · [社区讨论](https://news.ycombinator.com/item?id=50630462)

**背景**: Dock 是 macOS 自带的启动器，通常固定在屏幕底部或侧边，用户在其中放置应用图标、文件夹和最小化的窗口。Jetty Pro 用多个用户自定义的浮动面板替换了这条单一栏位，这些面板分布在每块显示器的边缘。沙盒（sandboxing）是苹果的安全机制，用于限制应用能访问系统的哪些部分；在 Mac App Store 上架的应用必须启用它，而直接分发的应用可以选择不用，以部分安全性换取更强的能力。此外，“氛围编程”（vibe coding）指的是向 Claude、Codex 等 AI 模型描述需求、再对生成的代码进行迭代，从而构建软件的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hypercritical.co/2026/11/23/jetty-pro">Hypercritical: Jetty Pro</a></li>
<li><a href="https://dzen.ru/a/awXdEsnf31f2lBfZ">Вышла Jetty Pro с несколькими панелями вместо одного Dock | Дзен</a></li>
<li><a href="https://nativelinelabs.com/tutorials/build-mac-app-with-ai/">How to Build a Mac App with AI in 2026 | NativeLine Labs</a></li>

</ul>
</details>

**社区讨论**: 整体情绪褒贬不一，但明显偏向对订阅制的抵触：一位评论者表示自己“实在无法再为又一个订阅找理由”，并强调金额多少（一年 1 美元还是 100 美元）并无区别。也有人建议采用断供后仍可继续使用的授权方式，让买家保留停止付费时所拥有的版本；另有一位开发者称已用 AI 打造的原生 Mac 工具替换了多款笨重应用，这些自建工具专注于性能与极小的内存占用。

**标签**: `#Mac apps`, `#subscription pricing`, `#indie software`, `#native development`, `#Hacker News discussion`

---

<a id="item-11"></a>
## [Songe：用闲置算力训练本地模型的开源训练引擎](https://github.com/sous-labs/songe) ⭐️ 7.0/10

Songe 是 sous-labs 在 GitHub 上以 Apache-2.0 许可证发布的一个训练引擎，它利用机器本身的闲置算力来微调本地模型，而不需要专门的训练设备。在首次训练开始前，它会自动测量这台电脑一次能“学”多少，然后只训练装得下的部分，这一设计思路记录在仓库的 DESIGN.md 中。 如果它确实如宣传所说，那么它就把普通台式机变成了“兼职”微调机器，从而降低了模型定制的门槛——这与近年来一批关于利用边缘闲置算力训练基础模型的研究目标一致。对租不起 GPU 的个人开发者和小团队来说，这可能让针对特定任务的小型本地模型适配变得切实可行。 该引擎最突出的特点是先做一次硬件能力探测，之后只训练机器真正能承担的工作量，从而避免在配置一般的设备上出现显存不足崩溃。不过，项目目前尚未公布模型在每次训练后究竟能提升多少的基准数据，而这正是评论者抓住的主要空白。

hackernews · bluepeter · 11月24日 15:03 · [社区讨论](https://news.ycombinator.com/item?id=50629231)

**背景**: 微调是指让预训练模型适配特定任务或风格，Unsloth、Axolotl、torchtune 等工具主要借助大幅降低显存占用的 LoRA 和 QLoRA 技术，让这在消费级 GPU 上变得可行。而分布式训练传统上假设数据中心里有同构的 GPU，因此像 Cleave 框架这样的研究正在探讨：异构、时有时无的边缘设备能否贡献有用的训练工作。Songe 正处在这两股趋势的交汇处：个人规模的微调，加上对原本被浪费的算力的机会性利用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/sous-labs/songe">GitHub - sous-labs/ songe : A training engine for your local model ...</a></li>
<li><a href="https://arxiv.org/html/2512.22142v2">On Harnessing Idle Compute at the Edge for Foundation Model ...</a></li>
<li><a href="https://toolhalla.ai/blog/fine-tune-llm-locally-guide-2026">How to Fine - Tune an LLM Locally : Complete Guide (2026) | ToolHalla</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者颇感兴趣，但更想要证据：有人希望能有“LLM 版的 SETI@home”，并询问 Songe 能否做成分布式；也有人询问每个“梦境 epoch”或周末训练大致能带来多少提升。还有人追问引擎如何判断模型是否变好，并希望在 README 中看到一个前后对比的完整示例；另有一位用户想知道，在没有 GPU、仅通过 Ollama 运行小型 Qwen 模型的 Windows 电脑上，它是否值得一用。

**标签**: `#local LLMs`, `#distributed training`, `#idle compute`, `#model fine-tuning`, `#open-source tools`

---

<a id="item-12"></a>
## [爱丁堡大学研究：心脏病发作与中风风险可提前数十年预测](https://www.ed.ac.uk/news/heart-attack-and-stroke-risk-detectable-decades-in-advance) ⭐️ 6.0/10

一项由爱丁堡大学主导的研究表明，提前数年甚至数十年测量的心血管风险因素，可以预测一个人未来发生心脏病发作和中风的可能性，其时间跨度远超目前临床实践的常规做法。该研究在 Hacker News 上引发关注，因为它说明利用临床医生本就常规检测的指标进行超长期风险预测是可行的。 如果风险能在数十年前就被识别出来，那么预防措施——包括生活方式改变、他汀类药物或 GLP-1 受体激动剂等新型药物——就可以更早启动，此时动脉仍相对健康，干预成本最低、效果也最好。这一转变可能重塑基层医疗对数百万表面上健康人群的筛查与治疗方式。 研究考察的风险因素包括血压、高密度脂蛋白与总胆固醇、以 CRP 衡量的炎症水平、BMI、肌钙蛋白以及糖尿病和吸烟状况；有评论者指出，其中许多指标可以通过美国心脏协会的 PREVENT 方程组合成一个 30 年风险估计值。与任何观察性风险模型一样，这种预测是概率性的，描述的是群体层面的关联而非某个人的必然结局，而且各因素的可改变程度差异很大。

hackernews · gmays · 11月24日 21:51 · [社区讨论](https://news.ycombinator.com/item?id=50635271)

**背景**: 心血管疾病——心脏病发作和中风——仍是全球首要死因，它的发展十分缓慢，胆固醇斑块会在数十年间逐渐沉积在动脉中。他汀类药物通过抑制肝脏合成胆固醇所需的酶来降低低密度脂蛋白（“坏”胆固醇），被广泛用于高风险人群的一级预防；GLP-1 受体激动剂原本是糖尿病药物，如今也因其减重效果和对血管的作用而被研究用于心血管保护。CRP（C 反应蛋白）是一种通用的炎症标志物，肌钙蛋白则是心肌受损时释放的蛋白质，两者都被用来在胆固醇之外进一步细化风险估计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Statin">Statin - Wikipedia</a></li>
<li><a href="https://my.clevelandclinic.org/health/treatments/22282-statins">Statins: Benefits & Side Effects - Cleveland Clinic</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10455499/">SGLT2 Inhibitors vs. GLP - 1 Agonists to Treat the Heart, the Kidneys...</a></li>

</ul>
</details>

**社区讨论**: 评论者观点分歧明显：一些人认为这些发现显而易见，有人质问该研究除了肌钙蛋白和 CRP 的结果外，还比“高血压和高胆固醇会增加心脏病风险”这一常识多提供了什么。另一些人则聚焦于可操作性，提到基于 PREVENT 的计算器、用洋车前子壳降低低密度脂蛋白、他汀类药物（其中一位用户讲述了自己的不良反应以及随后的饮食调整），以及被视作未被充分利用的万能方案的 GLP-1 药物，这反映出关于早期风险预测究竟能在多大程度上改变结局的更广泛争论。

**标签**: `#health`, `#cardiovascular-risk`, `#medical-research`, `#prevention`, `#hacker-news`

---