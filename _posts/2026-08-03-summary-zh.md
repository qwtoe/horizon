---
layout: default
title: "Horizon Summary: 2026-08-03 (ZH)"
date: 2026-08-03
lang: zh
---

> 从 20 条内容中筛选出 9 条重要资讯。

---

1. [Qwen3.8-Max：阿里开源 2.4T 参数旗舰模型，主打编码与协作](#item-1) ⭐️ 8.0/10
2. [卡帕西的鹈鹕推文引发基准测试讨论](#item-2) ⭐️ 8.0/10
3. [Kakehashi：实验性用户空间，在 Linux ARM 上运行 macOS 二进制文件](#item-3) ⭐️ 8.0/10
4. [OpenAI Astra 模型以每个不到 2000 美元解决十个十年未解数学问题](#item-4) ⭐️ 8.0/10
5. [SwiftUI After 7 Years](#item-5) ⭐️ 7.0/10
6. [英语学习者核心词汇的转变：从人际美德到社会概念](#item-6) ⭐️ 7.0/10
7. [AI 基准测试：画一只长着哈布斯堡下巴的青蛙](#item-7) ⭐️ 7.0/10
8. [微软牵头 235 家公司联名公开信捍卫开放权重 AI 模型](#item-8) ⭐️ 7.0/10
9. [Greg Brockman：人们反感同事的 ChatGPT 来请求帮助](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Qwen3.8-Max：阿里开源 2.4T 参数旗舰模型，主打编码与协作](https://qwen.ai/blog?id=qwen3.8) ⭐️ 8.0/10

阿里巴巴通义团队正式发布 Qwen3.8-Max，这是迄今为止 Qwen 家族中最强大的模型，并宣布将于下周开放其权重。这标志着 Qwen-Max 级别模型首次开放源代码权重。 将 2.4T 参数的旗舰模型以开放权重形式发布，可能改变开源 AI 格局，为开发者和企业提供替代 OpenAI 和 Anthropic 闭源模型的高性能选择。社区尤其关注较小的 27B 版本，预计其在本地部署方面表现出色。 根据评测，Qwen3.8-Max 是阿里巴巴首款参数超过 1 万亿的多模态模型，确认采用 2.4T 参数架构，针对编码、长时程智能体和数据分析进行了优化。开放权重版本将于下周发布，该模型也已通过 Qoder 和 QwenCloud 提供，支持结构化输出。

hackernews · ai2027 · 8月3日 02:16 · [社区讨论](https://news.ycombinator.com/item?id=49150470)

**背景**: 在 AI 领域，“开放权重”指的是发布训练好的模型参数，同时保留训练数据和架构细节，介于完全闭源和完全开源之间。Qwen 系列是阿里巴巴的开源大语言模型系列，其中 Qwen3.6-27B 被广泛认为是本地部署的最佳模型之一。AI 助手中的“cowork（协作）”趋势，指的是智能体能够在共享环境中自主规划和执行多步骤任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eesel.ai/blog/qwen38-max-review">Qwen 3 . 8 Max review: Alibaba's 2.4T flagship, tested (2026) | eesel AI</a></li>
<li><a href="https://www.orcarouter.ai/blog/qwen-3-8-max-review">Qwen 3 . 8 - Max Review: Alibaba's 2.4T AI for Coding Agents</a></li>
<li><a href="https://www.cnet.com/tech/services-and-software/openai-just-teased-a-new-open-weights-ai-model-heres-what-that-means/">OpenAI Just Teased a New ' Open - Weights ' AI Model... - CNET</a></li>

</ul>
</details>

**社区讨论**: 评论区对即将发布的开放权重 Qwen3.8-27B 充满期待，指出 Qwen3.6-27B 已经是顶级本地模型。也有人对营销时机表示怀疑，称一旦 OpenAI 和 Anthropic 上市，此类公告将成为可靠的卖出信号，而另一些人则关注 27B 模型在本地使用中的潜力。

**标签**: `#AI`, `#Qwen`, `#open-source`, `#LLM`, `#coding`

---

<a id="item-2"></a>
## [卡帕西的鹈鹕推文引发基准测试讨论](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 8.0/10

安德烈·卡帕西（Andrej Karpathy）发推展示了一个 AI 模型生成鹈鹕的示例，在 Hacker News 上引发了关于模型生成的 3D/动画输出能否作为物理世界理解基准的热烈讨论。 这标志着评估 AI 对物理世界动态理解的方式正在从文本和图像转向交互式 3D 生成。它可能影响未来多模态模型的测试和比较方式。 讨论指出，如果没有确切的提示词，这类输出可能无法复现，而且一些模型（如 Anthropic 的模型）似乎是专门针对 three.js 代码生成调优的。像制作一个可玩弹珠游戏这样简单的物理提示，仍然经常难倒前沿 LLM。

hackernews · delichon · 8月2日 04:05 · [社区讨论](https://news.ycombinator.com/item?id=49140998)

**背景**: “鹈鹕基准”源于西蒙·威利森（Simon Willison），他让 LLM 生成一只骑自行车的鹈鹕的 SVG 图片，作为一种轻量级的定性能力测试。卡帕西曾在特斯拉和 OpenAI 任职，以其对大型语言模型的科普讲解而闻名。他的推文将这个想法延伸到 3D 生成领域，引发了关于这类输出究竟在衡量什么的争论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2025/Jun/6/six-months-in-llms/">The last six months in LLMs, illustrated by pelicans on bicycles</a></li>
<li><a href="https://simonw.substack.com/p/trying-out-gemini-3-pro-with-audio">Trying out Gemini 3 Pro with audio transcription and a new pelican benchmark</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者意见不一：有人认为不完美的鹈鹕输出正是重点——它是一个有用的物理理解定性基准；也有人质疑可复现性，并指出模型可能对 three.js 代码生成过拟合。一位评论者强调，像创建可玩弹珠游戏这样的简单挑战仍然失败，凸显了代码生成与真正物理推理之间的差距。

**标签**: `#AI`, `#Machine Learning`, `#Benchmarks`, `#Karpathy`, `#3D Generation`

---

<a id="item-3"></a>
## [Kakehashi：实验性用户空间，在 Linux ARM 上运行 macOS 二进制文件](https://github.com/wie-project/kakehashi) ⭐️ 8.0/10

新的开源项目 Kakehashi 旨在 Linux ARM 机器上原生运行 macOS 命令行二进制文件。目前已有 7-Zip、curl 和 Xcode Tools Git 的工作原型，其中 7-Zip 通过了 8k 文件树上的多线程压缩测试，curl 在自动化 Docker 测试中通过了 200 多条命令。 如果成功，Kakehashi 可以在无需完整系统模拟的情况下，为 Linux ARM 生态带来 macOS 二进制兼容性，类似于 WINE/Proton 对 Windows 应用所做的那样。这将惠及依赖 macOS 命令行工具但更喜欢在 ARM 硬件上使用 Linux 的开发者、CI 流水线和用户。 该项目被描述为一个用户空间的 macOS ARM64 到 Linux aarch64 转换层，以 CLI 为主、不使用 JIT。它在 Linux aarch64 上加载 Darwin Mach-O 二进制文件，映射一个独立的 libSystem，并翻译 BSD 系统调用；目前 7-Zip 原型比原生 Linux 执行慢约 5.2 倍，不过作者已经制定了优化计划。

hackernews · vlad_kalinkin · 8月2日 16:26 · [社区讨论](https://news.ycombinator.com/item?id=49145937)

**背景**: Mach-O 是 macOS 使用的原生可执行文件格式，Darwin 是苹果操作系统基于 XNU 内核和 BSD 组件的开源类 Unix 核心。要在 Linux 上运行 macOS 二进制文件，需要处理 Mach-O 格式、提供等效的系统库并翻译系统调用。Kakehashi 是探索这一方向的多个项目之一；例如，Darling 就是一个已有的 macOS 转换层，目前有一个开放的 ARM64 支持 pull request。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/wie-project/kakehashi">GitHub - wie-project/kakehashi: Userspace macOS translation layer for Linux ARM64 · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mach-O">Mach-O - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Darwin_(operating_system)">Darwin (operating system) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上对这个工作原型感兴趣并表示赞赏，其中一人询问 Kakehashi 是否可以与已有开放 ARM64 PR 的 Darling 项目合作。另一位评论者指出该方案仍处于早期阶段，并表示会关注其进展。此外还有人质疑是否可以设计一个以原始二进制为输入的虚拟化框架，也有人抱怨项目名字起得不好。

**标签**: `#macOS`, `#Linux`, `#ARM`, `#binary compatibility`, `#open source`

---

<a id="item-4"></a>
## [OpenAI Astra 模型以每个不到 2000 美元解决十个十年未解数学问题](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 8.0/10

OpenAI 宣布，其下一代主力模型的内部版本 Astra 解决了数学与理论计算机科学中十个至少十年未有进展的开放问题。该公司称，按 GPT-5.6 Sol 的 token 价格计算，每个问题的解决成本不到 2000 美元。 这是前沿 AI 模型能以极低成本产出可审计研究成果的一个惊人示范，可能为以“发现基础设施”为定位的 AI 系统开辟市场。它也加剧了数学界关于 AI 会变革还是冲击这门学科的争论，呼应了陶哲轩提出的“大数学”愿景。 OpenAI 在 openai/ten-proofs 仓库中发布了这些结果的 Lean 4 形式化证明，并附有一篇描述解决方案的论文，以及一份由 LLM 生成的、基于未公开推理轨迹重建证明形成过程的 PDF。该公告没有披露模型尝试过但未能解决的问题数量，也没有公布所使用的提示词。

rss · Simon Willison · 8月1日 20:34

**背景**: OpenAI 称 Astra 是其下一代主力模型的内部版本，但部分公开的 OpenAI 发布材料中并未出现这一名称。成本数字基于 GPT-5.6 Sol，这是 OpenAI 的旗舰 API 档位，定价为每百万输入 token 5 美元、每百万输出 token 30 美元。此前几天，Anthropic 报告其未发布的 Claude Mythos Preview 模型花费约 10 万美元的 token 发现了密码学弱点。数学界的反应从惊叹和“深刻的精神危机”，到陶哲轩更乐观的“大数学”愿景——即人类与 AI 大规模协作开展研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://runtimewire.com/article/openai-astra-ten-open-math-problems">OpenAI says unreleased Astra model solved 10 open... - RuntimeWire</a></li>
<li><a href="https://openrouter.ai/openai/gpt-5.6-sol">GPT-5.6 Sol - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://scalevise.com/resources/openai-public-materials-no-astra-model/">OpenAI Public Materials Do Not List Astra</a></li>

</ul>
</details>

**标签**: `#AI research`, `#OpenAI`, `#mathematics`, `#theoretical computer science`, `#announcement`

---

<a id="item-5"></a>
## [SwiftUI After 7 Years](https://ykvm.com/2026/07/swiftui-a-story-of-mediocrity/) ⭐️ 7.0/10

A critical retrospective on SwiftUI's mediocrity after 7 years, prompting a nuanced community debate on its strengths and limitations compared to UIKit.

hackernews · mpweiher · 8月2日 18:59 · [社区讨论](https://news.ycombinator.com/item?id=49147263)

**标签**: `#SwiftUI`, `#UIKit`, `#Apple`, `#UI Frameworks`, `#Software Engineering`

---

<a id="item-6"></a>
## [英语学习者核心词汇的转变：从人际美德到社会概念](https://pudding.cool/2026/07/essential-words/) ⭐️ 7.0/10

文章分析了 1953 年《通用词汇表》与 2013 年（2026 年更新）《新通用词汇表》之间的变化，显示词汇从“humble”、“loyalty”等人际价值观词汇转向“community”、“identity”、“gender”等抽象社会术语。 这之所以重要，是因为核心词汇表影响着全球数百万英语学习者的学习内容，而这些变化反映了多样性、身份认同和数字通信等更广泛的社会优先事项。理解这些转变有助于教育者和学习者跟上当代语言用法。 新通用词汇表包含 2,809 个词元，而 1953 年的原始词汇表约有 2,000 个词族。分析指出，近四分之一的 1953 年词汇消失，而 2023 年词汇中有 39%是新词；像“apple”、“fork”、“soap”等常见具体名词已从核心词汇中移除。

hackernews · c-oreills · 8月2日 15:41 · [社区讨论](https://news.ycombinator.com/item?id=49145590)

**背景**: 《通用词汇表》（GSL）由 Michael West 于 1953 年出版，是包含约 2,000 个高频词族的基础词汇列表，旨在帮助英语学习者。《新通用词汇表》（NGSL）由 Charles Browne、Brent Culligan 和 Joseph Phillips 于 2013 年发布，并于 2026 年更新，包含从现代语料库中提取的 2,809 个词元。几十年来，这些列表广泛应用于 ESL 教学、教材设计和词汇评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/General_Service_List">General Service List</a></li>
<li><a href="https://en.wikipedia.org/wiki/New_General_Service_List">New General Service List - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者提出了不同观点：一些人认为“正确的”词汇取决于学习者的目标（如旅行、电视或报纸），另一些人则称赞关于从人际美德转向抽象社会概念的观察，认为这反映了不平等的加剧。少数人对“fork”等日常词汇被删除表示困惑，认为新列表可能只是更高级，而非真正反映日常需求。

**标签**: `#linguistics`, `#education`, `#data-analysis`, `#language-learning`, `#society`

---

<a id="item-7"></a>
## [AI 基准测试：画一只长着哈布斯堡下巴的青蛙](https://frogs.vaguespac.es/) ⭐️ 7.0/10

一位 AI 开发者用个人基准测试要求图像生成模型创建一张长着哈布斯堡下巴的青蛙 SVG 图。在线分享的结果显示，即便是顶尖模型也难以将青蛙形态与突出的下颌概念结合起来，其中 Opus 5 被认为最接近通过测试。 这个有趣的基准测试提供了一种快速、可复现的方法来比较不同多模态 AI 系统如何理解复合概念提示。它暴露出当前模型往往能处理好单个元素，却无法将其连贯融合，这对实际设计和插画任务具有重要意义。 该提示要求模型输出有效的 SVG 代码，同时理解'哈布斯堡下巴'这一指代哈布斯堡王朝下颌前突症的术语。值得注意的是，所有被测模型都从正面绘制青蛙，而不是侧面，尽管侧面更能表现下颌的突出。

hackernews · thebigship · 8月2日 19:42 · [社区讨论](https://news.ycombinator.com/item?id=49147622)

**背景**: '哈布斯堡下巴'是下颌前突症的俗称，指下颌明显前突的情况；这在近亲通婚的哈布斯堡王室成员中很常见。SVG（可缩放矢量图形）是一种基于文本的图像格式，AI 模型可以直接将其作为代码生成，因此它成为检验生成系统的便捷、可检查的基准测试。这个基准测试体现了社区驱动的趣味性 AI 评测趋势，通过检验概念理解和视觉推理来补充正式测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Habsburg_jaw">Habsburg jaw</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prognathism">Prognathism - Wikipedia</a></li>
<li><a href="https://www.smithsonianmag.com/smart-news/distinctive-habsburg-jaw-was-likely-result-royal-familys-inbreeding-180973688/">The Distinctive ‘Habsburg Jaw’ Was Likely the Result of the Royal Family’s Inbreeding</a></li>

</ul>
</details>

**社区讨论**: 评论者认为这个测试既搞笑又很有启发性。有用户称赞 Opus 5 是唯一几乎通过的模型，也有人指出失败的模型通常会画一个随机的肿块当作下巴，说明模型'知道'这个概念但无法合理地将其连接到青蛙脸上。还有评论者注意到所有模型都选择了青蛙正面姿势而不是侧面，明明侧面更容易表现下颌；另一位用户提到自己用爆米花物理学做的个人基准，其中 Fable 拒绝执行，其他模型的结果也平平。

**标签**: `#AI`, `#benchmark`, `#SVG`, `#image generation`, `#LLM evaluation`

---

<a id="item-8"></a>
## [微软牵头 235 家公司联名公开信捍卫开放权重 AI 模型](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 7.0/10

2026 年 7 月 24 日，微软牵头发布公开信《开放权重与美国 AI 领导力》，由包括英伟达、亚马逊和 OpenAI 在内的 235 家 AI 公司签署，敦促美国政策制定者不要禁止或限制开放权重模型。随后，Anthropic 发布了自身关于开放权重的立场；7 月 28 日，一封由 1324 名前沿 AI 公司员工签署的名为《Pacing the Frontier》的公开信请求美国政府支持国际社会共同努力，以把控自动化 AI 开发的节奏。 这封联合公开信标志着行业对美国政府可能限制开放权重模型（此举源于安全担忧及与中国模型的竞争）的一次重大反击。其结果将影响美国乃至全球开源 AI、产业竞争以及 AI 安全监管的未来。 值得注意的是，Anthropic 没有签署微软牵头的这封公开信，而是发布了自己的回应；其 CEO Dario Amodei 警告了威权国家滥用模型及“工业规模蒸馏”的风险，同时重申 Anthropic 从未主张禁止开放权重模型。微软的信中明确将蒸馏（用其他模型的输出训练或改进另一个模型）辩护为合法的模型开发技术，以此反驳要求打击蒸馏的呼声。

rss · Simon Willison · 8月2日 04:16

**背景**: 开放权重模型是指公开其训练后参数（即“权重”）的 AI 模型，其他人可以对其进行微调或部署，但由于训练数据通常不公开，这类模型并不完全等同于“开源”AI。随着 DeepSeek、Kimi 等中国开放权重模型受到关注，一些美国官员开始考虑限制其使用，而英伟达、微软、Meta 等公司则警告不要“过早限制”。支持者认为开放权重有助于更广泛的安全研究和竞争，批评者则担心先进能力可能被滥用或扩散。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html">Nvidia, Microsoft, Meta warn against 'premature restrictions' of open-weight models</a></li>
<li><a href="https://www.anthropic.com/news/position-open-weights-models">Our position on open-weights models \ Anthropic</a></li>
<li><a href="https://www.pbs.org/newshour/science/whats-the-difference-between-closed-open‑source-and-open-weight-ai-a-researcher-explains">What's the difference between closed, open‑source and open-weight AI? A researcher explains | PBS News</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#open source`, `#open weights`, `#regulation`, `#Simon Willison`

---

<a id="item-9"></a>
## [Greg Brockman：人们反感同事的 ChatGPT 来请求帮助](https://simonwillison.net/2026/Aug/1/greg-brockman/#atom-everything) ⭐️ 6.0/10

OpenAI 总裁兼联合创始人 Greg Brockman 在 Twitter 上分享，OpenAI 员工将 ChatGPT 接入 Slack 后发现，人们非常反感被同事的 AI 助手联系，即使他们愿意帮助这位同事。他认为这表明人们珍视人际关系，希望 AI 增强而非取代人际互动。 这表明 AI 代理在工作场所面临一个关键的社会障碍：即使底层任务完全相同，人们对 AI 作为中间人的反应也是负面的。这对 AI 助手的设计具有启示意义，特别是在协作工具中部署多代理或主动式 AI 系统时。 Brockman 的观察带有轶事性质，来源于一条 Twitter 帖子，并非正式研究。例子具体涉及 ChatGPT 与 Slack（常见的职场通讯平台）的集成，AI 助手会主动联系同事请求帮助。

rss · Simon Willison · 8月1日 22:29

**背景**: Greg Brockman 是 OpenAI 的总裁兼联合创始人，OpenAI 是 ChatGPT 的开发商。ChatGPT 是一种对话式 AI 系统，可以集成到 Slack 等职场工具中协助完成任务，包括主动联系同事。更广泛地说，这句话涉及到日益普及的‘AI 代理’——不仅响应提示，还能主动采取行动的软件——以及它们如何与组织中的社会规范相互作用。

**标签**: `#AI ethics`, `#OpenAI`, `#generative AI`, `#workplace`, `#human-AI interaction`

---