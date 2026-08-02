---
layout: default
title: "Horizon Summary: 2026-08-02 (ZH)"
date: 2026-08-02
lang: zh
---

> 从 22 条内容中筛选出 11 条重要资讯。

---

1. [MCP 2.0 无状态设计催生 mcp-explorer 与 datasette-mcp](#item-1) ⭐️ 9.0/10
2. [字节跳动 Seedance 2.5：一次性拍摄式视频生成与灵活引用](#item-2) ⭐️ 8.0/10
3. [Diátaxis 框架：将技术文档划分为四种模式](#item-3) ⭐️ 8.0/10
4. [Lean 内核健全性漏洞 #14576 事后剖析发布](#item-4) ⭐️ 8.0/10
5. [OpenAI Astra 模型据称攻克十个十年未解的数学难题](#item-5) ⭐️ 8.0/10
6. [DeepSeek V4 Flash 0731 发布：304B 参数模型性价比亮眼](#item-6) ⭐️ 8.0/10
7. [《64 位汇编艺术》：800 页 MASM 新书引发讨论](#item-7) ⭐️ 7.0/10
8. [Simon Willison 做客 Oxide and Friends，畅聊开源权重模型革命](#item-8) ⭐️ 7.0/10
9. [AI 理财建议：问对问题效果出奇地好](#item-9) ⭐️ 6.0/10
10. [格雷格·布罗克曼：Slack 中的 AI 应促进人际联系而非疏远](#item-10) ⭐️ 6.0/10
11. [smevals：用于测试模型、提示词和测试框架的小型评测套件](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [MCP 2.0 无状态设计催生 mcp-explorer 与 datasette-mcp](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 9.0/10

2026 年 7 月 28 日发布的 Model Context Protocol 规范（MCP 2.0）引入了无状态模式，每次工具调用只需一个 HTTP 请求。这促使 Simon Willison 在一周内构建了三个 MCP 实现，包括 CLI 工具 mcp-explorer 和 datasette-mcp。 无状态 MCP 大幅简化了客户端和服务端的实现，使 MCP 成为比赋予代理不受限制的 shell 访问更可行的选择。这重新点燃了对 MCP 的兴趣，并可能加速 AI 代理采用可审计、可控的工具集成方式。 旧版有状态 MCP 需要两个 HTTP 请求——一个用于初始化会话并获取 Mcp-Session-Id，另一个用于调用工具。新版无状态方法通过单个请求配以 MCP-Protocol-Version 和 Mcp-Method 头部完成，消除了服务器端会话状态并简化了扩展。

rss · Simon Willison · 7月31日 23:13

**背景**: MCP（模型上下文协议）是 Anthropic 于 2024 年 11 月推出的开放标准，旨在规范 AI 应用连接外部工具和数据源的方式。它在 2025 年引发了巨大关注，但后来被 Anthropic 的'Skills'方案部分取代，后者允许代理直接使用终端和 curl。无状态协议是一种每个请求都可独立理解、无需在请求之间保留会话状态的协议，具备更好的可靠性、可观测性和可扩展性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stateless_protocol">Stateless protocol</a></li>

</ul>
</details>

**标签**: `#MCP`, `#Model Context Protocol`, `#AI agents`, `#LLM`, `#protocol`

---

<a id="item-2"></a>
## [字节跳动 Seedance 2.5：一次性拍摄式视频生成与灵活引用](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) ⭐️ 8.0/10

字节跳动发布了 Seedance 2.5，这是其 AI 视频生成模型的重大升级，支持一次性拍摄式生成和多模态参考输入。用户可以一次输入最多 30 张图片、10 个视频片段和 10 个音频片段来引导生成。 此次发布标志着字节跳动在竞争激烈的 AI 视频生成市场中的领先意图，正面挑战 Sora、Veo 和 Kling 等西方模型。一次输入大量多模态引用能力有望大幅改善角色一致性和导演控制，这是电影制作人和创意专业人士的核心需求。 Seedance 2.5 加强了多模态引用生成能力，单次输入最多可包含 30 张图片、10 个视频片段和 10 个音频片段。官方发布页面强调“一次性拍摄式创作”，表明该模型致力于生成连贯的长镜头单次视频，而非短片。

hackernews · njaremko · 8月1日 20:45 · [社区讨论](https://news.ycombinator.com/item?id=49138302)

**背景**: Seedance、Sora 和 Veo 等 AI 视频生成模型可以根据文本、图片或视频参考生成视频。'一次性拍摄'生成是指在一次连续处理中完整生成整个场景或镜头，这需要很强的角色一致性和时间连贯性。参考到视频（R2V）是一种从参考图像保持主体身份的新兴技术；Seedance 2.5 将其扩展到多张图片、多个视频片段和音频，比常见的单一参考方案更为复杂。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5">Seedance 2.5 — One-take Creation, Flexible Referencing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Seedance_2.0">Seedance 2.0 - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2512.06905v1">Scaling Zero-Shot Reference-to-Video Generation</a></li>

</ul>
</details>

**社区讨论**: Hacker News（及相关讨论串）上的评论承认输出质量很高，但对产品方向存在分歧：有人指出 Seedance 2.5 重度聚焦于动作/高特效的文本生成视频，而美国电影制作人更需要保持演员一致性的视频到视频功能。另一些人赞赏其趣味性，但对推理成本表示担忧；还有用户提到即将开源权重的 MiniMax H3 是更便宜、更可控的替代选择。

**标签**: `#AI video generation`, `#ByteDance`, `#Seedance`, `#machine learning`, `#creative tools`

---

<a id="item-3"></a>
## [Diátaxis 框架：将技术文档划分为四种模式](https://diataxis.fr/) ⭐️ 8.0/10

Diátaxis 作为一套实用框架受到关注，它将技术文档划分为四种模式：教程、操作指南、参考资料和解释。该项目的官网及正在进行的多语言翻译工作引发了社区新的讨论，包括在面向 AI 代理的文档中的应用。 Diátaxis 为文档团队提供了统一的结构和词汇，让团队更容易决定应写什么类型的页面、以什么语气来写。它已被 Canonical/Ubuntu 等大型项目采用，并越来越多地用于 AI 代理的知识管理，正成为组织技术信息的标准方法之一。 四种模式来自两条轴线的交叉：行动与知识、学习与工作。社区实践者还提出了实用规则，例如操作指南和教程只能单向链接到参考文件、保持参考文件精简（约 400 行），以及使用验证时间戳防止内容过期。

hackernews · ryanseys · 8月1日 20:33 · [社区讨论](https://news.ycombinator.com/item?id=49138188)

**背景**: Diátaxis 是一套围绕用户需求来组织技术写作的文档框架。它识别出四种不同的需求——学习、解决问题、查阅事实和理解背景——并将其对应到教程、操作指南、参考资料和解释。该框架设计轻量且务实，Canonical 已将其作为文档体系的新基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://diataxis.fr/">Diátaxis</a></li>
<li><a href="https://ubuntu.com/blog/diataxis-a-new-foundation-for-canonical-documentation">Diátaxis , a new foundation for Canonical documentation | Ubuntu</a></li>
<li><a href="https://pasqualepillitteri.it/en/news/5528/diataxis-framework-documentation-ai">Diátaxis: The 4 Types of Technical Documentation and Their ...</a></li>

</ul>
</details>

**社区讨论**: 评论者大多非常热情，称赞 Diátaxis 在大型代码库交接中表现出色，并认为它能让 AI 代理文档保持 DRY，通过链接到唯一的事实来源来避免重复。也有人提醒文档可能随时间漂移，并建议引入验证时间戳；还有评论者开玩笑说千万别读它，因为读完你会发现自己的文档认知被彻底改变。

**标签**: `#documentation`, `#technical-writing`, `#framework`, `#knowledge-management`, `#developer-productivity`

---

<a id="item-4"></a>
## [Lean 内核健全性漏洞 #14576 事后剖析发布](https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/) ⭐️ 8.0/10

Lean 证明助手内核健全性漏洞 #14576 的事后分析已在 Leonardo de Moura 的博客上发布。该漏洞可能允许不健全的证明通过内核，事后分析讨论了其被发现和修复的过程。 由于 Lean 广泛用于形式化验证，内核健全性漏洞会削弱对证明认证的信任。此次事件凸显了在复杂的证明助手内核中维护健全性的持续挑战，以及独立验证方法的重要性。 社区讨论表明，该漏洞利用需要两个不同证明检查器实现中的两个不同缺陷，因此只要两者都更新，独立内核检查仍有效。该漏洞由证明系统研究人员以漏洞利用的形式呈现，事后分析除了修复特定缺陷外，还考虑了更广泛的验证实践。

hackernews · juhopitk · 8月1日 18:32 · [社区讨论](https://news.ycombinator.com/item?id=49137060)

**背景**: Lean 是一个基于归纳构造演算的证明助手，用于验证数学证明和代码。证明助手通常依赖一个小而可信的内核来认证证明，但这些内核很复杂，可能包含缺陷，正如 McTT 论文所指出的那样。最近的健全性漏洞凸显了进行基础类型论研究的必要性，以确保内核设计在理论上是健全的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant)</a></li>
<li><a href="https://dl.acm.org/doi/epdf/10.1145/3747511">McTT: A Verified Kernel for a Proof Assistant</a></li>
<li><a href="https://x.com/TaliaRinger/status/2082439129061609679">The recent Lean kernel soundness bug shows the importance of ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映了实用主义与哲学关切的混合。一些人将此漏洞视为预期的局限性，指出独立内核仍能提供强有力的保证，而另一些人则认为健全性漏洞是一个严重缺陷，并建议像 Metamath 这样的替代系统可能更严密。Knuth 的名言——'小心上述代码中的缺陷；我只证明了它的正确性，并未尝试过它'——很能概括这种情绪。

**标签**: `#Lean`, `#formal verification`, `#soundness`, `#proof assistants`, `#kernel`

---

<a id="item-5"></a>
## [OpenAI Astra 模型据称攻克十个十年未解的数学难题](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 8.0/10

OpenAI 宣布，其下一代主要模型 Astra 的一个内部版本，解决了十个至少十年未有进展的数学问题，每个问题在 GPT-5.6 Sol 的 token 价格下花费不到 2,000 美元。相关结果以 Lean 4 形式化证明的形式发布在 openai/ten-proofs 仓库中，并附有一篇论文和一份由 LLM 生成的推理回顾。 如果这些结果得到验证，这标志着一个重要的 AI 研究里程碑：一个前沿模型以极低的成本自主取得了真正的数学突破。这可能加速向 Terence Tao 所说的“大数学”（大型人机协作）转变，同时加剧数学家们的存在性反思。 OpenAI 没有披露模型在成功解决这十个问题之前，曾失败尝试过多少次，Simon Willison 也指出缺少提示词透明性。这些解决方案涵盖群论、高维几何、编码理论、量子复杂性、格密码学和极值组合学，并附有机器可检验的 Lean 4 证书。

rss · Simon Willison · 8月1日 20:34

**背景**: 这一公告之前，Anthropic 最近披露其未发布的 Claude Mythos Preview 模型在软件中发现了加密弱点，花费了 100,000 美元的 token。据报道，OpenAI 的 Astra 是一个多智能体模型系列，可以连续数小时甚至数天处理复杂问题，CEO Sam Altman 已向政策制定者演示了该模型。许多数学家正在经历所谓的“深蓝时刻”，Terence Tao 则描述了“大数学”的未来：AI 处理大量技术性苦活，人类专注于创造性部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://the-decoder.com/openai-announces-its-next-major-model-astra-by-dropping-ten-previously-unsolved-math-solutions/">OpenAI announces its "next major model" Astra by dropping ten ...</a></li>
<li><a href="https://www.bitsminds.com/news/openai-astra-ten-open-math-problems-lean-proofs-2026">OpenAI Names Its Next Model Family Astra — and Says It Solved ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#OpenAI`, `#mathematics`, `#theoretical computer science`, `#research`

---

<a id="item-6"></a>
## [DeepSeek V4 Flash 0731 发布：304B 参数模型性价比亮眼](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 8.0/10

DeepSeek 发布了 DeepSeek-V4-Flash-0731，这是一个 3040 亿参数的开源权重模型，宣称具备大幅增强的 agentic 能力。Artificial Analysis 将其排名置于 MiniMax M3 之前，且其每百万输入 token 0.14 美元、每百万输出 token 0.27 美元的定价，使其可能是当前性价比最高的模型。 在 Artificial Analysis 的“智能指数 vs 每任务成本”图中，该模型以远低于那些更大、更贵竞品的成本实现强劲表现，让强大的 agentic 能力以极低价格普及。这加剧了快速演进的 LLM 市场中，闭源及其他开源权重模型厂商面临的竞争压力。 该模型拥有 3040 亿参数，在 Hugging Face 上以 167GB 体量提供下载，并支持可调的推理强度。Simon Willison 在“鹈鹕骑自行车”测试中发现，通过 OpenRouter 将 reasoning_effort 从默认调至 high 后，输出质量显著提升。

rss · Simon Willison · 7月31日 23:59

**背景**: Agentic AI 指那些具有目标导向、能使用外部工具并执行多步骤任务的系统，其控制流通常由大语言模型驱动。Artificial Analysis 智能指数是多个生产环境基准分数的加权平均值（0-100 分），而“单位智能价值”则将该智能分数与每任务成本进行对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index | Artificial Analysis</a></li>
<li><a href="https://shellypalmer.com/2026/06/price-per-intelligence-unit/">Price Per Intelligence Unit | Shelly Palmer</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#LLM`, `#Model Release`, `#AI`, `#Artificial Intelligence`

---

<a id="item-7"></a>
## [《64 位汇编艺术》：800 页 MASM 新书引发讨论](https://nostarch.com/art-64-bit-assembly-v2) ⭐️ 7.0/10

No Starch Press 推出了约 800 页的《64 位汇编艺术》（The Art of 64-bit Assembly），该书使用 Microsoft Macro Assembler (MASM) 讲授 x86-64 汇编编程。这本书在 Hacker News 上引发了关于汇编语言价值以及书中 AI 辅助内容质量的讨论。 这场讨论表明，即使在高阶语言和 AI 代码生成的时代，人们对性能关键系统、操作系统和硬件所需的底层专业知识仍有浓厚兴趣。它也凸显了社区对技术书籍中 AI 生成文本的担忧。 该书使用 MASM 语法，具体采用针对 64 位代码的 ML64 汇编器，并涵盖 while 循环和字符串处理等宏功能。一位 Hacker News 评论者指出 GNU Assembler 缺少 MASM 的某些功能，另一位评论者则批评开篇部分包含 AI 生成的文本。

hackernews · 0x54MUR41 · 8月1日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49134599)

**背景**: x86 汇编语言是一种与 CPU 指令密切对应的底层编程语言，常用于需要精确控制硬件的嵌入式系统、内核和设备驱动程序中。MASM 是微软的宏汇编器，历史上随 Visual Studio 和 Windows SDK 提供，并针对 MS-DOS 和 Windows 开发采用 Intel 语法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MASM">MASM</a></li>
<li><a href="https://en.wikipedia.org/wiki/X86_assembly_language">X86 assembly language</a></li>

</ul>
</details>

**社区讨论**: 评论者大多称赞这本书的宏大目标以及汇编语言的持续价值，但也有人批评其 AI 生成的营销开篇，并认为讨论过多集中在琐碎细节上。还有人询问 Linux 下的替代书籍，并分享自己使用汇编的经验，例如通过 MASM 构建面向 16 位 x86 的编译器。

**标签**: `#assembly`, `#low-level programming`, `#systems programming`, `#book`, `#MASM`

---

<a id="item-8"></a>
## [Simon Willison 做客 Oxide and Friends，畅聊开源权重模型革命](https://simonwillison.net/2026/Jul/31/oxide-and-friends/#atom-everything) ⭐️ 7.0/10

Simon Willison 做客 Oxide and Friends 播客，讨论了过去一周 AI 领域的剧烈变化，包括 Kimi K3 证明开源权重模型能与专有前沿模型一较高下，以及几乎各大 AI 公司联署的关于开源权重模型的行业公开信。他还回顾了自己 2026 年 1 月的预测，并新增一条：到今年年底，教皇会就开源模型发表某种言论。 这期讨论捕捉到了一个关键节点：开源权重模型似乎正与封闭前沿系统达到同等水平，这可能重塑 AI 能力的发布方式与治理格局。节目还突显了行业在开源权重问题上的分歧日益扩大，Anthropic 拒签该公开信就是例证。 节目录制之后又发生了两件值得一提的事：DeepSeek V4 Flash 0731 发布，以及 Anthropic 自身也遭遇了网络安全事件。据搜索结果，Kimi K3 是一个 2.8 万亿参数模型，基于 Kimi Delta Attention，原生支持视觉理解，上下文窗口达 100 万 token。

rss · Simon Willison · 7月31日 21:33

**背景**: 开源权重模型是指将训练得到的参数（即权重）公开发布，任何人都可以下载并在本地运行的 AI 模型。它与完全开源 AI 不同，后者还要求以开放许可证发布训练数据和代码。Moonshot AI 打造的 Kimi K3 是一个 2.8 万亿参数模型，被引为开源权重模型如今能与专有前沿模型匹敌的证据。同期，DeepSeek V4 Flash 的发布也进一步改变了 AI 行业格局。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek - ai / DeepSeek - V 4 - Flash · Hugging Face</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-weights`, `#podcast`, `#Simon-Willison`, `#frontier-models`

---

<a id="item-9"></a>
## [AI 理财建议：问对问题效果出奇地好](https://mitsloan.mit.edu/ideas-made-to-matter/ai-financial-advice-surprisingly-good-especially-if-you-ask-right-questions) ⭐️ 6.0/10

麻省理工斯隆管理学院的一项新研究发现，当用户提出正确的问题时，AI 模型能够提供出乎意料的高质量理财建议，这表明提问质量对 AI 建议的实用性起着关键作用。 这很重要，因为这意味着 AI 可以成为一种低成本、易获取的理财咨询工具，可能让无法负担人工顾问的人群也能获得财务指导。同时，它也凸显了用户自身金融素养对获得良好 AI 建议的重要性。 该研究聚焦于大型语言模型，以及提问措辞与回答质量之间的互动。其局限性包括：AI 建议可能仍偏泛泛而谈，且需要结合具体情境进行追问。

hackernews · foxtrot8672 · 8月1日 22:25 · [社区讨论](https://news.ycombinator.com/item?id=49139102)

**背景**: 大型语言模型（如 GPT-4）在海量文本数据上训练，并根据语言模式生成回答。它们本质上并不是理财顾问，但可以综合常见的理财建议。其输出质量往往取决于用户如何精确地表述问题，这正是 MIT 斯隆研究强调“问对问题”之所以重要的原因。

**社区讨论**: 评论区总体持怀疑态度。一些人认为 LLM 只是‘自动补全’提示词而非真正给出建议，另一些人则指出真正的问题在于用户普遍的金融素养不足。还有人对该研究的评估方法是否反映真实场景提出质疑，指出模型没有‘切身利益’，可能会影响其风险建议。

**标签**: `#AI`, `#LLM`, `#finance`, `#financial advice`, `#research`

---

<a id="item-10"></a>
## [格雷格·布罗克曼：Slack 中的 AI 应促进人际联系而非疏远](https://simonwillison.net/2026/Aug/1/greg-brockman/#atom-everything) ⭐️ 6.0/10

OpenAI 总裁兼联合创始人格雷格·布罗克曼观察到，OpenAI 员工将 ChatGPT 接入 Slack 后，同事们不喜欢被他人的 AI 助手联系求助，即使他们很乐意帮助这位同事本人。他在推特上分享了这一观察，指出这反映了人们对人际关系的重视。 这一观察非常重要，因为 AI 代理正越来越多地集成到 Slack 等职场协作工具中。它表明，AI 若要被接受，应当增强人们的时间效率和情感纽带，而不是成为冷冰冰的中间层。 这条引文出自格雷格·布罗克曼的推文，并被 Simon Willison 的博客引用。布罗克曼强调，人们希望 AI 能‘把时间还给人’或‘增进共处时光’，而不是成为‘隔绝人的一层’。这一观察虽属轶事，但来自 AI 领域的重要人物。

rss · Simon Willison · 8月1日 22:29

**背景**: ChatGPT 等 AI 助手可以接入 Slack，帮助自动化任务和回答问题。布罗克曼的观察指出了一个常见陷阱：当 AI 代表同事发起请求时，会让人感到缺乏人情味甚至被打扰。这涉及 AI 伦理与职场人机互动的更广泛讨论，即维护信任和人际联系至关重要。

**标签**: `#ai-ethics`, `#generative-ai`, `#openai`, `#workplace-ai`, `#human-ai-interaction`

---

<a id="item-11"></a>
## [smevals：用于测试模型、提示词和测试框架的小型评测套件](https://simonwillison.net/2026/Jul/31/smevals/#atom-everything) ⭐️ 6.0/10

Simon Willison 与 Prime Radiant 发布了 smevals，这是一个新的开源工具，用于在多种模型配置上运行小型评测套件并评分结果。该工具提供 `uvx smevals docs`、`run`、`grade`、`serve` 和 `build` 等命令行命令，用于创建、运行和报告评测。 它为 AI/机器学习从业者提供了一种轻量、实用的方式，无需构建自定义基础设施即可比较模型、提示词和智能体测试框架。这也凸显了在 LLM 开发流程中，可复现的小型评测正变得越来越重要。 一个 eval 是包含任务（tasks）的 YAML 文件目录，每个任务可针对多个 config（配置）运行，配置可指定模型、提示词或测试框架参数。运行（runs）使用 checker（检查器）单独评分，检查器可以是简单的字符串或格式检查，也可以是自定义脚本，包括以 LLM 作为评审的评估；结果可通过本地服务器查看，或构建为静态 HTML。

rss · Simon Willison · 7月31日 21:15

**背景**: 评测测试框架（evaluation harness）是自动化测试 LLM 和智能体的框架，用于在定义好的任务上衡量质量；像 EleutherAI 的 lm-evaluation-harness 这类成熟工具在研究领域被广泛使用。smevals 刻意采用小规模方法，专注于快速比较模型、提示词和测试框架，这是 Simon Willison 对这个想法的第三次迭代，其设计目标是让编码智能体易于学习和使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/EleutherAI/lm-evaluation-harness">GitHub - EleutherAI/lm-evaluation-harness: A framework for ...</a></li>
<li><a href="https://arize.com/blog/what-is-an-evaluation-harness/">What is an evaluation harness? Definition & guide - Arize AI</a></li>
<li><a href="https://primeradiant.com/blog/2026/smevals.html">smevals - a small eval suite for evaluating models, prompts, and harnesses | Prime Radiant</a></li>

</ul>
</details>

**标签**: `#AI evaluation`, `#evals`, `#models`, `#prompts`, `#open source`

---