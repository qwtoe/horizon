---
layout: default
title: "Horizon Summary: 2026-08-17 (ZH)"
date: 2026-08-17
lang: zh
---

> 从 17 条内容中筛选出 9 条重要资讯。

---

1. [Anthropic 公开 Claude 系统提示词](#item-1) ⭐️ 8.0/10
2. [AI 模型正故意变笨：从记忆转向外部工具](#item-2) ⭐️ 8.0/10
3. [Qwen 3.8 27B 表现出色，但默认过度思考](#item-3) ⭐️ 8.0/10
4. [嵌入式工程师为 RISC-V 在发展中世界的价值辩护](#item-4) ⭐️ 7.0/10
5. [AI 额度转售经济：代币经纪人与风险](#item-5) ⭐️ 7.0/10
6. [英伟达缩减对 OpenAI 数据中心融资的担保规模](#item-6) ⭐️ 7.0/10
7. [达里奥·阿莫代伊：AI 不信任反映更深层制度信任危机](#item-7) ⭐️ 7.0/10
8. [Buf 推出 Protobuf 语言服务器支持](#item-8) ⭐️ 6.0/10
9. [CORS Chat：浏览器中测试 OpenAI-Responses 端点的工具](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic 公开 Claude 系统提示词](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic 已在官方文档平台公开发布了其 Claude 模型所使用的系统提示词。这一发布使任何人都能查看影响 Claude 各版本行为的系统级指令。 这是领先 AI 公司在透明度方面的一项显著举措，使外部研究人员、开发者和用户能够分析 Claude 如何被引导。这可能会提高行业的披露标准，并促进对模型对齐和决策的更深入研究。 发布的提示词相当冗长，社区分析显示其中包含具体指令，比如告诉 Claude 即使使用者暗示有图片上传，也要自行确认图片是否真实存在。Simon Willison 还构建了这些提示词的 git 提交历史，揭示了版本间的变化以及 Claude Fable 5 和 Claude Mythos 5 等未发布模型的引用。

hackernews · tosh · 8月16日 12:48 · [社区讨论](https://news.ycombinator.com/item?id=49319556)

**背景**: 系统提示词（system prompt）是在用户查询之前发送给大语言模型的预定义指令，用于设定模型的角色、行为、语气和约束条件。Claude 是 Anthropic 推出的 AI 助手，面向分析、编程和问题解决等任务。公开这些提示词，使通常隐藏在模型响应背后的指令可供公众检视。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://promptengineering.org/system-prompts-in-large-language-models/">System Prompts in Large Language Models</a></li>
<li><a href="https://www.pluralsight.com/resources/blog/ai-and-data/what-is-claude-ai">What is Claude AI ? Anthropic 's LLM vs ChatGPT | Pluralsight</a></li>

</ul>
</details>

**社区讨论**: 社区成员的反应有褒有贬。Simon Willison 分享了一个追踪提示词变化的 git 仓库，并指出其中出现了 Claude Fable 5 等未来模型名称。其他人质疑为什么提示词如此冗长，认为更短的指令往往效果更好；另有评论担忧版主疑似删除对 AI 持负面态度的文章。

**标签**: `#AI`, `#Claude`, `#system prompts`, `#transparency`, `#LLM`

---

<a id="item-2"></a>
## [AI 模型正故意变笨：从记忆转向外部工具](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) ⭐️ 8.0/10

文章指出，AI 模型正有意降低对权重中存储事实的依赖，转而将知识外包给检索系统和外部工具。这标志着设计方向从记忆密集型模型转向以灵活性换取原始召回能力的系统。 这一趋势可能重塑模型的训练、评估和部署方式，尤其是当检索增强生成和工具使用成为标配后。如果模型变成可插拔知识的推理引擎，幻觉问题可能减少，用户也无需重新训练即可组合不同知识模块。 文章引用了不允许使用工具的纯事实召回基准 SimpleQA，其中 Gemini 2.5 Pro 得分 53%，并预测未来模型卡可能不再标注知识截止日期。评论者指出文章可能过时，并提及更新的模型以及 Cactus 推出的 14 MB 工具调用 LLM Needle。

hackernews · hruvhwe · 8月16日 19:04 · [社区讨论](https://news.ycombinator.com/item?id=49322695)

**背景**: 检索增强生成（RAG）是一种让 LLM 先从外部数据源检索相关文档、再生成回答的技术，从而能够使用最新或特定领域的信息。工具使用则允许模型调用外部函数和 API，而不必完全依靠记忆作答。文章基于这一趋势提出：模型权重不再是事实的主要载体，这有望缓解幻觉问题，即 LLM 会自信地编造错误信息的倾向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://aws.amazon.com/what-is/retrieval-augmented-generation/">What is RAG? - Retrieval-Augmented Generation AI Explained - AWS</a></li>

</ul>
</details>

**社区讨论**: 评论者大多围绕这一前提展开讨论：kennywinker 设想了可插拔知识库，以便模块化组合技能；COAGULOPATH 则批评文章过时，指出 SimpleQA 长期未更新、Gemini 2.5 Pro 已经发布十六个月。msdz 分享了 Cactus 的 Needle 等更多案例，pulkitsh1234 则质疑推理与事实能否真正分离，因为要推理人类行为，往往必须依赖历史事实。

**标签**: `#AI`, `#LLM`, `#Retrieval`, `#Model Architecture`, `#Machine Learning`

---

<a id="item-3"></a>
## [Qwen 3.8 27B 表现出色，但默认过度思考](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 8.0/10

阿里巴巴 Qwen 团队于周五发布了 Qwen 3.8 27B，这是一款采用 Apache 2.0 许可的 27B 参数视觉语言模型。Simon Willison 的评测发现该模型带来了显著的基准提升，但默认采用 'xhigh' 推理强度，导致即使面对简单提示也会进行惊人的过度思考。 27B 参数规模非常适合在笔记本电脑上本地运行模型，且宽松的许可协议让先进的视觉语言能力得以广泛使用。默认的过度思考行为是一个重大的可用性缺陷，会显著增加延迟和计算成本，尤其在消费级硬件上。 Willison 在 128GB M5 Max MacBook Pro 和 NVIDIA DGX Spark 上通过 LM Studio 运行了 17GB 的 Q4_K_M 量化版本。一个简单的 SVG 提示词消耗了 22,276 个推理 token，用时 21 分钟才生成 3,223 个输出 token；LM Studio 默认的 8,192 token 上下文限制很快被耗尽，直到他将上下文提升到完整的 262,144 token。

rss · Simon Willison · 8月16日 22:00

**背景**: 视觉语言模型（VLM）能够同时理解和生成来自图像与文本的信息，扩展了纯文本大语言模型（LLM）的能力。模型参数是训练过程中学到的内部权重，用于捕捉语言规律；27B 参数属于中等规模，在能力与本地硬件可行性之间取得了平衡。Apache 2.0 许可证是一种宽松的开源许可，允许自由使用、修改和分发，这也是此次发布对开源 AI 社区意义重大的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_License">Apache License - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vision-language_model">Vision-language model - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/llm-parameters">What are LLM parameters? - IBM</a></li>

</ul>
</details>

**标签**: `#Qwen`, `#LLM`, `#open-source`, `#AI`, `#model release`

---

<a id="item-4"></a>
## [嵌入式工程师为 RISC-V 在发展中世界的价值辩护](https://rvembedded.com/blog_post/12/) ⭐️ 7.0/10

在一篇新的博文中，一位来自发展中国家的嵌入式工程师回应了对 RISC-V 的批评，认为其开放、免许可费的架构为西方市场以外的嵌入式开发带来了显著的成本和可及性优势。该文章用可负担性和可获得性来反驳以性能为中心的批评。 这一视角将 RISC-V 的讨论从性能基准扩展到新兴市场的经济现实，在这些市场中，价格和可获得性可能比纯粹性能更重要。它挑战了“RISC-V 必须在性能上击败 ARM 或 x86 才有意义”的假设。 作者指出，运送一美元的芯片可能需要 60 到 200 美元，因此 10 美分与 1 美元零件之间的差价并非无关紧要。然而，评论者指出一个明显的矛盾：作者一边声称 RISC-V 芯片能以 10 美分一片运抵他的国家，一边又描述到其所在国的运费高昂。

hackernews · Narishma · 8月16日 17:01 · [社区讨论](https://news.ycombinator.com/item?id=49321717)

**背景**: RISC-V 是一种基于 RISC 原则的免费开放标准指令集架构（ISA），2010 年起源于加州大学伯克利分校，现由 RISC-V 国际协会维护。与 x86 和 ARM 等专有 ISA 不同，RISC-V 允许免版税实施，因此在微控制器和嵌入式系统中特别有吸引力。开放的规范还使世界各地（包括发展中国家）的公司和爱好者能够在不支付许可费的情况下设计和制造芯片，从而降低开发和采购成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V">RISC-V</a></li>
<li><a href="https://riscv.org/">Home - RISC-V International</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上欣赏作者的发展中国家视角，但也提出了逻辑上的质疑。一些人指出，该文章谈到的是嵌入式领域的优势，而没有直接回应原批评中关于 RISC-V 性能和 ISA 碎片化的问题。另一些人指出了作者描述的高昂运费与他声称 10 美分零件能运抵其所在国之间的矛盾。还有评论者以历史为例，提到 x86 最终在性能上超越更昂贵的工作站 CPU。

**标签**: `#RISC-V`, `#embedded systems`, `#hardware`, `#cost analysis`, `#community discussion`

---

<a id="item-5"></a>
## [AI 额度转售经济：代币经纪人与风险](https://vectoral.com/blog/who-are-the-token-brokers) ⭐️ 7.0/10

这篇文章探讨了新兴的 AI 额度（credit）二级转售市场，包括代币经纪人（token broker）的角色、滥用模式以及相关安全风险。文章指出，用户正在交易未使用的 API 额度或订阅权益，这通常违反了平台的服务条款。 这一灰色市场给 AI 平台的经济模式和安全性带来了重大挑战。它可能导致账户被盗用、凭证滥用以及 OpenAI 等提供商的收入流失，同时使买家面临欺诈和数据隐私风险。 文章提到了具体的滥用模式，如账户自动化注册、转售 B2B 合作伙伴的员工福利以及被黑客攻击的账户。文章还指出，通过中继（relay）购买时难以验证用户实际获得的是哪个模型，并提到 linux.do 和 nodeseek.com 等平台上存在蓬勃发展的代币转售生态。

hackernews · mlenhard · 8月16日 14:44 · [社区讨论](https://news.ycombinator.com/item?id=49320611)

**背景**: AI 额度是 AI 服务提供商授予的按使用量计算的配额，通常以免费试用额度或包含在订阅计划中的形式发放。目前已经出现了一个二级市场，经纪商以折扣价汇集并转售这些额度，类似于航空公司和酒店中常见的忠诚度积分套利。这些做法违反了大多数平台的服务条款，提供商通常会尝试通过 IP 追踪和账户标记来检测并阻止此类活动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aicredits.co/en/ai/buy-discounted-ai-credits">Buy Discounted AI Credits: Save Up to 60% in 2026 | AI Credits</a></li>
<li><a href="https://www.aicredits.co/en/blogs/sell-unused-ai-credits">How to Sell Unused AI Credits Before They Expire | AI Credits</a></li>
<li><a href="https://www.verisoul.ai/industries/saas-ai-tech">Verisoul</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍将转售市场视为一种可预见的滥用模式，并将其与存在了几十年的忠诚度账户灰色市场相比较。有评论者警告说，信任一个没有信誉的第三方经纪人无异于招致黑客攻击和数据泄露，即使打了 99%的折扣也不划算。另一位评论者认为文章研究过于肤浅，指出 linux.do 和 nodeseek.com 上的代币转售经济远为庞大；还有评论者提出一个实际问题：如何验证购买到的模型确实是实际使用的模型。

**标签**: `#AI`, `#economics`, `#security`, `#gray market`

---

<a id="item-6"></a>
## [英伟达缩减对 OpenAI 数据中心融资的担保规模](https://www.reuters.com/business/nvidia-scales-back-250-billion-openai-data-center-guarantee-wsj-reports-2026-08-14/) ⭐️ 7.0/10

据路透社报道，英伟达大幅缩减了其可能为 OpenAI 基础设施融资提供的担保金额，较此前报道的 250 亿美元数据中心担保规模明显下降。此举发生在双方据称推进一座总造价可能高达 5000 亿美元的园区项目之际。 这一动向意义重大，因为它表明市场对支撑大规模 AI 数据中心投资的金融工程信心减弱，可能使 OpenAI 更难为算力扩张获得低成本资金。同时，它也凸显了 AI 硬件供应商与其最大客户之间日益加深的金融捆绑风险。 据报道，缩减后的担保与一个总建设成本可能达到 5000 亿美元的数据中心园区项目相关；评论者指出，该交易从未正式签署，并涉及大规模的天然气发电配套设施。怀疑者认为，即使担保规模降低，这种融资结构本质上仍是循环的，且未经市场充分检验。

hackernews · root-parent · 8月16日 21:07 · [社区讨论](https://news.ycombinator.com/item?id=49323686)

**背景**: 英伟达是 AI 训练 GPU 市场的主导供应商，OpenAI 是其最大的客户之一。为帮助 OpenAI 承担高昂的数据中心和电力成本，英伟达据称曾考虑为债务融资提供担保，实际上将硬件销售与长期资本市场押注绑定。这种由供应商支持的融资方式在科技行业并不常见，并可能带来金融稳定方面的更广泛影响。

**社区讨论**: 评论区总体持怀疑态度：有人调侃英伟达正在变成一家顺带设计芯片的储蓄贷款公司；也有人认为，即使担保出现部分减记，通过折价转售算力仍可能让交易保持盈利。多位评论者警告循环融资和“虚假利润”的风险，另有人认为英伟达的真实意图是让 GPU 成为一种由更广泛融资市场支持的可交易资产类别。

**标签**: `#Nvidia`, `#OpenAI`, `#AI infrastructure`, `#data centers`, `#financing`

---

<a id="item-7"></a>
## [达里奥·阿莫代伊：AI 不信任反映更深层制度信任危机](https://simonwillison.net/2026/Aug/16/dario-amodei/) ⭐️ 7.0/10

Anthropic CEO 达里奥·阿莫代伊表示，公众对 AI 的不信任主要源于对机构整体的信任危机，而非 AI 领袖对风险的警告。他认为，Anthropic 应该通过真正实现“治愈癌症”这类具体成果来重建信任，而不是靠光鲜的营销宣传。 作为顶级 AI 公司高管，阿莫代伊的观点将有关 AI 抵制的讨论从“如何宣传”转向“如何兑现成果”，可能影响 AI 企业在怀疑情绪高涨时如何应对公众沟通、问责和政策讨论。 阿莫代伊特别批评了“AI 将治愈癌症”这种陈词滥调，认为大多数人觉得它带有欺骗性而非激励性。他承认对包括 Anthropic 在内的 AI 公司最准确的批评是：它们尚未兑现造福世界的重大承诺。

rss · Simon Willison · 8月16日 15:05

**背景**: 达里奥·阿莫代伊是 AI 公司 Anthropic 的 CEO，该公司开发了 Claude AI 助手。近年来，AI 领袖多次对高级 AI 可能带来的生存风险发出警告，而监管机构和公众对这项技术的怀疑日益加深。阿莫代伊认为，这种怀疑是几十年来公众对公司、政府和科技行业信任长期下降的一部分，只有实实在在的积极成果才能修复信任。

**标签**: `#AI`, `#Public Trust`, `#Anthropic`, `#AI Risk`, `#Policy`

---

<a id="item-8"></a>
## [Buf 推出 Protobuf 语言服务器支持](https://buf.build/blog/protobuf-lsp) ⭐️ 6.0/10

Buf 宣布为 Protocol Buffers 提供新的语言服务器协议（LSP）实现，为 .proto 文件带来自动补全、诊断和导航等现代 IDE 功能。该消息发布在 Buf 博客上，标题为“Protobuf has LSP support. You're welcome”。 Protobuf 是 API 和 gRPC 中广泛使用的模式语言，改进编辑器工具可以提升开发者生产力。然而，该公告招致了批评，因为现有的 LSP 和 IDE 插件已经满足这一需求，使得“首创”的说法存疑。 该博客文章声称这是“首次获得现代 IDE 支持”，但评论者指出 IntelliJ protobuf 插件和已有的 protobuf-language-server 是更早的实现。此外，williamcotton 指出该实现似乎从头重新实现了 protobuf 解析器，而非复用现有解析器，这可能使维护变得更加复杂。

hackernews · theanonymousone · 8月16日 18:48 · [社区讨论](https://news.ycombinator.com/item?id=49322573)

**背景**: Buf 是一个用于 Protocol Buffers 的工具链，它取代了标准 protoc 编译器，提供 lint、破坏性变更检测和 schema 注册表等功能。LSP（语言服务器协议）标准化了编辑器与语言服务器之间的通信方式，使不同的 IDE 都能实现转到定义和重构等功能。这一新闻涉及为 .proto 文件格式扩展该工具链，提供 LSP 支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/bufbuild/buf">GitHub - bufbuild/buf: The best way of working with Protocol Buffers. · GitHub</a></li>
<li><a href="https://buf.build/">Buf · Modern Protobuf and gRPC</a></li>

</ul>
</details>

**社区讨论**: 评论区大多持批评态度。jvolkman 指出，IntelliJ 的 protobuf 支持早已存在，并在约 2021 年默认随 IntelliJ 发布；alecthomas 则提到多年前已有可用的 Protobuf LSP；lacoolj 认为“You're welcome”的措辞不妥。williamcotton 对重新实现解析器提出技术担忧，而 eterm 认为对手写 .proto 文件而言 LSP 可能有用，但也承认字段重命名等限制。

**标签**: `#protobuf`, `#LSP`, `#developer-tools`, `#buf`

---

<a id="item-9"></a>
## [CORS Chat：浏览器中测试 OpenAI-Responses 端点的工具](https://simonwillison.net/2026/Aug/15/cors-chat/) ⭐️ 6.0/10

Simon Willison 构建了 CORS Chat，这是一个基于浏览器的 Web UI，可通过 CORS 调用 OpenAI-Responses 兼容的聊天端点。他已在 LM Studio（使用 --cors 选项）和 OpenRouter 上成功测试，该工具能在浏览器中持久化对话并导出为 JSON，还支持渐进式渲染 SVG。 这款工具解决了开发者的一个现实痛点：浏览器安全机制会阻止对本地 LLM 服务器的直接请求，因此 CORS Chat 让开发者可以轻松地从网页中交互和测试 OpenAI-Responses 兼容端点。它还展示了一种有用的模式——在聊天界面中渐进式渲染流式 SVG 输出，这可能为 LLM 界面带来更丰富的实时可视化。 CORS Chat 是一个托管在 tools.simonwillison.net 上的独立页面，借助 GPT-5.6-Sol xhigh 构建。它适用于任何兼容 OpenAI Responses API 的端点，能检测令牌流中的 SVG 图像并渐进渲染，对话记录保存在浏览器中并可导出为 JSON。作者用它测试了在 M5 MacBook Pro 和 NVIDIA DGX Spark 上通过 LM Studio 本地运行的 Qwen 3.8 27B 模型。

rss · Simon Willison · 8月15日 14:49

**背景**: CORS（跨源资源共享）是一种浏览器安全机制，通常会阻止网页向另一个源发起请求。开发者往往需要在本地开发服务器上开启 CORS 头，或使用变通方法让基于浏览器的工具与本地 LLM 端点通信。LM Studio 是一款在本地运行 LLM 的桌面应用，而 OpenRouter 则提供了跨多个模型提供商的统一 API。OpenAI Responses API 支持有状态、可调用工具的交互。渐进式渲染是指在内容到达时逐步显示，而不是等待完整响应，这对流式传输像 SVG 这样的大输出尤其有用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/reference/responses/overview">Responses Overview | OpenAI API Reference</a></li>
<li><a href="https://lmstudio.ai/">LM Studio Bionic - Your Agent for Work and Code</a></li>
<li><a href="https://www.w3.org/TR/2004/WD-SVG12-20041027/progressiverendering.html">Progressive rendering ( SVG 1.2)</a></li>

</ul>
</details>

**标签**: `#CORS`, `#chat`, `#developer-tools`, `#LLM`, `#OpenAI`

---