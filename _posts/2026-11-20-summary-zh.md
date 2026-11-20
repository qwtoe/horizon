---
layout: default
title: "Horizon Summary: 2026-11-20 (ZH)"
date: 2026-11-20
lang: zh
---

> 从 15 条内容中筛选出 11 条重要资讯。

---

1. [PostgreSQL 19 正式发布，新增 WAIT FOR LSN 让备库实现读己之写一致性](#item-1) ⭐️ 9.0/10
2. [Anthropic 登陆纳斯达克，检验 AI 估值与工程师焦虑](#item-2) ⭐️ 8.0/10
3. [Anthropic 称 Claude 解决了黑洞物理学的两个未解难题](#item-3) ⭐️ 8.0/10
4. [OpenJDK“java4shell”补丁 PR 引发 LLM 审计归因之争](#item-4) ⭐️ 8.0/10
5. [英国法庭迫使政府承认曾向苹果发出秘密加密命令](#item-5) ⭐️ 8.0/10
6. [ruby2ßhell：单字节堆溢出导致原生 Rails 面临预认证 RCE](#item-6) ⭐️ 8.0/10
7. [实验性病毒注射使三名胰腺癌患者病情得到控制](#item-7) ⭐️ 7.0/10
8. [98%老虎机：付费广告如何变成榨取税](#item-8) ⭐️ 7.0/10
9. [Daniel Stenberg：AI 生成的 Rust 重写版跟不上 curl 的真实修复速度](#item-9) ⭐️ 7.0/10
10. [浏览器应用可从单张 A4 纸打印 8 页可折叠小志](#item-10) ⭐️ 6.0/10
11. [datasette-arrows 0.1a0 为 Datasette 带来流式 Apache Arrow 导出功能](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [PostgreSQL 19 正式发布，新增 WAIT FOR LSN 让备库实现读己之写一致性](https://simonwillison.net/2026/Nov/19/postgresql-19/) ⭐️ 9.0/10

PostgreSQL 19 已正式发布，比该项目通常的 9 月发布节奏晚了约两个月；其中最受关注的新特性之一是面向备库会话的 `WAIT FOR LSN` 命令。备库上的会话现在可以阻塞等待，直到其重放预写日志（WAL）至指定的日志序列号（LSN）后再执行查询，从而让应用能够可靠地读到刚刚在主库写入的数据。 读副本是大多数大型应用扩展读能力的主要手段，但在此之前，备库上的读己之写一致性要么由应用自己手工实现，要么干脆放弃。把这一原语直接内置到数据库核心里，消除了主备架构用户长期面临的一个陷阱；与此同时，这次发布也反映出大量由 AI 报告的安全漏洞如何改变了项目的发布日程。 该机制依赖主库上的 `pg_current_wal_insert_lsn()` 获取类似 `0/0306EE20` 的令牌，应用将其保存（作者建议存入签名 Cookie），随后在备库上执行 `WAIT FOR LSN '0/0306EE20' WITH (TIMEOUT '0.1s')`；超时参数是可选的，一旦指定，若副本未能在限定时间内追上则会报错。这与维基百科的 MediaWiki 长期在 MySQL 上实现的模式如出一辙，后者使用 `WAIT_FOR_EXECUTED_GTID_SET()` 及其回退方案 `SOURCE_POS_WAIT()`。

rss · Simon Willison · 11月19日 20:43

**背景**: PostgreSQL 大约每年发布一个新的主版本，项目历来以 9 月为目标。复制的工作原理是把预写日志（WAL）从主库流式传输到一个或多个备库，备库通过重放这些日志保持同步；日志中的每条记录都带有一个单调递增的日志序列号（LSN），而由于重放总是落后于主库，备库上的读取可能读不到刚刚写入的数据。所谓“读己之写”一致性，是指刚刚执行过写入的用户，在后续读取中一定能看到这次写入的效果，即便这些读取是由副本处理的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.postgresql.org/about/news/postgresql-19-released-3449/">PostgreSQL : PostgreSQL 19 Released!</a></li>
<li><a href="https://www.crunchydata.com/blog/postgres-wal-files-and-sequuence-numbers">Postgres WAL Files and Sequence Numbers | Crunchy Data Blog</a></li>
<li><a href="https://www.postgresql.org/docs/current/runtime-config-replication.html">PostgreSQL: Documentation: 18: 19.6. Replication</a></li>

</ul>
</details>

**标签**: `#postgresql`, `#databases`, `#release`, `#replication`, `#security`

---

<a id="item-2"></a>
## [Anthropic 登陆纳斯达克，检验 AI 估值与工程师焦虑](https://www.reuters.com/business/finance/anthropics-historic-debut-put-ais-promise-peril-wall-st-test-2026-11-19/) ⭐️ 8.0/10

Anthropic 正式在纳斯达克挂牌上市，IPO 定价为每股 83 美元，开盘价 111.50 美元，收盘报 97.17 美元——较发行价上涨约 17%，但较首笔成交价下跌约 13%。有评论者援引约 1.26 万亿美元的估值，并引用 Yahoo Finance 的说法称这是“2008 年以来大型 IPO 最糟糕的开局半小时”。 这次上市被视为一场关键的公开市场检验：AI 公司能否为其巨额私募估值提供合理支撑；而疲软的开局已被解读为对 OpenAI 自身估值野心的警示信号。与此同时，这对在职软件工程师也是一次心理冲击，因为许多人把前沿 AI 实验室的产品视为对自己生计的直接竞争。 83 美元发行价与 111.50 美元开盘价之间的差距很关键：IPO 股份主要配售给机构投资者，因此在交易开始后才买入的人到收盘时基本处于亏损状态，除非他们以发行价拿到股票。评论者还指出，隐含估值已从几周前传出的 2 万亿美元以上水平回落，并跌破 OpenAI 在私募市场上一度寻求的估值水平。

hackernews · wslh · 11月19日 17:02 · [社区讨论](https://news.ycombinator.com/item?id=50562754)

**背景**: IPO（首次公开募股）是指一家私有公司向公众发行股票并在纳斯达克等交易所上市的过程。所谓“IPO 发行价”是在上市前夜确定的，主要出售给大型机构投资者；而“开盘价”则是股票在交易所实际成交的第一笔价格，可能远高于或远低于发行价。此前，包括 Anthropic 和 OpenAI 在内的主要 AI 实验室主要通过私募融资轮次估值，因此公开上市是更广泛的市场第一次能够每天对这些数字“投票”。Anthropic 由前 OpenAI 研究人员于 2021 年创立，是 Claude 系列 AI 模型背后的公司。

**社区讨论**: 这条拥有 1660 条评论的讨论帖情绪焦虑且充满怀疑：一位工程师称这次上市是“人类历史上的重大时刻”，但同时断言对软件开发者而言“好日子基本结束了”；其他人则细究估值较几周前传闻的 2 万亿美元以上水平跌了多少，认为这对 OpenAI 不是好兆头。一位有 50 年编程经验的资深人士提供了历史视角，回忆当年学习 C 语言还能换来一趟公司全包的新加坡之旅，但他也承认如今很难给行业新人什么明确建议。

**标签**: `#AI industry`, `#IPO`, `#Anthropic`, `#valuation`, `#software-engineering-careers`

---

<a id="item-3"></a>
## [Anthropic 称 Claude 解决了黑洞物理学的两个未解难题](https://www.anthropic.com/research/claude-black-hole-physics) ⭐️ 8.0/10

Anthropic 发布研究文章，声称其 Claude 模型解决了黑洞物理学中的两个未解难题，相关成果以技术论文形式呈现（其中一篇是晦涩难读的“bootstrap”论文）。该消息迅速登上 Hacker News 热榜，有评论者感慨：如今这类成果已经可以像例行公事一样出现在前沿模型的发布清单里。 如果这些说法站得住脚，这就是 AI 系统参与理论物理研究、而非只做软件和文本任务的醒目案例，也会增强“前沿模型可作为科研合作者”的论据。与此同时，它也激化了社区反复争论的问题：功劳到底该归于模型，还是归于提出问题、设计提示词并验证答案的研究者。 据浏览过材料的评论者称，第一个结果本质上是一次复杂且易出错的计算，第二个结果则更令人印象深刻：Claude 据称证明了与给定中心电荷相容的黑洞质量上限，从而排除任何预言更大质量的理论成为该宇宙中自洽的量子引力理论。批评者指出，博客文章和两篇论文中都没有出现“prompt（提示词）”一词，因此读者无法判断模型获得了多少引导。

hackernews · cybermango · 11月19日 17:30 · [社区讨论](https://news.ycombinator.com/item?id=50563148)

**背景**: Anthropic 是一家 AI 安全与研究公司，开发了 Claude 系列大语言模型，其研究博客用于发布能力与可解释性方面的发现。这里涉及的物理属于黑洞与量子引力的理论研究，“bootstrap”方法以及中心电荷这类量被用来约束哪些理论在数学上自洽，而不是用来做实验。由于这类结果是在纸面上证明出来的，一旦声称由大语言模型完成，就会立刻引出关于验证、来源归属以及问题如何被提出的疑问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/">Home \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/models/overview">Models overview - Claude Platform Docs</a></li>

</ul>
</details>

**社区讨论**: 社区情绪复杂，且多停留在元讨论层面：一些评论者认为第二个结果确实很酷，并称赞博客文章比论文更易读；另一些人则反对“Claude 解决了”这种说法，认为这是在把机器拟人化，主张应像“我们没能造出合格的沙箱”而不是“它逃出了沙箱”那样表述。多人要求把提示词历史作为附录公开，以便评估这项工作，还有一条高赞评论感叹数十条评论竟没有一条真正讨论论文本身。

**标签**: `#AI for Science`, `#Physics`, `#Black Holes`, `#Large Language Models`, `#Anthropic`

---

<a id="item-4"></a>
## [OpenJDK“java4shell”补丁 PR 引发 LLM 审计归因之争](https://github.com/openjdk/jdk/pull/32781) ⭐️ 8.0/10

针对 OpenJDK jdk 仓库的第 32781 号 PR 报告了一个被称为“java4shell”的漏洞，随后 Oracle 要求作者暂缓提交并最终接管了修复工作，由此引发争议。争论的焦点在于：这次由 LLM 辅助安全审计“发现”的漏洞，究竟属于独立发现，还是仅仅重复了此前已提交的报告。 这场争议直指 AI 辅助漏洞研究究竟该获得多少信任：如果模型只是把公开 issue 中已有的线索重新翻出来，那么“AI 独立发现高危漏洞”的说法就需要更严格的审视。这对运行 Java 的企业也有直接影响，因为涉及的底层缺陷是一个广泛部署的运行时中的严重远程代码执行问题。 评论者指出，Oracle 合并提交所用的说明与 PR 原文逐字相同；PR 作者称 10 月 1 日收到 Oracle 邮件，要求其在获得批准前不要继续推进，10 月 28 日又表示工作“已由 Oracle 接管”。据公开披露，该问题编号为 CVE-2026-114938，CVSSv4.0 评分 9.2，是 OpenJDK Base64 解码器中的内存破坏漏洞，畸形的 Base64 输入即可触发远程代码执行，由 Calif 的研究人员于 2026 年 11 月 17 日公开。

hackernews · notmine1337 · 11月19日 11:47 · [社区讨论](https://news.ycombinator.com/item?id=50558906)

**背景**: OpenJDK 是 Java SE 的开源参考实现，因此其中的内存安全缺陷会影响数量极其庞大的 Java 运行时与应用服务器。"java4shell" 这一命名显然是在致敬 2021 年的 Log4Shell（CVE-2021-44228）——那是 Log4j 中通过 JNDI 查找实现任意代码执行的著名漏洞，也为此后灾难级 Java 漏洞定下了命名范式。LLM 辅助漏洞发现是指让 Codex 之类的大模型去扫描代码库、标记可疑缺陷的工作流，近年来已成为安全研究中快速升温的方向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sentinelone.com/blog/java4shell-vulnerability-in-openjdk-enables-rce-on-avx-512-cpus/">Defending Against Java 4 Shell : Vulnerability in OpenJDK Enables...</a></li>
<li><a href="https://www.wiz.io/blog/cve-2026-114938-rce-java4shell-openjdk">CVE-2026-114938 OpenJDK RCE ( Java 4 Shell ): Everything... | Wiz Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Log4Shell">Log4Shell - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论普遍持怀疑态度：有人指出 PR 讨论中引用的第一个 issue（adoptium-support #1480）显示该问题此前已被报告，暗示模型可能读到了这份已有报告，而非独立发现漏洞。也有人认为，判断漏洞严重性并构造利用代码仍属需要人工监督的能力，而模型是否被旧报告“污染”恐怕永远无法证实。

**标签**: `#security`, `#OpenJDK`, `#vulnerability research`, `#LLM`, `#AI-assisted auditing`

---

<a id="item-5"></a>
## [英国法庭迫使政府承认曾向苹果发出秘密加密命令](https://macanorak.com/uk-government-forced-to-admit-it-issued-apple-a-secret-encryption-order/) ⭐️ 8.0/10

英国调查权力法庭（Investigatory Powers Tribunal）确认，英国政府曾向苹果发出一份秘密法律通知，针对的是保护 iCloud 账户的加密措施，从而结束了近两年来官方对该命令拒不承认的状态——尽管此事早已被广泛报道。法庭认定，媒体是通过保密的安全简报而非泄密得知这份“技术能力通知”的，而通知的具体内容目前仍属机密。 这是英国首次正式确认其动用了法律权力，迫使一家大型外国科技公司削弱端到端加密，印证了业界长期的警告，也为其他政府树立了先例。这直接影响到那些“高级数据保护”功能被下架的英国苹果用户，同时也让所有在英国市场提供强加密服务的厂商面临更大风险。 据报道，该命令后来被收窄至仅涵盖存储在苹果加密云端的英国公民数据，而苹果对第二份通知同样提出了挑战；通知原文仍属机密，因此具体的技术要求外界无从得知。技术能力通知由英国国务大臣依据《2016 年调查权力法》第 253 条发出，可要求运营商构建或维持用于合法拦截、设备干扰或获取通信数据的能力。

hackernews · Terretta · 11月19日 16:21 · [社区讨论](https://news.ycombinator.com/item?id=50562113)

**背景**: 《2016 年调查权力法》是英国整合后的监控法律，其第 253 条允许内政大臣命令电信和邮政运营商确保具备协助拦截的能力，具体义务列于 2018 年的《技术能力条例》之中。苹果的“高级数据保护”（ADP）是一项可选的 iCloud 设置，可将端到端加密扩展到备份、照片和备忘录，使苹果自身也无法读取。2025 年初，苹果选择在英国对新用户下架 ADP 而非遵从该命令，并通过调查权力法庭对该通知提出抗辩——该法庭的程序在设计上大部分是保密的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/11/19/u-k-government-forced-to-disclose-secret-apple-backdoor-order/">UK government forced to disclose secret Apple backdoor order</a></li>
<li><a href="https://therecord.media/apple-uk-encryption-notice">UK court confirms British government served Apple with secret ...</a></li>
<li><a href="https://www.legislation.gov.uk/ukpga/2016/25/section/253">Investigatory Powers Act 2016 - Legislation.gov.uk</a></li>

</ul>
</details>

**社区讨论**: 评论者大多持批评态度：有人指出苹果已悄然把安全承诺从“任何人都无法获取你的数据，包括苹果”弱化为仅仅是“苹果无法获取你的数据”，并解释道设备上生成的密钥很可能只是密钥加密密钥，而非真正保护数据的密钥。也有人给出法庭判决作为一手信源，并强调这一披露源自保密简报而非泄密；还有几位评论者认为这不过是印证了英国长期以来咄咄逼人的大规模监控，并非全新的范式转变。

**标签**: `#encryption`, `#Apple`, `#UK surveillance`, `#privacy`, `#government policy`

---

<a id="item-6"></a>
## [ruby2ßhell：单字节堆溢出导致原生 Rails 面临预认证 RCE](https://verialabs.com/ruby2shell/) ⭐️ 8.0/10

研究人员公开了名为“ruby2ßhell”的漏洞细节（CVE-2026-132825），这是 Ruby 字符串大小写转换代码中的一个单字节堆溢出，可被串联利用，在未经身份验证的情况下对原生 Ruby on Rails 应用实现远程代码执行。该漏洞的成因是：在多种单字节编码中，德语特殊字符“ß”（字节 0xDF）转为大写时会扩展为两个字符“SS”，但 Ruby 只按一个字节的结果进行了处理。 Rails 是部署最广泛的 Web 框架之一，而预认证 RCE 意味着攻击者无需任何凭据或用户交互即可利用，未打补丁的应用可能被直接完全攻陷。这一发现还引发了更广泛的讨论：AI 辅助工具是否正在把过去难以利用的内存安全缺陷，变成可以例行武器化的 RCE。 该缺陷存在于 Ruby 对 ISO-8859-1、ISO-8859-2 及其他 ISO-8859 变体，以及 Windows-1250、Windows-1252、Windows-1254 和 Windows-1257 编码字符串执行大写转换的方式中，利用时需要存在一条攻击者可控输入进入大小写转换的路径。社区成员指出，该问题与一份已发布的 Ruby 安全公告存在重叠，该公告已涵盖另外六个漏洞，因此应用该公告的补丁很可能也能修复此问题。

hackernews · jdns · 11月19日 05:09 · [社区讨论](https://news.ycombinator.com/item?id=50556287)

**背景**: Ruby on Rails 是基于 Ruby 语言的开源 Web 框架，“原生 Rails”指默认、未做深度定制的安装实例，而非经过大量改造的应用。预认证 RCE 指的是在服务端执行任意代码时无需通过任何登录校验，通常借助请求解析等在身份验证生效之前发生的处理流程实现。堆溢出是指程序写入的数据超出内存缓冲区容量；虽然单字节溢出只是一个很小的原语，但攻击者可以将其与其他行为串联以劫持执行流。该命名沿用了由 Log4Shell 普及开来的“-shell”式命名习惯，其中“ß”的发音类似英语的“S”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://orca.security/resources/blog/ruby2shell-ruby-heap-overflow-rce/">ruby2ßhell: CVE-2026-132825 Ruby Heap Overflow RCE</a></li>
<li><a href="https://cybersecuritynews.com/ruby2shell-rce/">ruby2ßhell: Critical One-Byte Heap Overflow in Ruby Could ...</a></li>
<li><a href="https://nhimg.org/glossary/pre-auth-rce/">What Is Pre-auth RCE? Definition & Examples - nhimg.org</a></li>

</ul>
</details>

**社区讨论**: 评论者对源源不断的“x2shell”式严重 CVE 持怀疑态度，有人认为是 AI 自动完成了构建完整利用链的繁琐工作，使任何单字节溢出都能被报告为 RCE，从而实质上迫使整个行业转向内存安全的软件。也有人追问，在如此高产的情况下这类发现何时才不再值得当作新闻；还有评论者澄清，这一问题其实已被当前讨论中的 Ruby 安全公告所涵盖（该公告还涉及另外六个漏洞）。不少读者最感兴趣的还是技术问题：单字节溢出究竟如何被利用来实现可靠的代码执行。

**标签**: `#security`, `#rails`, `#ruby`, `#rce`, `#vulnerability-research`

---

<a id="item-7"></a>
## [实验性病毒注射使三名胰腺癌患者病情得到控制](https://www.newscientist.com/article/2528235-pancreatic-cancer-halted-by-virus-injection-in-three-patients/) ⭐️ 7.0/10

在明尼苏达大学开展的一项一期临床试验中，三名无法手术的胰腺癌患者在接受治疗后病情趋于稳定，该治疗将一种经过基因工程改造的腺病毒直接注射进他们的肿瘤内部。New Scientist 报道了这一结果，认为它针对一种通常在数月内就会恶化的癌症释放出了早期但令人鼓舞的信号。 胰腺癌是所有实体瘤中生存率最差的癌种之一，多数患者确诊时已错过手术时机，中位生存期常常只有几个月，因此一期试验中任何病情得到控制的迹象都会引发关注。这一早期积极结果也为溶瘤病毒疗法作为现有免疫治疗手段的补充提供了更多支持。 该试验是一项仅有三人参加的一期研究，因此其结果只是安全性与可行性的信号，而非疗效证明，报道中也尚未明确给药方案、缓解持续时间以及所用病毒载体的具体类型。有评论者指出，公开信息过于有限，以至于要确定具体是哪项试验还需到 ClinicalTrials.gov 上交叉比对，而该网站上已经列出了数十项针对胰腺癌的溶瘤病毒研究。

hackernews · cybermango · 11月19日 17:25 · [社区讨论](https://news.ycombinator.com/item?id=50563066)

**背景**: 溶瘤病毒是天然存在或经过基因工程改造的病毒，能够选择性地感染肿瘤细胞并在其中复制，直接将其杀死，同时释放肿瘤抗原，帮助免疫系统识别并攻击身体其他部位的癌细胞。这类病毒可通过瘤内注射、静脉给药或其他途径递送；胰腺癌因其致密且具有免疫抑制作用的基质使传统化疗和免疫治疗大多失效，因而成为该疗法的重点攻关对象。过去十年间该领域已开展多项一期试验，但在胰腺癌中能否获得持久的临床获益仍未被证实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scienceinhand.com/pancreatic-cancer-halted-by-virus-injection-in-three-patients/">Pancreatic cancer halted by virus injection in three patients</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8474975/">Oncolytic virus therapy in cancer: A current review - PMC</a></li>
<li><a href="https://tgh.amegroups.org/article/view/10455/html">Intratumoral oncolytic virotherapy in pancreatic cancer : from...</a></li>

</ul>
</details>

**社区讨论**: 讨论中充满了个人悲痛：多位评论者讲述了父亲和叔父在误诊或病情迅速恶化后死于胰腺癌的经历，并表示这类新闻虽然对自家人来说为时已晚，却让他们对其他人抱有希望。另一些人则试图弄清背后的科学，分享了 ClinicalTrials.gov 上的溶瘤病毒研究清单和综述论文，想确认究竟注射了什么，并对文章提供的信息过于简略表达了不满。

**标签**: `#pancreatic cancer`, `#oncolytic virus`, `#immunotherapy`, `#medical research`, `#clinical trial`

---

<a id="item-8"></a>
## [98%老虎机：付费广告如何变成榨取税](https://globalcommercegraph.com/writing/the-ninety-eight-percent-slot-machine) ⭐️ 7.0/10

一篇题为《98%老虎机》的文章认为，付费在线广告已演变为对企业征收的抽取性税负，并用赌场/老虎机作类比，同时在 Hacker News 上引发了对该类比是否成立的辩论。 这篇文章之所以重要，是因为广告支出是线上企业的一项主要成本，而“平台拿走了大部分价值”的说法加剧了人们对平台权力、不透明拍卖机制以及广告主和发布商回报下降的持续担忧。 该论点属于评论分析而非技术突破，批评者指出广告拍卖是一个市场，广告主的回报来自第三方客户而非平台本身，这削弱了赌场类比的成立基础；评论者还认为算法化广告系统可能更奖励优化能力而非创意质量。

hackernews · dev1one1 · 11月19日 18:35 · [社区讨论](https://news.ycombinator.com/item?id=50564159)

**背景**: 付费在线广告通常通过程序化拍卖运行，包括实时竞价和头部竞价，广告位会在毫秒级时间内卖给出价最高者。平台位于广告主和发布商之间，设定拍卖规则、定向条件和衡量方式，这使它们对定价和价值分配拥有很大控制权。经济学家将这类中介视为可通过费用和设计选择抽取租金的平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://advertising.amazon.com/library/guides/real-time-bidding">What is Real - Time Bidding ? Definition and Importance | Amazon Ads</a></li>
<li><a href="https://advertising.amazon.com/library/guides/header-bidding">What is Header Bidding? How Does It Work? | Amazon Ads</a></li>
<li><a href="https://onlinelibrary.wiley.com/doi/10.1111/joie.12404">Platform design and rent extraction* - Piolatto - 2025 - The ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者意见分化：hatthew 认为赌场类比不成立，因为广告拍卖是市场，广告主的收益来自第三方客户；hackthemack 则称广告行业是反复出现的“万灵药”叙事，并链接到 2019 年的讨论和 Freakonomics 节目。bearjaws 承认广告有效，但认为随着算法捕获取代过去对巧妙创意的奖励，广告变得更具抽取性；PaulHoule 则从构建者角度补充了病毒传播和漏斗优化的经验。

**标签**: `#adtech`, `#online advertising`, `#platform economics`, `#extraction`, `#Hacker News discussion`

---

<a id="item-9"></a>
## [Daniel Stenberg：AI 生成的 Rust 重写版跟不上 curl 的真实修复速度](https://simonwillison.net/2026/Nov/18/daniel-stenberg/) ⭐️ 7.0/10

在 2026 年 11 月 17 日题为《Actual curl rewrites in Rust》的博客文章中，curl 创始人 Daniel Stenberg 将 AI 生成的重写版本与真实的维护工作做了对比：在短短三周多的时间里，编码智能体把 18.5 万行 C 代码转换成了 34 万行 Rust 代码，而同一时期真正的 curl 项目合并了 300 多个提交，其中包括 200 多个缺陷修复和若干安全漏洞修复。 这是对“氛围移植”（vibe porting）论调的一次有力反驳——该论调认为 LLM 智能体可以一次性把成熟的 C 代码库翻译成内存安全的 Rust；而发声者是全球部署最广的软件之一的维护者，他把讨论的焦点从“生成了多少行代码”转向“生成的克隆版本能否继承多年积累的安全加固”。 这一对比针对的是维护水平的对等，而非代码数量：AI 生成的 Rust 代码大约是原 C 代码的 1.8 倍长，但它在诞生时就被冻结在某个时间点上；Stenberg 反问，当 curl 在接下来一个月里再完成 200 个修复、可能还有更多漏洞补丁时，这些克隆版本还能跟得上吗。值得注意的是，他的论点并不是说 Rust 毫无意义——curl 自己的安全文档就把许多历史缺陷归为“C 语言错误”（溢出、越界读取、双重释放、释放后使用、空指针和未初始化值等），而内存安全的语言很可能可以避免这些问题。

rss · Simon Willison · 11月18日 15:58

**背景**: curl 及其库 libcurl 是一个用于在网络协议上传输数据的命令行工具和编程库，据估计被嵌入到数百亿台设备中，从服务器到汽车再到手机随处可见。由于它用 C 语言编写，而 C 不提供内存安全保证，普通的编码失误就会变成可被利用的安全漏洞，因此该项目有一套正式的漏洞公告流程，并在定期发布版本中交付修复——仅 2026 年 10 月的 curl 8.23.0 就包含了 24 项安全修复。正是同样的内存安全动机推动了 2026 年的一系列实验，例如 Google 借助 AI 把 giflib 这个 C 库迁移到 Rust，用 LLM 智能体配合差分模糊测试来翻译整个代码仓库；Stenberg 的文章则是对这类“翻译副本”与仍在活跃演进的上游项目之间关系的现实审视。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://curl.se/docs/security.html">curl - CVEs 24 Security Vulnerabilities Patched in curl Used Across 30 ... curl - Security advisory Security - everything curl Curl Latest Vulnerabilities - securityvulnerability.io How the curl Project Finds and Fixes Vulnerabilities With AISLE</a></li>
<li><a href="https://www.infoq.com/news/2026/09/c-rust-rewrite/">Google Rewrites Critical C Dependencies to Rust Using AI and ...</a></li>
<li><a href="https://cybersecuritynews.com/curl-security-update-24-vulnerabilities/">24 Security Vulnerabilities Patched in curl Used Across 30 ...</a></li>

</ul>
</details>

**标签**: `#curl`, `#rust`, `#ai-code-generation`, `#open-source-maintenance`, `#security`

---

<a id="item-10"></a>
## [浏览器应用可从单张 A4 纸打印 8 页可折叠小志](https://krthr.co/paper-folds-and-whats-new-in-fanzines-app/) ⭐️ 6.0/10

一篇博客文章介绍了一款基于浏览器的应用，它利用特定的折叠算法把每一页放到正确的位置和方向，从而用单张 A4 纸排版并打印出一本完整的 8 页可折叠小志（zine）。用户在浏览器中编辑好各页内容后，即可直接发送到家用打印机输出。 它把通常属于印刷厂专业印前软件范畴的拼版工作搬到了一个免费网页中，降低了爱好者、教师和学生自行制作迷你小册子的门槛。这也说明仅靠 CSS 就能把浏览器打印能力发挥到什么程度。 该应用只针对一种特定的 8 页折叠方式，而非通用的骑马订书帖拼版，并依赖 CSS @page 规则等浏览器打印样式来控制纸张尺寸、方向和页边距。因此最终输出质量取决于用户的打印机驱动和纸张设置。

hackernews · krthr · 11月19日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=50559719)

**背景**: 小志（zine）是一种小型的自行出版小册子，通常靠复印和手工折叠制作；经典的 8 页形式来自对单张纸的折叠与剪裁，无需胶水或订书钉。印前工作中，为了让页面在打印和折叠后按阅读顺序出现而对页面重新排序（有时还要旋转）的做法被称为拼版（impositioning），传统上由面向商业印刷的专用软件完成。这个项目把同样的思路带到了一个面向爱好者的浏览器工具中，利用 CSS 打印媒体样式来定义打印页面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://snipzine.com/how-to-fold-a-zine">How to fold an 8-page zine from one sheet of paper — snipzine</a></li>
<li><a href="https://printingnumbering.com/imposition-printing.html">Imposition Printing — Page Layout Calculator + Signatures Guide</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Printing">Printing - CSS | MDN - MDN Web Docs</a></li>

</ul>
</details>

**社区讨论**: 评论者给出了专业术语“拼版（impositioning）”，并提到 Bookbinder JS 和 PocketMod 等相关工具，其中一些人对文章只字未提 PocketMod 感到不满，认为这种折叠创意很可能源自它。还有人分享了用这种折法做考试小抄的趣事，并认为只需要一个简单的命令行或 PDF 拼版工具就够了，不必做一个完整的编辑器。

**标签**: `#web-app`, `#printing`, `#paper-craft`, `#hackernews`, `#personal-project`

---

<a id="item-11"></a>
## [datasette-arrows 0.1a0 为 Datasette 带来流式 Apache Arrow 导出功能](https://simonwillison.net/2026/Nov/18/datasette-arrows/) ⭐️ 6.0/10

Simon Willison 发布了 datasette-arrows 0.1a0，这是一个 alpha 版插件，为 Datasette 的表格导出对话框增加了 Apache Arrow IPC 流导出选项。它基于 Datasette 1.0a43（2026 年 11 月 15 日发布）引入的新流式导出能力，允许插件通过 register_output_renderer() 钩子实现流式导出格式。 Datasette 原本已能对拥有数百万行的表进行流式 CSV 和 TSV 导出，而无需将所有数据载入内存，这个插件证明同样的模式现在可以扩展到其他格式。Arrow 输出可被 DuckDB、pandas、Polars 等分析工具直接读取，使把大型 Datasette 表导入数据分析流程变得更加容易。 该插件为 alpha 版本，可通过 `datasette install datasette-arrows` 安装，导出对话框会以“Apache Arrow IPC stream”的形式呈现，并提供下载和复制 URL 按钮。Willison 指出，截图来自 Datasette 的 main 分支：最新正式版本尚未把 Arrow 与 TSV、CSV 一起归入“All rows in this table”区域，这一分组预计会在下一个 alpha 版本中出现。

rss · Simon Willison · 11月18日 17:09

**背景**: Datasette 是一个用于浏览和发布 SQLite 数据库的 Python 工具，其导出功能以插件形式实现，通过为指定的表或查询注册输出渲染器来扩展格式。Apache Arrow 是一种与语言无关的列式内存格式；其 IPC 流式格式用于发送任意长度的记录批次序列，必须从头到尾依次处理，这与支持随机访问的 Arrow 文件格式不同。由于流式格式无需缓存整个数据集，它正好契合 Datasette 已在 CSV 上采用的按块导出方式。Willison 还提到，是 Claude Fable 5.2 建议采用 Arrow 流式格式，并且几乎一次性生成了这个插件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arrow.apache.org/docs/python/ipc.html">Streaming , Serialization, and IPC — Apache Arrow v26.0.1</a></li>
<li><a href="https://docs.datasette.io/en/stable/plugin_hooks.html">Plugin hooks - Datasette documentation</a></li>
<li><a href="https://dev.to/astrojuanlu/demystifying-apache-arrow-5b0a">Demystifying Apache Arrow - DEV Community</a></li>

</ul>
</details>

**标签**: `#Datasette`, `#Apache Arrow`, `#data-export`, `#plugin`, `#streaming`

---