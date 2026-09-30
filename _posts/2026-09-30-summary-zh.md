---
layout: default
title: "Horizon Summary: 2026-09-30 (ZH)"
date: 2026-09-30
lang: zh
---

> 从 23 条内容中筛选出 13 条重要资讯。

---

1. [德里将电网损耗从 50%降至 5%](#item-1) ⭐️ 8.0/10
2. [OpenAI 发布 GPT 6.1 Sol，价格仅为前代的五分之一](#item-2) ⭐️ 8.0/10
3. [LiveneRF：检测大模型“削弱”的开源基准引发热议](#item-3) ⭐️ 7.0/10
4. [OpenAI 在 DevDay 2026 发布常驻智能体“Dots”](#item-4) ⭐️ 7.0/10
5. [佛蒙特州家用电池组成虚拟电厂，已取代两座调峰电厂](#item-5) ⭐️ 7.0/10
6. [Show HN：含 52.6 万颗小行星和全部在轨卫星的实时太阳系](#item-6) ⭐️ 7.0/10
7. [Anthropic：GLM-5.3 与 Claude Mythos Preview 首次实现二进制漏洞利用中的控制流劫持](#item-7) ⭐️ 7.0/10
8. [Anthropic 发布 Claude Sonnet 5.5：更快、更便宜，并成为免费层默认模型](#item-8) ⭐️ 7.0/10
9. [NASA 招募前 SR-71 团队成员，秘密重启黑鸟计划](#item-9) ⭐️ 6.0/10
10. [白宫推出 America.gov：面向政府服务的 AI 聊天机器人](#item-10) ⭐️ 6.0/10
11. [Backblaze 发布 2026 年第二季度硬盘可靠性统计报告](#item-11) ⭐️ 6.0/10
12. [PS5「Relapse」漏洞可越狱 7.00 至 13.60 固件主机](#item-12) ⭐️ 6.0/10
13. [OpenAI 安全人员警告 AI 能力跃升超出防御准备](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [德里将电网损耗从 50%降至 5%](https://spectrum.ieee.org/delhi-electricity-loss) ⭐️ 8.0/10

IEEE Spectrum 发表了一篇详细案例研究，记录了德里如何将综合技术及商业（AT&C）电力损耗从大约 50%降至约 5%，这一改变也基本消除了这座印度首都的日常拉闸限电。这一转变是通过全面安装电表、配电区域私有化以及电网物理加固等措施共同实现的。 它表明，长期被视为发展中国家电力公司不可避免的技术问题的损耗，本质上更多是商业与治理问题，可以通过计量、责任落实和防窃电手段解决。在一个拥有数千万人口的大都市取得成功，为印度举步维艰的各邦配电公司（discoms）及其他新兴市场提供了一套可复制的范本。 文章强调，德里的损耗并非纯技术问题：无论权贵还是普通居民都普遍存在窃电行为，因此改革必须把技术手段与执法和制度变革结合起来。一个值得注意的副作用是，为防止窃电而对社区电力线进行绝缘和包覆处理，也让这些电线变得足够安全，猴子可以将其当作在社区之间穿行的“高架公路”。

hackernews · rbanffy · 9月29日 12:43 · [社区讨论](https://news.ycombinator.com/item?id=49892245)

**背景**: AT&C 损耗衡量的是送入电网的电量与实际计费并收回费用的电量之间的差距，它同时包含技术损耗（导线和变压器中的发热与电阻损耗）和商业损耗（窃电与欠费）。拉闸限电指为匹配需求与受限供应而进行的计划外断电；二十年前的德里，一天停电数次是常态，恢复供电时还常伴随损坏电器的电压浪涌。智能电表可记录用电量和电压数据并回传给电力公司，从而实现准确计费和发现篡改行为；而电网加固则指对电网基础设施进行物理强化与升级，例如用包覆导线替换裸导线，以抵御扰动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://anyline.com/news/atc-losses-facts-and-solutions">AT & C Losses : Key Facts and Solutions for the Utility Industry</a></li>
<li><a href="https://en.wikipedia.org/wiki/Smart_meter">Smart meter - Wikipedia</a></li>
<li><a href="https://scienceinsights.org/what-is-grid-hardening-and-how-does-it-protect-the-grid/">What Is Grid Hardening and How Does It Protect the Grid?</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论整体非常热情：有初次接触该话题的读者称这篇文章是了解电网运作的绝佳入门读物，而在德里长期生活的网友则强调，真正具有革命性意义的是消除了拉闸限电以及停电后随之而来的破坏性电压浪涌。其他人也分享了亲身经历，例如防窃电绝缘线如何变成猴群穿行的便利“道路”，还有人主张印度应将这些改革与屋顶光伏、储能电池和垂直太阳能板结合起来。

**标签**: `#energy-grid`, `#infrastructure`, `#india`, `#utility-losses`, `#policy`

---

<a id="item-2"></a>
## [OpenAI 发布 GPT 6.1 Sol，价格仅为前代的五分之一](https://openai.com/index/introducing-gpt-6-1-sol/) ⭐️ 8.0/10

OpenAI 发布了 GPT 6.1 Sol，宣称其具备“接近 Astra 的智能水平，而价格仅为后者的五分之一”。最受关注的定价细节是缓存输入价格低至每百万 token 0.10 美元，官方称这比标准输入价格低 95%，也比 GPT-6 Sol 的缓存输入价格低 50%。 这次发布把 token 价格推到了前沿模型竞争的核心位置，OpenAI 明显是在对标 Anthropic 的 Opus 系列以及 DeepSeek 等低价挑战者。更便宜的缓存输入会直接降低 Codex 等智能体与编程工作流的成本，因此即便能力提升有限，也可能改变开发者的预算分配。 每百万 token 0.10 美元的缓存输入价格是与 GPT-6 Sol 对比时被反复引用的具体数字，评论区认为这才是本次发布的实质内容。社区成员还声称该模型可能只是此前在文件中被发现的“Astra-Minor”的临时改名，并反映 GPT 6 / Sol 6 相比 Sol 5.6 出现了质量退步。

hackernews · crorella · 9月29日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=49896586)

**背景**: 前沿大模型厂商通常按每百万 token 计费，并对“缓存”输入收取更低的价格——所谓缓存输入，是指服务方已经处理并存储过的提示上下文，因为复用它的服务成本更低。在本次发布中，OpenAI 把 GPT 6.1 Sol 描述为以约五分之一的成本提供“接近 Astra”的能力，而 Astra 看起来是讨论中提到的更高端层级。随着 Anthropic 的 Opus 系列和以低成本大模型著称的中国开源权重挑战者 DeepSeek 加剧竞争，Hacker News 的讨论普遍把这次发布解读为对价格压力的回应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>

</ul>
</details>

**社区讨论**: 整体情绪偏向怀疑：一位高赞评论者表示 DeepSeek 足够便宜，自己已不再关注用量配额，并愿意在性价比优先的前提下落后前沿六个月；另一位则称 Sol 6 出现了严重退步，使其彻底转用 Opus 5.5。也有人认为真正的亮点是 Codex 所用缓存价格便宜了 50%，还有评论者警告说 token 价格成为主要战场对整个行业和投资者而言并非好兆头。

**标签**: `#OpenAI`, `#LLM`, `#AI models`, `#pricing`, `#model release`

---

<a id="item-3"></a>
## [LiveneRF：检测大模型“削弱”的开源基准引发热议](https://github.com/ninjahawk/livenerf) ⭐️ 7.0/10

由 ninjahawk 发布的 GitHub 项目 LiveneRF 是一个“用于追踪模型发布后能力变化”的基准工具，旨在检测 Opus 5.5 等前沿大语言模型上线后出现的性能下降（即所谓“削弱/nerfing”）。该项目登上 Hacker News 首页，获得约 420 分和 172 条评论，使一个偏小众的工具演变为关于“模型退化究竟真实存在还是主观错觉”的大讨论。 如今大多数用户都是通过服务端可被静默更新的托管 API 来使用前沿模型，因此如果模型能力在上线后真的下降，将会损害所有基于这些 API 构建产品的团队的可复现性、信任度与成本预期。这场争论也有两面性：如果退化多半只是主观感受，社区同样需要更严谨的评测方法；而这种被认为不透明的做法，正在把部分开发者推向开放权重模型。 其思路是在模型发布当天先做一次基准测试，把此后与该基线的偏差视为可能的性能退化——有评论者提到同类项目 Nerf Bench 采用 10% 偏差作为判定阈值，并称其正在跟踪 Opus 5.5 和 GPT-6 Astra。需要注意的局限是：该仓库本身并未公开太多关于方法论与统计显著性的细节，而硬件负载、流量路由与基础设施变更都可能干扰结果，早期 Google Translate 质量随时段波动就是例证。

hackernews · bryan0 · 9月29日 22:36 · [社区讨论](https://news.ycombinator.com/item?id=49901736)

**背景**: 通过 API 提供的大语言模型随时可能被重新训练、重新路由，或调整系统提示与安全层，而版本号并不改变，因此同一个模型名称未必对应同样的行为。“Nerfing”一词借自游戏术语，指削弱角色能力，被社区用来形容这种疑似静默的性能退化。回归基准的做法是固定一组任务，随时间反复对同一模型重跑，观察分数是否漂移；而持怀疑态度的人则把感知到的能力下降归因于“蜜月效应”——新模型之所以感觉更好，只是因为它够新，且用户会主动调整提示词去适配它。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ninjahawk/livenerf">GitHub - ninjahawk/livenerf: Benchmark for tracking model capability after release. · GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论者观点明显分化。用户 jug 以 Nerf Bench 为例，指其曾成功检测出 Opus 4.6 的性能退化、Anthropic 后来还专门发博客说明，但他仍认为由于蜜月效应，人们感知到“被削弱”的频率远高于实际发生；johnfn 则主张绝大多数所谓 nerfing 并不真实，这种感受源于新模型一旦超过某个复杂度阈值就会崩坏。sheepscreek 反驳说 Anthropic 每天有上千名员工做出十万量级的细小改动，其叠加效应确实可能让内部测试覆盖不足的领域出现暂时性退化；kingcauchy 指出有证据显示硬件负载会影响模型质量；gr_norm 则认为这种“不诚实与不透明”正是人们转向开放模型的原因之一。

**标签**: `#LLM evaluation`, `#benchmarking`, `#model regression`, `#AI/ML`, `#community discussion`

---

<a id="item-4"></a>
## [OpenAI 在 DevDay 2026 发布常驻智能体“Dots”](https://openai.com/index/introducing-dots/) ⭐️ 7.0/10

OpenAI 于 2026 年 9 月 29 日的 DevDay 2026 活动上发布了名为 Dots 的常驻个人智能体产品，每个 Dot 都拥有独立的云端电脑和浏览器，可自主完成长流程任务。Pro 与 Business Premium 套餐各附带一个 Dot，这些智能体由 GPT-6 Astra 驱动，并通过插件接入超过 4000 个应用。 Dots 标志着整个行业正朝着“常驻云端、代用户行事”的智能体方向转变，这带来的平台锁定效应可能远超可自由切换的聊天模型。对 OpenAI 而言，这也意味着从慷慨的 Codex 订阅时代转向变现，这一转变直接影响着正在决定把工作流押注何处的开发者与企业。 每个 Dot 都运行在独立的云端电脑和浏览器上，并通过覆盖 4000 多个应用的插件扩展能力，Pro 与 Business Premium 套餐各包含一个 Dot。主要的隐患在于产品线模糊：Dots、Codex 和 ChatGPT Work 都在趋同于同一个概念——拥有长期记忆的远程沙箱智能体，使得三者的区分变得不清晰。

hackernews · alvis · 9月29日 17:07 · [社区讨论](https://news.ycombinator.com/item?id=49896604)

**背景**: 所谓“常驻智能体”，是指一种在自己的虚拟机上持续后台运行、理解跨应用工作流程并在无需逐次提示的情况下主动执行任务的 AI 系统，这与需要一问一答的聊天机器人不同。DevDay 是 OpenAI 的年度开发者大会，通常用于发布重要产品，而据称 Dots 由 GPT-6 Astra 驱动。微软与 Meta 也提出了类似概念（分别为 Scout 和 Muse），因此 Dots 是这波竞争浪潮的一部分，而非孤立的创新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datacamp.com/blog/openai-dots">OpenAI Dots : Always - On Agents in ChatGPT, Explained | DataCamp</a></li>
<li><a href="https://www.oflight.co.jp/en/columns/openai-dots-always-on-personal-agent-2026">OpenAI dots Explained: Always - On Agent , Safety, Pricing | Oflight Inc.</a></li>
<li><a href="https://www.wired.com/story/openai-dots-always-on-ai-agents-that-proactively-help/">OpenAI’s Dots Are Always-On AI Agents—and Its ... - WIRED</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论总体偏批评：多位用户认为常驻智能体通过各类集成和工作历史把用户深度绑定到平台上，使其比更换模型难得多，有人称其是在模型之上加的一层“抽象层”。另一些人指出 Codex、ChatGPT Work 与 Dots 之间的界限日益模糊，质疑 OpenAI 从慷慨订阅转向兜售“不必要的产品”，并认为这类云端智能体的目标用户可能是不懂技术的人群和“AI 原住民”，而非能在本地自行运行的极客用户。

**标签**: `#AI agents`, `#OpenAI`, `#platform lock-in`, `#product launch`, `#AI industry`

---

<a id="item-5"></a>
## [佛蒙特州家用电池组成虚拟电厂，已取代两座调峰电厂](https://www.bbc.com/future/article/20260928-a-virtual-power-plant-hidden-in-vermont-homes-is-keeping-the-lights-on-during-storms) ⭐️ 7.0/10

佛蒙特州正在把安装在居民家中的 Tesla Powerwall 聚合为一个虚拟电厂（VPP），其规模已经大到足以成为该州最大的单一电力来源；据 Electrek 报道，该计划已使两座调峰电厂得以关停。据报道，用户每月支付约 55 美元即可获得两块 Powerwall，账单减免额度取决于他们在用电高峰和停电期间愿意向电网回送多少储存的电量。 这是一个已经落地运行的实例：分布式家用电池取代了化石燃料调峰电厂。已有研究表明，电池储能的成本比燃气调峰机组低约 30%，这一替代可能重塑电力公司的容量规划方式。如果该模式推广开来，电网投资将从集中式电厂转向数以百万计的消费者自有设备，并引发“谁为这些基础设施付费、谁从中获益”的新问题。 推广受制于一些很实际、并不光鲜的约束：有评论者指出，建筑规范要求电池与任何窗户或门之间留出约 3 英尺（约 0.9 米）的间距，如果家中没有一面开口之间相隔 8 至 9 英尺的墙，唯一替代方案是建造防火房间，结果反而不如安装丙烷或柴油发电机方便。Powerwall 是特斯拉的住宅锂离子储能产品，2015 年首次推出，现行 Powerwall 3 集成了直流转交流逆变器。

hackernews · devonnull · 9月29日 18:19 · [社区讨论](https://news.ycombinator.com/item?id=49897993)

**背景**: 虚拟电厂（VPP）是通过软件编排把小型分布式能源资源——屋顶光伏、家用电池，乃至电动汽车电池和热泵——聚合成一个整体，由电力公司或运营方统一调度，使这一群设备表现得像一座电厂，从而提供容量、削峰填谷以及快速响应的电网辅助服务。调峰电厂只在用电需求最高的时段运行，由于运行时间很短，其每千瓦时电力的成本非常高，而这正是电池如今填补的生态位。Tesla Powerwall 是一种家用电池，用于储存光伏或电网电力以实现备用供电和分时电价下的负荷转移；当大量 Powerwall 被纳入同一计划时，它们就能作为一个电网资产被统一调度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Virtual_power_plant">Virtual power plant</a></li>
<li><a href="https://en.wikipedia.org/wiki/Peaker_power_plant">Peaker power plant</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Powerwall">Tesla Powerwall</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：有人认为这是一项实打实的成果（有人指出它已经关停了两座调峰电厂，也有人把它比作家用 UPS），但最强烈的反对声音是，电力公司把基础设施成本转嫁给了购买电池的消费者，而用户既不一定拥有这些电池，也不是唯一受益方，因此他们认为住户应当因提供并开放这部分容量而获得报酬。另一条讨论则指出一个平淡却决定性的障碍：建筑规范对电池与门窗间距的要求，使许多住宅根本无法通过认证安装，反而让化石燃料发电机成为更省事的选择。

**标签**: `#energy`, `#virtual-power-plant`, `#grid-storage`, `#distributed-systems`, `#climate-tech`

---

<a id="item-6"></a>
## [Show HN：含 52.6 万颗小行星和全部在轨卫星的实时太阳系](https://space.bl2.net/) ⭐️ 7.0/10

一位开发者发布了 space.bl2.net，这是一个在浏览器中运行、真实比例、实时的太阳系可视化项目，可渲染约 52.6 万颗小行星与彗星，以及航天器和全部被编目的地球卫星。场景数据每日从 JPL SBDB、JPL Horizons 和 CelesTrak TLE 数据刷新，并以 Show HN 帖子的形式发布在 Hacker News 上。 它把专业级别的轨道数据（卫星运营方和研究人员使用的同一批目录）放进一个无需安装的网页里，降低了学生、记者和航天爱好者了解空间态势感知的门槛。它也展示了浏览器图形能力的进步：数十万量级的目标如今可以在普通硬件上实时推算轨道并渲染。 据作者介绍，卫星轨道基于 CelesTrak 的 TLE 数据用 SGP4 模型推算，轨道推算在 Web Worker 中运行，渲染采用 WebGL2；约 30 MB 的小行星数据集在后台加载。时间滑块可正向和反向运行，卫星会按其发射日期出现或消失。

hackernews · wanick · 9月29日 19:08 · [社区讨论](https://news.ycombinator.com/item?id=49898778)

**背景**: CelesTrak 是由 T.S. Kelso 博士于 1985 年创立的非营利轨道数据服务，发布两行根数（TLE）——一种描述卫星轨道的紧凑格式；SGP4 则是把这些根数推算成位置的标准模型。JPL 的小天体数据库（SBDB）收录小行星和彗星，JPL Horizons 则提供行星与航天器的星历。WebGL 是一套 JavaScript API，可在任何现代浏览器中无需插件地做硬件加速 3D 渲染；Web Worker 则让 JavaScript 在后台线程执行繁重计算，从而保持界面流畅。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://celestrak.org/">CelesTrak</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebGL">WebGL - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API">WebGL: 2D and 3D graphics for the web - Web APIs | MDN</a></li>

</ul>
</details>

**社区讨论**: 作者亲自回帖确认了数据来源与技术栈；有用户表示喜欢用它跟踪 Europa Clipper 即将到来的地球飞掠，也有人称赞关闭卫星图层后画面非常宁静。主要的质疑是 Celestia 早在十多年前就实现了这些功能甚至更多，另有评论者调侃说以自己命名的小行星没有出现在小行星数据集中。

**标签**: `#astronomy`, `#visualization`, `#WebGL`, `#space-data`, `#Show HN`

---

<a id="item-7"></a>
## [Anthropic：GLM-5.3 与 Claude Mythos Preview 首次实现二进制漏洞利用中的控制流劫持](https://simonwillison.net/2026/Sep/29/anthropic-frontier-red-team/) ⭐️ 7.0/10

Anthropic 的 Frontier Red Team 在一个内部二进制漏洞利用（Binary Exploitation）基准中随机抽取 100 个任务，对多个模型进行了评测，发现 GLM-5.3 在 4% 的试验中实现了完整的控制流劫持，Claude Mythos Preview 则为 6%。而此前的模型，如 Claude Opus 4.6 和 GLM-5.2，在这些任务中一次都没有成功，说明一个明确的能力阈值已被跨过。 这是一个 AI 安全信号：自主网络攻击能力并非只是渐进提升，而是跨过了一个真实的门槛——此前的旗舰模型在同一基准上得分为零。它之所以重要，是因为一个能力较强的中国开放权重模型与 Anthropic 自家的预览模型之间只差几个百分点，意味着先进的攻击性能力会在整个生态中迅速扩散，这对模型开发者、安全研究者和政策制定者都极为关键。 绝对成功率仍然很低——在随机抽取的 100 个内部任务中分别为 4% 和 6%——因此这一发现更应被理解为跨过阈值，而非展示了可靠的漏洞利用能力。该基准是 Anthropic 自有的内部二进制漏洞利用套件，而且此次发布只是简短引文摘录，没有公布方法论、误差范围，也未说明模型获得了多少人工协助。

rss · Simon Willison · 9月29日 22:20

**背景**: 二进制漏洞利用（binary exploitation）是指滥用软件漏洞、通常是缓冲区溢出等内存破坏型缺陷，使程序表现出开发者从未预期的行为。控制流劫持（control flow hijack）是其中一类特定且严重的攻击方式：攻击者通过覆盖返回地址或函数指针等手段重定向程序的执行流，从而运行自己控制的代码。这属于攻击性安全中较为高级的技能，通常要求深入掌握汇编、内存布局以及 ASLR、栈保护等缓解机制，因此自主 LLM 即便只有个位数成功率也会被视为值得关注。Anthropic 的 Frontier Red Team 是公司内部负责对前沿模型进行危险能力压力测试（包括网络攻击能力）的团队。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pwn.college/intro-to-cybersecurity/binary-exploitation/">Binary Exploitation - pwn.college</a></li>
<li><a href="https://cyberpedia.reasonlabs.com/EN/control+flow+hijacking.html">What is Control Flow Hijacking ?</a></li>
<li><a href="https://pathogenickatt.github.io/notes/binary-exploitation/">Binary Exploitation Fundamentals</a></li>

</ul>
</details>

**标签**: `#ai-security-research`, `#anthropic`, `#generative-ai`, `#cybersecurity`, `#llm-capabilities`

---

<a id="item-8"></a>
## [Anthropic 发布 Claude Sonnet 5.5：更快、更便宜，并成为免费层默认模型](https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/) ⭐️ 7.0/10

Anthropic 发布了 Claude Sonnet 5.5，官方称其运行速度快了 30% 以上，多数任务的成本最多降低 30%，而定价与 Sonnet 5 相同，并在各项基准测试上全面超越前代。该模型现在已成为 claude.ai 免费层的默认模型，Simon Willison 还指出它继承了 Opus 5.5 上出现的「max」思考档位缺陷。 由于 Sonnet 5.5 现在驱动 claude.ai 的免费层，Anthropic 的免费服务能力已明显强于目前使用 Luna 5.6 的 OpenAI ChatGPT 免费层。对开发者而言，它以 Sonnet 的价格提供了接近 Opus 级别的编码表现，从而降低了构建智能体与代码生成类应用的成本。 该缺陷出现在最高推理档位：在「max」思考强度下，模型消耗了 128,000 个 token（约 1.28 美元），最终触及 token 上限并没能生成所要求的 SVG；而在「xhigh」档位下，它用 41 秒、花费 5.74 美分就产出了不错的结果。Anthropic 还重申 Haiku 5.5 将在「未来几周内」推出，Willison 希望其价格能与 GPT-6 Luna 竞争。

rss · Simon Willison · 9月28日 22:07

**背景**: Simon Willison 的「骑自行车的鹈鹕」测试是一句提示词，要求模型生成一张鹈鹕骑自行车的 SVG 或 WebGL 页面，如今已成为衡量大语言模型用代码作画能力的非正式基准。Anthropic 的 Claude 系列按 Haiku（快而便宜）、Sonnet（均衡）和 Opus（最强）分层，近期版本还提供可调节的「思考强度」档位，用推理 token 和延迟换取回答质量。扩展思考的预算按输出 token 计费，这正是过于激进的 max 档位既慢又贵的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2024/Oct/25/pelicans-on-a-bicycle/">Pelicans on a bicycle | Simon Willison ’s Weblog</a></li>
<li><a href="https://pelicanbenchmark.com/">Pelican Riding a Bicycle — Pelican Benchmark</a></li>
<li><a href="https://ofox.ai/blog/claude-sonnet-5-5-effort-high-xhigh-max/">Sonnet 5.5 effort : when to use medium, high or max</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude Sonnet 5.5`, `#LLM`, `#AI model release`, `#Simon Willison`

---

<a id="item-9"></a>
## [NASA 招募前 SR-71 团队成员，秘密重启黑鸟计划](https://aviationweek.com/defense/aircraft-propulsion/nasa-asked-several-former-sr-71a-staffers-help-secret-restart) ⭐️ 6.0/10

《Aviation Week》报道称，NASA 已邀请多位前 SR-71A 项目工作人员参与一项被描述为“秘密”的努力，目标是让一架 SR-71A“黑鸟”侦察机在退役 25 年多后重新飞上天空。涉及的对象是编号 844 的 SR-71，它是最后一架被制造、也是最后一架飞行的黑鸟，NASA 最近将其从公开展示位置移入机库，局长 Jared Isaacman 也对此做了暗示性的预告。 重启黑鸟将是一项极其艰巨的工程与后勤挑战，因为维持 SR-71 飞行所需的工装、备件供应链、燃料生产以及大量机构经验，自 1999 年退役以来已被有意拆解殆尽。这一消息也引发了更广泛的争论：在侦察卫星和无人机逐步接管相关任务之际，是否值得把老旧装备重新复活作为权宜之计。 前黑鸟工作人员表示，NASA 团队面临的是一长串“看似无法攻克的难题”：美国空军和 NASA 在 2007 年销毁了价值约 6 亿美元的 SR-71 备件，如今没有任何其他飞机使用 SR-71 专用的 JP-7 燃料，而且需要重新改装一架加油机来携带这种燃料。SR-71 本身可在 8.5 万英尺高空以 3.2 马赫飞行，NASA 是其最后的运营方，作为研究平台一直使用到 1999 年退役。

hackernews · ilamont · 9月29日 10:10 · [社区讨论](https://news.ycombinator.com/item?id=49890733)

**背景**: SR-71“黑鸟”是洛克希德“臭鼬工厂”在 1960 年代由工程师克拉伦斯·“凯利”·约翰逊主持研制的远程高空战略侦察机，速度超过 3 马赫，1966 年 1 月进入美国空军服役。该机共生产 32 架，其中 12 架因事故损失，从未被敌方击落；1976 年它还创下了至今未被打破的最快有人驾驶吸气式飞机纪录。美国空军先后于 1989 年和 1998 年将其退役，此后 NASA 继续以研究平台身份使用部分机体，直至 1999 年。此后其侦察角色由卫星和无人机接手，而洛克希德·马丁提出的后继机型 SR-72 至今仍停留在概念阶段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aviationweek.com/defense/aircraft-propulsion/nasa-asked-several-former-sr-71a-staffers-help-secret-restart">NASA Asked Several Former SR-71A Staffers To Help Secret Restart</a></li>
<li><a href="https://theaviationist.com/2026/09/28/is-nasa-sr-71-blackbird-returning-to-flight/">Is An SR-71 Blackbird Returning to Flight 27 Years Later?</a></li>
<li><a href="https://en.wikipedia.org/wiki/SR-71A_Blackbird">SR-71A Blackbird</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论总体持怀疑态度：多人指出，一项“秘密”到人人都知道的复飞计划本身就有些奇怪，还有人把它与今年早些时候的蒸汽弹射器争议相提并论，认为重拾 60 年前的技术并不令人振奋。另一些评论聚焦现实障碍，指出 2007 年销毁的 6 亿美元备件、JP-7 燃料停产以及需要改装加油机，都让重新服役的代价极其高昂。一位与 SR-71 后座飞行员有私人交集的评论者对让飞行员重返该机表达了安全担忧，也有人认为，性能优于 SR-71 的机型（很可能是无人的）恐怕早已从 Groom Lake 之类的基地夜航多年。

**标签**: `#aerospace`, `#SR-71`, `#NASA`, `#military-technology`, `#aviation`

---

<a id="item-10"></a>
## [白宫推出 America.gov：面向政府服务的 AI 聊天机器人](https://america.gov/) ⭐️ 6.0/10

白宫正式上线 America.gov，这是由总统唐纳德·特朗普宣布推出的 AI 聊天机器人门户，把约 2.9 万至 3 万个官方政府信息源整合进一个对话式界面。用户可以用文字或语音提问，内容涵盖福利、登记与续期等事务，还能上传附件，随后在页面上获得 AI 生成的回答。谷歌确认自己是该项目的发布合作伙伴，其 Gemini 模型参与其中，另有报道称 SpaceX 的 Grok 也为该站点提供支持。 如果运转良好，单一入口可以让民众不必再在联邦网站迷宫中摸索，并降低被钓鱼的风险，这对申请应得福利的人来说是体验上的重大改善。同时，这也是一次高调的检验：大语言模型能否被信任来承载权威的公共信息，谷歌以及据称的其他 AI 厂商都把声誉押在了结果之上。 据报道，该站点调用了超过 2.9 万个官方政府信息源，除文字聊天外还支持语音输入与附件上传，但早期报道指出，回答如何被验证或审核尚不明确。从表现看，这套系统很可能是 Gemini 加上严格护栏（guardrails）的实现，因此已经会对部分问题直接拒答，同时可访问性与老旧浏览器支持情况仍存疑问。

hackernews · plesiv · 9月29日 14:04 · [社区讨论](https://news.ycombinator.com/item?id=49893509)

**背景**: 美国的联邦服务分散在成千上万个不同的机构网站上，找对表格、资格规则或续期截止日期一直是常见抱怨，而诈骗者往往利用这种困惑搭建仿冒的钓鱼页面。由谷歌 Gemini 等大语言模型驱动的 AI 聊天机器人能以对话方式汇总和引导这类信息，但它们也容易自信地给出错误答案，因此政府部门会配套使用护栏来限制其可讨论的范围。America.gov 是美国联邦政府首次尝试把这类模型放在公共服务的“正门”位置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/09/29/can-a-chatbot-fix-the-government-maze-the-white-house-is-about-to-find-out/">Can a chatbot fix the government maze? The White... | TechCrunch</a></li>
<li><a href="https://www.axios.com/2026/09/29/america-gov-trump-ai-website">America . gov is live. Here's everything to know about Trump's new AI ...</a></li>
<li><a href="https://www.zerohedge.com/political/trump-launches-americagov-website-simplifying-access-government-services">Trump Launches America . Gov Website Simplifying... | ZeroHedge</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的情绪介于谨慎赞赏与调侃之间：有评论认为这个想法在宏观层面很棒，因为普通人确实很难知道该去哪里办事，也容易被钓鱼；另一些人则以玩笑回应机器人拒绝回答历史问题或不愿谈论歌词。用户还批评了界面设计，例如一个指纹解锁图标遮住了有关隐私保护的文字且无法关闭；也有一位评论者指出其技术栈是 Gemini 加护栏，并引用了谷歌自家的博客文章。

**标签**: `#AI`, `#Government`, `#Chatbot`, `#UX`, `#Hacker News`

---

<a id="item-11"></a>
## [Backblaze 发布 2026 年第二季度硬盘可靠性统计报告](https://www.backblaze.com/blog/backblaze-drive-stats-for-q2-2026/) ⭐️ 6.0/10

Backblaze 发布了 2026 年第二季度硬盘统计报告，公布了其自家云存储数据中心大规模硬盘阵列中收集的故障率数据。这份报告属于其例行发布的实测数据更新，而非方法论变更或新产品发布。 Backblaze 的硬盘统计是少数公开的大规模真实环境硬盘故障数据来源之一，因此常被家庭实验室用户、NAS 用户和数据中心运维人员用来选购硬盘或判断更换时机。该报告也参与并推动了整个行业关于现代大容量机械硬盘是否越来越可靠、以及存储经济性是否正在变化的讨论。 这些统计本质上属于观测数据：只覆盖 Backblaze 自己采购的硬盘型号、固件版本和工作负载，因此并非受控基准测试，市面上同名型号的消费级硬盘表现可能并不相同。有评论者指出数据反映出的长期趋势——2013 年约三年时故障率约 14%，而 2025 年约十年时故障率仅约 5%——说明随着硬盘技术成熟，故障率已明显下降。

hackernews · HieronymusBosch · 9月29日 13:34 · [社区讨论](https://news.ycombinator.com/item?id=49893002)

**背景**: Backblaze 是一家成立于 2007 年的美国云备份与存储公司，其数据中心运行着数万块消费级硬盘。自 2013 年起，该公司每季度发布“Drive Stats”报告，公布其硬盘阵列中各型号硬盘的年化故障率（AFR），这为外界观察机械硬盘在生产环境中的实际老化情况提供了一个罕见的公开窗口。机械硬盘至今仍是大容量廉价存储的主流介质（固态硬盘则主攻速度），而大容量 HDD 的可靠性直接关系到 RAID 阵列、NAS 设备、备份系统与冷数据归档。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Backblaze">Backblaze - Wikipedia</a></li>
<li><a href="https://www.backblaze.com/">High-Performance Cloud Storage for AI Workloads | Backblaze</a></li>
<li><a href="https://www.pcmag.com/reviews/backblaze">Backblaze Review: A Simple Set-and-Forget Backup ... - PCMag About Backblaze | Cloud Storage & Data Protection Company Backblaze Review (2026): Pros, Cons & Verdict - SoftVerdict What is a backup? What is Backblaze? – Backblaze Help Backblaze Review 2026: Pricing, Features, Security & More</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上肯定这份数据的长期价值，有人还汇总数据指出硬盘可用寿命已从 2013 年的约四年延长到 2025 年的约十年。另一些人则聚焦成本与实际困扰：有用户反映硬盘价格几乎翻倍，两块 WD Red 6TB NAS 硬盘两年内相继损坏，获得的退款按现价已买不起同款。还有一个反复出现的技术担忧是，机械硬盘容量不断增长而顺序读写速度几乎没变，导致超大容量硬盘的阵列重建和整盘读取需要数天时间。

**标签**: `#storage`, `#hard-drives`, `#reliability`, `#Backblaze`, `#data-centers`

---

<a id="item-12"></a>
## [PS5「Relapse」漏洞可越狱 7.00 至 13.60 固件主机](https://github.com/ntfargo/Relapse-Exploit) ⭐️ 6.0/10

一个名为 Relapse 的公开漏洞利用已在 GitHub（ntfargo/Relapse-Exploit）发布，可让运行 7.00 至 13.60 固件的 PlayStation 5 主机实现越狱并加载自制程序（homebrew payload）。据项目仓库说明，9 月 16 日及之后更新的主机并不兼容，因此并非所有 PS5 用户都能使用。 Relapse 覆盖了相当宽的当代主机固件范围，为 PS5 越狱社区提供了一个久违的、适用范围较广的入口，也会促使索尼采取防御性措施。它同时再次引发关于索尼存档备份限制与 DRM 的争论，因为越狱往往是玩家把存档复制到本地存储的唯一途径。 该攻击链分为两个阶段：先利用基于浏览器的 WebKit JavaScriptCore 漏洞，再配合一个内核漏洞，二者结合才能进入越狱环境。与多数此类发布一样，维护者声明对由此造成的损害不承担责任；而索尼一种可能的反制手段是禁用或收窄 WebKit 的 JIT，以缩小攻击面。

hackernews · therepanic · 9月29日 15:44 · [社区讨论](https://news.ycombinator.com/item?id=49895304)

**背景**: JavaScriptCore 是 WebKit 内置的 JavaScript 引擎，而 WebKit 也是 Safari 使用的浏览器引擎；游戏主机为渲染网页内容同样嵌入了 WebKit，因此一个浏览器漏洞就可能成为执行未签名代码的第一块跳板。越狱让主机能够运行索尼未签名的代码，从而启用自制工具（包括存档管理工具），有时也会被用于盗版。索尼的 PS5 将游戏存档备份限制在通过 PS Plus 进行的云端备份，这是一项付费订阅，在部分区域还需要为每个用户档案单独购买。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.superpsx.com/ps5-relapse-jailbreak-13-60-and-lower-complete-guide/">PS 5 Relapse Jailbreak 13.60 and Lower – Complete Guide</a></li>
<li><a href="https://www.notebookcheck.net/Insider-thinks-the-PlayStation-DRM-may-brick-jailbroken-PS5s-to-counter-piracy.1287741.0.html">Insider thinks the PlayStation DRM may brick jailbroken PS5s ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上 152 条评论的讨论焦点并非漏洞本身，而是存档问题的挫败感：有评论者称，直到女儿因数据损坏损失了一年的《Minecraft》进度后，才发现 PS5 不允许像 PS1 至 PS4 那样把存档备份到 USB，而且云存档还需要为每个用户档案单独订阅 PS Plus。其他人则推测越狱团队手里还攥着用于突破引导程序层级的零日漏洞，并警告索尼可能会以禁用 JavaScriptCore 的 JIT 作为回应；也有人调侃要等到《GTA 6》再放出漏洞，还有人认为能在 PS5 上玩 Steam 游戏会是一大胜利。

**标签**: `#security-exploit`, `#ps5`, `#jailbreak`, `#webkit`, `#drm`

---

<a id="item-13"></a>
## [OpenAI 安全人员警告 AI 能力跃升超出防御准备](https://simonwillison.net/2026/Sep/28/joedaroo/) ⭐️ 6.0/10

在 Simon Willison 转载的一段引文中，一位被确认为 OpenAI Agent Security 团队成员、账号名为@joedaroo 的人表示，其模型在“cyber（网络）”、“swarming（集群）”、“message boards（留言板）”等方面的能力提升之快、之突然，让组织措手不及，并由此带来了极其棘手的安全与事件响应难题。 这是一次罕见的内部人士表态：前沿 AI 实验室也可能被自家模型涌现出的能力打个措手不及，这意味着依赖这些实验室安全承诺的客户、企业和监管者，同样可能面对无人来得及准备的新型风险。 这段引文强调，安全态势是一项缓慢的文化工程——不仅是加固系统，还要让组织内部的人员与流程随之改变；结尾提出一系列自我评估问题，追问团队、沟通机制与事件响应能否扛住一次 AI“意外”。该账号身份由 The Information 的 Rocket Drew 确认，但文中始终没有说明具体事件与能力领域究竟指什么。

rss · Simon Willison · 9月28日 19:11

**背景**: Simon Willison 的博客经常引用 AI 从业者发布的简短而值得注意的言论，并附上出处与背景说明，而非原创报道。事件响应（incident response）是安全领域的标准流程，指对入侵事件进行发现、遏制与恢复；“能力跃升”（capability jump）则指模型在扩大规模或继续训练后，能力突然且常常出人意料地提升。这段引文的预设是：AI 系统获得危险或破坏性能力的速度，可能快于组织建立相应文化与管理流程的速度。

**标签**: `#ai-safety`, `#ai-security`, `#incident-response`, `#capability-jumps`, `#organizational-resilience`

---