---
layout: default
title: "Horizon Summary: 2026-11-26 (ZH)"
date: 2026-11-26
lang: zh
---

> 从 18 条内容中筛选出 12 条重要资讯。

---

1. [Scott Aaronson 惊叹：矩阵乘法指数或被证明恰为 9/4](#item-1) ⭐️ 9.0/10
2. [1Password 披露恶意代码被推送到后端服务的安全事件](#item-2) ⭐️ 8.0/10
3. [Anthropic 的 GRH Lean 形式化从 1700 万行压缩至 7.6 万行](#item-3) ⭐️ 8.0/10
4. [Google Research 发布“Cogentic”论文，涉及整数分解与离散对数](#item-4) ⭐️ 8.0/10
5. [开发者用 Lean 审计 Clojure 核心库，发现未报告的缺陷](#item-5) ⭐️ 8.0/10
6. [GPT-6.2 Astra 自主破解 1808 年耶鲁匿名素描本的作者之谜](#item-6) ⭐️ 8.0/10
7. [《纽约时报》建议摄影师不要更新 Photoshop，理由是 AI 功能](#item-7) ⭐️ 7.0/10
8. [Ubuntu 安全补丁响应缓慢，用户转向 Debian](#item-8) ⭐️ 7.0/10
9. [博客通过延迟特征分析断言神秘模型「Jev」实为 Qwen3.5-35B-A3B](#item-9) ⭐️ 7.0/10
10. [多项式 Hirsch 猜想被证伪：简单多面体图直径呈超多项式](#item-10) ⭐️ 7.0/10
11. [开发者逆向 Windows 响度均衡并移植到 PipeWire](#item-11) ⭐️ 7.0/10
12. [Simon Willison 梳理十二个月内 LLM 的三个拐点](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Scott Aaronson 惊叹：矩阵乘法指数或被证明恰为 9/4](https://scottaaronson.blog/?p=10379) ⭐️ 9.0/10

Scott Aaronson 发表了一篇极为简短却广为流传的博文，对一篇新论文表示震惊：据称这是一篇 OpenAI 的预印本，其主要定理声称在任意域 F 上，方阵乘法的指数恰为 ω = 9/4，也就是 2.25。博文同时链接了该论文在 Hacker News 上的讨论帖，二者迅速成为近期讨论热度最高的数学话题之一。 如果这一结果经得起检验，它既会给出更快的矩阵乘法算法，又会给出与之匹配的下界，从而解决自 1969 年 Strassen 突破以来悬而未决的问题，并推翻长期流行的 ω = 2 猜想。由于矩阵乘法是线性代数、图算法、机器学习核心算子以及大量科学计算的基础，一个精确的指数值将同时重塑理论与实践；而围绕它的讨论也显示，AI 辅助数学可能正在进入一个新阶段。 所声称的精确值 9/4 将优于数十年来逐步改进后约 2.37 的已知最好上界；而“等于”这一断言远比常见的“至多为 9/4”类结果强得多，因此独立验证——最好是借助 Lean 等证明助手完成形式化——才是关键问题。Aaronson 的博文刻意写得十分简短，他还提到从多个可靠信源听说 AI 实验室手上还压着若干尚未公布的结果，这些在正式发表前都应视为传闻。

hackernews · Kotlopou · 11月25日 19:11 · [社区讨论](https://news.ycombinator.com/item?id=50646108)

**背景**: 矩阵乘法指数 ω 指的是：使得两个 n×n 矩阵能在 O(n^ω) 时间内相乘的最小指数。朴素算法给出 ω = 3，Strassen 在 1969 年的方法将其降到 2.81 以下，此后数十年的研究把已知最好上界推进到约 2.37，而许多研究者猜想真实值就是 2。Lean 是一个基于依赖类型论的开源证明助手，其社区数学库 MathLib 致力于形式化大量本科乃至前沿研究级别的数学内容，这也正是评论者追问“真正的推手究竟是机器可检验的证明加上海量算力，还是大语言模型本身”的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://lean-lang.org/">Lean Programming Language</a></li>

</ul>
</details>

**社区讨论**: 评论者们借用历史类比，把这一刻比作第谷·布拉赫建立的那种使开普勒定律成为可能的“计算中心”，并猜测一场即将到来的“数学末日（Mathocalypse）”会像量子力学把经典物理挤到一角那样重组整个学科。也有人追问：如果“只有”Lean、MathLib 和算力而没有大语言模型，这一切还会发生多少；他们怀疑这类成果是否会像零日漏洞一样被囤积以获取竞争或商业优势，并对“若重大未解问题都被机器攻克，人类还剩下什么挑战”表达了相当复杂的心情。

**标签**: `#mathematics`, `#matrix-multiplication`, `#AI-for-math`, `#Lean-proof-assistant`, `#research-breakthrough`

---

<a id="item-2"></a>
## [1Password 披露恶意代码被推送到后端服务的安全事件](https://1password.com/blog/update-on-nov-2026-security-incident) ⭐️ 8.0/10

1Password 在其博客上发布了关于 2026 年 11 月安全事件的更新，确认有恶意代码被推送到其后端服务，并列出了一系列补救措施。但公告并未说明究竟是哪一道代码部署防护措施失效，因此外界对代码究竟如何进入生产环境提出了强烈质疑。 1Password 是使用最广泛的密码管理器之一，因此任何触及其后端生产环境的事件都会直接影响所有依赖其云同步保险库的用户的信任基础。此案也揭示了 SaaS 公司最主要的被攻击模式：一旦攻击者能够向部署流水线推送代码，他们就等于继承了厂商对所有用户的访问能力。 评论者指出，公告中的补救措施完全没有说明主分支的分支保护规则究竟是缺失还是可以被绕过，从而无法解释“推送至主分支”是如何发生的。讨论还强调，加密保险库的设计限制了最坏情况，但恶意的客户端构建仍可能在本地解密后窃取明文密钥，而且用户希望官方明确声明加密保险库并未被下载。

hackernews · lxhrstn · 11月25日 17:18 · [社区讨论](https://news.ycombinator.com/item?id=50644817)

**背景**: 1Password 是一款订阅制密码管理器，它把加密后的保险库保存在云端并在多设备间同步，客户端应用则通过 Secret Key 与用户主密码结合的方式在本地解密数据。由于应用和后端都以服务形式交付，能够向构建与部署流水线注入代码的攻击者就处在一个可以同时触达所有用户的位置——这类风险被称为软件供应链攻击。常见的防护手段包括生产分支上的分支保护与强制代码评审、借助 SLSA 框架和 Sigstore 等实现带来源证明的构建签名，以及用软件物料清单（SBOM）追踪组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://slsa.dev/">SLSA • Supply-chain Levels for Software Artifacts</a></li>
<li><a href="https://www.sigstore.dev/">Home · Sigstore</a></li>

</ul>
</details>

**社区讨论**: 安全从业者 tptacek 称这是 SaaS 公司最重要的单一攻击向量，并指出随着员工数量增长，某台笔记本电脑被攻陷的概率趋近于一，而 1Password 的加密保险库设计在一定程度上缓解了本次事件的最坏后果。其他评论者批评公告没有说明分支保护是否缺失、推送至主分支为何可行，也有人质疑 Passkey 的安全性可能弱于“密码加第二因素”，并要求官方明确确认加密保险库从未被下载。

**标签**: `#security`, `#1Password`, `#supply-chain`, `#SaaS`, `#incident-response`

---

<a id="item-3"></a>
## [Anthropic 的 GRH Lean 形式化从 1700 万行压缩至 7.6 万行](https://github.com/lsernau/grh-lean) ⭐️ 8.0/10

新仓库 lsernau/grh-lean 发布了一个大幅精简、可读性更强的 Lean 版本，针对 Anthropic 围绕广义黎曼猜想（GRH）的形式化工作，把约 1700 万行压缩到约 7.6 万行，缩减幅度约 99.56%。该重写版本还把“已知数学”与“新数学”明确分开，并补充了大量人类可读的文档，使这份成果更容易审查和理解。 机器生成的大规模形式化证明只有在人类能够阅读、核查并从中学习时才有价值，因此超过 99% 的规模压缩加上文档化，直接回应了人们对 AI 生成形式化的主要质疑。如果 LLM 辅助的“证明压缩（proof golfing）”能够稳定地把庞大开发压缩成可维护的版本，它可能成为 AI 数学产出以及人类编写的基础库的标准后处理步骤。 该重写版本清晰地区分了已有结果与真正的新内容，而这正是形式化成果可被审查的关键；Hacker News 的讨论还指向 Lean Zulip 上的帖子以作更深入的技术跟进。行数统计会随统计口径不同而变化——有评论者称这份可读证明约有 30 万行代码，意味着 7.6 万行可能只覆盖了完整依赖栈的一部分。

hackernews · nb-t · 11月25日 21:48 · [社区讨论](https://news.ycombinator.com/item?id=50648050)

**背景**: Lean 是一个开源证明助手兼函数式编程语言，定理以代码形式书写，每一步都由机器检查，因此形式化成果是可被机器验证的证明，而非纸面论证。广义黎曼猜想把黎曼猜想从经典的 zeta 函数推广到 Dirichlet L 函数及其他全局 L 函数；在数域情形下它仍未被证明，是解析数论的核心未解问题之一。由于形式化证明必须写出每一步推理，对深刻结果的朴素形式化很容易膨胀到数百万行——而被称为“proof golf（证明压缩）”的做法，就是把这类证明重写得更短、更整洁。在此次发布的一个月前，陶哲轩（Terence Tao）提出，缺乏洞见的巨型形式化对数学是个问题，而这份精简版本正是被放在这一批评的尺度下衡量的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis">Generalized Riemann hypothesis</a></li>
<li><a href="https://github.com/cameronfreer/lean4-skills/blob/main/plugins/lean4/skills/lean4/references/proof-golfing-patterns.md">lean4-skills/plugins/lean4/skills/lean4/references/proof ...</a></li>

</ul>
</details>

**社区讨论**: 评论区总体态度积极，赞赏明确区分已知数学与新数学、以及随处可读的文档，认为这对消化这份工作帮助很大。核心争论在于：可读的、经过压缩的证明是否能回应陶哲轩关于巨型证明缺乏洞见的批评；以及是否有实验室让内部模型去简化人类编写的基础 Lean 证明。有评论者贴出了 Lean Zulip 上的相关讨论以供深入了解。

**标签**: `#lean`, `#formal-verification`, `#mathematics`, `#riemann-hypothesis`, `#ai-for-math`

---

<a id="item-4"></a>
## [Google Research 发布“Cogentic”论文，涉及整数分解与离散对数](https://github.com/google-research/google-research/tree/master/cogentic_research_papers) ⭐️ 8.0/10

Google Research 上线了一个名为 cogentic_research_papers 的新仓库，其中的论文涉及整数分解、离散对数以及其他若干开放数学问题，并且据称是由一个名为 Cogentic 的系统产出的。按照与此次发布一同流传的介绍，Cogentic 是一个多智能体编排框架，它把现有的 LLM 分别安排为证明提出者、对抗性验证者、策略统筹者、文献综述者和论文撰写者，并围绕一个共享的中间证明数据库协同工作。 整数分解与离散对数问题正是 RSA、Diffie-Hellman 和椭圆曲线密码学的安全基础，因此这方面任何可信的进展都会直接牵动现实安全，而不只是学术上的趣闻。这次发布还强化了一种更大的叙事：AI 系统正开始对真正的数学发现作出贡献，而这会影响人们对数学与计算机科学领域的研究方式、经费投入和职业前景的预期。 这条提交只是一个 GitHub 目录，里面是若干 PDF 论文，既没有摘要，也没有说明各项声称结果的实际适用范围——例如它们是否削弱了标准密码参数的强度——这些结论尚未经过独立验证。所描述的架构与其说是一种新的定理证明模型，不如说是一层包裹在现有 LLM 之外的编排系统，其中内置了验证和对抗性检查机制以筛除错误的证明。

hackernews · rgwohlbold · 11月25日 13:33 · [社区讨论](https://news.ycombinator.com/item?id=50642086)

**背景**: 整数分解是指找出若干素数使其乘积等于给定整数的过程，RSA 加密正是建立在“对大合数做分解不可行”这一假设之上。离散对数问题则是在有限域或椭圆曲线群中由 g^x 反推出指数 x，它是 Diffie-Hellman 密钥交换以及许多签名方案背后的同类困难性假设。这两类问题被认为对经典计算机而言是困难的，而一旦出现能在实际密钥规模上高效求解的算法，广泛部署的公钥密码体系将被攻破。Cogentic 属于“AI 用于数学”这一波尝试，即把大语言模型与搜索、验证以及多智能体工作流结合起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50642086">Google releases Cogentic papers on integer... | Hacker News</a></li>
<li><a href="https://www.linkedin.com/posts/aranyak-mehta-13098b4a_these-are-exciting-times-for-ai-math-and-activity-7513102901817393153-npTr">Google Researchers Introduce Cogentic Multi-Agent... | LinkedIn</a></li>
<li><a href="https://en.wikipedia.org/wiki/Integer_factorization">Integer factorization - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Discrete_logarithm">Discrete logarithm - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论区整体相当兴奋：有人援引可信人士的传言，称这只是“更大成果的冰山一角”；也有人用 AlphaGo 到 AlphaGo Zero 的类比，认为 AI 在巨大搜索空间中的探索会持续产出数学成果。不少人讨论了突破频出与 AI 股市下滑之间的反差，还有人表示自己原本以为数学不会被“砸钱”解决。还有一种反复出现的看法是：现在正是进入计算机科学领域的好时机，而不是应当避开它。

**标签**: `#cryptography`, `#AI-for-math`, `#google-research`, `#integer-factorization`, `#research-papers`

---

<a id="item-5"></a>
## [开发者用 Lean 审计 Clojure 核心库，发现未报告的缺陷](https://s.conao3.com/blog/2026/e4f733) ⭐️ 8.0/10

一位开发者使用 Lean 证明助手对 Clojure 核心库进行了形式化检查，并称发现了此前未被报告的缺陷，相关结果发布在一篇博客文章中，并在 Hacker News 上获得 8.0/10 的评分。该帖引发了 65 条评论的讨论，涉及验证工具、疑似误报以及 Lean 与 Rocq 的对比。 Clojure 支撑着 Nubank（该公司收购了 Cognitect）等企业的生产系统，因此 `get`、`.indexOf` 这类基础函数中的缺陷可能影响庞大的工业用户群。这一实验还表明，轻量级形式化方法与证明助手正从学术数学领域走向对主流语言运行时的日常审计。 评论者对部分缺陷清单提出了反驳：rvprasad 指出 `(.indexOf (seq (byte-array [1 2 3])) 2)` 之所以失败，只是因为参数是 Long 而非 byte；而 `(get "abc" 1.9)` 反映的是 `get` 对字符串键会做整数强制转换这一既定语义，因此简单的类型检查本可把第一种情况识别为误用。这说明审计的原始结果中既有真实发现也夹杂噪声，如何区分二者是当前的主要问题。

hackernews · encyclopedism · 11月25日 14:56 · [社区讨论](https://news.ycombinator.com/item?id=50642939)

**背景**: Lean 是一个开源证明助手兼函数式编程语言，基于依赖类型论，最初由微软研究院的 Leonardo de Moura 于 2013 年发起，目前由非营利组织 Lean FRO 支持。Lean、Rocq（原 Coq）这类证明助手允许用户陈述数学或程序性质，并由机器机械地检验证明，因此适合用来验证代码是否符合规范。Clojure 是运行在 JVM 上的 Lisp 方言，其 `clojure.core` 库提供了大多数程序赖以构建的基础函数和数据结构，因此其中哪怕很小的不一致也会产生广泛影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant)</a></li>
<li><a href="https://lean-lang.org/">Lean Programming Language</a></li>
<li><a href="https://clojuredocs.org/core-library">Clojure 's Core Library | ClojureDocs - Community-Powered Clojure ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论技术性强但意见分歧：rvprasad 认为若干被报告的缺陷其实是由错误用法或既定强制转换导致的误报，并建议作者减少噪声；networked 则追问 Lean 是否正在取代 Rocq 用于程序验证，以及语言模型是否只是更擅长写 Lean。还有人通过 Nubank 和 Cognitect 强调 Clojure 的工业分量，yababa_y 则贴出了一项针对 Common Lisp 编译器（SBCL、Clozure、ACL2）的类似审计，其中发现了数十个问题。

**标签**: `#Clojure`, `#Lean`, `#formal verification`, `#programming languages`, `#bug hunting`

---

<a id="item-6"></a>
## [GPT-6.2 Astra 自主破解 1808 年耶鲁匿名素描本的作者之谜](https://simonwillison.net/2026/Nov/24/astra-historical-mystery/) ⭐️ 8.0/10

历史学教授 Mark Humphries 报告称，GPT-6.2 Astra 在仅有极少提示的情况下，仅用 22 分钟便自主确认了耶鲁大学拜内克图书馆藏一本 1808 年匿名素描本的作者身份，所用材料均为公开的一手与二手文献。在此过程中，该模型还发现了一份鲜为人知的档案材料——沙博子爵（vicomte de Chabot）的旅行日记，该日记只能向克利夫兰州立大学订购获取，而模型准确预测查阅该日记将验证其假设，结果确实如此。 这是一个极具冲击力的具体案例，说明 AI 智能体能够从事真正的档案研究，而不只是在基准测试中刷分，也表明智能体式大模型已经可以产出被历史学家认为有价值的发现。它还引出一个问题：当一个学科面对能做人类历史学家做不到之事的系统时应当如何回应——Humphries 将这一时刻比作国际象棋和数学界曾经经历的冲击。 Astra 的推理链条始于一条日记记载：沙博子爵的到访日期比素描本中提到的附近某条河流的日期早五天，据此它提出沙博的旅行日记可以确认作者身份。该结果只是一个单一轶事性案例，并非经过同行评审或系统性评测的成果；Humphries 认为，历史学即将面临的冲击会比数学界温和，因为历史学家是在不断重新阐释过去，而不是追求唯一的普遍真理。

rss · Simon Willison · 11月24日 16:53

**背景**: GPT-6.2 Astra 属于 OpenAI 的 GPT-6.2 大语言模型系列，于 2026 年 11 月 17 日与 GPT-6.2 Sol 一同发布，仅向付费用户开放；早期重度用户的评价褒贬不一，批评其错误频繁、相较前代提升有限。Astra 被定位为可处理文本与图像、胜任多步骤任务的推理模型，这正是长时间自主研究得以可行的原因。拜内克图书馆是耶鲁大学的珍本与手稿馆藏机构，涉事素描本已在耶鲁在线馆藏中完成数字化。Simon Willison 使用的“Deep Blue”标签指 1997 年 IBM 国际象棋计算机击败卡斯帕罗夫一事，用作 AI 在被视为人类强项的任务上实现超越的代称。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-6.2_Astra">GPT-6.2 Astra</a></li>
<li><a href="https://simonwillison.net/2026/Nov/17/gpt62-astra-and-sol/">GPT ‑ 6 . 2 Astra and GPT ‑ 6 . 2 Sol | Simon Willison’s Weblog</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#LLM applications`, `#historical research`, `#autonomous research`, `#GPT-6.2`

---

<a id="item-7"></a>
## [《纽约时报》建议摄影师不要更新 Photoshop，理由是 AI 功能](https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features) ⭐️ 7.0/10

据报道，《纽约时报》正在建议其摄影师不要更新 Adobe Photoshop，理由是该软件内置的生成式 AI 功能会给公开发布的图片带来可信度问题。这一消息出自一篇文章（通过 archive.ph 镜像传播），并迅速在 Hacker News 上引发讨论，获得 147 条评论。 这是一个值得注意的信号：一家权威的大型新闻机构把旗舰创意工具中主流的 AI 集成视为风险而非升级，这进一步强化了业界对生成式 AI 日益增长的职业性排斥。如果其他出版机构跟进，可能会对 Adobe 的产品决策形成压力，并加速新闻摄影工作流对“无 AI”替代方案的关注。 最实际的担忧在于标注环节：当文件带有来源凭证数据或被平台检测标记时，即便 AI 只被用于微调颜色、抠图或调整版式，观众和社交平台也可能把整张图片标记为“AI 生成”。Photoshop 的生成式填充由 Adobe Firefly 模型驱动，而 Adobe 的 Content Credentials 会在导出文件中嵌入签名的 C2PA 清单，这正是让此类标注得以实现的机制。

hackernews · rmason · 11月25日 21:18 · [社区讨论](https://news.ycombinator.com/item?id=50647673)

**背景**: Photoshop 已经内置了生成式填充（Generative Fill）等生成式 AI 功能，用户可以通过文本提示在图像中添加或移除内容。与此同时，Adobe 一直力推 Content Credentials，这是其对开放 C2PA 来源标准的实现，会在媒体文件中嵌入防篡改的元数据，说明作品是如何制作的，常被形容为“数字营养标签”。新闻摄影高度依赖“发布的图片未经操纵”这一前提，因此新闻编辑部正面临一个难题：在编辑工具默认嵌入 AI 与来源元数据的情况下，如何维持这种信任。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://metadatacleaner.app/blog/adobe-content-credentials-remove/">Adobe Content Credentials Explained — and... — Metadata Cleaner</a></li>
<li><a href="https://arstechnica.com/information-technology/2023/10/adobe-launches-new-symbol-to-tag-ai-generated-content-but-will-anyone-use-it/">Adobe launches new symbol to tag AI-generated content —but will...</a></li>
<li><a href="https://www.adobe.com/products/photoshop/generative-fill.html">Photoshop Generative Fill: Use AI to Fill in Images | Adobe</a></li>

</ul>
</details>

**社区讨论**: 评论者大多认同《纽约时报》的立场，认为公众对生成式 AI 的观感总体偏负面，任何与之关联的做法都会成为负担，这与 Tidal 近期在平台上封禁 AI 音乐的做法类似。一位从事创意工具行业的从业者表示，最大的问题是：完全由 AI 生成的图片与仅做轻度 AI 修图的图片，在导出后几乎无法区分，因此一旦在 Instagram 或 Facebook 上被打上“AI 生成内容”标签，对权威品牌的公信力就是致命打击；也有人建议只做小修改时可用 Krita，并认为在订阅疲劳的背景下，Affinity 等一次性买断的替代品迎来了机会。

**标签**: `#generative-ai`, `#adobe-photoshop`, `#content-authenticity`, `#creative-tools`, `#ai-ethics`

---

<a id="item-8"></a>
## [Ubuntu 安全补丁响应缓慢，用户转向 Debian](https://www.openwall.com/lists/oss-security/2026/11/25/9) ⭐️ 7.0/10

oss-security 邮件列表中一篇题为“Slow Ubuntu security response times”（Ubuntu 安全响应缓慢）的帖子引发了 Hacker News 上的讨论，多位运维人员反映 Ubuntu 针对已知 CVE 的修复发布太慢。一些评论者表示，由于这些延迟，他们已将生产服务器镜像从 Ubuntu 迁移到了 Debian。 Ubuntu 是服务器、云镜像和容器中部署最广泛的 Linux 发行版之一，因此 CVE 修复迟缓会直接扩大大量面向互联网的基础设施的暴露窗口。如果运维人员开始在通用虚拟机上默认选择 Debian，将削弱 Ubuntu 作为安全、有支持的企业级选择地位，并改变发行版格局。 评论者指出，在 Ubuntu 中安全修复有时会先出现在 -updates 仓库，数小时后才进入 -security 仓库，这破坏了仅依赖 security 源进行无人值守升级（unattended-upgrades）的工作流。也有人提醒，这一比较并不只是速度问题，因为 Debian 等发行版在回归测试上投入很大精力，但仍可能推送造成破坏的更新。

hackernews · gslin · 11月25日 20:38 · [社区讨论](https://news.ycombinator.com/item?id=50647181)

**背景**: CVE（通用漏洞披露）是公开登记的安全缺陷，每个 Linux 发行版都需要为自己发布的版本回移或打包修复程序。发行版将软件包分到 -security、-updates 等不同仓库，管理员可用 unattended-upgrades 等工具仅自动安装安全修复。Ubuntu 与 Debian 的发布模式不同——Ubuntu 每六个月发布新版本、每两年发布一次 LTS 长期支持版本，而 Debian 稳定版大约每两年更新一次——这决定了两者交付补丁的速度与保守程度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://operavps.com/blog/debian-vs-ubuntu/">11 Key Differences Between Debian and Ubuntu</a></li>
<li><a href="https://blog.temok.com/debian-vs-ubuntu/">Debian vs Ubuntu : Which Linux Distro Should You Choose?</a></li>

</ul>
</details>

**社区讨论**: 讨论整体对 Ubuntu 持批评态度：一位评论者称，对如此广泛使用的发行版而言补丁迟缓“完全不可接受”，并表示公司已将所有服务器镜像迁至 Debian；另一位则说自己第一次因补丁慢而犹豫，最终为通用虚拟机选择了 Debian。反方观点聚焦于权衡：有人引用 Debian 的缺陷报告说明 QA 不足也会导致回归问题，还有人引用稳定内核维护者的警告称，挑拣个别补丁比跟进完整的 stable/LTS 版本会让系统更不安全。

**标签**: `#Ubuntu`, `#Linux security`, `#distributions`, `#CVE patching`, `#Debian`

---

<a id="item-9"></a>
## [博客通过延迟特征分析断言神秘模型「Jev」实为 Qwen3.5-35B-A3B](https://modaic.dev/blog/latency-doesnt-lie) ⭐️ 7.0/10

Modaic 发布的一篇题为《Latency doesn't lie》（延迟不会说谎）的博客文章声称，未公开身份的模型「Jev」实际上是 Qwen3.5-35B-A3B，依据有两点：一是对模型响应行为的延迟（latency）特征进行剖析，二是通过提示词让模型自我指认为 Qwen。该说法在 Hacker News 上引发热议（216 分、60 条评论），但讨论整体对证据强度持质疑态度。 这一事件是 LLM 溯源与逆向工程的典型案例：随着越来越多产品隐藏在其未披露的模型接口之后，把某个模型追溯到具体上游基座的技术在实践和商业层面都变得重要。同时其结论存在争议而非已经确立，这也暴露出公开的模型归因证据往往相当薄弱。 批评者指出的核心弱点在于：据称仅凭延迟数据无法区分 Qwen 与 Gemma，而自我识别实验显然没有在对照模型上运行以作比较。评论者还指出，TypeSafe 官网明确表示 Jev「既不小，也不是 LLM」，而 Modaic 是 TypeSafe 的竞争对手，这一利益冲突使得结果更需要独立复现。

hackernews · csoham · 11月25日 22:57 · [社区讨论](https://news.ycombinator.com/item?id=50648823)

**背景**: LLM 指纹识别（fingerprinting）是一个试图判定某个不透明 API 背后究竟是哪个具体模型（或版本）的研究方向，常用手段是发送精心构造的查询，并分析响应内容或时间、token 输出节奏、网络流量等侧信道。由于服务方很少公开其推理栈，指纹本质上具有概率性且容易出错。而「自我识别」——直接问模型「你是谁做的」——是一种流行但出了名不可靠的捷径，因为模型经常幻觉出身份，或从训练数据与蒸馏过程中继承身份。Qwen3.5-35B-A3B 是阿里巴巴开源权重的推理型视觉语言模型，总参数 35B、每 token 约激活 3B，采用线性注意力与稀疏混合专家（MoE）的混合架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2407.15847">[2407.15847] LLMmap: Fingerprinting For Large Language Models LLMmap: Fingerprinting for Large Language Models - arXiv.org LLMs Have Rhythm: Fingerprinting Large Language Models Using ... LLM Fingerprinting Techniques - emergentmind.com RIPPLE: Attacking Backdoor-based LLM Fingerprinting via ... LLMmap: Fingerprinting for Large Language Models - usenix.org Fingerprinting LLMs via Prompt Injection - ACL Anthology</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.5-35b-a3b">Qwen 3 . 5 - 35 B - A 3 B - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://arxiv.org/pdf/2411.10683">Measuring and Understanding LLM Identity Confusion</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的反应总体偏向怀疑：评论者认为延迟数据无法把 Qwen 与 Gemma 区分开，自我识别实验缺少对照模型基线，而且「问模型自己是谁」自 ChatGPT 早期起就被公认极不可靠。还有人指出 TypeSafe 官网明确否认 Jev 是 LLM，且 Modaic 与 TypeSafe 存在竞争关系，因此在被独立复现之前不应认真对待这一结论。

**标签**: `#LLM fingerprinting`, `#model provenance`, `#Qwen`, `#latency analysis`, `#AI industry`

---

<a id="item-10"></a>
## [多项式 Hirsch 猜想被证伪：简单多面体图直径呈超多项式](https://github.com/openai/math/blob/main/preprints/Superpolynomial-graph-diameter-of-simple-polytopes-November-24-2026/paper.pdf) ⭐️ 7.0/10

一篇预印本通过构造图直径相对于面数呈超多项式的简单多面体，证伪了多项式 Hirsch 猜想。这意味着不存在具有多项式最坏情况时间保证的沿边单纯形算法。 这一结果终结了多面体组合学中的一个核心问题，并进一步强化了 2010 年对原始 Hirsch 猜想的否证。它排除了单纯形类线性规划算法获得多项式最坏情况保证的可能性，但不影响内点法等多项式时间线性规划算法。 该构造针对简单多面体，即每个顶点恰好有 d 个面相交；其图直径的增长快于面数的任意多项式。这一下界是关于最坏情况图直径的，并未给出精确增长速率，也不直接改进所有多面体的上界。

hackernews · acossta · 11月25日 17:34 · [社区讨论](https://news.ycombinator.com/item?id=50644980)

**背景**: 线性规划是在由线性不等式定义的多面体上优化线性目标函数。单纯形算法沿多面体的边从一个顶点移动到另一个顶点，因此多面体图的直径是从最坏初始顶点到达最优顶点所需枢轴步数的下界。Hirsch 在 1957 年猜想：d 维、n 个面的多面体直径不超过 n−d；Santos 在 2010 年用 43 维、86 个面的反例推翻了它。多项式 Hirsch 猜想则弱化为直径可由面数的某个多项式界定，原本用于解释单纯形法在实际中为何表现良好。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Polynomial_Hirsch_conjecture">Polynomial Hirsch conjecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hirsch_conjecture">Hirsch conjecture - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Simplex_algorithm">Simplex algorithm - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为这一结果重要，但多将其视为 2010 年原始 Hirsch 猜想被推翻后的“收尾”工作，而非彻底的范式转变。他们强调了一个通俗结论：不存在多项式时间的单纯形算法，并调侃重大数学突破如今以 GitHub 补丁说明的形式出现。

**标签**: `#mathematics`, `#optimization`, `#linear-programming`, `#complexity-theory`, `#polytopes`

---

<a id="item-11"></a>
## [开发者逆向 Windows 响度均衡并移植到 PipeWire](https://github.com/xoxorwr/pw-loudness-eq) ⭐️ 7.0/10

开发者 xoxorwr 在 GitHub 上发布了名为 pw-loudness-eq 的项目，逆向分析了 Windows 共享模式音频管线中的响度均衡/限幅行为，并将其重新实现为 Linux 上 PipeWire 的滤波器。该工作复现了 Windows 音频引擎在接近峰值时悄悄进行压缩、而不仅仅是整体增益归一化的处理方式。 对于双系统用户或从 Windows 迁移过来的 Linux 桌面用户来说，现在可以获得与 Windows 默认相同的响度处理效果，这在观看音量起伏很大的视频时尤其有用。同时，它也让 Windows 音频中一个大多数用户从不知晓的隐藏处理环节浮出水面，这对进行严谨听音或测量的用户很重要。 据讨论所述，Windows 仅在共享模式路径（WASAPI 共享/环回、DirectSound、MME）中通过 audiodg.exe 以及 AudioEng.dll 中的 CAudioLimiter 施加这种压缩，而 WASAPI 独占模式和 ASIO 则完全绕过它；效果非常细微，峰值处大约只有零点几 dB。评论者还指出，所描述的算法容易抬升持续的单音（如口哨声），因此需要在末端额外加一级限幅器。

hackernews · ThrowNotAway · 11月25日 11:34 · [社区讨论](https://news.ycombinator.com/item?id=50641171)

**背景**: PipeWire 是一个低延迟、基于图结构的多媒体处理引擎，已成为大多数现代 Linux 桌面的默认音频服务器，实际上取代了 PulseAudio 和 JACK。在 Windows 上，“响度均衡”（Loudness Equalization）是一项音频增强功能，通过拉平感知响度让轻与响的内容以相近音量播放，而共享模式播放会经由 audiodg.exe 音频引擎，此类处理正是在那里进行的。因此该项目把一个来自闭源 Windows DLL 的未公开专有行为，重新实现为开源的 Linux 滤波器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.thewindowsclub.com/disable-or-enable-loudness-equalization-in-windows-10">How to disable or enable Loudness Equalization in Windows 11/10</a></li>
<li><a href="https://allthings.how/how-to-enable-sound-equalization-on-windows-11/">How to Enable Sound Equalization on Windows 11</a></li>

</ul>
</details>

**社区讨论**: 讨论情绪褒贬不一：有人觉得这个隐藏的 Windows 限幅器很有意思，也有人反对把它称作“均衡”，认为这实际上是响度归一化，并警告该算法会抬升集中的单音、因此需要末端限幅。还有一部分人质疑为何非要去逆向 Windows DLL，认为用标准限幅算法就能实现，并提出了伦理层面的担忧，同时指出重视动态范围的听者可能根本不想要这种处理。

**标签**: `#audio`, `#PipeWire`, `#reverse-engineering`, `#Linux`, `#DSP`

---

<a id="item-12"></a>
## [Simon Willison 梳理十二个月内 LLM 的三个拐点](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) ⭐️ 7.0/10

Simon Willison 发布文章，延伸他在 AI Engineer Code Summit（2026 年 11 月 10–12 日，旧金山）上的主题演讲，认为过去十二个月里 LLM 与编码智能体的能力出现了三个重要拐点。他把第一个拐点定在 2025 年 11 月 24 日——Claude Opus 4.5 发布一周年，同月 OpenAI 还推出了 GPT-5.1 Instant、GPT-5.1 Thinking、GPT-5.1-Codex 与 GPT-5.1-Codex-Max；第二个拐点是 2026 年 6、7 月间他所称的“Fable 级模型”登场，起点是 Claude Fable 5。 作为 LLM 工具生态中最受关注的评论者之一，Willison 的梳理为工程团队提供了一个时间线：编码智能体何时从“不太可靠”变为“真正好用”，这直接影响团队何时采用、如何自建还是采购的决策。他也把过去一年的模型发布重新解读为一连串质变式的能力跃升，而不是无差别的版本号堆叠。 Willison 指出，Opus 4.5 发布时 Claude Code 才诞生九个月——它于 2025 年 2 月 24 日与 Claude 3.7 Sonnet 一同推出；而 Opus 4.5 是第一个让他觉得 Claude Code 默认输出通常就正确的模型，从而改变了他的日常工作流。他对“Fable 级模型”的定义很具体：只要能定义目标并提供必要工具，它们就会用暴力方式解决问题——例如 Claude Fable 在排查 Safari 显示故障时，自行搭建了基于 pyobjc-framework-Quartz 的截图机制和一个启用 CORS 的本地日志服务器；此外 Fable 5 曾在 6 月至 7 月 1 日期间因美国出口管制而被短暂封禁。

rss · Simon Willison · 11月24日 23:02

**背景**: Claude 是 Anthropic 的大语言模型系列，自 2023 年起发布，通常按能力分为 Haiku、Sonnet、Opus 三档，其中 Opus 最强。Claude Code 是 Anthropic 的终端编码智能体，属于更广义的“编码智能体”类别——这类由 LLM 驱动的工具会读取代码库、执行命令并修改文件来完成任务，而不只是补全代码行。AI Engineer Code Summit 是面向编码智能体开发者与 AI 工程师的邀请制会议，2026 年由 Neon、Vercel 和 Factory 主办，因此非常适合做这类回顾式的总结。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.engineer/code/2026">AI Engineer Code Summit 2026: AI Engineering Conference, Nov...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Opus_4.5">Claude Opus 4.5</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM`, `#coding agents`, `#AI engineering`, `#Claude Opus`, `#keynote analysis`

---