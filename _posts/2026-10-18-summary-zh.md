---
layout: default
title: "Horizon Summary: 2026-10-18 (ZH)"
date: 2026-10-18
lang: zh
---

> 从 15 条内容中筛选出 7 条重要资讯。

---

1. [DeepSeek 发布 V4.1-Flash-1017，代码基准成绩大幅提升](#item-1) ⭐️ 9.0/10
2. [Pele 将 Mermaid 图表渲染为可用 CSS 变量主题化的 SVG](#item-2) ⭐️ 7.0/10
3. [爱沙尼亚网络投票系统源代码在 GitHub 公开](#item-3) ⭐️ 7.0/10
4. [博客从联想记忆的第一性原理推导出 Transformer](#item-4) ⭐️ 7.0/10
5. [全球太阳能发电量首次超过核电](#item-5) ⭐️ 7.0/10
6. [白化珊瑚接触健康邻居后数天内恢复颜色](#item-6) ⭐️ 6.0/10
7. [博主用多力多滋粉末把鸡胸肉变透明](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [DeepSeek 发布 V4.1-Flash-1017，代码基准成绩大幅提升](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) ⭐️ 9.0/10

10 月 17 日，DeepSeek 发布了 DeepSeek-V4.1-Flash-1017，这是对 V4.1-Flash 的一次更新，官方称其为一次“小幅更新”，但在推理、编码和智能体任务上带来了“实质性提升”。该模型现已上线 DeepSeek 官网、App 和 API，同时也出现在 OpenRouter 与 Ollama 云端模型库中。 这次发布加剧了开放模型与闭源前沿模型之间的竞争：据社区转述，新版本在 DeepSeek 官方新闻页展示的 11 项编码基准中有 10 项超过了 Sol 5.6。对于构建编码智能体的开发者而言，在各大闭源厂商将最强模型收紧于更严格条款之下的同时，它提供了又一个高吞吐、相对低成本的选择。 DeepSeek 将此次更新描述为帕累托改进——在基准成绩更强的同时，任务完成速度更快、输出比上一版更短。根据 Ollama 的模型说明，V4.1-Flash 是一个多模态混合专家（MoE）模型，主干参数规模为 552B，支持最长一百万 token 的上下文；在 OpenRouter 上以 deepseek-flash 这一 API 模型名提供服务，对应 2026 年 10 月 17 日的快照版本。

hackernews · theykk · 10月17日 08:21 · [社区讨论](https://news.ycombinator.com/item?id=50129045)

**背景**: DeepSeek 是一家中国 AI 实验室，以较低价格提供能力较强的模型而闻名，V4.1-Flash 属于其更快、更便宜的产品线，而非旗舰型号。“Flash”系列采用混合专家（MoE）架构，即每次生成 token 时只激活大参数量中的一小部分，从而压低推理成本。开发者通常通过 DeepSeek 自有 API，或通过 OpenRouter 这类聚合平台访问此类模型——后者用一个 API Key 和统一计费即可调用数百个模型。基准测试在此尤为关键，因为编码与智能体工作流（模型读取代码仓库、规划修改并直接编辑文件）目前是前沿大模型最主要的商业需求来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://api-docs.deepseek.com/news/news261017/">DeepSeek - V 4 . 1 - Flash - 1017 : Wish-Driven Programming Made Real</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4.1-flash-1017">DeepSeek V 4 . 1 Flash 1017 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://ollama.com/library/deepseek-v4.1-flash:1017-cloud">deepseek - v 4 . 1 - flash : 1017 -cloud</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的反应总体热烈，但对实际效果存在分歧：多位评论者称赞 DeepSeek 的吞吐量和较低的首次 token 延迟，以及可查看思维链（CoT）、不会被不明原因的安全审查拦截的开放性，认为这让它在“体感”上优于基准领先的对手。也有人用具体测试反驳——一位用户用 200 多个文件的 C++ 游戏引擎改动做代码审查，发现 DeepSeek 花了约 20 分钟才找出一个相关的 P1 问题，而 GPT-5.6/6.1 Sol 只需约 4 至 5 分钟。另一个反复出现的主题是生态多样性，有评论者认为正是这样的模型才让现有厂商想要设置监管门槛。

**标签**: `#DeepSeek`, `#LLM release`, `#AI benchmarks`, `#open models`, `#coding agents`

---

<a id="item-2"></a>
## [Pele 将 Mermaid 图表渲染为可用 CSS 变量主题化的 SVG](https://pele.run/) ⭐️ 7.0/10

Pele 是一个新的轻量级开源库，托管在 Obsidian 的 GitHub 组织下（github.com/obsidianmd/pele），它能把 Mermaid 图表渲染成 SVG，并通过 CSS 变量而不是硬编码颜色来设定样式。它以一个可嵌入的小型渲染器形式发布，并在 pele.run 提供了自己的演练场，目标场景是让生成的图表能够跟随宿主应用的主题变化。 Mermaid 已经成为文档、Wiki 和 Obsidian 等笔记工具中事实上的文本转图表格式，但其默认渲染链路较重，样式覆盖也很麻烦。如果 Pele 能在不依赖完整浏览器或无头浏览器的情况下生成可主题化的 SVG，那么把 Mermaid 渲染嵌入 Web 应用、静态站点生成器和编辑器就会容易得多，尤其是那些需要图表与自身设计系统保持一致的项目。 Pele 定位为一个轻量级库，用 CSS 变量为图表设定主题，这也是其输出能适配明暗模式和品牌配色的关键。发布后评论区有人追问官方 Mermaid 库是否仍然需要完整浏览器或无头浏览器才能完成 SVG 布局——这正是 Pele 宣称优势的核心所在；还有评论者指出，发布时 Pele 演练场里的 Mermaid 预览是坏的。

hackernews · dchest · 10月17日 15:55 · [社区讨论](https://news.ycombinator.com/item?id=50132193)

**背景**: Mermaid 是由 Knut Sveidqvist 于 2014 年创建的开源 JavaScript 图表工具，可以用纯文本语法生成流程图、时序图、甘特图等图表，因此迅速在以 Markdown 为基础的文档和笔记工具中流行开来。传统 Mermaid 渲染依赖与浏览器环境紧密耦合的布局代码，所以在服务端或非浏览器环境中嵌入时往往要跑一个无头浏览器。可主题化 SVG 指的是颜色和样式由外部 CSS（通常是自定义属性）驱动的 SVG，这样同一个生成文件无需重新生成就能适配不同主题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pele.run/">Pele · Mermaid diagrams as themeable SVG</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mermaid_(software)">Mermaid (software) - Wikipedia</a></li>
<li><a href="https://iconvectors.io/tutorials/make-your-svg-icons-themeable-with-css.html">Themeable SVG Icons: currentColor, Dark Mode — IconVectors</a></li>

</ul>
</details>

**社区讨论**: 评论者总体很感兴趣，但提出了两个实质性问题：一位用户表示，只要图表比玩具示例复杂一点，Mermaid 的布局引擎就会变得“晦涩且拓扑结构糟糕”，相比之下样式只是小问题；另一位则追问官方 Mermaid 库是否仍需要完整浏览器或无头浏览器，如果确实如此，Pele 就很有价值。还有人询问 Pele 是否开源（随后找到了 Obsidian 的 GitHub 仓库）、反馈演练场中的 Mermaid 预览无法正常显示，并指出“pele”在拉脱维亚语中是“老鼠”的意思。

**标签**: `#mermaid`, `#svg`, `#diagrams`, `#open-source`, `#obsidian`

---

<a id="item-3"></a>
## [爱沙尼亚网络投票系统源代码在 GitHub 公开](https://github.com/valimised/ivxv) ⭐️ 7.0/10

爱沙尼亚全国选举所使用的网络投票系统 IVXV 的完整源代码，现已在 GitHub 的 valimised/ivxv 仓库中公开。该仓库并不用于日常开发，而是会持续保持更新，以确保公开的代码与实际选举中部署的代码一致。 爱沙尼亚是全球第一个将具有约束力的全国性网络投票投入实际使用的国家，因此公开完整代码可以让独立研究人员和公民审计这套决定整个国家选举结果的系统。这也让一个更广泛的争论更加尖锐：电子投票究竟能否做到可验证，还是最终仍要依赖制度信任。 IVXV 通过重加密混网（re-encryption mix-net）对加密选票进行匿名化处理，选民可以任意多次重新投票，且只有最后一次投票会被计入。包括 2025 年 IACR ePrint 上对 2023 至 2025 年间漏洞与修复的系统性梳理在内的学术分析指出，个体可验证性仍是一项实际挑战，并研究了在此混网设计中加入选票正确性零知识证明的可行性。

hackernews · theanonymousone · 10月17日 03:18 · [社区讨论](https://news.ycombinator.com/item?id=50127586)

**背景**: 爱沙尼亚于 2005 年地方选举中引入网络投票（i-voting），并在 2007 年议会选举中首次使用；IVXV 则是自 2017 年地方选举起部署的版本。由于网络投票发生在受控投票站之外，该系统依赖加密选票，以及由国家选举委员会监督的公开计票流程。在电子投票研究中，端到端可验证性被分为个体可验证性（选民可核验自己的选票被收录）与普遍可验证性（任何人都能核验所有选票被正确计票）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/valimised/ivxv">GitHub - valimised/ivxv: IVXV online voting system · GitHub</a></li>
<li><a href="https://eprint.iacr.org/2025/506">On the Estonian Internet Voting System, IVXV, SoK and Suggestions</a></li>
<li><a href="https://en.wikipedia.org/wiki/End-to-end_verifiable_voting">End-to-end verifiable voting</a></li>

</ul>
</details>

**社区讨论**: 评论者在技术怀疑与现实经验之间分化：有人主张仅靠软件乃至软硬件组合都无法保证选举安全，援引“信任信任”（Trusting Trust）问题，并呼吁在投票结束后的第一时间进行人工统计抽样审计；而爱沙尼亚居民则回应说电子投票已被广泛接受，其开源性质早已为人所知并广受认可。一位爱沙尼亚评论者坦言心情复杂，认为在对政府的信任尚存时系统运行良好，但担心信任崩塌的那一天；也有人指出 ElectionGuard 自 2020 年起已在多场美国真实选举中使用，瑞士同样将其电子投票软件开源。

**标签**: `#e-voting`, `#election-security`, `#open-source`, `#cryptography`, `#Estonia`

---

<a id="item-4"></a>
## [博客从联想记忆的第一性原理推导出 Transformer](https://alexwang.ai/posts/associative-memory/) ⭐️ 7.0/10

Alex Wang 在 alexwang.ai 上发表了一篇博客，从经典的联想记忆出发，把注意力视为对已存储键值对的记忆检索操作，一步步重建出 Transformer 架构。该文在 Hacker News 上引发热烈讨论，约获得 495 分和 116 条评论，既有人称赞其教学价值，也有人质疑其简化假设。 Transformer 的直觉通常是从《Attention Is All You Need》论文自上而下讲授的，因此自下而上的推导让这套架构显得顺理成章而非凭空设计，从而降低了学习门槛。它还强化了能量型联想记忆模型与现代注意力机制之间的深层联系，而这一联系已成为颇有成果的研究方向。 该推导假设键是随机单位向量，这使分析变得可处理，但所建模的更接近白噪声而非现实中的结构化数据；文章本身也承认这一分析并不精确。作者还在 X 上发布了一个精简的摘要帖，供希望快速浏览的读者参考。

hackernews · speckx · 10月16日 19:01 · [社区讨论](https://news.ycombinator.com/item?id=50122878)

**背景**: 联想记忆是一个经典概念：网络可以存储若干模式，之后凭部分或带噪声的线索检索出完整记忆，Hopfield 网络是其典型代表。2020 年的论文《Hopfield Networks is All You Need》表明，现代连续 Hopfield 网络的更新规则在数学上等价于 Transformer 中的自注意力机制——每个 token 会去查询一组已存储的键值对。这篇文章反向搭建这座桥梁，把注意力推导为存储与回忆联想关系的自然解法，而不是假定读者已经了解 Transformer 是什么。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ml-jku.github.io/hopfield-layers/">Hopfield Networks is All You Need | hopfield -layers</a></li>
<li><a href="https://courses.cit.cornell.edu/bionb330/readings/Associative+Memories.pdf">Neural Associative Memories</a></li>
<li><a href="https://poloclub.github.io/transformer-explainer/">Transformer Explainer: LLM Transformer Model Visually Explained</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上对文章的教学价值表示赞赏，但 zmmmmm 对随机单位向量的假设提出异议，认为真实数据具有结构，可以实现更高的存储效率，因此文章结论应被理解为上下界而非真实估计。也有人希望文章给出更具体的例子，例如存储美国 50 个州的首府；一位评论者打趣说文章应定义成为“你”的门槛条件，另一位则指出这个问题可追溯到 Ranulph Glanville 1978 年关于记忆的论述。作者本人也参与了讨论，并附上了简短摘要链接。

**标签**: `#transformers`, `#associative-memory`, `#machine-learning`, `#technical-explainer`, `#deep-learning`

---

<a id="item-5"></a>
## [全球太阳能发电量首次超过核电](https://www.pv-magazine.com/2026/09/29/solar-surpasses-nuclear-power-globally-for-first-time/) ⭐️ 7.0/10

根据截至 2026 年中的数据，全球太阳能光伏发电量在实际发电太瓦时上首次超过核电，这是太阳能首次在发电量而非仅装机容量上领先。从 2025 年 3 月到 2026 年 6 月，太阳能或风能每个月都分别有其一超过核电发电量，而在 2026 年 3 月、4 月和 5 月，两者更是各自独立地超过了核电。 这一交叉具有象征意义，说明电力结构正在快速转变：太阳能装机容量同比增长 27%，而核电装机几乎停滞，这意味着可再生能源已在绝对发电量上开始取代现有的低碳电源，而不仅仅是在满足新增需求。这也表明风能紧随其后，太阳能与风能正在共同改写电网规划者、公用事业公司和能源政策制定者长期依赖的基本假设。 全球太阳能装机容量增加 510 GW，达到 2,383 GW（同比增长 27%）；风能新增创纪录的 159 GW，达到 1,291 GW（增长 14%）；相比之下，核电装机容量仅增加 1.5 GW 至 399.5 GW，且运行中的核电容量还下降了 0.5 GW。尽管核电的容量系数远高于太阳能，但太阳能仍取得领先，因为其装机规模约为核电的六倍，而且增长速度仍快得多。

hackernews · xbmcuser · 10月17日 14:01 · [社区讨论](https://news.ycombinator.com/item?id=50131256)

**背景**: 容量系数是指实际发电量与机组满负荷运行所能发出电量之比；核电站通常有 90%以上的时间在运行，而太阳能电站在有阳光时才能满功率发电，因此每吉瓦太阳能每年产生的太瓦时远少于每吉瓦核电。这正是太阳能多年前就在装机容量上超过核电、却直到现在才在发电量上实现超越的原因。该里程碑以实际发电量（太瓦时）衡量，相比铭牌装机容量，这一指标对排放和电网结构更有意义。

**社区讨论**: 评论者以理性而非炒作的热情看待这一消息：有人指出尽管核电容量系数更高，这一比较仍是以实际太瓦时衡量的，并认为水力发电是几年后的下一个里程碑；也有人惋惜核电数十年的停滞使世界损失了进度。讨论中反复出现的主题是任务远未完成——清洁发电还需进一步扩大规模，不仅要取代肮脏的电力，还要取代作为化工原料的碳氢化合物，而电解与合成在这方面的能效仍然极低。

**标签**: `#solar energy`, `#nuclear power`, `#energy transition`, `#renewables`, `#climate tech`

---

<a id="item-6"></a>
## [白化珊瑚接触健康邻居后数天内恢复颜色](https://www.nature.com/articles/d41586-026-03266-x) ⭐️ 6.0/10

《Nature》报道称，白化珊瑚在与健康的邻近珊瑚发生物理接触后，能在数天内重新获得共生藻，从而恢复颜色。报道涉及的实验使用的是来自同一遗传个体的珊瑚碎片，也就是说恢复的珊瑚实际上是克隆体。 这一发现表明，珊瑚从白化中恢复可能比此前认为的更快，并且更依赖与健康珊瑚的接触，这可能为珊瑚修复和培育实践提供参考。但由于目前只在遗传上相同的碎片之间观察到该效应，它对野生、遗传多样的珊瑚礁以及大规模白化事件的意义仍不确定。 恢复现象是在来自同一基因型（即遗传上相同的珊瑚群体）的碎片之间观察到的，这限制了该结果直接应用于野外遗传不同的珊瑚的程度。目前也尚不清楚这种基于接触的恢复能否在珊瑚礁尺度上重现，尤其是在大规模白化导致附近几乎没有健康邻居的情况下。

hackernews · alkyon · 10月16日 23:38 · [社区讨论](https://news.ycombinator.com/item?id=50126253)

**背景**: 珊瑚是与被称为虫黄藻（zooxanthellae）的光合单细胞藻类共生的动物，这些藻类为珊瑚提供能量，并赋予珊瑚大部分颜色。白化发生在珊瑚排出这些藻类时，通常由热应激引起；白化珊瑚处于应激状态，但不一定已经死亡。适应性白化假说（Adaptive Bleaching Hypothesis）认为，珊瑚可能失去一种共生藻，并获得一种更适合变化后环境的共生藻，尽管白化仍是一种可能导致死亡的高风险策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zooxanthellae">Zooxanthellae - Wikipedia</a></li>
<li><a href="https://oceanservice.noaa.gov/education/tutorial_corals/coral02_zooxanthellae.html">Corals Tutorial: What is Zooxanthellae? - NOAA's National ...</a></li>
<li><a href="https://www.journals.uchicago.edu/doi/full/10.2307/1543084">The Adaptive Bleaching Hypothesis: Experimental Tests of ...</a></li>

</ul>
</details>

**社区讨论**: HN 评论者普遍认为这一结果有趣但实际意义有限：他们解释了虫黄藻共生和适应性白化假说，同时指出该效应只在遗传上相同的碎片中观察到，在野外很难规模化。一位大堡礁潜水员补充说，大规模白化事件常常导致大片区域没有健康邻居，其他人则认为珊瑚培育者和水族爱好者可能早已熟悉快速恢复现象。

**标签**: `#biology`, `#marine science`, `#coral bleaching`, `#symbiosis`, `#science news`

---

<a id="item-7"></a>
## [博主用多力多滋粉末把鸡胸肉变透明](https://chillphysicsenjoyer.substack.com/p/making-chicken-transparent-using) ⭐️ 6.0/10

Substack 博客“Chill Physics Enjoyer”上的一篇 DIY 实验显示，把生鸡胸肉切成薄片后浸泡在用多力多滋（Doritos）粉末调制的腌料中，肉片会明显变得透明；这种粉末富含黄色食用色素酒石黄（tartrazine）。作者推测，含染料溶液提高了肉内液体的折射率，使其接近组织蛋白的折射率，从而抑制了光的散射。 这个实验是在厨房餐桌上演示了折射率匹配这一原理，而它正是神经科学和生物医学成像中组织透明化技术的核心；与此同时，研究人员正在积极发表关于用酒石黄配制折射率液体以增强光在散射介质中穿透深度的工作。它说明一种常见的消费级产品至少能在定性层面复现实验室里用甘油、去垢剂或水凝胶等透明化试剂所达到的光学效果。 最终结果只是部分半透明，而非真正的光学透明；文中也提到把生鸡肉切得足够薄、足够均匀本身就很困难，会直接影响效果。评论者建议先轻微冷冻再切片，并在样品与网格图案之间以及表面加水，甚至把整个实验放在水下进行，以降低表面粗糙度——即便体相折射率匹配成功，表面粗糙仍是散射的主要来源。

hackernews · crescit_eundo · 10月17日 13:55 · [社区讨论](https://news.ycombinator.com/item?id=50131213)

**背景**: 生物组织之所以看起来浑浊，是因为其中充满了脂质、蛋白质和水等折射率不同的物质之间的微小界面，光每穿过一个界面就会发生散射。组织透明化的目标是让整个样品的折射率趋于均匀，常见做法是去除脂质，并用折射率与剩余蛋白质接近的试剂替换组织间液，这也是透明化后的器官能够变得通透的原因。鸡胸肉是光学研究中常用的测试组织，此前已有研究用 75% 甘油浸泡来提高光在其中的穿透深度；折射率匹配液在光学中也是连接透镜和光纤的标准材料，而近期已有工作专门研究酒石黄等食用色素在这方面的用途。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://link.springer.com/article/10.1557/s43579-025-00729-6">Designing refractive index fluids of food dye for light ...</a></li>
<li><a href="https://scienceinsights.org/a-step-by-step-overview-of-a-tissue-clearing-protocol/">A Step-by-Step Overview of a Tissue Clearing Protocol</a></li>
<li><a href="https://www.nature.com/articles/s41598-023-48876-x">Multimodal optical clearing to minimize light attenuation in ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（244 分、64 条评论）气氛热烈且非常实用：有人开玩笑说这项发现大概源自某人想做多力多滋口味鸡肉的尝试，也有人给出实操建议，比如把肉稍微冷冻以便切出更平整的薄片，以及用水来改善表面粗糙度。一条值得注意的更正指出，欧洲和英国销售的多力多滋并不含酒石黄，而且欧盟规定含该色素的产品必须标注“可能对儿童的活动和注意力产生不良影响”的警示语。

**标签**: `#optics`, `#food science`, `#DIY experiment`, `#tissue clearing`, `#Hacker News`

---