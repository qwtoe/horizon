---
layout: default
title: "Horizon Summary: 2026-11-17 (ZH)"
date: 2026-11-17
lang: zh
---

> 从 21 条内容中筛选出 13 条重要资讯。

---

1. [Jiff 1.0 发布：burntsushi 推出全新 Rust 日期时间库](#item-1) ⭐️ 8.0/10
2. [卡内基梅隆大学推出 CS Learn，在 YouTube 上免费发布完整计算机科学课程](#item-2) ⭐️ 7.0/10
3. [Optimizely 被曝遭入侵，通过脚本向 Zoom、GitLab 等站点投放恶意软件](#item-3) ⭐️ 7.0/10
4. [Linebender 深入探讨方圆形与曲率连续曲线](#item-4) ⭐️ 7.0/10
5. [开发者反思 Rust 如何重塑其编码思维](#item-5) ⭐️ 7.0/10
6. [Windows 11 遥测被曝收集用户所用编码智能体与开发工具信息](#item-6) ⭐️ 6.0/10
7. [共享登录绕过注册墙的老牌服务 BugMeNot 已关闭](#item-7) ⭐️ 6.0/10
8. [化学本质上是几何？一篇随笔引发还原论争论](#item-8) ⭐️ 6.0/10
9. [TRMNL 推出 Frame：31.5 英寸彩色电子纸显示屏，售价 1200 美元](#item-9) ⭐️ 6.0/10
10. [康奈尔报告：太阳能阵列下放牧绵羊可带来经济与生态双重收益](#item-10) ⭐️ 6.0/10
11. [摩根大通技术故障导致美国多家银行网上银行服务中断](#item-11) ⭐️ 6.0/10
12. [Datasette 1.0a43 发布：新增流式输出渲染器并修复安全问题](#item-12) ⭐️ 6.0/10
13. [datasette-apps 0.4a0 发布：沙盒 SQL 小应用支持 URL 片段互相链接](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Jiff 1.0 发布：burntsushi 推出全新 Rust 日期时间库](https://burntsushi.net/jiff/) ⭐️ 8.0/10

ripgrep 和 regex crate 的作者 Andrew Gallant（burntsushi）发布了 Jiff 1.0，这是一个面向 Rust 的日期时间库，目标是用高层、难以误用的 API 取代常见陷阱。1.0 版本包含时区数据库集成、支持夏令时（DST）的算术运算，以及带时区日期时间的解析与格式化能力。 Rust 长期依赖事实上的标准日期时间库 chrono，尽管其 API 局限广为人知，因此由备受信任的维护者推出的成熟替代品为生态提供了真正的选择。日期时间处理在服务器、调度器和数据管道中无处不在，因此时区与夏令时正确性的提升可以减少大量 Rust 软件中的缺陷。 Jiff 明确的设计目标是通过难以误用的原语和合理的性能把用户引向“成功的陷阱”（pit of success），并提供可选的 Serde 序列化支持。值得注意的是，它仅支持 Unix 时间标度，因此需要为天文或轨道计算使用 TAI、UT1 等其他时间标度的用户，被建议改用 hifitime 等替代库。

hackernews · burntsushi · 11月16日 16:53 · [社区讨论](https://news.ycombinator.com/item?id=50519744)

**背景**: 日期时间库负责日期与时间的解析、格式化、算术运算和时区转换，由于闰秒、夏令时切换以及本地时间存在歧义或不存在的时刻，这一领域出了名的微妙。多年来，chrono crate 一直是 Rust 的默认选择，但其 API 设计长期被批评容易出错。Gallant 因 ripgrep 和 regex crate 而在 Rust 社区广为人知，这两个项目都以严谨的设计和文档著称，因此他进入这一基础领域立刻引发了关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50519744">Jiff 1.0: A datetime library for Rust | Hacker News</a></li>
<li><a href="https://docs.rs/jiff/latest/jiff/">jiff - Rust</a></li>
<li><a href="https://www.websitehunt.co/websites/jiff-rust-datetime-library">Jiff : Rust datetime library - Website Hunt</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论总体热烈，评论者称赞 Jiff 的质量，并希望更广泛的生态从 chrono 迁移过来。一位前 chrono 维护者坦率地表示，留住用户的是 API 稳定性而非质量，由此产生的倦怠感让他选择退出；也有人赞赏 Jiff 坦诚说明自己并非适用于所有场景。技术疑问集中在时间标度语义上，一位从事轨道模拟的评论者询问对 TAI 和 UT1 的支持，也有至少一位用户表示 chrono 已经足够好，自己没有理由切换。

**标签**: `#rust`, `#datetime`, `#open-source`, `#library-release`, `#time-handling`

---

<a id="item-2"></a>
## [卡内基梅隆大学推出 CS Learn，在 YouTube 上免费发布完整计算机科学课程](https://www.cs.cmu.edu/learn/) ⭐️ 7.0/10

卡内基梅隆大学推出了 CS Learn 项目，将当前 CMU 计算机科学课程的整学期讲座免费发布到 YouTube 上，发布当周每天上线一门课程，明年一月还会有更多课程推出。该项目由 CMU 格里芬计算机科学学院的 Phillip Compeau 负责，并由几位 CMU 学生开发了用于自动化大部分制作流程的工具。 CMU 是全球最顶尖的计算机科学项目之一，因此发布当前课程的完整学期讲座（而非旧版或精简材料），让全球自学者和学生能够接触到与在校付费学生相同的教学内容。这也延续了由 MIT 开创的开放式课程资源（open courseware）趋势，而本次发布强调自动化制作流程，意味着上线速度可能远快于此前的同类项目。 Compeau 坦承 MIT 的 OpenCourseWare 大约早了 25 年，并表示 CS Learn 的新意在于制作方式而非概念本身。配套课程资料（项目、幻灯片、讲义和反馈机制）计划作为后续工作推出，而像 15-259 概率与计算这样的进阶课程预计很快上线。

hackernews · pcompeau · 11月16日 20:43 · [社区讨论](https://news.ycombinator.com/item?id=50522980)

**背景**: 开放式课程资源（open courseware）是一项由大学公开发布课程材料、并越来越多地包括完整讲座视频以供任何人免费使用的运动，其中最著名的例子是 MIT 于 2000 年代初推出的 OpenCourseWare。历史上这类发布并不均衡，往往缺少进阶或研究生课程，以及让一门课真正完整的作业环节。CMU 此前其实也发布过讲座录像，例如广为人知的数据库系统课程，但 CS Learn 将这项工作组织成了一个协调、持续的项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Carnegie_Mellon_University">Carnegie Mellon University - Wikipedia</a></li>
<li><a href="https://www.cmu.edu/">Carnegie Mellon University | CMU</a></li>

</ul>
</details>

**社区讨论**: 社区反响非常积极，评论者纷纷点名期待看到的具体课程，例如 15-259 概率与计算。主要保留意见是实用层面的：一位评论者认为，如果缺少项目和反馈，仅有讲座视频效果会大打折扣，并抱怨这类发布常常只包含入门课而跳过研究生编译器之类的进阶课程。另一位则提出了被广泛认同的观点：把基础学扎实，AI 就会成为你的强力工具，否则它就会取代你。

**标签**: `#education`, `#computer-science`, `#open-courseware`, `#online-learning`, `#CMU`

---

<a id="item-3"></a>
## [Optimizely 被曝遭入侵，通过脚本向 Zoom、GitLab 等站点投放恶意软件](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/) ⭐️ 7.0/10

据 report-uri.com 报道，营销实验平台供应商 Optimizely 遭到入侵，攻击者利用其被嵌入到 Zoom、GitLab 等高流量站点的第三方 JavaScript 投放恶意软件。由于恶意载荷是通过可信供应商的脚本而非站点自有代码下发的，访问这些页面的用户可能在站点本身并未被攻破的情况下就遭到感染。 这是一次典型的 Web 供应链攻击：一个被广泛部署的营销脚本，摇身一变成为面向众多互不相关品牌、覆盖数百万访客的分发渠道。它凸显出第三方标签与优化供应商实际上已成为每个客户攻击面的一部分，而由营销部门控制的脚本注入则绕过了自有代码变更通常要经历的代码审查。 根据对该报告的讨论，注入的代码会从两个 .icu 域名加载 boot.js，并在 iOS 18.6 及更早版本上嵌入一个隐藏 iframe，评论者认为这看起来是一条漏洞利用链（被指为 Coruna 与 DarkSword）。该事件表明，即便是发布流程相对成熟的供应商，也可能把恶意或被篡改的代码包直接推送到生产环境，而客户端对此没有任何拦截环节。

hackernews · kristjansson · 11月16日 23:00 · [社区讨论](https://news.ycombinator.com/item?id=50524767)

**背景**: Optimizely 是一款广泛使用的营销平台，用于 A/B 测试、实验与个性化；客户在其页面中安装它的代码片段，营销团队便可在不发布新代码的情况下修改页面内容、运行测试。这与 Google Tag Manager 普及的模式相同：非工程人员也能添加第三方“标签”（分析、广告、热力图、在线客服组件等），而这些标签会在每位访客的浏览器中执行任意 JavaScript。这种便利制造了供应链盲区——一旦供应商自身的基础设施或构建流水线被攻破，所有加载该脚本的站点都会继承恶意载荷。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.velir.com/ideas/what-is-optimizely">What is Optimizely ? | Velir</a></li>
<li><a href="https://jscrambler.com/blog/managing-third-party-tags-hospitality-industry">Managing Third - Party Tags in the Hospitality Industry | blog</a></li>
<li><a href="https://www.geetest.com/en/article/what-is-formjacking">Formjacking Attacks : How They Work and the Best Ways to Prevent...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者批评态度鲜明：他们认为 Google Tag Manager 这类标签管理器是用安全性换取营销便利，还让页面变得臃肿，而 Optimizely 与大型内容站点都没有为此承担真正的责任。有人建议供应商一侧应引入分阶段发布、冷却期和自动化安全检查等防护措施，客户端则可用 NoScript 等工具降低暴露面；也有人指出，iOS 上的载荷更像是定向漏洞利用链，而非普通恶意软件。

**标签**: `#security`, `#supply-chain`, `#third-party-scripts`, `#malware`, `#web`

---

<a id="item-4"></a>
## [Linebender 深入探讨方圆形与曲率连续曲线](https://linebender.org/wiki/curves/squircle/) ⭐️ 7.0/10

Linebender 项目发布了一篇技术 wiki 页面，探讨方圆形（squircle）以及平滑、曲率连续形状的数学，涉及样条曲线和超椭圆。文章分析了这类曲线的构造方式及其在图形与设计中的意义。 这项探索很重要，因为曲率连续性直接影响形状的视觉与触感：曲率突变会产生可见的折角或着色伪影，而平滑过渡被广泛用于界面图标、字体和工业设计。它为开发者和设计师提供了超越简单 border-radius 圆角矩形的共同数学语言。 讨论指出，相关图表通常以弧长为横轴、曲率为纵轴，这是可视化 G2 连续性的一种常见方式；涉及的相关构造包括超椭圆（Lamé 曲线）、样条曲线和回旋曲线（clothoid）。方圆形并非单一标准形状：该词指介于正方形与圆形之间的形状，目前至少有两种数学定义在使用。

hackernews · raphlinus · 11月16日 07:55 · [社区讨论](https://news.ycombinator.com/item?id=50515151)

**背景**: 方圆形（squircle）是介于正方形与圆形之间的形状，最常见的数学构造是超椭圆（Lamé 曲线），其方程为 |x/a|^n + |y/b|^n = 1。普通的圆角矩形将直边与圆弧连接，在连接处可能出现曲率的突然跳变。曲率连续曲线（有时称为 G2 连续）让曲率在过渡中平滑变化，这正是 Apple 的 iOS 图标和许多现代界面系统采用类方圆形而非简单 border-radius 圆角的原因。样条曲线是用于建模这类形状的分段多项式曲线，而回旋曲线（clothoid）的曲率随弧长线性变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Squircle">Squircle - Wikipedia</a></li>
<li><a href="https://squircle.js.org/blog/what-is-a-squircle">What is a Squircle ? - Squircle .js</a></li>
<li><a href="https://www.appscreenstudio.com/en/blog/understanding-ios-squircle-continuous-curvature">The Math Behind iOS Bezels: Continuous... | AppScreenStudio</a></li>

</ul>
</details>

**社区讨论**: 评论者欢迎这篇深度文章并补充了实用资源：一位正在开发实验性的样条/超椭圆/回旋曲线创作工具，另一位则指出更高维度的“sphube”是相关形状。多位评论者强调，导数连续性正是曲线能用于物理交互和设计的关键，还有人说明文章图表的横轴是弧长、纵轴是曲率。

**标签**: `#geometry`, `#curves`, `#graphics`, `#design`, `#splines`

---

<a id="item-5"></a>
## [开发者反思 Rust 如何重塑其编码思维](https://blog.startifact.com/posts/how-rust-changed-me/) ⭐️ 7.0/10

Startifact 上的一篇博客文章回顾了作者学习 Rust 后编码习惯的改变，并在 Hacker News 引发 181 分、119 条评论的热议，讨论将 Rust 的类型系统与错误处理同 Zig 进行比较。 这场讨论凸显 Rust 的所有权与显式错误处理模型如何重塑开发者习惯，也延续了关于语言设计应如何表示失败与和类型（sum types）、并与 Zig 等替代方案比较的争论。 评论者对 Rust 枚举（将标签与关联数据合在一起）与 Zig 将 enum 和 union 分离的设计孰优孰劣存在分歧；也有人赞赏 Rust 在可能失败时强制做出显式决定，尽管 unwrap 仍可能被误用。

hackernews · speckx · 11月16日 20:16 · [社区讨论](https://news.ycombinator.com/item?id=50522563)

**背景**: Rust 是一种系统编程语言，以编译期的所有权和借用规则著称，能在没有垃圾回收器的情况下防止许多内存安全错误。它的 Result 和 Option 枚举让错误与缺失值处理变得显式；Zig 则是较新的系统编程语言，强调简单性和显式控制，使用错误联合（error unions）以及分离的 enum/union 概念。相比之下，C 更依赖开发者自觉检查 NULL 等约定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://learningzig.org/lessons/06-error-handling">Error Handling · Learn Zig | LearningZig.org</a></li>

</ul>
</details>

**社区讨论**: 整体情绪对这篇文章持正面态度，评论者称其文笔和设计俱佳，同时讨论也深入技术细节。bryanlarsen 认为开发者应在不同语言家族中各做一个大型项目，dabinat 赞赏 Rust 承认人可能犯错，xeubie 则批评 Rust 枚举把标签类型与联合类型混在一起，而 Zig 将二者分开。sedatk 还补充了一种历史反讽：C 当年因不受检查的强大而受推崇，如今安全却成为优先事项。

**标签**: `#rust`, `#programming-languages`, `#type-systems`, `#error-handling`, `#zig`

---

<a id="item-6"></a>
## [Windows 11 遥测被曝收集用户所用编码智能体与开发工具信息](https://xusheng.dev/posts/windows-coding-agent-telemetry/) ⭐️ 6.0/10

xusheng.dev 上的一篇博客文章指出，Windows 11 内置的遥测机制会收集用户机器上正在运行哪些 AI 编码智能体和开发工具的信息。该发现在 Hacker News 上引发讨论，获得约 225 分和 107 条评论。 一台机器上安装了哪些开发工具和 AI 编码智能体，往往能反映出个人的工作流程、所属公司使用的工具链，甚至所处理代码的类型；把这类信息作为操作系统级遥测上报，对那些以为编辑器和命令行工具选择只留在本地的开发者来说，是一个实实在在的隐私问题。这也给围绕 Windows 诊断数据的长期争论添了一把火，并为注重隐私的开发者又多提供了一个转向 Linux 或 macOS 的理由。 这份报告基于作者自己对 Windows 11 上报内容的观察，而非正式的审计，Hacker News 上的讨论也没有明确说清具体上报了哪些字段，或给出审计、阻断收集的操作方法。由于 Windows 提供了诊断数据级别选项（例如“仅必选”与可选/完整级别）以及企业组策略控制，实际的缓解手段在很大程度上取决于 Windows 版本以及该设备是否由 IT 部门统一管理。

hackernews · cwaffles · 11月16日 22:58 · [社区讨论](https://news.ycombinator.com/item?id=50524736)

**背景**: 自 Windows 10 起，Windows 就内置了诊断数据收集（通常称为遥测）：系统会定期向微软发送使用情况、配置和可靠性信息，用户可以在最低限度的“仅必选”级别和更完整的可选级别之间选择，管理员则可以通过组策略和注册表设置进一步限制收集范围。这里的“编码智能体”指的是 AI 驱动的开发工具——基于终端的助手或集成在 IDE 中的智能体——它们会读取、修改并执行项目中的代码，因此相比普通的应用使用情况遥测，得知机器上存在哪些编码智能体所泄露的信息要多得多。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Privacy_in_Microsoft_Windows">Privacy in Microsoft Windows</a></li>
<li><a href="https://en.wikipedia.org/wiki/Microsoft_Windows">Microsoft Windows - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 整体情绪明显偏向对隐私的怀疑，但讨论很快转向了对 Linux 的推崇：一位评论者认为，到 2026 年 Linux 已经成为真正可用的游戏平台，单机游戏体验完美，只有多人游戏还会有些毛病；另一位则表示迁移大约只需要一周时间，并推荐 Ubuntu、Fedora 或 Mint，称“没有错误答案”。还有人更进一步，表示自己已经不再做双系统，需要时会在虚拟机里跑 Windows，其中一位计划转向 Omarchy；也有一位评论者直言怀疑 Windows 11 收集的数据远不止文章所记录的那些。

**标签**: `#windows`, `#privacy`, `#telemetry`, `#developer-tools`, `#linux`

---

<a id="item-7"></a>
## [共享登录绕过注册墙的老牌服务 BugMeNot 已关闭](https://www.bugmenot.com/) ⭐️ 6.0/10

曾让用户检索并共享用户名和密码、以跳过网站强制注册流程的 BugMeNot 已经下线，结束了二十多年的运营。其主页如今只剩下一则关闭通知，而 Hacker News 上 315 分、160 条评论的讨论则通过引用维基百科条目来为读者补充背景信息。 BugMeNot 是 2000 年代早期开放网络的象征，那个时代注册墙被视为麻烦而非商业模式，因此它的关闭成为网络转向账号体系、用户追踪和付费墙的一个文化里程碑。该服务的消失也凸显出现代反滥用机制、邮箱验证与法律压力如何让众包式的凭据共享变得不可行。 评论者指出，过去五年里随着网站打击共享账号和被滥用的凭据，几乎所有 BugMeNot 登录都失效了，而且网站本身可以申请从该数据库中移除自己。作为替代方案，用户如今转而依赖临时邮箱或隐藏邮箱服务以及一次性账号，不过许多网站对临时邮箱域名的识别能力已明显增强。

hackernews · lode · 11月16日 21:32 · [社区讨论](https://news.ycombinator.com/item?id=50523601)

**背景**: BugMeNot 于 2003 年 8 月上线，由一位匿名创建者（后来被确认为 Guy King）发起，最初只是一个周末项目。它针对的是越来越多要求免费注册才能阅读内容的新闻与内容网站（例如《纽约时报》），用户普遍认为这种注册既麻烦又可能招来垃圾邮件。该服务本质上是一个众包数据库：用户提交可用的账号密码，其他人按域名查询使用；对于社区型站点或按次付费站点，站方可以申请将其从数据库中移除。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/BugMeNot">BugMeNot</a></li>
<li><a href="https://grokipedia.com/page/BugMeNot">BugMeNot</a></li>

</ul>
</details>

**社区讨论**: 讨论整体弥漫着怀旧但又无奈的情绪：多位评论者回忆多年前用过 BugMeNot 并称其非常有用，也有人表示近些年几乎没有一次登录成功。主流解释是网站因共享凭据被恶意行为者滥用而加强了封堵，还有评论者认为这种模式注定难以为继——若它真能大规模运作就会被合法手段关停，而按本性它又无法在小规模下发挥作用。

**标签**: `#internet-culture`, `#web-history`, `#authentication`, `#privacy`, `#paywalls`

---

<a id="item-8"></a>
## [化学本质上是几何？一篇随笔引发还原论争论](https://chillphysicsenjoyer.substack.com/p/chemistry-is-actually-geometry) ⭐️ 6.0/10

发表在 Chill Physics Enjoyer 通讯上的一篇题为《化学本质上是几何》的 Substack 随笔认为，化学行为可以被归结为几何原理来理解。该文登上 Hacker News 首页，获得约 107 分和 35 条评论，讨论这类类比究竟是在描述真实世界，还是仅仅是有用的模型。 这篇随笔并非技术突破，而是一种哲学上的挑衅：它重新打开了关于科学还原论的长期争论——数学描述究竟是对自然的发现，还是便利的“地图”。这些讨论关系到科学家和教育者如何为用更简单的形式结构去建模化学反应等复杂系统提供理由。 评论者指出，文章自身关于“令人惊讶的行为”的一节反而削弱了那套整洁的几何叙事，因为诸如 pH 与其他性质之间的振荡等现象并没有明显的现实几何对应物。还有人指出，化学其实已经可以相当干净地还原为量子电动力学（QED）的第一性原理，而文中描述的框架早已被称为动力系统理论。

hackernews · sebg · 11月16日 20:22 · [社区讨论](https://news.ycombinator.com/item?id=50522643)

**背景**: 科学还原论是一种哲学立场，认为复杂现象可以用更简单、更基本的现象来描述，即系统是其各部分之和，这与整体论相对。与之相关的争论是科学实在论与工具主义之争：前者认为成功的理论至少近似地描述了真实世界，后者则把理论视为预测工具、不必与世界的真实结构对应。Hacker News 上的这场讨论，实质上就是在化学与几何这一具体案例上重演了这些争论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Scientific_reductionism">Scientific reductionism</a></li>
<li><a href="https://memorywizards.com/scientific-knowledge/scientific-realism-vs-instrumentalism/">Scientific Realism Vs . Instrumentalism Explained | Memory Wizards</a></li>

</ul>
</details>

**社区讨论**: 整体氛围是欣赏但怀疑这种还原论框架：最高赞评论警告不要把“地图”当成“疆域”，称该类比虽然有用却无法被证明。其他人则用动力系统以及“所有自然科学都是随时间演化的几何”这一思路重新表述该主张，还有评论者承认像 pH 振荡这样的现象难以用简单的几何来解读。

**标签**: `#chemistry`, `#geometry`, `#philosophy-of-science`, `#reductionism`, `#education`

---

<a id="item-9"></a>
## [TRMNL 推出 Frame：31.5 英寸彩色电子纸显示屏，售价 1200 美元](https://trmnl.com/blog/introducing-frame) ⭐️ 6.0/10

TRMNL 发布了 Frame，这是一块 31.5 英寸的彩色电子纸显示屏，售价 1200 美元，标志着这家独立硬件公司从 7.5 英寸的小型仪表盘面板跨入大尺寸壁挂屏领域。该消息在 Hacker News 上引发热议，帖子获得 295 分、207 条评论，讨论集中在价格与实用性上。 大尺寸彩色电子纸此前主要面向零售、物流等商用数字标牌市场，因此一款面向消费者、并公开标价的产品向普及迈出了值得注意的一步。1200 美元的价格让它仍属于发烧友级别，但这也说明 30 英寸以上的电子纸面板正开始对个人买家开放，而不再只服务企业客户。 讨论的核心在于，受专利保护的电子纸供应链是否是这一尺寸面板价格高企的原因；评论者还指出，彩色电子纸刷新速度慢，更适合静态或低频更新的内容，而非视频。TRMNL 早期设备主打开源与插件生态，因此 Frame 的成败很可能同样取决于软件与可靠性，而不只是面板本身。

hackernews · geerlingguy · 11月16日 16:23 · [社区讨论](https://news.ycombinator.com/item?id=50519354)

**背景**: 电子纸（E Ink）显示屏具有双稳态特性：只有在画面变化时才耗电，因此非常适合常亮的信息面板和数字标牌。TRMNL 是一家自力更生的独立消费电子公司，由 Ryan Kulp 于 2023 年创立，其首款电子纸设备在 2024 年通过众筹上市，最初定位为可显示日历、天气并支持 1000 多个插件的“免打扰”仪表盘。彩色电子纸面板通常在黑白墨水层上叠加彩色滤光层，这往往会降低对比度和刷新速度；而 30 英寸以上的大尺寸面板此前主要作为商用标牌硬件销售。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://trmnl.com/">ePaper dashboard to stay focused | TRMNL</a></li>
<li><a href="https://arstechnica.com/gadgets/2026/11/this-48-e-paper-display-can-be-whatever-you-want-it-to-be/">This $48 e - paper display can be whatever you want it... - Ars Technica</a></li>
<li><a href="https://www.datallen.com/blogs/the-color-epaper-display-guide.html">The Color E - Paper Display Guide: Technology , Cost, and the...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍感兴趣但对价格敏感：多人表示 1200 美元超出自己的心理价位，一位老用户还称品控下滑、发货延迟以及创始人的政治立场让他不愿再购买该公司的产品。也有人聚焦技术本身，认为电子纸是阅读 AI 编程助手输出内容、减轻眼睛疲劳的理想方式；还有人分享了自己用二手三星 Frame 电视展示 AI 生成画作的自制方案。

**标签**: `#ePaper`, `#hardware`, `#displays`, `#consumer-electronics`, `#hacker-news`

---

<a id="item-10"></a>
## [康奈尔报告：太阳能阵列下放牧绵羊可带来经济与生态双重收益](https://news.cornell.edu/stories/2026/10/sheep-grazing-solar-fields-offers-farmers-economic-ecological-gains) ⭐️ 6.0/10

康奈尔大学的一份报告指出，在太阳能阵列下放牧绵羊可为农民带来经济和生态双重收益，相关报道发表于 2026 年 10 月的《康奈尔纪事报》。该消息在 Hacker News 上引发了关于农业光伏、牲畜遮阴和实际推广障碍的广泛讨论。 农业光伏让同一块土地同时生产食物和电力，有望在太阳能部署扩张的背景下使农场收入多元化，并让土地继续用于农业。若更广泛采用，太阳能放牧还可满足牲畜遮阴和植被管理需求，同时减少能源与农业之间的土地利用冲突。 这种做法通常选用绵羊，因为其体型和采食习性适合在光伏板行间活动；好处包括为牲畜遮阴、保持土壤水分和控制植被，但抬高面板或加大间距带来的更高前期成本仍是障碍。评论者还提到一些实际难题，例如需要能承受牛只摩擦的廉价支架，以及电力公司对余电上网支持不足。

hackernews · PaulHoule · 11月16日 17:27 · [社区讨论](https://news.ycombinator.com/item?id=50520182)

**背景**: 农业光伏（又称农业太阳能或双用途太阳能）是指在同一块土地上同时进行太阳能发电和农业生产，例如把光伏板架高在作物或牲畜上方，或安装在作物行间。由于光伏板会吸收阳光，作物产量和发电量之间可能存在权衡，但部分作物和牲畜能从额外遮阴中受益，农民也可获得第二份收入。太阳能放牧则专门利用绵羊清理光伏板下的植被，是一个日益增长的细分领域，有时被称为“太阳能牧羊”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agrivoltaics">Agrivoltaics</a></li>
<li><a href="https://theconversation.com/solar-shepherds-earn-big-by-grazing-sheep-on-solar-farms-and-they-benefit-everyone-involved-247169">‘ Solar shepherds’ earn big by grazing sheep on solar farms — and...</a></li>
<li><a href="https://news.sunhub.com/agrivoltaics-economic-benefits-report/">Agrivoltaics Report Reveals Huge Economic Gains</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上支持农业光伏，但更关注实际障碍：有人把加州 5 号州际公路旁无遮阴、在烈日下暴晒的牛群称为残忍，有人把光伏板比作能吸收阳光并提供遮阴的“人造树”，认为这是接近自然的土地改造；还有养牛户表示，廉价耐用的支架和电力公司对太阳能并网支持不足是主要阻碍。其他人则提到西德州风力发电机下放羊的景象，以及对能让绿光透过的半透明粉色光伏板感到好奇。

**标签**: `#agrivoltaics`, `#solar-energy`, `#agriculture`, `#sustainable-farming`, `#hacker-news`

---

<a id="item-11"></a>
## [摩根大通技术故障导致美国多家银行网上银行服务中断](https://apnews.com/article/bank-outage-chase-wells-fargo-truist-50fee2693c22f597fa6ca51a97ef2cda) ⭐️ 6.0/10

摩根大通（JPMorgan Chase）发生技术故障，导致客户的网上银行、银行卡支付和实体网点服务受到影响，同一时间段内富国银行（Wells Fargo）、Truist 等美国银行也出现了服务中断的报告。该行尚未公开确认此次故障的根本原因。 数以百万计的个人客户和企业依赖数字银行渠道完成支付和账户访问，因此即使只有数小时的中断也会立刻造成现实影响。此次事件还引发了一个问题：银行业面向客户的技术栈如今在多大程度上依赖少数几家共享的云服务和数据库供应商。 目前尚无官方的根因分析，Hacker News 上的评论者指出可用性存在地区差异——一些西海岸用户表示同样的服务可以正常加载——这更符合区域性的云服务或数据库故障，而非整个系统崩溃。评论者还将其与 Revolut 去年 10 月的故障相类比，那次事故被归因于 Google Cloud 的问题，大约用了 12 小时才完全恢复。

hackernews · samk3nny · 11月16日 18:31 · [社区讨论](https://news.ycombinator.com/item?id=50521045)

**背景**: 大型银行的核心账户与账务处理至今仍运行在 IBM 大型机上，使用 COBOL、CICS、IMS、DB/2 等已有数十年历史的软件栈，这些系统以可靠性著称，但迁移风险高、成本大。而面向客户的层面——手机 App、网站和银行卡授权——通常构建在现代云基础设施和中间件之上，因此故障可能发生在远离大型机的地方。这种分层架构解释了为什么同一家机构在 App 用户看来“宕机”时，后端的交易处理可能依然正常。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://softwarepower.ir/articles/banking-core-modernization-legacy-mainframe-migration">Core Banking Modernization: Why Migrating Off a 1970s Mainframe Is...</a></li>
<li><a href="https://www.ververica.com/blog/global-bank-achieves-90-cost-savings-with-mainframe-offloading">Global Bank Achieves 90% Cost Savings with Mainframe Offloading!</a></li>
<li><a href="https://medium.com/@suddhasvatta.das92/mainframes-meet-aws-9810b6f1cd8a">Mainframes , Meet AWS!. Mentored by abhijit chakraborty, Sr | Medium</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（约 714 分、591 条评论）以有根据的推测为主，而非已确认的事实：许多读者怀疑是类似 Revolut 谷歌云事故的云服务或数据库故障，也有人指责预算收紧时 QA 总是第一个被砍掉的环节，还有几位反驳说核心银行系统运行在非常老旧但非常可靠的大型机上。一个反复出现的主题是公众认知——微软 365 中断、FAA 停飞等事件被公众笼统地归为同一类系统性问题，即便这种关联在技术上并不准确，这种普遍的不安也很难被消除。

**标签**: `#outage`, `#banking`, `#infrastructure`, `#cloud-reliability`, `#systems`

---

<a id="item-12"></a>
## [Datasette 1.0a43 发布：新增流式输出渲染器并修复安全问题](https://simonwillison.net/2026/Nov/15/datasette/) ⭐️ 6.0/10

Datasette 1.0a43 为输出渲染器（output renderer）加入了流式支持：插件可以通过新的 Response.stream() 方法注册一个能够一次性流式输出整张表所有行的渲染器，内置的 TSV 和 CSV 导出机制也已改用这一方式。该版本还包含安全修复，其中一项因私有存储查询可能被泄露（会暴露查询的标题和 SQL）而单独发布了 GitHub 安全公告（GHSA-mw6v-83vp-7c4c）。 流式输出是 Datasette 1.0 待办清单上剩下的最大一项，对于大表尤为关键——此前导出完整数据必须先全部缓冲，才能发出第一个字节。对插件开发者而言，这也稳定了一组公开 API；目前 1.0 里程碑的完成度报告为 53%。 除流式输出外，行页面的 JSON 表示终于有了适合 1.0 的设计；新增的 <datasette-copy-button> Web Component 可在多处提供复制 schema 的功能，行页面列中的 JSON 可以格式化显示，还增加了 DatasetteModal.confirm() 这一 JavaScript 工具方法，以及受 prefers-reduced-motion 保护的 CSS 跨文档视图过渡（view transitions），让分面结果和表格容器在页面切换时平滑变形。该存储查询漏洞只暴露标题和 SQL，并不允许执行查询；更新日志还致谢了外部贡献者 Zihan Dai、Peter Olkhovets、Ilya Khalafi 和 Ankita Advitot，并提到 Simon Willison 大量借助 Claude Fable 5.2 来推进里程碑任务。

rss · Simon Willison · 11月15日 23:20

**背景**: Datasette 是 Simon Willison 的开源数据探索与发布工具，它把 SQLite 数据库包装成一个可交互网站并附带 JSON API，主要面向数据记者、档案管理员、研究者和地方政府。它的灵活性很大程度上来自基于插件钩子（hook）的插件架构，其中输出渲染器（output renderer）负责把查询结果序列化为 CSV、TSV、GeoJSON 等格式。Datasette 1.0 经历了漫长的 alpha 版本迭代，并用 GitHub 里程碑来跟踪稳定版发布前必须完成的剩余工作项。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datasette.io/">Datasette : An open source multi-tool for exploring and publishing...</a></li>
<li><a href="https://github.com/simonw/datasette">GitHub - simonw/ datasette : An open source multi-tool for...</a></li>

</ul>
</details>

**标签**: `#Datasette`, `#release`, `#streaming`, `#security`, `#open-source`

---

<a id="item-13"></a>
## [datasette-apps 0.4a0 发布：沙盒 SQL 小应用支持 URL 片段互相链接](https://simonwillison.net/2026/Nov/15/datasette-apps/) ⭐️ 6.0/10

datasette-apps 0.4a0 新增了应用之间的链接支持：现在可以通过在 URL 中带上 #fragment 打开某个应用，应用能够读取并使用该片段。此版本还会把应用支持的 URL scheme 上报给 Datasette Agent，让这个 AI 助手能够生成互相链接的应用。 这让原本彼此孤立的沙盒小应用连成一体，一个搜索类应用可以直接跳转到由另一个完全独立的应用渲染的详情视图。对于用 Datasette 搭建轻量数据界面的用户来说，这意味着无需离开沙盒、也无需写一个庞大的单体应用，就能组合出多应用协同的体验。 这是一个尚未到 1.0 的 alpha 版本（`0.4a0`），API 仍可能发生变化。Datasette Apps 在由严格 CSP 约束的沙盒中运行 HTML/JS，并注册了细粒度权限（如 create-app、view-app、edit-app、delete-app、manage-app-access、apps-set-csp）来控制谁能创建和查看应用。

rss · Simon Willison · 11月15日 04:02

**背景**: Datasette 是一个用于探索和发布数据的开源工具，通常以 SQLite 作为后端。Datasette Apps 是运行在 Datasette 内部的沙盒化 HTML 与 JavaScript 应用，概念上类似 Claude Artifacts，但区别在于它们可以对自己的数据执行 SQL 查询。Datasette Agent 则是配套的、由大模型驱动的助手，它通过编写并执行 SQL 来回答关于数据的问题，同时也能替你编写这类应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/datasette/datasette-apps">GitHub - datasette / datasette - apps : Apps that live inside Datasette</a></li>
<li><a href="https://simonwillison.net/2026/Jun/18/datasette-apps/">Datasette Apps : Host custom HTML applications inside Datasette</a></li>
<li><a href="https://github.com/datasette/datasette-agent">GitHub - datasette / datasette - agent : An LLM-powered agent for...</a></li>

</ul>
</details>

**标签**: `#datasette`, `#data-exploration`, `#web-apps`, `#sandboxing`, `#release`

---