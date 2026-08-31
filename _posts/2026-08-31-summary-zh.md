---
layout: default
title: "Horizon Summary: 2026-08-31 (ZH)"
date: 2026-08-31
lang: zh
---

> 从 11 条内容中筛选出 5 条重要资讯。

---

1. [内核.org 维护者关于 Anubis 的文章引发反爬虫争论](#item-1) ⭐️ 8.0/10
2. [西蒙·威利森拆解 ChatGPT Work：云端与桌面双产品](#item-2) ⭐️ 8.0/10
3. [腾讯发布 Hy4 预览版：超大规模开源权重 LLM](#item-3) ⭐️ 8.0/10
4. [精心遣词：写作与编程中的用词之道](#item-4) ⭐️ 6.0/10
5. [Haiku R1/beta6 发布：BeOS 风格开源操作系统继续前进](#item-5) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [内核.org 维护者关于 Anubis 的文章引发反爬虫争论](https://people.kernel.org/monsieuricon/creepy-crawlies) ⭐️ 8.0/10

一位 kernel.org 维护者发表了一篇题为《Creepy Crawlies》的文章，讨论与网络爬虫的持续斗争以及 Anubis 工作量证明系统，该文在 Lobsters 上吸引了 514 条评论。文章及讨论揭示了 Anubis 的实际使用体验，包括某些难度设置会让移动设备上的网站无法使用。 这一讨论之所以重要，是因为它揭示了反爬虫策略的核心权衡：工作量证明挑战或许能阻止部分爬虫，但往往会惩罚使用低性能设备的真实用户，而高性能爬虫反而更容易解决这些挑战。随着 AI 公司越来越多地抓取公开网站，寻找公平且有效的反爬虫方案已成为小型互联网基础设施领域的紧迫问题。 Anubis 是一个开源工作量证明系统，由 Xe Iaso 创建，最初是为了应对亚马逊爬虫无视 robots.txt 导致 Git 服务器过载的问题。其默认难度要求 SHA-256 哈希有 5 个前导零，但有评论者报告更高难度（如难度 6）在手机上可能需要约 180 秒，导致网站无法使用；评论中还提到了如 iocaine 这类应用层陷阱等替代方案。

hackernews · zdw · 8月29日 17:49 · [社区讨论](https://news.ycombinator.com/item?id=49491791)

**背景**: 网络爬虫会自动抓取网页，网站所有者传统上使用 robots.txt 来请求限制访问，但许多机器人会忽略该协议。诸如 Anubis 之类的工作量证明系统要求客户端在访问网站前先解决一个计算难题，目的是证明其是真实浏览器而非自动化机器人。Anubis 主要被 Git 托管服务和自由/开源软件项目采用，以保护上游资源免受 AI 公司爬虫机器人的冲击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anubis_(software)">Anubis (software) - Wikipedia</a></li>
<li><a href="https://github.com/TecharoHQ/anubis">Anubis - GitHub</a></li>
<li><a href="https://anubis.techaro.lol/docs/design/how-anubis-works/">How Anubis works | Anubis</a></li>

</ul>
</details>

**社区讨论**: 讨论对 Anubis 的批评居多，tptacek 等评论者指出，Tavis Ormandy 一年前就预言过工作量证明会更有利于爬虫而非普通用户；有评论者发现较高难度下移动用户实际上会被拒之门外。其他人则分享了替代方案，比如利用 LLM 构建蜜罐陷阱或为爬虫设置无限黑洞路径，这表明有人更倾向于服务端欺骗而非计算挑战。

**标签**: `#web scraping`, `#anti-bot`, `#proof-of-work`, `#infrastructure`, `#security`

---

<a id="item-2"></a>
## [西蒙·威利森拆解 ChatGPT Work：云端与桌面双产品](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) ⭐️ 8.0/10

西蒙·威利森发布了一篇关于 OpenAI ChatGPT Work 的详细分析，揭示它实际上由两个产品组成：Work Cloud（网页/移动端）和 Work Local（前身为 Codex 的桌面应用）。他确定了模型选择、带互联网访问的代码执行、无头 Chrome 浏览器和持久化共享文件系统是 Work 独有的功能。 ChatGPT Work 是 OpenAI 面向企业的一款功能强大但令人困惑的产品，这一分析帮助用户理解何时使用 Chat、何时使用 Work。它同时指出了来自 Anthropic Claude Cowork 的安全风险和竞争压力，对开发者与企业用户都很重要。 Work 仅对每月 20 美元及以上的订阅者开放，而 Chat 中每月 20 美元用户最高只能使用“High”推理级别，“Extra High”和“Pro”仅限每月 100 美元档位。在 Work 中，用户可以选择 GPT-5.6 Sol、Luna 或 Terra，推理级别从 Light 到 Ultra，其中 Ultra 会更积极地把任务委派给子代理。

rss · Simon Willison · 8月30日 23:59 · [社区讨论](https://news.ycombinator.com/item?id=49504625)

**背景**: OpenAI Codex 是 OpenAI 的 AI 编码代理套件；其中 Codex CLI 于 2025 年 4 月 16 日发布，在本地终端中运行，将 OpenAI 的语言模型与本地代码和命令行任务连接起来。ChatGPT Work 的桌面组件就是重新品牌化的 Codex，经过重新包装以降低对非开发者的门槛，而 Work Cloud 则在 OpenAI 的基础设施上运行同类代理能力。理解这一传承有助于解释为什么 Work 继承了代码执行和模型选择等功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://openai.com/codex/">Codex in ChatGPT | AI Coding Agents for Software Engineering | ...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，ChatGPT Work 似乎是对 Anthropic Claude Cowork 的回应——后者在企业领域迅速崛起，甚至被微软授权并贴牌为 Copilot Cowork。一位评论者警告存在“致命三合一”风险：私有数据、不受信任的内容和向外泄露信息的通道组合在一起，建议建立更强的隐私边界；也有人称赞计算机操作功能非常实用，并怀疑 Work 基本上只是 Codex 换了层皮。

**标签**: `#ChatGPT`, `#OpenAI`, `#AI agents`, `#enterprise software`, `#security`

---

<a id="item-3"></a>
## [腾讯发布 Hy4 预览版：超大规模开源权重 LLM](https://simonwillison.net/2026/Aug/29/hy4/) ⭐️ 8.0/10

腾讯发布了 Hy4 预览版，这是一个纯文本（无视觉）的开源权重 LLM，总参数 770B，激活参数 49B，上下文窗口达 1M token。模型已在 Hugging Face 上提供，检查点大小为 1.56TB。 Hy4 预览版相比腾讯之前的 Hy3 模型规模大幅提升，表明中国 AI 实验室继续将开源权重模型推向更大规模和更长上下文。此次发布让研究人员和开发者能够在没有专有限制的情况下使用前沿规模的模型，其规模可与领先的闭源模型相媲美。 模型的 chat template 显示有两种推理努力级别：'high'（默认）和'no_think'。在测试提示中，模型的隐藏推理痕迹使用了截断式英语，表明内部推理不注重语法，以节省 token。

rss · Simon Willison · 8月29日 23:53

**背景**: 混合专家（MoE）架构将神经网络划分为多个专家子网络，每个 token 只激活其中一部分，从而在总参数量很大的情况下保持较低的计算成本。'总参数'指模型的完整大小，而'激活参数'是推理时实际使用的参数。Hugging Face 上使用 Jinja2 格式的 chat template 是标准做法，用于定义对话轮次如何格式化，并可包含推理难度设置等逻辑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts">A Visual Guide to Mixture of Experts (MoE)</a></li>
<li><a href="https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/">Applying Mixture of Experts in LLM Architectures | NVIDIA Technical Blog</a></li>
<li><a href="https://huggingface.co/blog/FriendliAI/custom-chat-template">Customizing Chat Templates in LLMs</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Tencent`, `#open weights`, `#Hugging Face`, `#AI`

---

<a id="item-4"></a>
## [精心遣词：写作与编程中的用词之道](https://unsung.aresluna.org/i-just-chose-words-carefully/) ⭐️ 6.0/10

一篇题为《我只是仔细选择了措辞》的文章主张，刻意选择用词能塑造写作的清晰度与节奏。这篇文章引发了热烈的评论讨论，人们将其与编程、排版和 UI 设计联系起来。 这篇文章能引起技术写作者和开发者的共鸣，因为用词选择既是写作技艺的核心，也关乎代码的可读性。它凸显出微小的语言决策可能对用户体验和可维护性产生重大影响。 文章的标题呼应了作者明确选择词语的决定，并通过散文和代码中的例子来探讨这一主题。评论中提到了排版概念如孤行（widows）、《超级银河战士》攻略里'missles'的拼写，以及固定宽度工具提示和德语本地化等 UI 约束。

hackernews · zdw · 8月30日 22:49 · [社区讨论](https://news.ycombinator.com/item?id=49503601)

**背景**: 这篇文章延续了将语言精确性视为一种技艺的写作传统。在编程中，选择长度相等的词语对（如 old/new、head/tail）可以改善视觉对齐和可读性。排版中的孤行（widow）概念也反映出精心的版面决策如何影响阅读体验。

**社区讨论**: 评论者热情地分享了相关轶事：吉莲·安德森采访中提到的克里斯·卡特对剧本排版的执念、编程中词语对的排列技巧、《超级银河战士》攻略中有意保留的拼写错误，以及 UI 文案适应宽度限制的难题。整体氛围是赞赏的，读者们补充了各自领域中的技艺实例。

**标签**: `#writing`, `#craft`, `#programming`, `#language`, `#essay`

---

<a id="item-5"></a>
## [Haiku R1/beta6 发布：BeOS 风格开源操作系统继续前进](https://www.haiku-os.org/news/2026-08-26_haiku_r1_beta6) ⭐️ 6.0/10

Haiku R1/beta6 于 2026 年 8 月 26 日发布，这是这款灵感来自 BeOS 的开源操作系统的最新测试版。此次发布为社区提供了一个可测试的新版本，是该计划持续推进 R1 稳定版过程中的一步。 Haiku 是 BeOS 为数不多的社区驱动延续项目之一，吸引了重视速度、简洁和经典桌面美学的爱好者。每一次 beta 发布对其小众社区和更广泛的开源生态都有意义，尽管对主流用户的影响仍然有限。 与之前的测试版一样，Haiku R1/beta6 尚未被视为可正式用于生产环境。早期用户报告提到某些硬件上出现启动回归问题，不过安全模式选项可以帮助绕过问题；另外，部分潜在用户仍然担心辅助功能支持不足。

hackernews · metrofun · 8月30日 16:01 · [社区讨论](https://news.ycombinator.com/item?id=49499867)

**背景**: Haiku 最初名为 OpenBeOS，是一款免费开源操作系统，始于 2001 年，是 BeOS 的社区驱动延续；BeOS 在 2001 年 Palm 收购 Be Inc. 后停止开发。Haiku 旨在与 BeOS 保持二进制兼容，同时支持现代硬件、协议和网络标准。该项目目前仍处于 beta 阶段，目标是以 BeOS 为灵感，打造快速、易学且强大的个人计算操作系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Haiku_(operating_system)">Haiku (operating system) - Wikipedia</a></li>
<li><a href="https://www.haiku-os.org/">Home | Haiku Project</a></li>
<li><a href="https://en.wikipedia.org/wiki/BeOS">BeOS</a></li>

</ul>
</details>

**社区讨论**: 社区评论中既有兴奋也有谨慎。一些用户称赞 Haiku 的视觉设计和哲学，认为它是充满遥测、注册和通知的现代操作系统之外的一个另类选择；也有用户报告了回归问题，例如某些笔记本上出现启动卡死。还有人希望它能在音乐制作场景中发挥作用，并呼吁在系统广泛可用之前改进辅助功能。

**标签**: `#Haiku`, `#operating system`, `#open source`, `#release`

---