---
layout: default
title: "Horizon Summary: 2026-05-25 (ZH)"
date: 2026-05-25
lang: zh
---

> 从 25 条内容中筛选出 13 条重要资讯。

---

1. [推翻航空工程原理：粗糙表面可减少阻力](#item-1) ⭐️ 9.0/10
2. [Audiomass：免费开源的 Web 多轨音频编辑器](#item-2) ⭐️ 8.0/10
3. [AI 芯片中内存成本占比近三分之二](#item-3) ⭐️ 8.0/10
4. [约束衰减：LLM 智能体在架构规则下表现脆弱](#item-4) ⭐️ 8.0/10
5. [微软开源最早 DOS 源代码，从纸质打印件恢复](#item-5) ⭐️ 8.0/10
6. [骗子滥用微软内部账户发送垃圾邮件](#item-6) ⭐️ 8.0/10
7. [苹果推出 PICO：面向感知质量的学习型图像编解码器](#item-7) ⭐️ 8.0/10
8. [Armin Ronacher 批评 AI 生成的错误报告](#item-8) ⭐️ 8.0/10
9. [DeepSeek Reasonix：高缓存原生编码代理](#item-9) ⭐️ 7.0/10
10. [从 Go 迁移到 Rust 的指南引发语言之争](#item-10) ⭐️ 7.0/10
11. [掌握 Dyalog APL：交互式 Jupyter Notebook 入门教程](#item-11) ⭐️ 7.0/10
12. [Greg Brockman 访谈揭示 OpenAI 历史内幕](#item-12) ⭐️ 7.0/10
13. [Claude 从 Usborne PDF 重现 1983 年游戏《Mad House》](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [推翻航空工程原理：粗糙表面可减少阻力](https://www.wired.com/story/a-fundamental-principle-of-aeronautical-engineering-has-been-overturned/) ⭐️ 9.0/10

日本东北大学研究人员在风洞测试中发现，分布式的微粗糙度可将空气阻力降低高达 43.6%，挑战了长期以来认为表面越光滑阻力越小的传统观点。 这一发现可通过简单的表面处理（如喷砂）来减少阻力，从而显著提升飞机、汽车和高铁等交通工具的燃油效率，有望重塑飞行器设计并促进现有车辆的改造。 阻力降低仅在边界层过渡区观测到，整个表面的净改善幅度在文章中未量化。该技术通过制造微米级粗糙度（类似高尔夫球表面的凹坑），促使边界层提前转捩为湍流，从而减小分离区。

hackernews · littlexsparkee · 5月24日 19:10 · [社区讨论](https://news.ycombinator.com/item?id=48260117)

**背景**: 在流体力学中，边界层是贴近物体表面的薄层流体。层流边界层摩擦阻力小但易分离，导致压差阻力大；湍流边界层摩擦阻力大却不易分离，从而降低压差阻力。传统观点认为光滑表面能维持层流从而总阻力最小，但这项研究表明，在适当位置引入可控粗糙度可触发湍流，实现整体减阻。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.onenewspage.com/n/World/1ztfis6087/surface-roughness-trick-can-reduce-aerodynamic-drag.htm">A surface roughness trick can reduce aerodynamic drag - One News Page</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，竞技帆船选手早已使用细砂纸打磨船体以减少摩擦，高尔夫球表面的凹坑也是粗糙度减阻的已知案例。部分人质疑整个表面的净减阻效果是否足够显著，以及是否适用于实际改造。

**标签**: `#aeronautical engineering`, `#aerodynamics`, `#drag reduction`, `#fluid dynamics`, `#aircraft design`

---

<a id="item-2"></a>
## [Audiomass：免费开源的 Web 多轨音频编辑器](https://audiomass.co/?multitrack=1) ⭐️ 8.0/10

Audiomass 已作为一款完全在浏览器中运行的免费开源多轨音频编辑器发布，支持 FLAC 文件，并拥有直观的用户界面。 该工具使任何拥有浏览器的人都能进行高质量的多轨音频编辑，降低了音乐制作和音频编辑的门槛。其开源特性也允许社区贡献和定制。 该编辑器具有干净、直观的用户体验，让人想起 Cool Edit Pro，并且开箱即用支持 FLAC 文件。它使用 JavaScript 构建，编码风格让一些用户感到怀旧。

hackernews · pantelisk · 5月24日 15:25 · [社区讨论](https://news.ycombinator.com/item?id=48258015)

**背景**: 像 Audacity 或 Adobe Audition 这样的多轨音频编辑器通常需要安装，并且对初学者来说可能很复杂。Audiomass 提供了一个基于 Web 的替代方案，无需下载，方便快速编辑或存储空间有限的用户使用。

**社区讨论**: 社区评论普遍非常积极，称赞其直观的用户体验、FLAC 支持和怀旧的编码风格。一些用户表达了对云基础轨道共享和分支等协作功能的兴趣，并请求支持 XM 等追踪器格式。

**标签**: `#audio editor`, `#open source`, `#web app`, `#multitrack`, `#free tool`

---

<a id="item-3"></a>
## [AI 芯片中内存成本占比近三分之二](https://epoch.ai/data-insights/ai-chip-component-cost-shares) ⭐️ 8.0/10

Epoch AI 的最新分析显示，AI 加速器芯片中内存的组件成本占比已接近三分之二，较往年大幅上升。 这一成本转变表明，未来 AI 硬件降价可能更多取决于内存供应动态而非芯片制造改进，将对数据中心基础设施和消费级内存市场产生影响。 分析指出，高带宽内存（HBM）作为一种关键的 AI 加速器 3D 堆叠 DRAM 技术，是成本上涨的主要推手，其需求已超过供应。

hackernews · intelkishan · 5月24日 16:31 · [社区讨论](https://news.ycombinator.com/item?id=48258684)

**背景**: AI 加速器（如 GPU 和 TPU）高度依赖高速内存向计算单元输送数据。高带宽内存（HBM）通过垂直堆叠 DRAM 晶片实现高带宽和大容量，但制造成本高昂。随着 AI 工作负载增长，对 HBM 的需求激增，导致内存成本在芯片总成本中的占比持续攀升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://semiengineering.com/high-bandwidth-memory-hbm-everything-you-need-to-know/">High Bandwidth Memory (HBM): Everything You Need To Know</a></li>

</ul>
</details>

**社区讨论**: 社区评论意见不一：有人认为一旦 DRAM 供应赶上需求，硬件成本可能降低 3 倍；也有人感叹消费级内存价格飙升（例如 96GB 内存从几年前 250 美元涨至 1200 美元）。游戏玩家和 PC 爱好者感到受 AI 内存需求挤压。

**标签**: `#AI hardware`, `#memory costs`, `#DRAM`, `#chip components`, `#economics`

---

<a id="item-4"></a>
## [约束衰减：LLM 智能体在架构规则下表现脆弱](https://arxiv.org/abs/2605.06445) ⭐️ 8.0/10

一项新研究提出了“约束衰减”现象，即基于 LLM 的编码智能体在被要求遵循明确的架构约束时，生成的代码质量下降，从而使其在生产后端开发中不可靠。 这一发现意义重大，因为它揭示了将 LLM 智能体用于实际软件工程时的关键弱点——在安全性和可扩展性等非功能约束至关重要的情况下。这表明，虽然 LLM 擅长原型开发，但它们还不足以胜任生产级代码生成。 该研究系统地测量了随着非功能约束密度增加时智能体的性能，观察到了明显下降。然而，由于成本限制，GPT-4 或 Claude 等前沿模型并未得到全面测试，因此结果可能不适用于最先进的 LLM。

hackernews · wek · 5月24日 12:55 · [社区讨论](https://news.ycombinator.com/item?id=48256912)

**背景**: LLM 智能体是根据提示自动生成代码的 AI 系统。在后端开发中，代码通常必须遵循严格的架构规则和非功能需求。约束衰减指的是当这些约束被明确施加时，生成质量下降的现象，这与无约束任务中看到的高性能形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48256912">Constraint Decay: The Fragility of LLM Agents in Back End Code Generation</a></li>
<li><a href="https://arxiv.org/pdf/2605.06445">[PDF] Constraint Decay: The Fragility of LLM Agents in Backend Code Generation</a></li>

</ul>
</details>

**社区讨论**: 评论者从个人经验证实了这一现象，指出增加约束和风格指南常常会使智能体输出变差。一位开发者建议在生成过程中逐步引入约束可能会缓解衰减，而另一位则指出该研究未测试前沿模型的局限性。

**标签**: `#LLM`, `#code generation`, `#agents`, `#software engineering`, `#AI reliability`

---

<a id="item-5"></a>
## [微软开源最早 DOS 源代码，从纸质打印件恢复](https://arstechnica.com/gadgets/2026/04/microsoft-open-sources-the-earliest-dos-source-code-discovered-to-date/) ⭐️ 8.0/10

微软开源了“迄今发现最早的 DOS 源代码”，这些代码是由一个专门的保护团队通过 OCR 和手动转录从纸质打印件中恢复的。 此次发布保护了计算史上的关键片段，使开发者和历史学家能够研究最具影响力的操作系统之一的起源，同时也凸显了数字保存的重要性。 源代码由 Yufeng Gao 和 Rich Cini 领导的“DOS 反汇编小组”转录，由于现代 OCR 软件难以处理几十年前的打印件质量，需要付出大量手动努力。

hackernews · DamnInteresting · 5月24日 01:21 · [社区讨论](https://news.ycombinator.com/item?id=48253386)

**背景**: MS-DOS 是 1980 年代 IBM 兼容 PC 的基础操作系统。微软最初从 Seattle Computer Products 收购了 86-DOS 并进行了适配。这批早期源代码比之前可用的版本更早，曾被认为已丢失，直到这些打印件被恢复。

**社区讨论**: 评论者表达了感激和怀旧之情，有人指出微软还开源了早期的 BASIC 代码。一位用户成功在 DOSBox 中运行了该源代码，其他人则讨论了有趣的 OCR 恢复过程。

**标签**: `#open-source`, `#retro-computing`, `#history`, `#Microsoft`, `#DOS`

---

<a id="item-6"></a>
## [骗子滥用微软内部账户发送垃圾邮件](https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/) ⭐️ 8.0/10

数月以来，骗子利用一个漏洞，从微软内部邮箱（msonlineservicesteam@microsoftonline.com）发送垃圾邮件，该邮箱通常用于合法的账户通知。 这一滥用行为削弱了用户对微软域身份验证的信任，暴露了其邮件基础设施中的系统性安全缺陷，可能使用户面临钓鱼攻击的风险。 该漏洞的具体机制尚不明确，但骗子发送的邮件看似来自合法的 msonlineservicesteam@microsoftonline.com 地址，从而绕过了常规的垃圾邮件过滤器。

hackernews · spike021 · 5月24日 00:51 · [社区讨论](https://news.ycombinator.com/item?id=48253186)

**背景**: 邮件伪造是一种攻击技术，攻击者伪造发件人地址以冒充可信来源。DMARC（基于域的消息认证、报告和一致性）是一种旨在防止此类伪造的标准，但其有效性取决于正确的域配置。微软对其众多域的管理被批评为分散，导致难以执行一致的安全策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/">Scammers are abusing an internal Microsoft account ... | TechCrunch</a></li>
<li><a href="https://techplanet.today/post/microsofts-internal-account-abuse-a-critical-security-failure-that-undermines-user-trust">Microsoft 's Internal Account Abuse : A Critical Security... | TechPlanet</a></li>
<li><a href="https://powerdmarc.com/email-spoofing-security/">Email Spoofing Security</a></li>

</ul>
</details>

**社区讨论**: 评论者对微软的域名管理表示不满，有人指出微软内部甚至没有完整的域名资产清单。其他用户分享了从微软官方地址收到垃圾邮件的经历，并指出更广泛的问题，比如 Outlook 字体中'rn'和'm'难以区分。

**标签**: `#security`, `#microsoft`, `#spam`, `#phishing`, `#domain-security`

---

<a id="item-7"></a>
## [苹果推出 PICO：面向感知质量的学习型图像编解码器](https://apple.github.io/ml-pico/) ⭐️ 8.0/10

苹果发布了 PICO，这是首个直接针对人类视觉系统优化的学习型图像编解码器，能在极低比特率下实现有竞争力的压缩比。 这代表着向实用的学习型图像压缩迈出的重要一步，但社区反馈指出存在幻觉伪影、解码速度慢以及对比编解码器选择等问题。 PICO 利用神经架构搜索优化感知质量，在移动设备上运行时间低于 230 毫秒，但解码 1200 万像素图像约需 150 毫秒，比 JPEG-XL 等传统编解码器慢得多。

hackernews · ksec · 5月24日 12:01 · [社区讨论](https://news.ycombinator.com/item?id=48256565)

**背景**: 学习型图像压缩使用神经网络将图像编码为紧凑的潜在表示，再解码还原，通常针对 PSNR 或 MS-SSIM 等指标进行优化。PICO 则直接使用 LPIPS 等指标和自定义神经架构搜索来优化感知质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apple.github.io/ml-pico/">What Matters in Practical Learned Image Compression</a></li>
<li><a href="https://axbrief.com/blog/applemlresearch-nokeau">Learned Image Compression Delivers 40% Lower Bitrate... - AX BRIEF</a></li>
<li><a href="https://huggingface.co/papers/2605.05148">Paper page - What Matters in Practical Learned Image Compression</a></li>

</ul>
</details>

**社区讨论**: 评论指出压缩后的图像常出现不自然的幻觉感，如针织纹理被模糊条纹替代。有人质疑对比中未包含 JPEG-XL 的公平性，并指出每 1200 万像素 150 毫秒的解码速度对于实际使用来说太慢。

**标签**: `#image compression`, `#machine learning`, `#Apple`, `#codec`, `#perceptual`

---

<a id="item-8"></a>
## [Armin Ronacher 批评 AI 生成的错误报告](https://simonwillison.net/2026/May/24/armin-ronacher/#atom-everything) ⭐️ 8.0/10

Flask 和 Jinja 的创建者 Armin Ronacher 于 2026 年 5 月 24 日发表博文，批评提交给他的开源项目 Pi 的 AI 生成的错误报告，称其不准确、过于自信，且缺乏人类自己的表达。 这一批评突显了开源维护中日益严重的问题：低质量的 AI 生成问题报告浪费维护者时间，并削弱对自动化工具的信任。它呼吁回归简单、由人类撰写的观察报告，以维护项目健康。 Ronacher 提出了一种四要点的问题报告格式：运行了什么命令、预期什么结果、实际发生了什么、以及确切的错误或日志。他指出，AI 工具常常产生“对根本原因的完全猜测、虚假的最小复现步骤以及建议的实现策略”，这些内容充满自信但却是错误的。

rss · Simon Willison · 5月24日 18:46

**背景**: 大型语言模型（LLM）越来越被开发者用于生成错误报告，通常是将错误消息或代码片段粘贴到 AI 工具中，然后直接将 AI 的输出提交到问题追踪器。这种做法可能因提示工程错误或模型幻觉而引入不准确信息，导致 Ronacher 所称的“垃圾问题”。Ronacher 是 Python 社区中受人尊敬的人物，以创建 Flask 和 Jinja 等流行框架而闻名。

**标签**: `#open source`, `#AI`, `#bug reports`, `#software maintenance`

---

<a id="item-9"></a>
## [DeepSeek Reasonix：高缓存原生编码代理](https://esengine.github.io/DeepSeek-Reasonix/) ⭐️ 7.0/10

DeepSeek Reasonix 是一个新的终端 AI 编码代理，原生集成 DeepSeek API，旨在通过保持高前缀缓存命中率来大幅降低长编码会话中的令牌成本。 通过优化缓存使用，Reasonix 可以实现比其他编码代理更低的成本，从而可能使 AI 辅助编码对大型项目更加平民化。 该代理围绕前缀缓存稳定性构建，确保重复提示命中缓存。它在终端中运行，专为 DeepSeek V4 Pro 模型设计。

hackernews · Alifatisk · 5月24日 13:02 · [社区讨论](https://news.ycombinator.com/item?id=48256953)

**背景**: 前缀缓存允许 AI API 重用共享提示初始部分的计算结果，从而减少延迟和成本。许多编码代理通过添加唯一令牌来破坏缓存，而 Reasonix 则设计为避免这种情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://api-docs.deepseek.com/quick_start/agent_integrations/reasonix">Integrate with Reasonix - DeepSeek API Docs</a></li>
<li><a href="https://news.ycombinator.com/item?id=48256953">DeepSeek reasonix, DeepSeek native coding agent with high caching ...</a></li>
<li><a href="https://github.com/esengine/deepseek-reasonix">GitHub - esengine/DeepSeek-Reasonix ...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论观点不一：一些用户成功使用了 DeepSeek 的缓存而无需专用代理，另一些人则批评该代理生成的网站过于复杂。还有关于是否有时为了更好结果而故意破坏缓存的争论。

**标签**: `#deepseek`, `#coding agent`, `#caching`, `#AI tools`, `#cost efficiency`

---

<a id="item-10"></a>
## [从 Go 迁移到 Rust 的指南引发语言之争](https://corrode.dev/learn/migration-guides/go-to-rust/) ⭐️ 7.0/10

一篇从 Go 迁移到 Rust 的指南已经发布，重点比较了错误处理、托管运行时和包管理方面的差异，引发了关于两种语言取舍的社区辩论。 这很重要，因为 Go 与 Rust 的选择影响许多构建后端系统的开发者；理解这些取舍有助于团队就性能、安全性和生产率的语言选择做出明智决策。 该指南指出 Go 冗长的错误处理与 Rust 的'?'运算符对比，并强调 Rust 缺乏托管运行时（无垃圾回收）对延迟敏感的应用程序是有利的，但也增加了内存管理的复杂性。

hackernews · jabits · 5月24日 18:31 · [社区讨论](https://news.ycombinator.com/item?id=48259808)

**背景**: Go 和 Rust 是两种现代系统编程语言。Go 具有托管运行时，包含 goroutine 和垃圾回收，使得编写并发代码变得简单，但存在潜在的 GC 暂停。Rust 使用所有权和借用模型来保证内存安全而无需垃圾回收器，提供了对性能的控制，但学习曲线更陡峭。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://go.dev/doc/gc-guide">A Guide to the Go Garbage Collector</a></li>
<li><a href="https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html">Understanding Ownership - The Rust Programming Language</a></li>

</ul>
</details>

**社区讨论**: 社区评论态度不一：Animats 指出 Go 更适合 Web 后端，tptacek 认为核心选择在于是否使用托管运行时，amusingimpala75 抱怨 Rust 的包管理不如 Go 的全面标准库，nemo1618 指出指南措辞中有 AI 写作的痕迹。

**标签**: `#Rust`, `#Go`, `#programming languages`, `#migration`, `#systems programming`

---

<a id="item-11"></a>
## [掌握 Dyalog APL：交互式 Jupyter Notebook 入门教程](https://mastering.dyalog.com/README.html) ⭐️ 7.0/10

新的交互式 Jupyter Notebook 资源“Mastering Dyalog APL”已发布，通过动手示例提供对 APL 编程语言的全面介绍。 该资源结合了 Jupyter 的交互性与 APL 简洁的符号语法，降低了学习这门在 2025 年重新受到关注的强大数组导向语言的门槛。 原版印刷书《Mastering Dyalog APL》已改编为交互式笔记本格式，托管在 mastering.dyalog.com 上；Dyalog APL 本身是专有实现，但允许个人免费使用，符合 ISO/IEC 13751 标准。

hackernews · tosh · 5月24日 11:42 · [社区讨论](https://news.ycombinator.com/item?id=48256475)

**背景**: APL 是肯尼斯·E·艾弗森在 1960 年代开发的编程语言，以其特殊符号和以多维数组为核心数据类型而闻名，能够编写非常简洁的代码。Dyalog APL 是最广泛使用的现代实现，已有 40 多年优化历史，可在 Windows、macOS 和 Linux 上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/APL_(programming_language)">APL (programming language) - Wikipedia</a></li>
<li><a href="https://aplwiki.com/wiki/Dyalog_APL">Dyalog APL - APL Wiki TryAPL Introduction — Learning APL - GitHub Pages Why Are More Engineers Discovering Dyalog APL in 2025? GitHub - Dyalog/APLCourse: Dyalog APL self-study course</a></li>

</ul>
</details>

**社区讨论**: 评论中表达了对交互格式的赞赏，认为它有助于建立对 APL 符号的肌肉记忆，但有些人批评 Dyalog 的专有企业许可对这样一种小众语言限制过多。其他人分享了“Learn APL”等替代资源以及将 APL 翻译为 NumPy 的个人项目。

**标签**: `#APL`, `#programming languages`, `#array programming`, `#Jupyter`, `#tutorial`

---

<a id="item-12"></a>
## [Greg Brockman 访谈揭示 OpenAI 历史内幕](https://fs.blog/knowledge-project-podcast/greg-brockman/) ⭐️ 7.0/10

The Knowledge Project 播客发布了对 OpenAI 联合创始人 Greg Brockman 的深度访谈，涉及 OpenAI 的起源、内部冲突以及与 Elon Musk 的诉讼。 该访谈提供了对 OpenAI 动荡历史的罕见第一手见解，包括董事会解雇 Sam Altman 的决定以及随后与 Musk 的法律战，这些事件持续影响着 AI 领域的格局。 作为 Musk 诉讼的一部分，Brockman 的个人日记被公开，其中包含一条关于达到 10 亿美元的笔记。Musk 的诉讼因提交过晚而被驳回。采访可能忽略了 Ilya Sutskever 在 Altman 被解雇一事上改变立场的关键时刻。

hackernews · prakashqwerty · 5月24日 08:29 · [社区讨论](https://news.ycombinator.com/item?id=48255593)

**背景**: Greg Brockman 是 OpenAI 的联合创始人兼前总裁，OpenAI 是 ChatGPT 背后的领先 AI 研究机构。该公司在 2023 年 11 月经历了一场高度关注的内部危机，CEO Sam Altman 被短暂解雇后又复职。另外，早期联合创始人 Elon Musk（已离开 OpenAI）提起了一项违约诉讼，该诉讼后来被驳回。

**社区讨论**: 评论显示出不同的反应：一些人认为企业报道乏味，将其比作科技真人秀。其他人要求更深入地探讨关键事件，如 Ilya Sutskever 的立场转变。有评论者指出 Brockman 日记中关于个人财富的记载，质疑其动机。

**标签**: `#OpenAI`, `#Greg Brockman`, `#AI`, `#interview`, `#tech history`

---

<a id="item-13"></a>
## [Claude 从 Usborne PDF 重现 1983 年游戏《Mad House》](https://simonwillison.net/2026/May/24/usborne-mad-house/#atom-everything) ⭐️ 6.0/10

Simon Willison 使用 Claude AI 将 1983 年 Usborne 书籍《Creepy Computer Games》的扫描 PDF 转换成了可玩的 JavaScript 版《Mad House》游戏。生成的交互式构件在浏览器中运行，具有复古风格并适配移动设备。 这一示范展示了 AI 如何从印刷书籍中复活老旧软件，无需手动转录即可让现代受众访问历史代码。它凸显了大语言模型在教育和复古计算保存方面的潜力。 Willison 向 Claude 提供了精确提示，要求构建与原始游戏匹配的纯 JavaScript 构件，包括移动端适配和复古样式。最终页面注明了原书信息并链接到 Usborne 的免费 PDF 合集。

rss · Simon Willison · 5月24日 17:14

**背景**: Claude 是 Anthropic 开发的一系列大语言模型，能够生成称为“artifacts（构件）”的交互式应用程序，这些构件可直接在浏览器中运行。英国出版商 Usborne 免费发布了其 1980 年代计算机书籍的 PDF，其中包括《Creepy Computer Games》，该书收录了供 Commodore 64 等家用计算机输入的程序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_AI">Claude AI</a></li>
<li><a href="https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them">What are artifacts and how do I use them? | Claude Help Center</a></li>

</ul>
</details>

**标签**: `#retro computing`, `#AI`, `#JavaScript`, `#game recreation`

---