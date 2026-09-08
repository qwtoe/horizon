---
layout: default
title: "Horizon Summary: 2026-09-08 (ZH)"
date: 2026-09-08
lang: zh
---

> 从 21 条内容中筛选出 13 条重要资讯。

---

1. [消费级 GPU 两天破解 90 年代证书机构的 512 位 RSA 密钥](#item-1) ⭐️ 8.0/10
2. [Terrastruct 将 D2 高级布局引擎 TALA 开源](#item-2) ⭐️ 8.0/10
3. [Jellyfin 12.0 发布：升级更顺畅，性能修复显著](#item-3) ⭐️ 8.0/10
4. [博通撤下 VDDK 下载，离开 VMware 难度加大](#item-4) ⭐️ 8.0/10
5. [LG 智能电视被曝熄屏录音并扫描局域网设备](#item-5) ⭐️ 8.0/10
6. [OpenAI 内部视角：编程代理与 RSI 加速研究](#item-6) ⭐️ 8.0/10
7. [交互式地图展示洛杉矶 1880 至 2026 年建筑演进](#item-7) ⭐️ 7.0/10
8. [开发者公开重建版“震网”恶意软件源代码](#item-8) ⭐️ 7.0/10
9. [恶意爬虫在 git.kernel.org 上比正常 Git 流量消耗更多 CPU](#item-9) ⭐️ 7.0/10
10. [OpenAI 首席科学家：需强大且对齐的 AI 用于防御，反对鲁莽竞赛](#item-10) ⭐️ 7.0/10
11. [DNS 滥用：约两成新增 gTLD 域名或为诈骗](#item-11) ⭐️ 7.0/10
12. [从头重写遗留系统很少成功](#item-12) ⭐️ 7.0/10
13. [从 Mercator 到 Equal Earth：GPT 制作的地图投影动画](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [消费级 GPU 两天破解 90 年代证书机构的 512 位 RSA 密钥](https://mcpherrin.ca/2026/09/07/rsa.html) ⭐️ 8.0/10

一位安全研究者利用一块消费级 GPU 在两天内成功分解了上世纪 90 年代某证书颁发机构（CA）的 512 位 RSA 密钥。该成果表明，随着现代硬件和算法的发展，过去认为安全的旧式加密密钥现已很容易被攻破。 这一演示说明，个人使用现成的硬件就能破解旧式 512 位 RSA 密钥，这将削弱受此类密钥保护的数据的长期机密性和真实性。同时它也引发担忧：政府或攻击者可能会存储今天的加密流量，等待未来算力提升后再进行解密（即“先收割、后解密”）。 研究者使用运行在消费级 GPU 上的通用数域筛法（GNFS）实现，仅用约两天时间就完成了对 512 位模数的分解。相关逆向工作针对的是 Netscape Communicator 4.51 等老旧软件，研究者也提醒，由大语言模型（LLM）辅助生成的逆向分析结果必须经过人工验证。

hackernews · ahlCVA · 9月8日 01:16 · [社区讨论](https://news.ycombinator.com/item?id=49604637)

**背景**: RSA 是一种广泛用于互联网通信的公钥密码体制，其安全性依赖于对大整数进行质因数分解的困难性：密钥越长（如 2048 位），分解所需的计算量就越大。上世纪 90 年代，受出口管制和当年硬件性能的限制，512 位密钥曾被普遍使用；到 RSA 实验室的“RSA 分解挑战”开展时，人们已意识到这类密钥在拥有足够资源的对手面前并不安全。如今，通用数域筛法（GNFS）是经典计算机上已知分解大整数最高效的算法，GPU 算力的快速提升更大大降低了此类攻击的成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/General_number_field_sieve">General number field sieve</a></li>
<li><a href="https://en.wikipedia.org/wiki/RSA_Factoring_Challenge">RSA Factoring Challenge</a></li>

</ul>
</details>

**社区讨论**: 评论区对这项“逆向考古”项目表现出极大热情，并认为它对旧 SSL/TLS 报告打出多个“F”的结尾非常有戏剧性。多位网友提醒，LLM 辅助生成的代码或结果必须人工仔细验证，因为“看起来合理”并不等于正确；还有人指出，90 年代多数网络流量并未加密，这也让今天的监控焦虑有了新的参照。

**标签**: `#security`, `#cryptography`, `#RSA`, `#retrocomputing`, `#TLS`

---

<a id="item-2"></a>
## [Terrastruct 将 D2 高级布局引擎 TALA 开源](https://d2lang.com/blog/tala-is-open-source/) ⭐️ 8.0/10

Terrastruct 宣布其此前专有的 D2 图表布局引擎 TALA 现已开源。源代码已托管在 GitHub 的 terrastruct/TALA 仓库中。 TALA 专为软件架构图设计，通常能比 ELK 等现有引擎生成更整洁的布局。开源后可能加速 D2 的普及，并让 Daedalus 等其他工具集成更优秀的自动布局能力。 TALA 是与 D2 分开的独立组件，此前需付费购买且保持闭源。评论指出 TALA 的输出并非总是更优，例如某些图中可能破坏从左到右的流向和分组，因此需要按具体场景进行评估。

hackernews · alixanderwang · 9月7日 23:37 · [社区讨论](https://news.ycombinator.com/item?id=49604150)

**背景**: D2 是一种现代声明式图表语言，用户可以用文本描述图表，类似于 Mermaid 或 Graphviz。TALA 是 Terrastruct 开发的布局引擎，专门用于美观地排列软件架构图，而非通用图。布局引擎会自动决定节点和连线的位置；对于架构图等图类型，引擎质量会显著影响可读性。TALA 的开源也顺应了图表基础设施日益开放的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://d2lang.com/tour/tala/">TALA | D2 Documentation</a></li>
<li><a href="https://github.com/terrastruct/TALA">GitHub - terrastruct/TALA: A diagram layout engine designed specifically for software architecture diagrams · GitHub</a></li>
<li><a href="https://terrastruct.com/tala/">TALA | Terrastruct's AutoLayout Approach</a></li>

</ul>
</details>

**社区讨论**: 评论者整体很热情：有人说会把 TALA 加入 Daedalus，也有人称赞它相比默认引擎有明显改进。但也有相反看法，认为 TALA 的布局并非处处更好——例如一个 Go 队列示例被认为更差，因为它破坏了分组和从左到右的流向。还有人询问关键启发式规则，并分享了对 D2 的正面使用体验。

**标签**: `#open-source`, `#diagramming`, `#D2`, `#layout-engine`

---

<a id="item-3"></a>
## [Jellyfin 12.0 发布：升级更顺畅，性能修复显著](https://jellyfin.org/posts/jellyfin-release-12.0/) ⭐️ 8.0/10

开源媒体服务器 Jellyfin 现已推出 12.0 主要版本。用户反馈从旧版本迁移变得明显更顺畅、更快捷，同时修复了先前 10.11 系列存在的性能问题，但字幕处理仍是已知的短板。 此版本意义重大，因为 Jellyfin 是 Plex 之外领先的免费、自托管替代方案，这些改进进一步巩固了它在追求更多控制权和隐私的用户中的地位。更顺畅的升级和更佳的性能降低了从商业媒体服务器迁移的门槛。 从 10.10.7 等旧版本升级的过程据称快速且无痛，仅有一些标题在重新扫描前暂时消失。Jellyfin 12.0 在 2024 年 6 月至 8 月间经历了 7 个候选版本，说明测试较为充分，但字幕问题仍存在，尤其在 Android 客户端串流到 Chromecast 电视棒时。

hackernews · 0xC0ncord · 9月8日 01:56 · [社区讨论](https://news.ycombinator.com/item?id=49604861)

**背景**: Jellyfin 是一款自由软件媒体服务器，可让用户从自己的硬件上收集、管理和串流电影、电视节目、音乐及照片。自托管软件是指部署并在用户自己控制的基础设施上运行的软件，能够提供更高的隐私性，并避免依赖第三方云服务。Jellyfin 被广泛视为 Plex 等专有平台的主要开源替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jellyfin.org/">The Free Software Media System | Jellyfin</a></li>
<li><a href="https://www.serverman.co.uk/server/jellyfin/what-is-jellyfin/">What Is Jellyfin ? The Free Self-Hosted Plex Alternative - Serverman</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-hosting_(web_services)">Self-hosting (network) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区对升级体验的评价总体正面，有用户称迁移到 12.0 “快速且无痛”，并相信先前的性能问题已经修复。Android 和 Chromecast 上的字幕处理仍是反复被提及的主要抱怨点，部分 Plex 用户也将 Jellyfin 视为在 Plex 更不友好时可用的迁移出路。

**标签**: `#Jellyfin`, `#media server`, `#open source`, `#self-hosted`, `#release`

---

<a id="item-4"></a>
## [博通撤下 VDDK 下载，离开 VMware 难度加大](https://www.virtualizationhowto.com/2026/09/leaving-vmware-just-got-harder-after-broadcom-pulled-vddk-downloads/) ⭐️ 8.0/10

博通在没有官方解释的情况下撤下了 VMware Virtual Disk Development Kit（VDDK）的下载页面，切断了用于虚拟机迁移、备份和灾难恢复的关键工具获取渠道。这次下架给计划离开 VMware 的组织增加了又一道障碍。 VDDK 是许多第三方迁移、备份和恢复产品读写与传输 VMware 虚拟磁盘的基础组件，因此这次下架可能延误或复杂化退出 VMware 的进程。这加剧了用户对博通管理下供应商锁定问题的担忧，也促使更多用户转向 Proxmox 等替代方案或手动磁盘转换。 并非所有迁移路径都受阻：Proxmox 的 VMware 导入工具并不依赖 VDDK，qemu-img 也仍可将.vmdk 镜像转换为其他虚拟机管理程序可用的格式。但据报道，Red Hat 的 Migration Toolkit for Virtualization 等工具已无法下载 VDDK，可见第三方迁移产品受到了直接影响。

hackernews · josephcsible · 9月7日 20:32 · [社区讨论](https://news.ycombinator.com/item?id=49602699)

**背景**: VMware VDDK 是一组 C/C++库、工具、代码示例和文档，允许开发者和合作伙伴创建并访问 VMware 虚拟磁盘存储。许多备份和迁移厂商通过 VixDiskLib 等 VDDK API 从 ESXi 数据存储中读取在线虚拟机磁盘。自博通收购 VMware 以来，它在授权、定价和产品获取方面做出了一系列有争议的调整，这次悄然下架 VDDK 下载也符合这一模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.shapeblue.com/broadcom-vddk-download-vmware-to-kvm/">Broadcom Removes VDDK Pages Without Explanation: What You Need to Know - ShapeBlue</a></li>
<li><a href="https://www.rackwareinc.com/post/the-impact-and-importance-of-vmware-s-restriction-on-vddk">The Impact and Importance of VMware's Restriction on VDDK</a></li>
<li><a href="https://www.infoworld.com/article/2310788/vmware-helps-developers-with-a-new-virtual-disk-development-kit.html">VMware helps developers with a new Virtual Disk ... | InfoWorld</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体是悲伤和沮丧的；一位前 VMware 工程师感叹博通正在从一个创新能力已过巅峰的公司身上榨取金钱。多位用户分享了迁移经历：有人发现从 VMware 迁往 Proxmox 出奇地轻松，而另一位参与过 Hyper-V 与 VMware 迁移项目的用户批评微软 Hyper-V 的工具过于零散。还有评论者指出 qemu-img 仍可转换.vmdk 文件，并询问完整迁移是否除了磁盘转换和手动配置虚拟硬件之外还需要其他步骤。

**标签**: `#VMware`, `#Broadcom`, `#VDDK`, `#Virtualization`, `#Migration`

---

<a id="item-5"></a>
## [LG 智能电视被曝熄屏录音并扫描局域网设备](https://www.youtube.com/watch?v=6IFVTcM28KA) ⭐️ 8.0/10

由 Gamers Nexus 进行、Notebookcheck 报道的一项新调查发现，LG 智能电视即使在屏幕关闭时也能通过麦克风捕获音频，并会扫描本地网络以识别附近的手机和设备；电视在重新联网后会上传这些数据。该报道引发了对多达 2.16 亿台 LG 电视的担忧。 这件事之所以重要，是因为它表明“智能”家居设备可以在未经用户明确同意的情况下暗中录制谈话并探测私有网络。考虑到可能受影响的 2.16 亿台设备，它给消费者带来了严重的隐私、法律和信任问题，也迫使整个智能电视行业正视内置监控问题。 测试中，LG 电视在屏幕关闭时仍会继续记录音频，并且只有在恢复网络连接后才上传数据；电视还会利用 UPnP 和本地网络扫描来枚举其他设备。报道称，LG 的服务条款要求用户负责获得并告知任何可能被捕获和处理语音的第三方。

hackernews · treve · 9月7日 00:22 · [社区讨论](https://news.ycombinator.com/item?id=49592375)

**背景**: 许多现代智能电视都内置麦克风和网络连接，以支持语音助手和定向广告。ACR（自动内容识别）能够识别屏幕内容并建立收视画像，而 UPnP 是一种常见的协议，可让家居设备在本地网络中相互发现和控制。调查人员发现，LG 电视会广泛使用此类网络发现功能，甚至在屏幕关闭时也会记录周围音频。制造商的服务条款通常允许这些行为，但用户很少预料到在待机模式下也会发生。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.notebookcheck.net/LG-smart-TVs-caught-logging-audio-with-screen-off-and-snooping-on-local-devices.1391214.0.html">LG smart TVs caught logging audio with screen off and snooping on local devices - Notebookcheck News</a></li>
<li><a href="https://www.youtube.com/watch?v=6IFVTcM28KA">216,000,000 Spy TVs | The LG Smart TV Problem - YouTube</a></li>
<li><a href="https://www.pocket-lint.com/automatic-content-recognition-explained/">New TVs come pre-loaded with spyware called ' ACR '. Here's how to....</a></li>

</ul>
</details>

**社区讨论**: 评论普遍持强烈批评态度：有用户指出 LG 的条款要求用户告知客人可能被监听，有人提到自己曾禁用网络功能并因此被嘲笑，还有不少人表示以后不愿再购买 LG 产品。另一些人质疑为何这没有违反窃听相关法律；也有评论者指出报道网站本身满是广告的讽刺之处，但仍希望这次风波能让 LG 受到教训。

**标签**: `#privacy`, `#security`, `#smart-tv`, `#surveillance`, `#lg`

---

<a id="item-6"></a>
## [OpenAI 内部视角：编程代理与 RSI 加速研究](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/) ⭐️ 8.0/10

OpenAI 发布了《研究加速：OpenAI 内部视角》一文，详细说明编程代理如何改变其研究人员的日常工作。文中图表显示，每位研究人员的每日 AI 支出从 2026 年 2 月接近 0 美元，上升到 2026 年 8 月下旬的约 600 美元。 这是一个难得的内幕视角，展示了前沿 AI 实验室自身研究工作流程的变化，表明到 2026 年，智能体式编程已成为核心研究基础设施。该文明确将这些进展与递归自我改进联系起来，表明 OpenAI 将其视为迈向 AGI 的一步。 图表显示，2026 年年中经历平台期后，7 月下旬开始急剧加速；Simon Willison 推测，这一跃升与内部员工获得后来以 GPT-6 Astra 发布的模型访问权限的时间吻合。据报道，OpenAI 在文中直接用 RSI 指代递归自我改进，而没有展开缩写，反映出该概念在其所述研究方向中的核心地位。

rss · Simon Willison · 9月6日 23:57

**背景**: 递归自我改进是一个假设性过程，指 AGI 系统改写自己的代码并增强自身能力，理论上可能引发智能爆炸。在当前实践中，大语言模型已经能编写代码和生成合成数据，因此编程代理被广泛视为这一趋势早期且具体的形态。OpenAI 的这篇文章以及 Jakub Pachocki 的配套随笔《An Alien Mind》表明，RSI 如今已成为该公司研究叙事的核心，而外部观察者仍在争论真正的自主自我改进能以多快实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://www.technologyreview.com/2026/08/18/1142188/ai-recursive-self-improvement/">AI’s recursive self-improvement might not come so quickly after all | MIT Technology Review</a></li>
<li><a href="https://www.anthropic.com/institute/recursive-self-improvement">When AI builds itself \ Anthropic</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#artificial general intelligence`, `#coding agents`, `#recursive self-improvement`, `#AI research`

---

<a id="item-7"></a>
## [交互式地图展示洛杉矶 1880 至 2026 年建筑演进](https://lax-skyline.parcelscope.net/) ⭐️ 7.0/10

新交互式地图 lax-skyline.parcelscope.net 逐地块展示洛杉矶建筑按建造年份（1880—2026）着色的演变，用户可以看到城市如何一步步扩张。该工具引发了关于区划、住房政策以及有轨电车拆除如何塑造这座城市的广泛讨论。 这张地图把复杂的城市政策问题——例如 1980 年代缩减区划的影响和当今住房可负担性危机——用直观画面呈现给普通公众。它还唤起了公众对洛杉矶已消失的太平洋电气铁路的记忆，显示出可见的历史可以为未来用地与交通辩论提供参考。 一个关键注意事项是，该地图来源于洛杉矶县税务评估官的地块记录，因此显示的是现存建筑的建造年份，而非曾建成的所有建筑。像 Palms 这样被整片重建的早期街区会显示为空白，尽管它们在 1890 年代曾有繁华的市中心。

hackernews · rustywasm · 9月7日 18:52 · [社区讨论](https://news.ycombinator.com/item?id=49601655)

**背景**: 洛杉矶的区划长期控制着土地用途和建筑规模，一部有影响力的历史将其描述为四套相继更替的监管体制。近年来，城市规划部门称该市正从严格的欧几里得式区划转向混合式与模块化框架。洛杉矶还曾是太平洋电气铁路的中心，这一庞大的城际电车网络在区域转向公路交通后基本消失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://planning.lacity.gov/zoning/overview">Zoning Introduction | Los Angeles City Planning</a></li>
<li><a href="https://www.jamesarsenault.com/pages/books/7184/d-w-pontius/lines-of-the-pacific-electric-railway-in-southern-california">Lines of the Pacific Electric Railway in Southern California</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞这一可视化，但也强调它统计的是现存建筑而非所有建成建筑，并指出 Palms 等地区因老建筑被拆除而看似空白。一些人认为 1980 年代的缩减区划造成了人为住房短缺，使洛杉矶生活成本高企；另一些人则回忆起该市曾长达 1300 英里的太平洋电气电车网络，并将此项目与早期 Mapbox GL 时代的可视化比较。

**标签**: `#data visualization`, `#urban planning`, `#Los Angeles`, `#building history`, `#zoning`

---

<a id="item-8"></a>
## [开发者公开重建版“震网”恶意软件源代码](https://github.com/Sadpainy/Stuxnet) ⭐️ 7.0/10

一名开发者在 GitHub 上发布了 Stuxnet 蠕虫的重建源代码，仓库名为 Sadpainy/Stuxnet。该项目被描述为教育和研究用途，代码量约为 1.5 万行。 Stuxnet 被广泛认为是第一个能对工业设施造成物理破坏的网络武器，因此一份可读的公开重建代码可以帮助防御者和研究人员研究攻击者如何滥用 Windows 和西门子 STEP 7 软件。这也再次引发人们对关键基础设施中 SCADA 与可编程逻辑控制器（PLC）环境脆弱性的关注。 这是重建版本，并非原始泄漏源码，目标是运行于 Windows 环境中的西门子 S7 PLC 系统。历史上的 Stuxnet 利用了四个零日漏洞，只有在检测到 PLC 网络上的 STEP 7 软件时才会激活，并借助被感染的 U 盘穿越气隙（air gap）。

hackernews · CMDDestory · 9月7日 22:12 · [社区讨论](https://news.ycombinator.com/item?id=49603546)

**背景**: Stuxnet 是一种恶意计算机蠕虫，于 2010 年 6 月首次被发现，据认为从 2005 年左右就开始开发。它以数据采集与监控系统（SCADA）为攻击目标，并被多家媒体报道为美以两国为破坏伊朗纳坦兹核计划而联合研制的武器。该蠕虫入侵西门子 Step7 软件，使高速运转的铀浓缩离心机损坏，最终摧毁了伊朗约五分之一的离心机。其设计采用模块化架构，包含蠕虫、链接文件和 rootkit 组件，并可被改造用于攻击其他现代 SCADA 与 PLC 系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stuxnet_(malware)">Stuxnet (malware)</a></li>
<li><a href="https://www.kaspersky.co.in/resource-center/definitions/what-is-stuxnet">Stuxnet Definition & Explanation</a></li>
<li><a href="https://www.trellix.com/security-awareness/ransomware/what-is-stuxnet/">What Is Stuxnet ? | Trellix</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍欢迎这次发布，认为它是有价值的资源，有人提到研究 Stuxnet 改变了他们对关键基础设施安全的看法，并推荐了 Zetter 的著作《Countdown to Zero Day》。也有评论者对 U 盘传播是否可能涉及被感染的第三方经销商表示疑问，并希望作者在文档整理和代码导航上投入更多精力；还有人用一条“被摧毁离心机计数加一”的玩笑表达对该历史事件的调侃。

**标签**: `#stuxnet`, `#cybersecurity`, `#reverse-engineering`, `#malware`, `#industrial-control-systems`

---

<a id="item-9"></a>
## [恶意爬虫在 git.kernel.org 上比正常 Git 流量消耗更多 CPU](https://simonwillison.net/2026/Sep/7/creepy-crawlies/) ⭐️ 7.0/10

Konstantin Ryabitsev 在题为“Creepy crawlies”的文章中表示，git.kernel.org 在渲染提交页面给恶意爬虫上消耗的 CPU 周期，已经超过包括 git clone 在内的所有合法访问。在任何时刻，分布在 5 个地理节点的 14 个 CPU 核心都只用于把 Git 提交渲染成 HTML 给爬虫。 这件事清楚地说明，AI/LLM 爬虫正给关键开源基础设施带来日益沉重的运维负担。由于很多项目都提供可被抓取的网页，同样的“背景辐射”也可能会给各类 Web 服务项目造成严重的性能与成本问题。 报道指出，服务器花在爬虫抓取上的 CPU 时间已经超过了所有其他合法访问的总和，而相比之下，git clone 本是获取仓库数据效率高得多的方式。Simon Willison 提到，从 Datasette 的角度出发，他很担心同样的问题，因为 Datasette 也提供了海量可抓取的网页。

rss · Simon Willison · 9月7日 23:08

**背景**: git.kernel.org 是 Linux 内核的官方 Git 仓库托管站点，它使用 cgit——一个用 C 编写的高性能 Web 前端——把提交、diff 等仓库页面渲染成 HTML。越来越多恶意爬虫和 AI 爬虫不去使用高效的 Git 传输协议，而是不断抓取这些网页。这种现象类似于“互联网背景辐射”的概念，即扫描、错误配置以及如今的内容爬虫所产生的持续非生产性流量；业内已广泛报道这类爬虫会消耗网站带宽并推高基础设施成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://git.zx2c4.com/cgit/about/">cgit - A hyperfast web frontend for git repositories written in C.</a></li>
<li><a href="https://www.searchenginejournal.com/ai-crawlers-draining-site-resources/543011/">AI Crawlers Are Reportedly Draining Site Resources & Skewing Analytics</a></li>
<li><a href="https://en.wikipedia.org/wiki/Internet_background_noise">Internet background noise - Wikipedia</a></li>

</ul>
</details>

**标签**: `#crawling`, `#open-source`, `#infrastructure`, `#web-scraping`, `#AI-crawlers`

---

<a id="item-10"></a>
## [OpenAI 首席科学家：需强大且对齐的 AI 用于防御，反对鲁莽竞赛](https://simonwillison.net/2026/Sep/7/jakub-pachocki/) ⭐️ 7.0/10

OpenAI 首席科学家 Jakub Pachocki 在 OpenAI 网站上发文称，快速开发强大且对齐的 AI，其主要理由是构建防御系统，以应对其他 AI 带来的危险。他还警告，防御需求不能成为鲁莽行事或不惜一切代价抢跑的理由。 这一表态分量很重，因为它出自 OpenAI 首席科学家，而当前全球正就 AI 安全与监管展开激烈辩论。它表明，即便是领先的 AI 开发者也将“对齐的防御性 AI”视为优先事项，同时明确反对以竞争为由进行鲁莽部署。 Pachocki 表示，防御性 AI 将用于保障基础设施安全、实时抵御 rogue agents（恶意代理/流氓智能体），并发明全新的防护措施；他将此称为 OpenAI 部署工作的首要重点。他承认整体 AI 进展存在不确定性，但认为一旦真正认识到利害关系之严重，就不应选择不计代价的竞赛。

rss · Simon Willison · 9月7日 22:26

**背景**: “AI 对齐”（AI alignment）是 AI 安全的一个重要方向，研究如何确保先进 AI 系统的行为符合人类意图，尤其是在模型能力超越人类之后。安全研究人员越来越担心，恶意或被入侵的 AI 智能体在网络中的移动速度可能远超人类防御者的追踪能力，因此需要借助 AI 本身来构建防御。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment - Wikipedia</a></li>
<li><a href="https://engineerine.com/rogue-ai-cybersecurity-threat/">Rogue AI Agents Are Creating a New Cybersecurity Threat – Engineerine</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#OpenAI`, `#AI ethics`, `#regulation`, `#AI policy`

---

<a id="item-11"></a>
## [DNS 滥用：约两成新增 gTLD 域名或为诈骗](https://simonwillison.net/2026/Sep/6/the-purpose-of-dns-is-to-spread-scams/) ⭐️ 7.0/10

Terence Eden 引用 Interisle 报告指出：2025 年新增的 8500 万个 gTLD 域名注册中，有 850 万个在 2025 年 5 月前被列入黑名单，这意味着新增 gTLD 域名中有 10%到 20%被用于诈骗或滥用。 这些数据将 DNS 重新定位为不只是中立的基础设施，而是互联网诈骗的主要分发渠道之一。如此普遍的滥用现象削弱了域名注册体系的公信力，也促使 ICANN、注册局和注册商必须采取更有力的应对措施。 相关数据来自 Interisle 发布的关于网络犯罪对域名需求的报告，Terence Eden 和 Andrew Campling 讨论了这一报告。Eden 认为 10% 的滥用率可能只是下限，实际比例可能接近 20%——大约每五个新注册的 gTLD 域名中就有一个涉及诈骗。

rss · Simon Willison · 9月6日 14:40

**背景**: 域名系统（DNS）负责将人类可读的域名转换为 IP 地址；通用顶级域（gTLD）如 .com 和 .org 是不与国家绑定的顶级域名类别。ICANN 负责协调 DNS，并资助了 INFERMAL 等项目来研究恶意注册的域名。DNS 滥用包括钓鱼、传播恶意软件和垃圾邮件，网络犯罪分子往往通过批量注册域名来实施这些行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generic_top-level_domain">Generic top-level domain - Wikipedia</a></li>
<li><a href="https://icannwiki.org/DNS_Abuse">DNS Abuse - ICANNWiki</a></li>
<li><a href="https://www.icann.org/dnsabuse">DNS Abuse Mitigation Program - ICANN</a></li>

</ul>
</details>

**标签**: `#DNS`, `#cybersecurity`, `#ICANN`, `#domain abuse`, `#scams`

---

<a id="item-12"></a>
## [从头重写遗留系统很少成功](https://simonwillison.net/2026/Sep/6/theres-no-limit-to-how-bad-code-can-get/) ⭐️ 7.0/10

西蒙·威利森发表评论认为，用全新重写替换遗留系统几乎总是失败，因为旧系统仍在不断演进，而维护它的团队失去动力。他建议用自动化测试和有针对性的重构来代替整体重写。 这一观点很重要，因为许多工程团队会考虑通过从零重写来摆脱技术债务，但这往往导致两套系统并行和资源浪费。Will Larson 的迁移策略提供了一种更具扩展性且风险更小的替代方案。 作者指出，在宣布重写之后，旧系统仍然是一个不断变化的目标，开发者只做最小改动来加功能，技术债务继续累积。最终“新”系统上线时只能处理旧系统的一部分功能，导致生产环境里同时存在两套系统。

rss · Simon Willison · 9月6日 09:08

**背景**: 技术债务指的是为快速交付而编写的草率代码在未来需要返工的隐性成本。从零重写很有吸引力，因为它承诺一个全新干净的代码库，但遗留系统通常缺少文档和测试，其完整行为很难被理解。Will Larson 的《迁移》一文推荐增量式、可测试的迁移，而不是“大爆炸”式重写。

**标签**: `#technical-debt`, `#software-engineering`, `#rewrite`, `#commentary`

---

<a id="item-13"></a>
## [从 Mercator 到 Equal Earth：GPT 制作的地图投影动画](https://simonwillison.net/2026/Sep/7/equal-earth/) ⭐️ 6.0/10

Simon Willison 发布了一个交互式工具，可使用 ChatGPT Work 中 GPT-6 Astra（medium）生成的 D3 代码，在经典 Mercator 投影与 Equal Earth 投影之间进行平滑的动画过渡。该动画让观看者直接比较各国在这两种投影下的面积与形状差异。 这是 AI 辅助编程在空间数据可视化领域的一个实际案例，表明一个热门新闻事件可以被多快地转化为可交互、可分享的演示。它也让公众能够直观理解广泛使用的 Mercator 投影所带来的面积扭曲，而这一问题是联合国近期鼓励采用等积投影决议的动因。 Equal Earth 是一种 2018 年由 Bojan Šavrič、Bernhard Jenny 和 Tom Patterson 发明的等积伪圆柱地图投影；与 Mercator 不同，它能够保持大陆块的相对面积。该工具托管在 tools.simonwillison.net，并附有一段展示形变效果的视频短片。

rss · Simon Willison · 9月7日 16:24

**背景**: 16 世纪诞生的 Mercator 投影保持了航向上的角度准确，但会严重放大高纬度地区的面积，使格陵兰等区域看起来比非洲大得多。Equal Earth 是 2018 年提出的一种等积投影，外观接近广泛使用的 Robinson 投影，却能保持各地区之间的相对面积。2026 年 9 月，联合国大会投票鼓励世界地图采用等积投影，并明确提到 Equal Earth。D3.js 是一种广泛用于在网页中制作动态与交互式数据可视化的 JavaScript 库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Equal_Earth_map_projection">Equal Earth map projection</a></li>
<li><a href="https://en.wikipedia.org/wiki/D3.js">D3.js</a></li>

</ul>
</details>

**标签**: `#geospatial`, `#d3`, `#AI-assisted coding`, `#data visualization`

---