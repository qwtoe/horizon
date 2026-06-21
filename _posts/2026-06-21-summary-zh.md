---
layout: default
title: "Horizon Summary: 2026-06-21 (ZH)"
date: 2026-06-21
lang: zh
---

> 从 20 条内容中筛选出 7 条重要资讯。

---

1. [Loupe iOS 应用揭示隐藏的设备指纹数据](#item-1) ⭐️ 8.0/10
2. [Slow breathing modulates brain function and risk behavior](#item-2) ⭐️ 8.0/10
3. [SMPTE 免费开放其标准库](#item-3) ⭐️ 8.0/10
4. [Epoll 对比 io_uring：Linux I/O 的性能与安全权衡](#item-4) ⭐️ 7.0/10
5. [AI 生成的代码即使能用也被拒绝](#item-5) ⭐️ 7.0/10
6. [TownSquare：一个实时聊天的小型在场层面临审核难题](#item-6) ⭐️ 6.0/10
7. [DOS 游戏 F-15 Strike Eagle II 逆向项目需要测试员](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Loupe iOS 应用揭示隐藏的设备指纹数据](https://github.com/mysk-research/loupe) ⭐️ 8.0/10

安全研究团队 Mysk 发布了一款免费开源的 iOS 应用 Loupe：What Apps Can See，该应用展示了第三方应用如何通过公共 iOS API 获取用户设备信息，且无需任何权限。 这款工具通过展示 iOS 设备如何被静默收集的数据指纹化，提升了关键的隐私意识，帮助用户理解并减轻追踪风险。 Loupe 从公共 iOS API 读取真实数据，并将其分类为“被动”、“权限”和“高级”级别，揭示了超过 20 个数据点，如已安装应用、卷创建日期和剪贴板更改次数。

hackernews · Cider9986 · 6月20日 12:08 · [社区讨论](https://news.ycombinator.com/item?id=48608645)

**背景**: iOS 应用运行在沙盒中，限制了访问其他应用数据和系统资源，但某些公共 API 仍然暴露可用于指纹识别的设备信息。与 Android 不同，iOS 不会随机化所有标识符，使得卷创建日期等数据持久存在。Loupe 将这些不可见的数据泄露展示给用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/mysk-research/loupe">GitHub - mysk-research/loupe: A privacy-focused iOS app that ...</a></li>
<li><a href="https://support.apple.com/guide/security/security-of-runtime-process-sec15bfe098e/web">Security of runtime process in iOS, iPadOS, and visionOS - Apple Support</a></li>
<li><a href="https://developer.apple.com/documentation/security/protecting-user-data-with-app-sandbox">Protecting user data with App Sandbox | Apple Developer Documentation</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 Loupe 的教育性设计和数据暴露级别的分组，有人指出它比 Android 当前状态更好。一些人对卷创建日期等具体泄露表示担忧，并建议操作系统应模糊这些数据。

**标签**: `#iOS`, `#privacy`, `#security`, `#awareness`, `#research`

---

<a id="item-2"></a>
## [Slow breathing modulates brain function and risk behavior](https://www.cell.com/neuron/fulltext/S0896-6273(26)00339-9) ⭐️ 8.0/10

This study reveals that slow breathing, particularly prolonged exhalation, modulates brain function and increases risk-taking behavior by enhancing parasympathetic activity, with potential clinical applications for anxiety and depression.

hackernews · croes · 6月20日 22:22 · [社区讨论](https://news.ycombinator.com/item?id=48613555)

**标签**: `#neuroscience`, `#breathing`, `#risk-taking`, `#parasympathetic`, `#anxiety`

---

<a id="item-3"></a>
## [SMPTE 免费开放其标准库](https://www.smpte.org/blog/smpte-makes-its-standards-freely-accessible-openingstandards-library-to-the-global-media-technology-community) ⭐️ 8.0/10

SMPTE 于 2026 年 6 月 17 日宣布，其全部标准目录现已免费向全球媒体技术社区开放，消除了付费墙障碍。 此举降低了开发者和公司的准入门槛，促进了媒体制作与发行领域的创新，并与开放标准的发展趋势相一致。 免费访问包括所有已发布的 SMPTE 标准，同时还包括近期现代化举措，如采用基于 GitHub 的工作流程、结构化 HTML 编写以及集成化发布管道。

hackernews · zdw · 6月20日 17:01 · [社区讨论](https://news.ycombinator.com/item?id=48610827)

**背景**: SMPTE（电影与电视工程师协会）成立于 1916 年，是一个全球性的专业协会，制定了诸如 SMPTE 时间码和 24 fps 胶片速度等关键媒体标准。此前，获取这些标准需要单独购买文档，这对小型开发者和初创企业构成了障碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.smpte.org/">SMPTE | The home of media professionals, technologists, and engineers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Society_of_Motion_Picture_and_Television_Engineers">Society of Motion Picture and Television Engineers - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应极其积极，例如用户 lambdaone 称赞此举早就该实行，并将其与 IETF 免费标准的成功相提并论。Geerlingguy 质疑为何默认不这样做，而 ksec 则强调了配套的 GitHub 现代化工作。少数用户分享了此前购买标准文件的怀旧轶事。

**标签**: `#standards`, `#open-access`, `#media-technology`, `#SMPTE`, `#GitHub`

---

<a id="item-4"></a>
## [Epoll 对比 io_uring：Linux I/O 的性能与安全权衡](https://sibexi.co/posts/epoll-vs-io_uring/) ⭐️ 7.0/10

一篇技术深度文章对比了 epoll 和 io_uring，指出 io_uring 在请求吞吐量上可提升高达 20%，但其安全风险限制了广泛采用。 这一对比对于决定采用哪种 I/O 模型的系统程序员至关重要，因为 io_uring 的性能优势被安全担忧所抵消，导致 Google 等主要平台在某些环境中禁用了它。 io_uring 通过共享环形缓冲区在内核和用户空间之间实现真正的零拷贝 I/O，但其直接内存共享产生了巨大的攻击面，导致多个漏洞利用案例，并在安全敏感应用中采用受限。

hackernews · Sibexico · 6月20日 23:07 · [社区讨论](https://news.ycombinator.com/item?id=48613872)

**背景**: Epoll 是 Linux 内核中用于可扩展 I/O 事件通知的系统调用，广泛应用于网络服务器。io_uring 是一种较新的异步 I/O 接口，通过环形缓冲区减少开销并提升性能，但其安全模型导致 Android、Chrome OS 等平台对其施加了限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Io_uring">io _ uring - Wikipedia</a></li>
<li><a href="https://man7.org/linux/man-pages/man7/io_uring.7.html">io _ uring (7) - Linux manual page</a></li>
<li><a href="https://www.phoronix.com/news/Google-Restricting-IO_uring">Google Limiting IO _ uring Use Due To Security Vulnerabilities - Phoronix</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出 io_uring 可提速 20%，但常因安全原因被禁用；有人建议使用 CPU 绑定和 mimalloc 等库进行进一步优化。评论中既有对性能的热情，也有对安全风险的谨慎态度。

**标签**: `#Linux`, `#I/O`, `#performance`, `#epoll`, `#io_uring`

---

<a id="item-5"></a>
## [AI 生成的代码即使能用也被拒绝](https://vinibrasil.com/when-i-reject-ai-code-even-if-it-works/) ⭐️ 7.0/10

一位开发者分享了拒绝功能正确的 AI 生成代码的原因，主要是担心可维护性、过度抽象以及开发者参与度降低。 这一反思凸显了 AI 辅助编程中的关键矛盾：功能正确还不够，代码还必须可维护且人类可理解。它强调了 AI 工具需要更好地符合软件工程最佳实践。 作者指出，AI 常常生成复杂的抽象，比更简单直接的解决方案更难维护。社区评论进一步表明，拒绝 AI 代码类似于因类似的质量原因拒绝同事的代码。

hackernews · vnbrs · 6月21日 00:58 · [社区讨论](https://news.ycombinator.com/item?id=48614631)

**背景**: 随着 GitHub Copilot 和 Cursor 等 AI 编程助手的广泛应用，开发者们正在权衡速度与代码质量之间的关系。拒绝功能正确但结构不佳的代码是软件工程中的一项关键技能，强调可维护性和简洁性与正确性同样重要。

**社区讨论**: 评论者普遍同意作者的观点，分享了拒绝 AI 生成的抽象代码的经历。一些人指出，AI 代码常常遵循过于复杂的“企业模式”，而另一些人则将拒绝 AI 代码比作因类似原因拒绝同事的代码。

**标签**: `#AI-assisted coding`, `#software engineering`, `#developer productivity`, `#code quality`, `#human-ai collaboration`

---

<a id="item-6"></a>
## [TownSquare：一个实时聊天的小型在场层面临审核难题](https://townsquare.cauenapier.com/) ⭐️ 6.0/10

TownSquare 是一个为网站提供实时聊天功能的小型在场层，其发布后的现场演示很快被恶意刷屏和攻击性信息淹没。 该项目凸显了网络上实时社交功能审核的关键挑战，尤其是对于缺乏强大内容过滤资源的小型或业余项目而言。 TownSquare 是一个轻量级 JavaScript 小部件，网站所有者可通过 script 标签嵌入；其项目站点的现场演示遭受了持续刷屏和攻击性言论，凸显了从一开始就需要审核机制。

hackernews · cauenapier · 6月20日 11:55 · [社区讨论](https://news.ycombinator.com/item?id=48608570)

**背景**: 在场层是一个编排层，显示谁在线并支持实时互动（如聊天或协作）。TownSquare 将此概念应用于任何网站，让访客之间能够交流。然而，如果没有审核，这种开放的聊天空间很容易被滥用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@bspartridgeCIS/what-the-presence-layer-actually-is-643326c33bf8">What the Presence Layer Actually Is | by Brittany Partridge | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者觉得项目干净截图与混乱现场演示之间的对比很有趣，并分享了自己对抗恶意刷屏和审核策略的经验，例如关键词过滤和身份验证。

**标签**: `#web development`, `#real-time chat`, `#moderation`, `#JavaScript`, `#side project`

---

<a id="item-7"></a>
## [DOS 游戏 F-15 Strike Eagle II 逆向项目需要测试员](https://neuviemeporte.github.io/f15-se2/2026/06/20/needyou.html) ⭐️ 6.0/10

DOS 游戏 F-15 Strike Eagle II 的逆向工程已进入新阶段，需要社区测试员来发现从汇编翻译成 C 代码后引入的 bug，同时保持二进制兼容性。 该项目对软件保护具有重要意义，它旨在将经典飞行模拟器完全移植为 C 代码，使其无需模拟即可在现代系统上原生运行。 该项目目前需要原始游戏文件（版本 451.03），并在 DOS 或 DOSBox 下运行；C 代码经过验证，必须生成与原始汇编完全相同的二进制输出。

hackernews · LowLevelMahn · 6月20日 15:10 · [社区讨论](https://news.ycombinator.com/item?id=48609766)

**背景**: 将 DOS 游戏从汇编逆向工程转换为 C 代码是一个细致的过程，需要确保功能完全一致。许多复古游戏爱好者更倾向于原生移植而非模拟，以获得更好的性能和集成度。该项目展示了通过让经典软件在现代硬件上原生运行来保护它们的努力。

**社区讨论**: 社区评论中既有怀旧情感也有技术兴趣。一些用户质疑为什么需要反编译而非模拟，另一些则分享了个人对游戏的回忆。一位开发者指出，使用现代 API 移植非常简单，但逆向过程本身容易引入 bug。

**标签**: `#reverse-engineering`, `#dos-games`, `#retro-gaming`, `#software-preservation`, `#porting`

---