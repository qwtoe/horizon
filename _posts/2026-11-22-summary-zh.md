---
layout: default
title: "Horizon Summary: 2026-11-22 (ZH)"
date: 2026-11-22
lang: zh
---

> 从 17 条内容中筛选出 9 条重要资讯。

---

1. [Lean verification of the Riemann Hypothesis](#item-1) ⭐️ 9.0/10
2. [研究者匆忙发布广义黎曼猜想的所谓证明](#item-2) ⭐️ 9.0/10
3. [Thinking Machines 发布开源权重模型 Inkling 2 Mini，采用循环 Transformer 架构](#item-3) ⭐️ 8.0/10
4. [口服 KRAS 抑制剂 daraxonrasib 被誉为胰腺癌数十年来最大突破](#item-4) ⭐️ 7.0/10
5. [博主将下载速度下降 75%归咎于显示器 USB 集线器延迟](#item-5) ⭐️ 7.0/10
6. [Go 生态迎来构建 PostgreSQL 扩展的工具](#item-6) ⭐️ 7.0/10
7. [ChatPRD 因代币欺诈泛滥而关闭免费试用](#item-7) ⭐️ 7.0/10
8. [美国旧炸药厂堆积极不稳定叠氮化铅，引发安全争论](#item-8) ⭐️ 6.0/10
9. [Show HN：Zero C# 让 C# 无需运行时和垃圾回收器即可编译为原生程序](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Lean verification of the Riemann Hypothesis](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) ⭐️ 9.0/10

A Lean formalization/verification of the Riemann Hypothesis is announced and discussed on Hacker News, with debate over kernel trust, checker independence, and the role of AI in the proof.

hackernews · g-b-r · 11月21日 14:36 · [社区讨论](https://news.ycombinator.com/item?id=50589618)

**标签**: `#formal-verification`, `#lean`, `#riemann-hypothesis`, `#mathematics`, `#AI-for-math`

---

<a id="item-2"></a>
## [研究者匆忙发布广义黎曼猜想的所谓证明](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/) ⭐️ 9.0/10

一位研究者匆忙发布公告，并在数小时内公开了手稿草稿，声称证明了广义黎曼猜想，并表示自己已在该问题上投入约 12 年时间。此番匆忙发布似乎是由 Anthropic 就同一问题发布的公告所触发，使这一事件演变成一场人类与 AI 之间的优先权竞赛。 广义黎曼猜想是数论中最深奥的未解问题之一，一旦被成功证明，将在解析数论乃至更广领域产生深远影响。除数学本身之外，这位独立研究者与一家 AI 公司之间显而易见的竞赛，也引发了关于成果归属、优先权，以及机器产出的结果是否可能借用了未公开的人类工作的争论。 目前尚无任何内容得到验证：据称该草稿长达约 940 页，评论者立刻注意到一些异常之处，例如开篇的小节 1.1.1 是空白的，作者似乎解释说这是因为希望有更多时间打磨文本。如此规模的结果若要经过同行评审或形式化验证，需要很长时间，因此无论这位研究者的声明还是 Anthropic 的声明，目前都不能被视为已确立。

hackernews · jasondavies · 11月20日 18:33 · [社区讨论](https://news.ycombinator.com/item?id=50579568)

**背景**: 黎曼猜想推测黎曼 zeta 函数的所有非平凡零点都位于实部等于 1/2 的临界线上；广义黎曼猜想则把这一论断推广到 Dirichlet L-函数与 Dedekind L-函数，这些函数刻画了素数在等差数列中的分布规律。它是克雷数学研究所悬赏的千禧年大奖难题之一，数学界普遍相信其成立，许多数论定理都以它为条件进行陈述。Anthropic 是一家以 Claude 模型闻名的 AI 公司，它此次涉足该问题，反映出 AI 实验室正加大力度进军原创数学研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis">Generalized Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/generalized-riemann-hypothesis">Generalized Riemann Hypothesis</a></li>

</ul>
</details>

**社区讨论**: 评论者的态度分为两派：一派敬佩这位研究者长达 12 年的孤独钻研，另一派则怀疑其时间线与 AI 公告的吻合方式，有人追问人类证明的部分内容是否曾被上传给模型做校验、从而实际上被模型吸收。还有人表达了对更广泛趋势的焦虑——靠脑力劳动谋生正越来越依赖由少数富豪掌控的机器访问权；怀疑者则聚焦于手稿本身的具体问题，例如这份 940 页文档中开篇章节的缺失。

**标签**: `#mathematics`, `#Riemann Hypothesis`, `#AI research`, `#research priority`, `#academia`

---

<a id="item-3"></a>
## [Thinking Machines 发布开源权重模型 Inkling 2 Mini，采用循环 Transformer 架构](https://thinkingmachines.ai/news/inkling-2-mini/) ⭐️ 8.0/10

Thinking Machines Lab 发布了 Inkling 2 Mini，这是一款采用循环 Transformer（looped transformer）架构的开源权重语言模型，社区称其基准成绩可与 Qwen 系列 27B 级别的更大模型相媲美。该公司表示，模型的参数规模和训练方案都是刻意针对本地部署优化的，其中包括全程使用 NVFP4 精度进行训练。 循环架构此前大多只存在于前沿实验室的传闻中，很少以开放形式发布，因此这次开源权重的发布为研究者和爱好者提供了一个可以实际研究和运行的具体对象。由于模型规模明确针对本地推理设计，它降低了在消费级硬件上运行一个具备竞争力模型的门槛。 早期实测报告显示，在 Ryzen 395 上通过 llama.cpp 的 Vulkan 后端解码速度约为 27 tokens/s（需要若干尚未合并的 PR 以及一个可带来约 30% 提速的社区小补丁），在 32GB M1 Pro 上以 q4 量化运行约为 10 tokens/s；另有开发者为 24GB 的 M2 MacBook Air 编写了专用推理引擎，达到约 110 tokens/s 的预填充和 19 tokens/s 的解码速度。这些数据均为非官方结果，主要基准成绩也尚未经过独立验证。

hackernews · jasondavies · 11月20日 20:12 · [社区讨论](https://news.ycombinator.com/item?id=50581260)

**背景**: 循环 Transformer 并不堆叠大量不同的层，而是把同一个固定的 Transformer 块重复应用多次，这种权重共享技巧让较小的参数量也能模拟出远大于自身的网络深度和推理深度。Thinking Machines Lab 是由 OpenAI 前 CTO Mira Murati 创立的 AI 初创公司，Inkling 是其旗舰模型系列；“开放权重”意味着训练好的参数可以被下载并在本地运行，但这并不一定意味着完全开源的许可。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Thinking_Machines_Lab">Thinking Machines Lab - Wikipedia</a></li>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/looped-depth-sharing/">Looped Transformer | Sebastian Raschka, PhD</a></li>
<li><a href="https://www.emergentmind.com/topics/looped-transformer-architecture">Looped Transformer Architecture</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者普遍持乐观态度：有人称其基准能与 27B 级别的 Qwen 模型持平“简直离谱地好”，其他人则分享了 llama.cpp 补丁、自研推理引擎以及在 M1、M2 Mac 上的快速编码测试结果。不少人推测，在这次发布之后，大多数开源模型都会转向循环架构；也有一位评论者提出，这种设计可以自由获取后，安全性和可解释性将成为新的开放问题。

**标签**: `#LLM`, `#open-weights`, `#looped-transformer`, `#local-inference`, `#model-release`

---

<a id="item-4"></a>
## [口服 KRAS 抑制剂 daraxonrasib 被誉为胰腺癌数十年来最大突破](https://www.theguardian.com/society/2026/nov/20/pill-pancreatic-cancer-breakthrough-daraxonrasib) ⭐️ 7.0/10

口服 KRAS 抑制剂 daraxonrasib 是一种每日一次的药物；在 III 期 RASolute 302 试验中，该药在既往接受过治疗的转移性胰腺癌患者中显著延长了总生存期和无进展生存期，因而被誉为数十年来首个有实质意义的治疗进展。 转移性胰腺癌是最致命的癌症之一，很少有患者能存活超过一年，因此即便是有限的生存获益，对长期以来只能依赖越来越严苛的化疗方案的患者群体也意味着重大转变。这一结果还证明 KRAS 在胰腺癌中是一个可成药的靶点，可能推动更多联合用药试验和药物开发。 报道的中位生存期约为 13 个月，而化疗组约为 6 个月；不过该试验入组的是经过大量治疗的晚期患者，这会使绝对生存获益看起来小于更早治疗线中的潜在效果。与其他 KRAS 抑制剂一样，daraxonrasib 也面临由继发性 KRAS 突变和下游信号通路重新激活导致的获得性耐药。

hackernews · rafaelc · 11月20日 21:03 · [社区讨论](https://news.ycombinator.com/item?id=50582069)

**背景**: KRAS 是一种小 GTP 酶，也是癌症中最常见的突变致癌基因之一；突变会使该蛋白持续处于活跃状态，从而驱动肿瘤不受控制地生长。几十年来 KRAS 一直被认为难以成药，转移性胰腺癌（最常见为胰腺导管腺癌）几乎只能依靠化疗。新型 KRAS 抑制剂旨在阻断突变蛋白，daraxonrasib 就是这一新兴药物类别中可口服、每日一次的药物。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11049385/">KRAS: Biology, Inhibition, and Mechanisms of Inhibitor ...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC13308734/">KRAS inhibitors: resistance drivers and combinatorial ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2090123226006624">From KRAS inhibition to tumor adaptation: mechanistic layers ...</a></li>

</ul>
</details>

**社区讨论**: 评论者大多认为‘突破’的说法站得住脚，指出看似有限的中位生存数据低估了其影响，因为临床试验通常针对已用尽其他方案的极晚期患者设计。他们还强调 daraxonrasib 不会治愈转移性疾病，但能帮助患者活得更久、更好，并指出这与近期另一项病毒注射试验的报道不同，同时提到这正是前参议员 Ben Sasse 据报正在接受的治疗。

**标签**: `#oncology`, `#drug-discovery`, `#kras-inhibitors`, `#clinical-trials`, `#science-news`

---

<a id="item-5"></a>
## [博主将下载速度下降 75%归咎于显示器 USB 集线器延迟](https://blog.tymscar.com/posts/studiodisplayethernet/) ⭐️ 7.0/10

一位博主记录了自己的下载速度在把以太网接入显示器内置 USB 集线器后下降了约 75%的经历。经过大量排查，他把限速的根源定位到集线器引入的延迟：延迟导致 TCP 确认包返回变慢，以太网适配器的内部缓冲区被填满，进而出现丢包。 这个故事提醒人们：USB、网络硬件与 TCP 之间不透明的多层交互可能会悄无声息地摧毁吞吐量，而每个单独组件看起来都工作正常。对于使用扩展坞、集线器或带网口的 USB-C 适配器的用户来说很有参考价值，而这已经是笔记本电脑非常常见的配置。 真正解决问题的并不是显示器，而是更换以太网适配器：换上一个确认包频率更低（也就是更多依赖延迟/合并确认）的适配器后，吞吐量恢复正常。评论者强调，显示器本身其实只是无关因素——真正的元凶是 USB 集线器带来的额外延迟，这类延迟对大多数用户完全不可见，如果不逐个替换硬件很难定位。

hackernews · soheilpro · 11月21日 10:36 · [社区讨论](https://news.ycombinator.com/item?id=50587875)

**背景**: USB 是一种轮询式的共享总线，经过集线器的数据必须等待调度好的传输时隙，无法立即送达，因此相比直接连接的接口会引入虽小但可测量的延迟。TCP 依赖接收端返回的确认包（ACK）来调节发送端的流量；当 ACK 迟到时，发送端可能发出超过接收端缓冲区容量的数据，导致缓冲区溢出和丢包。随后发送端会把丢包当作拥塞信号并缩小发送窗口，用户看到的就是下载速度骤降，而链路本身其实并无问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TCP_delayed_acknowledgment">TCP delayed acknowledgment - Wikipedia</a></li>
<li><a href="https://web.stanford.edu/class/cs244/papers/SizingRouterBuffersAppenzeller.pdf">Sizing Router Buffers - Stanford University</a></li>
<li><a href="https://www.anker.com/blogs/hubs-and-docks/do-usb-hubs-add-latency">Do USB Hubs Add Latency? How to Lessen It? - Anker US</a></li>

</ul>
</details>

**社区讨论**: 评论者大多把标题重新表述为“我的 USB 网卡在削减我的下载速度”，认为显示器本身无关紧要；还有一位用户清楚地解释了 ACK 时序与适配器缓冲区溢出的机制，许多人表示这正是原文所欠缺的。其他人也分享了类似的离奇经历，包括 Ghostty 使用 io_uring 导致《博德之门 3》误以为系统处于 I/O 压力下而限制着色器编译，以及在 MacBook 加雷雳扩展坞上被同一问题困扰一年多。

**标签**: `#networking`, `#usb`, `#hardware`, `#debugging`, `#performance`

---

<a id="item-6"></a>
## [Go 生态迎来构建 PostgreSQL 扩展的工具](https://jespino.github.io/gopgext/) ⭐️ 7.0/10

开发者 Jesús Espino（jespino）发布了一个名为“PostgreSQL Extensions in Go”（gopgext）的项目页面，演示如何用 Go 而不是 C 来编写 PostgreSQL 扩展。该项目将 Go 定位为比 Rust 生态中的 pgrx 框架等现有非 C 工具更高层的替代方案。 长期以来，PostgreSQL 扩展主要由 C 语言开发，近年则出现了基于 Rust 的 pgrx，因此支持 Go 能降低门槛，让庞大的 Go 开发者群体可以把业务逻辑下沉到数据库内部。这也说明业界越来越希望让数据库内部的编程变得更容易上手，而不必深入掌握 PostgreSQL 的 C 内部实现与内存管理。 任何 Go 扩展最终仍需与 PostgreSQL 面向 C 的扩展接口对接，因此该方案依赖桥接到服务器原生 ABI，并继承了在 postmaster 进程内运行托管运行时语言的固有约束。该页面更像是对这一技术路线的演示，而非像 pgrx 的 cargo 子命令那样完整的打包与测试工具链。

hackernews · valyala · 11月21日 17:08 · [社区讨论](https://news.ycombinator.com/item?id=50591260)

**背景**: PostgreSQL 扩展是加载进数据库服务器的共享库，通过服务器内部的 C API 注册新的函数、类型、操作符或索引方法。传统写法需要直接使用 C、手动管理内存上下文，并且一旦出错就可能导致整个数据库进程崩溃，这正是 pgrx 等项目用更安全的高级语言封装这些 API 的原因。Go 因开发者基数大、工具链简单、具备垃圾回收的易用性而成为有吸引力的选择，但在 Go 运行时与 PostgreSQL 的 C 代码之间跨界调用需要格外小心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/pgcentralfoundation/pgrx">GitHub - pgcentralfoundation/pgrx: Build Postgres Extensions with...</a></li>
<li><a href="https://deepwiki.com/pgcentralfoundation/pgrx">pgcentralfoundation/ pgrx | DeepWiki</a></li>

</ul>
</details>

**社区讨论**: 评论整体偏正面，有人称其“很酷”，并欢迎任何能让 PostgreSQL 扩展更易编写的东西，但也有人表示自己仍会继续使用 pgrx。其他人则指出了相关工作：同一作者的 gokm 项目（用 Go 写 Linux 内核模块）以及已有的 Go 扩展工具 plgo。另有一条讨论支线跑题到了对 Go 地鼠和 Rust 螃蟹 Ferris 等编程语言吉祥物的赞赏。

**标签**: `#PostgreSQL`, `#Go`, `#database-extensions`, `#developer-tools`, `#systems-programming`

---

<a id="item-7"></a>
## [ChatPRD 因代币欺诈泛滥而关闭免费试用](https://simonwillison.net/2026/Nov/20/token-fraud-is-here-and-its-bad/) ⭐️ 7.0/10

AI 产品管理平台 ChatPRD 的创始人 Claire Vo 在一段 YouTube 视频中表示，其产品遭到不法团伙利用免费试用进行的大规模代币欺诈，她因此决定全面关闭免费试用。 这是一个关于免费试用代币套利、转售和智能体隧道化的真实案例，说明 AI SaaS 开发者可能会通过免费额度为第三方生意买单，因此可能需要更严格的消费上限、模型白名单和滥用检测机制。 据报道，滥用者循环使用免费试用和优惠码，然后隧道化接入 ChatPRD 智能体来开展商业活动，例如制作 Roblox 和 Fortnite 地图；Claire 还发现大量要求生成骑自行车鹈鹕 SVG 的提示词，这是一种用于识别底层模型身份的已知手法。

rss · Simon Willison · 11月20日 02:49

**背景**: ChatPRD 是一款面向产品经理的 AI 副驾驶，可将想法转化为产品规格文档，自 GPT-4 时代起就已上线。在 LLM 产品中，代币欺诈通常指自动化创建大量账号以反复领取免费推理额度或试用额度，再将其归集并转售。这里的“隧道化”是指把产品的智能体当作代理来访问底层模型，而“骑自行车的鹈鹕”提示词是一种已知的模型指纹识别方法，因为不同模型绘制出的结果具有明显差异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://labs.cloudsecurityalliance.org/research/csa-research-note-llm-api-relay-market-shadow-risk-20260729/">The Shadow Relay Market: LLM API Reselling and Fraud Risk</a></li>
<li><a href="https://workos.com/blog/llm-token-theft">LLM token theft: how attackers drain your AI startup's bottom ...</a></li>
<li><a href="https://explainx.ai/blog/token-fraud-chatprd-claire-vo-free-trial-abuse-stripe-radar-ai-startups-2026">Token Fraud: How ChatPRD and Stripe Fight AI Trial Abuse ...</a></li>

</ul>
</details>

**标签**: `#AI security`, `#token fraud`, `#free trial abuse`, `#LLM economics`, `#SaaS abuse`

---

<a id="item-8"></a>
## [美国旧炸药厂堆积极不稳定叠氮化铅，引发安全争论](https://www.science.org/content/blog-post/detonating-huge-pile-lead-azide-really) ⭐️ 6.0/10

Science.org 的博客文章（In the Pipeline）描述了一处美国旧政府炸药设施中发现的严重变质的叠氮化铅堆，这批物质极不稳定，据称已无法安全搬运，只能就地销毁。该话题在 Hacker News 上引发热议（约 499 分、331 条评论），读者主要围绕承包商责任以及处理变质起爆药的现实极限展开讨论。 这一事件说明，老化的起爆药可以把一次常规清理变成几乎无解的难题，也让人质疑政府所有、承包商运营的设施是否有足够动力妥善处理危险物料。它的意义不限于化学领域：这是一个关于风险管理、监管监督以及把问题拖到再无安全选项时所付代价的典型案例。 叠氮化铅（Pb(N3)2）是用于雷管的起爆药，干燥状态下受震动、受热或摩擦即可爆炸，约在 350°C 起爆，并且会被铜、锌等金属盐进一步敏化；一旦物料在现场发生变质，哪怕容器轻微挪动都可能将其引爆。根据爱荷华州卫生与公众服务部的一份情况说明，美国陆军计划于 2026 年 11 月 23 日在爱荷华州米德尔敦的爱荷华陆军弹药厂对变质叠氮化铅实施两次受控引爆，预计会产生含铅颗粒的粉尘羽流。

hackernews · beginning_end · 11月21日 13:23 · [社区讨论](https://news.ycombinator.com/item?id=50588982)

**背景**: 叠氮化铅属于起爆药，即敏感度足够高、能被可靠触发并用于引爆 TNT、RDX 等次级炸药的少量物质。它在常规商用形态下是白色至浅黄色粉末，由于其敏感性，须在严格的爆炸物储存法规下管理。危险之处在于起爆药会随时间变质，尤其是在潮湿、与不相容金属或酸接触的情况下，变质后的物料对冲击的敏感度可能远高于新品——这也是应急人员通常选择就地销毁而非运输这类物质的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lead(II)_azide">Lead (II) azide - Wikipedia</a></li>
<li><a href="https://cameochemicals.noaa.gov/chemical/11731">LEAD AZIDE | CAMEO Chemicals | NOAA</a></li>
<li><a href="https://hhs.iowa.gov/media/19822/download?inline">PLANNED LEAD AZIDE DETONATION FACT SHEET - hhs.iowa.gov</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者大多把矛头指向承包商运营模式，指出该厂在 1960 年代前由政府运营、1998 年转为承包商运营，企业拿了大量经费却在弹药处理上偷工减料；也有人反驳“派机器人去搬”这类想当然的方案，指出即便实验室里只有一升这种物质，正确做法也是让排爆人员就地销毁，因为任何移动都可能引发爆炸。讨论的主流情绪是对机构的不满——把问题藏到再无良策，事后又无人担责；还有评论者依据 2025 年爱荷华陆军弹药厂的叠氮化铅中和合同，质疑事件的时间线。

**标签**: `#explosives-safety`, `#industrial-accidents`, `#risk-management`, `#government-contracting`, `#chemistry`

---

<a id="item-9"></a>
## [Show HN：Zero C# 让 C# 无需运行时和垃圾回收器即可编译为原生程序](https://onurgumus.github.io/zero-csharp/index.html) ⭐️ 6.0/10

一位开发者在 Hacker News 上发布了名为 "Zero C#" 的 Show HN 项目，宣称提供"不带任何 GC 的 C# 能力"，可把 C# 代码直接编译成体积很小的原生二进制文件，运行时不依赖 CLR 运行时，也不含垃圾回收器。根据社区对该帖的整理，这个项目是现有 C# 原生编译器 bflat 的一个分支，帖子在 Hacker News 上获得了约 100 多分和 80 多条评论。 这个项目正好落在长期争论的焦点上：C# 能否进入过去由 C、C++、Rust 和 Zig 把持的系统级、零分配编程领域。由于 .NET 本身已经提供 NativeAOT，以及 unsafe 指针、Span<T> 和 ref struct 等手动内存控制手段，这项实验与其说是带来了新能力，不如说是在促使人们重新审视 C# 的能力边界究竟在哪里。 对该帖的整理指出，原帖除了链接的网站之外，并没有提供基准测试、语法示例或实现细节，因此其性能主张尚未得到验证。评论者提出的一个结构性限制是：C# 本身并非为无 GC 运行而设计，因此标准库的很大一部分以及大多数现有 C# 代码在这种模式下无法运行。

hackernews · reverseblade2 · 11月21日 15:39 · [社区讨论](https://news.ycombinator.com/item?id=50590279)

**背景**: C# 通常运行在公共语言运行时（CLR）之中，这是一个托管执行环境，通过追踪式垃圾回收器自动管理内存，开发者很少需要手动释放对象。NativeAOT 是微软提供的提前编译（AOT）方案，可以把 C# 编译成独立的原生可执行文件，无需附带 .NET 运行时，代价是牺牲部分运行时吞吐量以换取更快的启动速度和更小的二进制体积。bflat 是社区中一个思路相近的独立项目，把 C# 直接编译成原生代码，只带极小的运行时且不含 GC。Zero C# 正是建立在 bflat 这条技术脉络之上，目标是走到极端：没有运行时、没有回收器、二进制极小。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zeli.app/story/50590279">Zero C# - C# compiled to tiny native · 86 HN comments | Zeli</a></li>
<li><a href="https://www.headstart.news/articles/f4f7150b9d3465a1db84a7d9cdd53c3b">Show HN: Zero C# – C# without a runtime or GC - headstart.news</a></li>
<li><a href="https://kblip.com/releases/show-hn-zero-c-a-c-powered-language-without-garbage-nx8AOcI">Show HN: Zero C# — a C#-powered language without garbage ...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍对其实际价值持怀疑态度。多人认为 C# 已经覆盖了这些需求——unsafe 指针、用 Marshal 分配非托管内存、用 Span 避免拷贝、手动向量化，以及用 NativeAOT 实现免运行时分发——其中一位直言不讳地问 Zero C# 相比 NativeAOT 有什么优势，并指出 NativeAOT 往往比 RyuJIT 更慢，唯一确定的优势只是二进制更小。另一些人则为 GC 辩护，认为 GC 是特性而非缺陷，能让开发者专注于真正要解决的问题，而不必冒内存泄漏的风险；还有人提出，类似 Java Epsilon GC 的"冻结 GC"模式会比彻底去掉 GC 更有用。另有评论把它与 bflat 相提并论，认为若要无 GC 编程，C、Rust 或 Zig 仍是更好的选择。

**标签**: `#C#`, `#.NET`, `#garbage collection`, `#NativeAOT`, `#compilers`

---