---
layout: default
title: "Horizon Summary: 2026-06-03 (ZH)"
date: 2026-06-03
lang: zh
---

> 从 36 条内容中筛选出 9 条重要资讯。

---

1. [VSCode 漏洞致 GitHub 令牌一键被盗](#item-1) ⭐️ 8.0/10
2. [斯坦福研究显示 AI 表现优于法学教授](#item-2) ⭐️ 8.0/10
3. [微软发布 MAI-Thinking-1 和 MAI-Code-1-Flash 大语言模型](#item-3) ⭐️ 8.0/10
4. [黑客利用 Meta AI 聊天机器人劫持 Instagram 账户](#item-4) ⭐️ 8.0/10
5. [How we index images for RAG](#item-5) ⭐️ 7.0/10
6. [NBD-VRAM：在 Linux 上使用 GPU 显存作为交换空间](#item-6) ⭐️ 6.0/10
7. [比亚迪零件 CT 扫描展现高品质制造](#item-7) ⭐️ 6.0/10
8. [试用 Clojure 一个月：开发者的感悟](#item-8) ⭐️ 6.0/10
9. [datasette-agent-micropython 0.1a0：安全代码沙盒](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [VSCode 漏洞致 GitHub 令牌一键被盗](https://blog.ammaraskar.com/github-token-stealing/) ⭐️ 8.0/10

一位安全研究员发现 VSCode 嵌入式 Web 编辑器中的一个漏洞，允许攻击者通过一次点击窃取 GitHub 令牌。微软在收到报告后悄悄修复了该漏洞，但由于与 MSRC 的糟糕体验，研究员公开了细节。 该漏洞对使用 VSCode Web 版的开发者构成严重威胁，可能导致 GitHub 账户和仓库被未经授权访问。同时也凸显了微软等大型平台需要改进安全响应流程。 该漏洞利用了 VSCode 嵌入式 Web 编辑器的认证机制，精心构造的链接可以窃取浏览器中存储的 GitHub 令牌。研究员此前向 MSRC 报告过类似的 VSCode 漏洞但遭遇糟糕体验，因此选择了公开披露。

hackernews · ammar2 · 6月2日 15:29 · [社区讨论](https://news.ycombinator.com/item?id=48371562)

**背景**: VSCode for the Web (vscode.dev) 是 Visual Studio Code 的浏览器版本，允许直接编辑 GitHub 仓库中的文件，需要 GitHub 认证。个人访问令牌（PAT）常用于 GitHub 操作认证，一旦泄露可能授予对仓库的广泛访问权限。嵌入式 Web 编辑器与 GitHub 的集成在隔离不足时创造了潜在攻击面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.visualstudio.com/docs/setup/vscode-web">Visual Studio Code for the Web and the vscode .dev URL</a></li>
<li><a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens">Managing your personal access tokens - GitHub Docs</a></li>

</ul>
</details>

**社区讨论**: 社区评论对微软安全响应中心（MSRC）表示不满，一位用户分享了亲身经历的令牌被盗事件，并建议进行令牌隔离。另一位用户赞扬研究员在 MSRC 处理不善的情况下仍提高了安全意识。

**标签**: `#security`, `#VSCode`, `#GitHub`, `#token-stealing`, `#vulnerability`

---

<a id="item-2"></a>
## [斯坦福研究显示 AI 表现优于法学教授](https://law.stanford.edu/press/ai-outperforms-law-professors-in-stanford-law-study/) ⭐️ 8.0/10

斯坦福法学院发表研究称，对于一年级合同法问题，法学教授更偏爱 AI 生成的答案而非教授自己撰写的答案。 这表明大型语言模型可能成为法律教育的有效辅导工具，或许能降低培训成本，但该研究的方法受到质疑。 该研究仅涉及 16 名教授，评分的方差很大，引发对统计效力的担忧。使用的 AI 模型可能基于问题所用的相同教材进行训练。

hackernews · berlianta · 6月2日 23:43 · [社区讨论](https://news.ycombinator.com/item?id=48377761)

**背景**: 大型语言模型是在海量文本数据上训练的神经网络，能够生成和理解人类语言。它们可以回答问题、撰写内容，但可能产生有偏见或不可靠的输出。本研究探讨了将 LLM 用作法学学生辅导工具的潜力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/large-language-model-llm/">Large Language Model (LLM) - GeeksforGeeks</a></li>

</ul>
</details>

**社区讨论**: 评论对小样本量和高方差表示怀疑，认为研究的统计效力有问题。有人澄清该研究聚焦于 AI 作为辅导工具，而非取代律师，并指出降低法律教育成本的潜在积极结果。

**标签**: `#AI`, `#LLM`, `#legal`, `#education`, `#research`

---

<a id="item-3"></a>
## [微软发布 MAI-Thinking-1 和 MAI-Code-1-Flash 大语言模型](https://simonwillison.net/2026/Jun/2/microsofts-new-models/#atom-everything) ⭐️ 8.0/10

微软宣布了两款新的文本大语言模型：MAI-Thinking-1（总参数 1 万亿，激活参数 350 亿）和 MAI-Code-1-Flash（总参数 1370 亿，激活参数 50 亿），前者面向特定早期合作伙伴，后者面向 GitHub Copilot 个人用户。 这些模型采用混合专家架构（MoE），激活参数数量低，展现了显著的效率优势，可能降低推理成本同时保持竞争力，有望推动 AI 行业向更具成本效益的部署方向发展。 技术论文显示，MAI-Thinking-1 的训练数据包括专有网页抓取和 Common Crawl，与其他主流大语言模型类似，并非完全基于授权数据。最初有报道错误地将模型总参数量说得很小，但实际上它们是大型 MoE 模型。

rss · Simon Willison · 6月2日 22:21

**背景**: 混合专家（MoE）是一种架构，它将模型分成多个“专家”子网络，由一个门控网络为每个输入 token 激活其中一部分。这使得模型可以拥有庞大的总参数量（知识容量），但每次计算只使用少量激活参数，从而降低计算成本和内存需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://medium.com/@csburakkilic/understanding-moe-architectures-the-difference-between-total-and-active-parameters-ad1d161fccaa">Understanding MoE Architectures: The Difference Between Total and Active Parameters | by Burak Kılıç | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，MAI-Code-1-Flash 在 SWE-bench Pro 上 51%的得分仅比更小的 Qwen3.6-35B-A3B 的 49.5%略有优势，并质疑小模型在严肃编码任务中的价值。还有人表达了对 GitHub Copilot 定价调整和基准测试表现与营销承诺之间差距的担忧。

**标签**: `#Microsoft`, `#LLM`, `#AI`, `#MAI`, `#Efficient Models`

---

<a id="item-4"></a>
## [黑客利用 Meta AI 聊天机器人劫持 Instagram 账户](https://simonwillison.net/2026/Jun/1/hackers-simply-asked-meta-ai/#atom-everything) ⭐️ 8.0/10

黑客通过简单地向 Meta 的 AI 支持聊天机器人请求将账户关联到新邮箱地址，成功接管了高知名度 Instagram 账户，绕过了标准的账户恢复流程。 此事件揭示了将 AI 聊天机器人与敏感支持功能集成存在的严重安全漏洞，表明即使是简单的攻击也能危及高价值账户。它凸显了在 AI 驱动的客户服务系统中建立强大防护措施的紧迫性。 该漏洞已由多个来源验证，不涉及复杂的提示注入；黑客只是简单地要求机器人关联新邮箱。受影响的账户包括奥巴马白宫 Instagram 账户等高知名度目标。

rss · Simon Willison · 6月1日 21:14

**背景**: 提示注入是一种安全漏洞，攻击者通过构造输入来操纵大型语言模型（LLM）执行非预期操作。Meta 于 2024 年 12 月推出了 AI 支持助手，提供全天候账户支持，包括密码重置和账户恢复。将聊天机器人直接接入账户恢复工作流程，无意中创造了一次性账户接管漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.macrumors.com/2026/06/01/meta-ai-instagram-attack/">Meta AI Support Bot Helped Hackers Hijack Instagram Accounts</a></li>
<li><a href="https://www.eweek.com/news/meta-ai-instagram-hack-obama-white-house/">Meta AI Support Exploit Hijacks Obama White House Instagram...</a></li>

</ul>
</details>

**标签**: `#security`, `#AI chatbot`, `#vulnerability`, `#social media`, `#account takeover`

---

<a id="item-5"></a>
## [How we index images for RAG](https://www.kapa.ai/blog/how-we-index-images-for-rag) ⭐️ 7.0/10

Describes a method to index images cheaply by generating text descriptions at indexing time for RAG retrieval.

hackernews · mooreds · 6月2日 16:13 · [社区讨论](https://news.ycombinator.com/item?id=48372239)

**标签**: `#RAG`, `#image indexing`, `#vision models`, `#cost-efficiency`, `#text descriptions`

---

<a id="item-6"></a>
## [NBD-VRAM：在 Linux 上使用 GPU 显存作为交换空间](https://github.com/c0dejedi/nbd-vram) ⭐️ 6.0/10

一款名为 NBD-VRAM 的开源工具允许 Linux 用户将 Nvidia GPU 的显存用作交换空间，专为焊接内存且 GPU 显存闲置的笔记本电脑设计。 这为升级选项有限的用户提供了一种扩展系统内存的新方法，尽管与 SSD 交换相比存在性能权衡。 该工具在 RTX 3070 笔记本上实现约 1.3 GB/s 的顺序吞吐量，比 NVMe SSD 慢但延迟更低。它适用于 Linux 和 Nvidia GPU，需要正确配置以避免与显示驱动冲突。

hackernews · tanelpoder · 6月2日 22:55 · [社区讨论](https://news.ycombinator.com/item?id=48377404)

**背景**: 交换空间是当 RAM 已满时用作虚拟内存的存储部分。通常交换空间位于硬盘或 SSD 上，比 RAM 慢。GPU 显存速度快，但通常保留给图形任务。该工具将闲置的显存重新用作交换空间，但适用场景有限，并非对所有用户都有益。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/c0dejedi/nbd-vram">GitHub - c0deJedi/nbd-vram: Use your NVIDIA GPU's VRAM as swap space on Linux. Built for laptops with soldered memory and no upgrade path. If you have an RTX card sitting there with 8GB of VRAM and you're getting swapped to SSD, this puts that VRAM to work · GitHub</a></li>
<li><a href="https://www.phoronix.com/news/NVIDIA-NBD-VRAM">NBD-VRAM Provides Swap Space On Your NVIDIA GeForce GPUs - Phoronix</a></li>
<li><a href="https://wiki.archlinux.org/title/Swap_on_video_RAM">Swap on video RAM - ArchWiki</a></li>

</ul>
</details>

**社区讨论**: 评论者指出了该工具的适用场景有限，但承认其对焊接内存笔记本电脑的价值。一些人指出了性能限制（例如顺序吞吐量低于 NVMe）以及历史先例，如 GpuRamDrive 和 ArchWiki 上的视频 RAM 交换。整体态度是谨慎乐观，同时认识到该工具的局限性。

**标签**: `#Linux`, `#swap`, `#GPU`, `#VRAM`, `#performance`

---

<a id="item-7"></a>
## [比亚迪零件 CT 扫描展现高品质制造](https://www.lumafield.com/scan-of-the-month/byd) ⭐️ 6.0/10

Lumafield 发布了比亚迪汽车零件的 CT 扫描图像，包括钥匙和控制臂，展示了详细的内部结构和高制造质量。这些扫描直观地体现了比亚迪的垂直整合和精密制造能力。 这提供了切实的证据，反驳了关于中国汽车质量的负面刻板印象，表明比亚迪的零件坚固且设计精良。同时也凸显了工业 CT 扫描在公共工程分析和教育中的应用价值。 钥匙的 CT 扫描显示，机械备用钥匙是从卡扣中滑出的，而非一些人认为的铰链设计。控制臂和其他部件展现出与高度垂直整合相符的坚固结构。

hackernews · viasfo · 6月2日 20:30 · [社区讨论](https://news.ycombinator.com/item?id=48375824)

**背景**: 工业 CT 扫描利用 X 射线非破坏性地创建物体的 3D 内部图像，常用于制造中的缺陷检测和质量控制。比亚迪是一家中国电动汽车制造商，以生产从锂矿开采到成品汽车的大部分自有组件而闻名，实现了与早期福特相当的垂直整合水平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Industrial_CT_scanning">Industrial CT scanning</a></li>
<li><a href="https://news.gm.com/home.detail.html/Pages/topic/us/en/2025/jul/0715-GM-CT-scanning-vehicle-manufacturing-quality.html">How GM uses CT scanning to boost vehicle manufacturing quality</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬了比亚迪部件的坚固制造质量，一位技术人员亲身证实了其耐用性。有修正指出钥匙的机械备用部分是从滑出而非铰链设计，讨论还对比了比亚迪（75% 内部组件）与特斯拉和福特的整合水平。

**标签**: `#BYD`, `#electric vehicles`, `#CT scanning`, `#automotive engineering`, `#vertical integration`

---

<a id="item-8"></a>
## [试用 Clojure 一个月：开发者的感悟](https://www.acdw.net/clojure/) ⭐️ 6.0/10

一位开发者发布博客，分享了使用 Clojure 约一个月后的初步印象，包括他们使用宏构建静态站点生成器的经历。 该帖子引发了社区的热烈讨论（167 分，88 条评论），内容涉及 Clojure 的语法、方言、运行时权衡以及生态系统成熟度，反映了对 JVM 上函数式编程的持续兴趣。 作者强调 Clojure 的宏系统是实现自定义模板引擎的关键。评论者指出了 Clojure 的各种方言（如 ClojureScript、ClojureDart 和 babashka），并讨论了运行时能力与语法的重要性。

hackernews · speckx · 6月2日 19:56 · [社区讨论](https://news.ycombinator.com/item?id=48375393)

**背景**: Clojure 是 Lisp 的一种动态、函数式方言，运行在 Java 虚拟机（JVM）上，强调不可变性和并发性。它通过宏系统将代码视为数据，并衍生出针对不同运行时（JavaScript、.NET、Dart 等）的多种方言。该语言由 Rich Hickey 在 21 世纪中期创建。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Clojure">Clojure - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Clojure_(programming_language)">Clojure (programming language)</a></li>
<li><a href="https://clojure.org/">The Clojure Programming Language</a></li>

</ul>
</details>

**社区讨论**: 社区积极参与：HiPhish 开玩笑说编写静态站点生成器是 Lisp 的成人礼，Jeaye 赞扬了 Clojure 跨运行时的可移植性。Pdimitar 则认为真正的价值在于运行时，批评了 Clojure 的并发模型不如 Erlang 或 Go。fbuilesv 提供了页面的存档副本。

**标签**: `#Clojure`, `#functional programming`, `#programming languages`, `#web development`, `#static site generator`

---

<a id="item-9"></a>
## [datasette-agent-micropython 0.1a0：安全代码沙盒](https://simonwillison.net/2026/Jun/2/datasette-agent-micropython/#atom-everything) ⭐️ 6.0/10

Simon Willison 发布了 datasette-agent-micropython 0.1a0 的首个 alpha 版本，这是一个 Datasette Agent 插件，使用编译为 WebAssembly 的 MicroPython 在沙盒环境中执行 Python 代码。该沙盒目前尚未被 GPT-5.5 突破。 这使得 Datasette Agent 能够安全地生成并执行来自 AI 模型响应的任意 Python 代码，在确保安全性的同时显著扩展其数据分析和自动化能力。它为 LLM 驱动的代码执行提供了一种实用的沙盒方法。 该插件利用编译为 WebAssembly 的 MicroPython，完全在浏览器或服务端 WebAssembly 运行时中运行。alpha 版本处于早期阶段，作者报告称 GPT-5.5 尚未逃离沙盒。

rss · Simon Willison · 6月2日 19:28

**背景**: Datasette Agent 是 Datasette 的 AI 助手，Datasette 是一个用于探索和发布数据的工具。MicroPython 是 Python 3 的轻量级实现，专为微控制器设计，但也可编译为 WebAssembly 以便在浏览器中执行。当允许 LLM 生成代码时，沙盒化至关重要，以防止恶意或错误代码影响主机系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agent.datasette.io/">Datasette Agent: an AI assistant for Datasette to help ...</a></li>
<li><a href="https://tools.simonwillison.net/micropython">MicroPython Code Executor</a></li>

</ul>
</details>

**标签**: `#datasette`, `#python`, `#sandboxing`, `#webassembly`, `#datasette-agent`

---