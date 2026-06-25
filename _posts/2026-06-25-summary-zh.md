---
layout: default
title: "Horizon Summary: 2026-06-25 (ZH)"
date: 2026-06-25
lang: zh
---

> 从 24 条内容中筛选出 14 条重要资讯。

---

1. [OpenAI 携手博通发布首款定制 AI 推理芯片 Jalapeno](#item-1) ⭐️ 9.0/10
2. [高通收购 Modular 以增强 AI 软件栈](#item-2) ⭐️ 8.0/10
3. [45°C 冷却设计使数据中心用水量降至近零](#item-3) ⭐️ 8.0/10
4. [开源中的 PR 垃圾邮件与早期电子邮件垃圾邮件相似](#item-4) ⭐️ 8.0/10
5. [新慈善基金旨在终结呼吸道感染](#item-5) ⭐️ 8.0/10
6. [Anthropic 指控阿里巴巴非法提取 Claude 模型能力](#item-6) ⭐️ 7.0/10
7. [RubyLLM：面向所有主要 AI 提供商的 Ruby 框架](#item-7) ⭐️ 7.0/10
8. [Gemini 3.5 Flash 新增电脑操控功能](#item-8) ⭐️ 7.0/10
9. [Simon Willison 将浏览器兼容数据转为 SQLite 数据库](#item-9) ⭐️ 7.0/10
10. [LLM 生成的求职申请掩盖了候选人的真实性](#item-10) ⭐️ 7.0/10
11. [Datasette 1.0a35 新增创建和修改表的界面](#item-11) ⭐️ 7.0/10
12. [uv 0.11.24 添加 CPython 3.15 beta 和可重定位环境](#item-12) ⭐️ 6.0/10
13. [直言显而易见：博客写作的关键](#item-13) ⭐️ 6.0/10
14. [OPFS + Pyodide 测试工具：浏览器中持久化文件编辑](#item-14) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI 携手博通发布首款定制 AI 推理芯片 Jalapeno](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI 与博通联合发布了名为 Jalapeno 的定制 AI 推理芯片，专为大语言模型设计，从设计到生产仅用九个月，并利用 OpenAI 自身的模型加速设计流程。 此举标志着 OpenAI 战略性进军 AI 硬件领域，有望减少对第三方芯片的依赖，并提高运行 ChatGPT 和 Codex 等模型的能效，影响 AI 基础设施的竞争格局。 芯片由台积电生产而非英特尔，初期结果显示能效比当前最先进的替代方案显著提升。设计过程借助 OpenAI 自家模型加速，但具体细节尚不明确。

hackernews · jamdesk · 6月24日 17:47 · [社区讨论](https://news.ycombinator.com/item?id=48663324)

**背景**: AI 推理芯片是专门用于高效运行已训练好的 AI 模型的处理器，与用于训练模型的训练芯片不同。博通此前与谷歌合作开发了自定义 AI 芯片如张量处理单元（TPU）。OpenAI 的 Jalapeno 芯片是一款针对大语言模型工作负载优化的推理芯片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip | OpenAI</a></li>
<li><a href="https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html">OpenAI and Broadcom reveal Jalapeno, first AI chip in partnership</a></li>
<li><a href="https://www.cnn.com/2026/06/24/tech/openai-broadcom-jalapeno-ai-chip">OpenAI just announced its first custom chip to help ChatGPT run better | CNN Business</a></li>

</ul>
</details>

**社区讨论**: 评论者对于 OpenAI 模型如何加速设计表示好奇，有人怀疑这可能是营销噱头。其他人指出芯片由台积电制造，并讨论了将权重硬编码到 ROM 中以实现极高吞吐量等替代方案。总体而言，讨论技术性强且参与度高。

**标签**: `#AI chips`, `#OpenAI`, `#hardware`, `#inference`, `#Broadcom`

---

<a id="item-2"></a>
## [高通收购 Modular 以增强 AI 软件栈](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/) ⭐️ 8.0/10

高通于 2026 年 6 月 24 日宣布收购 Modular，后者是 Mojo 编程语言和 MAX 编译器堆栈的开发者，此举旨在加强其 AI 软硬件集成能力。 此次收购标志着高通在 AI 推理领域与 NVIDIA 竞争的雄心，通过将其基于 ARM 的芯片与 Modular 的编译器技术相结合，可能提供比 CUDA 成本更低的替代方案，并在边缘和云端实现更高效的 AI 部署。 据报道，收购金额为 40 亿美元。Modular 的 MAX 编译器堆栈旨在优化跨多种硬件（包括 ARM、x86 和 RISC-V）的 AI 工作负载，其 Mojo 语言结合了类似 Python 的语法和 C 级别的性能。

hackernews · timmyd · 6月24日 13:49 · [社区讨论](https://news.ycombinator.com/item?id=48659798)

**背景**: Mojo 是 Modular 公司开发的系统编程语言，专为高性能 AI 基础设施设计，旨在弥合易用性与性能之间的差距。MAX 编译器堆栈提供统一的运行时，可在多种硬件上加速 AI 模型。高通作为领先的移动芯片设计商，正从智能手机领域拓展至 AI 和汽车市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language) - Wikipedia</a></li>
<li><a href="https://www.modular.com/blog/announcing-max-developer-edition-preview">Modular: Announcing MAX Developer Edition Preview</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一，有人质疑 Mojo 的发展时机和方向，也有人强调其与近期基于 ARM 的超级计算机成就以及高通向 RISC-V 拓展的战略契合。还有人对 Modular 此前关于硬件公司难以提供良好 AI 栈的言论表示质疑。

**标签**: `#Qualcomm`, `#acquisition`, `#AI`, `#compiler`, `#Mojo`

---

<a id="item-3"></a>
## [45°C 冷却设计使数据中心用水量降至近零](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) ⭐️ 8.0/10

NVIDIA 在伦敦气候周宣布，其 Rubin 架构 AI 数据中心将采用 45°C 液冷技术，实现 100%液冷，冷却水消耗近乎为零。这是数据中心冷却效率的重大进步。 该设计大幅降低水和能源消耗，每座设施每年可为运营商节省超过 400 万美元。它为超大规模和托管数据中心设定了新的可持续性基准，对日益增长的 AI 基础设施至关重要。 45°C 的冷却液温度允许通过被动散热排热，无需冷却塔或风扇，消除了水蒸发。然而，效率依赖于有利气候条件；环境温度与性能之间的关系需进一步说明。

hackernews · nitin_flanker · 6月24日 14:10 · [社区讨论](https://news.ycombinator.com/item?id=48660178)

**背景**: 传统数据中心依赖空气冷却或低温液冷，需要大量电力和水来散热。NVIDIA 的 Rubin 架构采用更高温度（45°C）的冷却液，使得散热系统可以直接将热量排放到周围空气中，无需蒸发冷却，从而实现近乎零耗水。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techstory.in/the-45c-breakthrough-nvidias-liquid-cooling-architecture-solves-data-center-water-crisis/">NVIDIA Liquid Cooling Design Cuts Water to Near Zero - TechStory</a></li>
<li><a href="https://www.edgen.tech/news/post/nvidia-rubin-runs-45c-liquid-cooling-cutting-water-use-to-near-zero">NVIDIA Rubin runs 45°C liquid cooling, cutting water use to near zero</a></li>

</ul>
</details>

**社区讨论**: 评论者注意到与区域供热结合的潜力：45°C 废热可免费提供给社区，每年价值数百万美元。也有人质疑其创新性，指出 NASA 已有类似高温水冷方案。一些用户分享了运行 40°C 冷却液的实际经验，并要求提供更多关于气候依赖性的细节。

**标签**: `#cooling`, `#data centers`, `#energy efficiency`, `#NVIDIA`, `#sustainability`

---

<a id="item-4"></a>
## [开源中的 PR 垃圾邮件与早期电子邮件垃圾邮件相似](https://www.greptile.com/blog/prs-on-openclaw) ⭐️ 8.0/10

Greptile 的一篇博文将开源社区中日益严重的垃圾 Pull Request 问题与 2000 年代初的电子邮件垃圾邮件相提并论，引发了社区关于信誉系统和贡献者验证等解决方案的讨论。 随着开源项目面临越来越多的垃圾信息，维护者被低质量贡献所困扰，浪费时间和资源，威胁生态系统健康。借鉴电子邮件垃圾邮件的教训，社区寻求可扩展的信誉和过滤机制来保护维护者。 评论中提到，GitHub 最近为维护者引入了可配置的 PR 限制，以部分解决垃圾信息问题。一些维护者要求新贡献者在合并第一个 PR 之前以非文本形式会面。

hackernews · dakshgupta · 6月24日 14:32 · [社区讨论](https://news.ycombinator.com/item?id=48660579)

**背景**: 垃圾 Pull Request 是不请自来、通常自动化的贡献，几乎没有价值，类似于电子邮件垃圾邮件。与基于发送者基础设施过滤的电子邮件垃圾邮件不同，PR 垃圾邮件涉及个人 GitHub 账户，使得信誉系统更加复杂。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://garvitasood.medium.com/github-clean-up-spam-babc5e5b5ab0">GitHub Clean-up Spam . by Garvita Sood, Anuj Bansal, Garima | Medium</a></li>
<li><a href="https://github.com/shitoberfest/spam-pullrequests">GitHub - shitoberfest/ spam - pullrequests : Show the world how many...</a></li>
<li><a href="https://opensauced.pizza/learn/becoming-a-maintainer/issues-and-pull-requests">How to Handle Open Issues and Pull Requests | Open Source...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出电子邮件和 PR 垃圾邮件之间的差异，强调电子邮件垃圾邮件针对发送者域名/IP，而 PR 垃圾邮件涉及个人用户。一些人建议创建类似于电子邮件的退订列表和信誉基础设施，而另一些则分享了非文本会面等实际措施。

**标签**: `#open source`, `#spam`, `#pull requests`, `#community management`, `#reputation`

---

<a id="item-5"></a>
## [新慈善基金旨在终结呼吸道感染](https://blog.interceptfund.com/p/ending-respiratory-infections) ⭐️ 8.0/10

Intercept Fund 发起了一项 5 亿美元的慈善计划，资助研究和推广空气净化技术，以消除感冒和流感等呼吸道感染。 呼吸道感染每年导致数百万人死亡和数十亿天的生产力损失，该计划可能通过预防和治疗突破显著减轻这一负担。 该基金重点关注三个支柱：了解感染生物学、开发新的预防和治疗手段，以及推广空气净化技术。

hackernews · EthanFantl · 6月25日 01:14 · [社区讨论](https://news.ycombinator.com/item?id=48667588)

**背景**: 呼吸道感染是由通过空气传播的病毒和细菌引起的。尽管这些感染很普遍，但许多常见感染的有效治疗和预防方法仍然难以实现。慈善资金可以加速那些政府和产业资金不足的研究。

**社区讨论**: 评论者分享了因呼吸道感染导致个人损失和残疾的故事，一些人质疑 5 亿美元的预算与大型政府项目相比微不足道。另一些人对所声称的疾病流行程度表示怀疑，但总体情绪支持这一使命。

**标签**: `#public health`, `#respiratory infections`, `#philanthropy`, `#research`

---

<a id="item-6"></a>
## [Anthropic 指控阿里巴巴非法提取 Claude 模型能力](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/) ⭐️ 7.0/10

据报道，Anthropic 于 2026 年 6 月 24 日公开指责阿里巴巴通过模型蒸馏技术非法提取其 Claude AI 模型的能力。 这一指控凸显了人工智能行业日益紧张的知识产权局势，模型蒸馏技术虽常用，但未经许可使用可能越界成为不道德或非法行为。 据称，阿里巴巴利用 Claude 的输出通过蒸馏技术训练自己的模型，该技术将知识从较大的“教师”模型转移到较小的“学生”模型；这种做法虽常见，但涉及专有模型时存在争议。

hackernews · htrp · 6月24日 19:48 · [社区讨论](https://news.ycombinator.com/item?id=48664814)

**背景**: 模型蒸馏（知识蒸馏）是一种机器学习技术，通过训练较小的模型来模仿较大、能力更强模型的行为。这通常用于以更低成本创建高效部署的模型。然而，未经授权从竞争对手的模型中提取能力可能引发法律和道德问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://www.datacamp.com/blog/distillation-llm">LLM Distillation Explained: Applications, Implementation & More</a></li>
<li><a href="https://openai.com/index/api-model-distillation/">Model Distillation in the API - OpenAI</a></li>

</ul>
</details>

**社区讨论**: 评论意见不一：一些用户指出 Anthropic 在利用公开数据训练的同时抱怨被复制的讽刺之处，而另一些人则为 Anthropic 辩护，认为系统性蒸馏用于商业盈利与一般训练不同。技术评论者区分了黑盒蒸馏和基于 AI 反馈的强化学习（RLAIF）。

**标签**: `#AI`, `#model distillation`, `#intellectual property`, `#Anthropic`, `#Alibaba`

---

<a id="item-7"></a>
## [RubyLLM：面向所有主要 AI 提供商的 Ruby 框架](https://rubyllm.com/) ⭐️ 7.0/10

RubyLLM 已发布，作为一个集成主要 AI 提供商的 Ruby 框架，为大型语言模型提供统一的 API。 该框架填补了 Ruby 生态系统在 AI 开发方面的重要空白，使 Ruby 开发者更容易将 LLM 集成到他们的应用中。高社区参与度（361 分，60 条评论）反映了强烈的需求和兴趣。 RubyLLM 因其易用性受到赞扬，但用户报告了缓存 bug（例如与 xAI 相关）、缺乏对 responses API 的原生支持（现已添加）以及 PR 处理缓慢和合并“vibe coded”PR 的问题。其易用性被认为接近 Vercel 的 AI 框架。

hackernews · doener · 6月24日 14:41 · [社区讨论](https://news.ycombinator.com/item?id=48660711)

**背景**: Ruby 是一种动态的面向对象编程语言，广泛用于 Web 开发，但直到最近才缺乏用于集成大型语言模型（LLM）的成熟框架。RubyLLM 旨在为 OpenAI、Anthropic 等提供商提供简单统一的接口，抽象掉 API 差异以改善开发者体验。

**社区讨论**: 社区评论对 RubyLLM 的易用性普遍持积极态度，有人称其“出奇地好”，可与 Vercel 的 AI 框架媲美。然而，一些用户指出了实际问题：某些提供商的缓存不一致、难以实现跟踪可观测性和重试逻辑，以及对维护者响应速度和合并 PR 质量的失望。社区也对新添加的原生 responses API 支持感到兴奋。

**标签**: `#Ruby`, `#AI framework`, `#LLM`, `#developer tools`

---

<a id="item-8"></a>
## [Gemini 3.5 Flash 新增电脑操控功能](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) ⭐️ 7.0/10

Google 在 Gemini 3.5 Flash 中引入了电脑操控功能，该模型可以直接与电脑界面交互来执行任务。 这标志着向智能体 AI 迈出了重要一步，使 Gemini 能够自动化现实任务，但社区反馈指出了可靠性问题和 MCP 支持等缺失功能，可能阻碍其与竞争对手的竞争。 用户报告了意外执行 `git reset --hard`、在数据提取任务中因超出错误阈值而放弃等问题，而 Google 自己的基准测试图显示 Gemini 3.5 Flash 落后于 GPT-5.5 和 Opus 4.8。

hackernews · swolpers · 6月24日 17:21 · [社区讨论](https://news.ycombinator.com/item?id=48662999)

**背景**: 电脑操控功能允许 AI 模型控制电脑的图形用户界面，从而执行点击按钮、输入文本等任务。Gemini 3.5 Flash 旨在以高速度和低成本执行智能体任务，但竞争对手如 GPT-5.5 和 Opus 4.8 在某些基准测试中目前表现更优。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3.5 Flash — Google DeepMind</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash">Gemini 3.5 Flash | Gemini API | Google AI for Developers</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/">Gemini 3.5: frontier intelligence with action</a></li>

</ul>
</details>

**社区讨论**: 社区反馈普遍持批评态度：用户报告模型在简单任务上放弃、执行破坏性 Git 命令以及缺乏 MCP 支持。一些用户表示失望，并认为 Gemini 不如 OpenAI 和 Anthropic 的产品。

**标签**: `#AI`, `#LLM`, `#Gemini`, `#computer-use`, `#agents`

---

<a id="item-9"></a>
## [Simon Willison 将浏览器兼容数据转为 SQLite 数据库](https://simonwillison.net/2026/Jun/24/browser-compat-db/#atom-everything) ⭐️ 7.0/10

Simon Willison 将 Mozilla 的全面浏览器兼容数据仓库转换为约 66MB 的 SQLite 数据库，并通过 GitHub 托管，使用开放的 CORS 头以便通过 CDN 轻松访问。 该工具省去了开发者解析原始 JSON 数据的麻烦，提供了一个可直接在应用中使用或通过 Datasette Lite 探索的可查询 SQLite 数据库。 数据库通过 GitHub Actions 工作流使用 sqlite-utils 构建，并强制推送到一个孤立分支，以利用 GitHub 支持 CORS 的 CDN。构建脚本的提示由 Claude Code for Web (Opus 4.8) 和 Codex Desktop (GPT-5.5) 编写。

rss · Simon Willison · 6月24日 23:59

**背景**: Mozilla 的 browser-compat-data 仓库包含跨浏览器的 Web 平台功能详细兼容性信息。MDN MCP 服务器通过 API 提供类似数据，但此 SQLite 转换提供了无需服务器依赖的离线或编程访问方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/blog/introducing-mdn-mcp-server/?ref=weeklyfoo">Introducing the MDN MCP server - MDN Web Docs</a></li>
<li><a href="https://github.com/mdn/mcp">GitHub - mdn/mcp: MDN's prototype MCP server · GitHub</a></li>
<li><a href="https://github.com/simonw/sqlite-utils">GitHub - simonw/sqlite-utils: Python CLI utility and library for manipulating SQLite databases · GitHub</a></li>

</ul>
</details>

**标签**: `#browser compatibility`, `#SQLite`, `#data conversion`, `#web development`, `#open data`

---

<a id="item-10"></a>
## [LLM 生成的求职申请掩盖了候选人的真实性](https://simonwillison.net/2026/Jun/24/tom-macwright/#atom-everything) ⭐️ 7.0/10

Tom MacWright 报告称，他看到了明显由大语言模型协作编写的求职申请，包括 AI 生成的个人作品集网站、GitHub 项目和提交信息，他认为这使得候选人显得缺乏个性且匿名。 这种趋势削弱了招聘的目的，因为招聘人员无法评估候选人的真实技能和个性，可能导致劳动力同质化，并侵蚀对申请流程的信任。 MacWright 指出，经过 LLM 润色的完美简历只揭示了使用特定工具，而没有展现个人的真实兴趣或经验，问题还扩展到生成的代码和项目历史记录。

rss · Simon Willison · 6月24日 18:13

**背景**: 大语言模型（LLM）是在大量文本数据上训练的神经网络，可以生成类似人类的内容。它们已成为撰写求职申请的热门工具，但其输出往往缺乏原创性和个人特色，使候选人看起来难以区分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model</a></li>

</ul>
</details>

**标签**: `#careers`, `#ai`, `#hiring`, `#authenticity`

---

<a id="item-11"></a>
## [Datasette 1.0a35 新增创建和修改表的界面](https://simonwillison.net/2026/Jun/23/datasette/#atom-everything) ⭐️ 7.0/10

Datasette 1.0a35 引入了新的创建和修改表界面，由 JSON API 支持，用户可以定义列、约束和外键。还新增了稳定的模板上下文文档，用于自定义模板。 此版本显著增强了 Datasette 的数据库管理能力，使用户能够通过编程或 UI 更轻松地操作 SQLite 表。它扩展了该工具对依赖 Datasette 进行数据探索和发布的数据记者和开发者的实用性。 创建表 API 支持定义列、主键、自定义类型、NOT NULL 约束、字面量和表达式默认值以及单列外键。修改表 API 允许添加、重命名、重新排序和删除列，以及更改类型、默认值和约束。模板上下文文档现在被视为稳定 API，直至 Datasette 2.0。

rss · Simon Willison · 6月23日 21:34

**背景**: Datasette 是一个开源工具，用于探索和发布 SQLite 数据库。它提供网页界面和 JSON API。这个 alpha 版本继续扩展其 API 表面，无需直接访问 SQL 即可实现更复杂的数据库操作。

**标签**: `#datasette`, `#database`, `#SQLite`, `#JSON API`, `#release`

---

<a id="item-12"></a>
## [uv 0.11.24 添加 CPython 3.15 beta 和可重定位环境](https://github.com/astral-sh/uv/releases/tag/0.11.24) ⭐️ 6.0/10

uv 0.11.24 添加了对 CPython 3.15.0b3 的支持，并引入了可重定位项目环境的预览功能，同时通过使用紧凑索引实现惰性版本映射的性能改进以及若干错误修复。 此版本使 uv 与最新的 Python 版本（3.15 beta）保持同步，允许早期测试。可重定位环境的预览解决了对可移植 Python 环境的长期需求，在 CI/CD 和部署场景中尤其有价值。 可重定位环境功能仍处于预览阶段，尚未稳定。性能改进使用了惰性版本映射的紧凑索引，减少了内存使用并加快了依赖解析。错误修复包括允许禁用 `exclude-newer` 以及修复归档 ID 冲突。

github · github-actions[bot] · 6月23日 21:16

**背景**: uv 是一个用 Rust 编写的快速 Python 包和项目管理器，旨在取代 pip、pipx、pip-tools、poetry 等工具。可重定位环境是指可以移动到不同路径而不会破坏 Python 路径引用的虚拟环境，这对于打包应用程序进行部署非常有用。惰性版本映射的紧凑索引是一种优化，它仅在需要时加载版本信息，提高了大型依赖树的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://yongweiwu.wordpress.com/2018/11/04/pipenv-and-relocatable-virtual-environments/">Pipenv and Relocatable Virtual Environments | Yongwei’s Blog</a></li>
<li><a href="https://relenv.readthedocs.io/en/v0.4.1/">Relenv - Build and use relocatable Python environments</a></li>
<li><a href="https://docs.astral.sh/uv/">uv is an extremely fast Python package and project manager , written...</a></li>

</ul>
</details>

**标签**: `#Python`, `#package manager`, `#uv`, `#performance`, `#tooling`

---

<a id="item-13"></a>
## [直言显而易见：博客写作的关键](https://blog.jim-nielsen.com/2026/blogging-stating-the-obvious/) ⭐️ 6.0/10

该博客文章认为，成功博客写作的一个关键要素是愿意陈述显而易见的事情，因为作者认为显而易见的事情对他人来说可能很新颖。 这一见解有益于内容创作者，鼓励他们分享知识而不必担心重复，并强调了随着新受众的出现，基础性解释的持续需求。 文章提到了“知识的诅咒”偏见，并指出总有一批新的人未曾接触过某些想法。社区讨论还涉及代际视角和个人在博客写作上的挣扎。

hackernews · Curiositry · 6月24日 23:46 · [社区讨论](https://news.ycombinator.com/item?id=48666927)

**背景**: “知识的诅咒”是一种认知偏差，即人们假设他人拥有与自己相同的背景知识。在博客写作中，这往往导致人们不愿解释基本概念。然而，正如该文章所言，陈述显而易见的事情有助于新手并巩固理解。此外，代际更替意味着对于经验丰富的人来说看似陈旧的想法，对年轻一代来说却是新颖的。

**社区讨论**: 评论普遍赞同这一观点，用户 'nate' 提到了“知识的诅咒”，'supertroop' 指出反复看到相同主题的疲劳感。其他人如 'jdw64' 则讨论了吸引读者和声誉的重要性。

**标签**: `#blogging`, `#knowledge sharing`, `#writing`, `#community`, `#content curation`

---

<a id="item-14"></a>
## [OPFS + Pyodide 测试工具：浏览器中持久化文件编辑](https://simonwillison.net/2026/Jun/23/opfs-pyodide/#atom-everything) ⭐️ 6.0/10

Simon Willison 创建了一个测试工具，将源私有文件系统（OPFS）与 Pyodide 结合，探索在 Datasette Lite（通过 WebAssembly 完全在浏览器中运行的 Python Web 应用）中持久编辑 SQLite 文件。 该测试工具使 Datasette Lite 能够直接在浏览器中持久化修改 SQLite 数据库，从而减少了服务器端存储的依赖，使其成为更实用的数据分析工具。 该工具提供了一个简单 UI，让用户在不同浏览器中体验 OPFS。OPFS 提供沙盒化、高性能的文件系统，对页面源私有。

rss · Simon Willison · 6月23日 18:58

**背景**: Datasette Lite 是 Datasette 的一个版本，通过 Pyodide（编译为 WebAssembly 的 Python 解释器）完全在浏览器中运行。源私有文件系统（OPFS）是一种浏览器 API，为 Web 应用提供沙盒化、持久的文件系统以高效存储数据。将两者结合可实现无后端服务器的长期数据处理任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/File_System_API/Origin_private_file_system">Origin private file system - Web APIs | MDN - MDN Web Docs</a></li>
<li><a href="https://web.dev/articles/origin-private-file-system">The origin private file system | Articles | web.dev</a></li>
<li><a href="https://pyodide.org/">Pyodide</a></li>

</ul>
</details>

**标签**: `#OPFS`, `#Pyodide`, `#Datasette Lite`, `#WebAssembly`, `#browser storage`

---