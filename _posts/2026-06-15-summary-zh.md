---
layout: default
title: "Horizon Summary: 2026-06-15 (ZH)"
date: 2026-06-15
lang: zh
---

> 从 17 条内容中筛选出 10 条重要资讯。

---

1. [Pyodide 314.0 允许直接将 WASM 包发布到 PyPI](#item-1) ⭐️ 9.0/10
2. [里约声称自主研发的大语言模型被揭为合并模型](#item-2) ⭐️ 8.0/10
3. [形式化方法与编程的未来](#item-3) ⭐️ 8.0/10
4. [AI 不会取代软件工程师：基于证据的观点](#item-4) ⭐️ 8.0/10
5. [Kage：将任何网站打包成单个二进制文件以供离线查看](#item-5) ⭐️ 7.0/10
6. [Alan Perlis 1982 年编程箴言重新浮现](#item-6) ⭐️ 7.0/10
7. [将 SQLite 结果列映射回源表.列](#item-7) ⭐️ 7.0/10
8. [Adobe RMSDK 导致 Kobo 电子书渲染问题](#item-8) ⭐️ 6.0/10
9. [Trace：离线 Mac 会议转录应用，支持会议中标记关键点](#item-9) ⭐️ 6.0/10
10. [luau-wasm 0.1a0：首个通过 Pyodide 将 Lua 带到 WebAssembly 的 Alpha 版本](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Pyodide 314.0 允许直接将 WASM 包发布到 PyPI](https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/#atom-everything) ⭐️ 9.0/10

Pyodide 314.0 现在允许 Python 包维护者直接向 PyPI 发布 WebAssembly (WASM) 包，使用 PEP 783 定义的新 PyEmscripten 平台标签。此前，Pyodide 维护者需要自己构建和托管超过 300 个包。 这消除了 Pyodide 生态系统的一个重大瓶颈，减轻了核心维护者的负担，并允许任何包作者轻松分发与 WASM 兼容的包。它还向更多库开放了浏览器中的 Python 生态系统。 PyPI 现在接受 PyEmscripten 平台标签（例如 pyemscripten_2026_0_wasm32）。PyPI 的 warehouse 仓库的 PR 于 4 月 21 日合并。cibuildwheel 等工具支持构建这些包。

rss · Simon Willison · 6月13日 23:55

**背景**: Pyodide 是一个用于 WebAssembly 的 Python 运行时，允许通过 Pyodide 的控制台或网页应用在浏览器中运行 Python 代码。以前，为 Pyodide 分发 Python 包需要 Pyodide 团队进行特殊处理和托管，这是一个手动瓶颈。PEP 783 标准化了 Emscripten 包的平台标签，而 PyPI 现在接受它们。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://peps.python.org/pep-0783/">PEP 783 – Emscripten Packaging | peps . python .org</a></li>
<li><a href="https://pyodide.org/en/latest/development/abi/314.html">pyemscripten _2026_0 (under development) — Version 314.1.0.dev0</a></li>
<li><a href="https://pydantic.dev/articles/emscripten-wheels-pydantic">Building Emscripten wheels for Pyodide and PyPI ( PEP 783 )</a></li>

</ul>
</details>

**社区讨论**: 在 Hacker News 上，这一公告受到了热烈欢迎，许多人称这是期待已久的修复。一些人讨论了剩余的限制，例如需要静态链接和 WASM 包的大小，但总体情绪非常积极。

**标签**: `#Pyodide`, `#WebAssembly`, `#Python`, `#PyPI`, `#package management`

---

<a id="item-2"></a>
## [里约声称自主研发的大语言模型被揭为合并模型](https://github.com/nex-agi/Nex-N2/issues/4) ⭐️ 8.0/10

调查显示，里约热内卢声称自主研发的大语言模型 Rio-3.5-Open-397B 实际上是 Nex-N2 Pro（60%）和 Qwen3.5-397B-A17B（40%）的加权合并，且未充分披露。 这一事件引发了对 AI 开发中透明性和归因的严重担忧，因为模型合并可能被误称为原创工作。它凸显了制定明确指南以披露模型来源的必要性。 合并使用线性插值，所有 60 层和组件的权重比例完全相同，表明未进行额外训练或蒸馏。'自主研发微调'的说法与实际方法相矛盾。

hackernews · unrvl22 · 6月14日 15:37 · [社区讨论](https://news.ycombinator.com/item?id=48528371)

**背景**: 模型合并是一种将多个预训练模型的权重合并到一个模型中的技术，无需重新训练，通常使用加权求和或球面线性插值（SLERP）。它被广泛用于高效提升性能，但若未正确归因则可能被滥用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://smithery.ai/skills/davila7/model-merging">model - merging - Skill | Smithery</a></li>
<li><a href="https://www.emergentmind.com/topics/homogeneous-heterogeneous-model-merging">Homogeneous-Heterogeneous Model Merging</a></li>

</ul>
</details>

**社区讨论**: 一些评论者认为遗漏可能非故意，因为 Nex 本身基于 Qwen，但其他人批评缺乏透明度。讨论还探讨了合并的工作原理，有人惊讶于简单的线性混合就能提升性能。

**标签**: `#LLM`, `#open-source`, `#model merging`, `#AI ethics`, `#controversy`

---

<a id="item-3"></a>
## [形式化方法与编程的未来](https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1) ⭐️ 8.0/10

Jane Street 发表了一篇博客文章，讨论了形式化方法在编程中的作用，强调了在 AI 驱动的代码生成领域中，证明自动化和向验证方向的转变。 随着 AI 生成代码越来越普遍，形式化验证可以确保正确性和安全性，将人类价值从编写代码转向验证代码。这一讨论反映了将形式化方法与现代开发实践相结合的日益增长的趋势。 该文章涵盖了证明自动化技术，例如 Boyer-Moore 证明器所用的技术，以及 AI 辅助形式化的潜力。社区评论强调了在 Scala 3 中使用表达性类型的实践经验，以及对形式化规范可能冗余于测试的怀疑。

hackernews · eatonphil · 6月14日 12:35 · [社区讨论](https://news.ycombinator.com/item?id=48526633)

**背景**: 形式化方法是用于规范和验证软件与硬件系统的数学技术，其中形式化验证是根据规范证明正确性的行为。自动定理证明使用计算机程序来证明数学定理，而证明助手则允许人类引导证明过程。在 AI 生成代码的时代，形式化方法提供了一种确保可靠性的严谨方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Proof_assistant">Proof assistant - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论揭示了多样化的观点：Animats 分享了证明自动化的历史背景，指出早期系统比后来的系统拥有更多自动化功能。Winwang 报告了在 Scala 3 中使用表达性类型来防止代理生成低质量代码的成功经验。Brap 表达了怀疑态度，认为形式化规范可能与测试或实现存在相同的错误。

**标签**: `#formal methods`, `#verification`, `#programming`, `#proof automation`, `#AI`

---

<a id="item-4"></a>
## [AI 不会取代软件工程师：基于证据的观点](https://simonwillison.net/2026/Jun/14/why-ai-hasnt-replaced-software-engineers/#atom-everything) ⭐️ 8.0/10

Arvind Narayanan 和 Sayash Kapoor 发表了一篇文章，认为数据并不支持 AI 会导致软件工程行业大规模失业的说法。他们引用纽约州 WARN 法案 AI 披露复选框实施第一年，没有一家公司在裁员时勾选 AI 选项。 这为当前关于 AI 取代工作的普遍炒作提供了反驳，用证据表明软件工程——看似最受 AI 影响的领域——并未面临大规模裁员，暗示其他职业可能更安全。 文章指出了软件工程中 AI 难以自动化的三个真正的瓶颈：决定构建什么、验证交付的内容，以及对代码库、业务和环境的深度理解。AI 加快了编码速度，但不能完成这些关键任务。

rss · Simon Willison · 6月14日 23:54

**背景**: WARN 法案（工人调整和再培训通知法案）要求特定雇主在大规模裁员前提前 60 天通知。2025 年 3 月，纽约成为第一个在 WARN 申报中增加 AI 披露复选框的州，询问雇主裁员是否与 AI 或自动化有关。文章利用这一数据论证 AI 导致的失业仍然微不足道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://legal.thomsonreuters.com/en/insights/articles/what-is-the-warn-act?trk=article-ssr-frontend-pulse_little-text-block">What is the WARN Act ? What employers need to... | Thomson Reuters</a></li>
<li><a href="https://www.ogcsolutions.com/ny-warn-act-requires-disclosure-of-ai-related-layoffs/">Attention New York Employers: The NY WARN Act Now Requires...</a></li>

</ul>
</details>

**标签**: `#AI`, `#software engineering`, `#job displacement`, `#employment`, `#technology policy`

---

<a id="item-5"></a>
## [Kage：将任何网站打包成单个二进制文件以供离线查看](https://github.com/tamnd/kage) ⭐️ 7.0/10

Kage 是一种工具，可将网站捕获并打包成单个可执行二进制文件，无需网络服务器即可离线查看。 它简化了离线访问和分发网页内容的过程，适用于文档、维基或存档，与现有工具相比提供了一种新颖的方法。 Kage 生成的二进制文件运行时可以提供捕获的站点；如社区评论所述，它需要单独的服务器进程，并且使用 Go 编写，通过无头浏览器捕获页面。

hackernews · tamnd · 6月14日 17:25 · [社区讨论](https://news.ycombinator.com/item?id=48529990)

**背景**: 像 SingleFile 和 HTTrack 这样的离线浏览工具常用于存档网页。Kage 的独特之处在于将整个站点打包成一个二进制文件，便于分享，但需要服务器才能查看内容是一个局限，与直接打开单个 HTML 文件相比。

**社区讨论**: 评论者讨论了如离线公司维基等用例，并将 Kage 与 SingleFile 比较，指出 SingleFile 更强大且可直接在浏览器中打开。一些人质疑是否需要服务器，建议输出自包含的 HTML 更便捷。作者参与的其他项目（如 ascii-gif）也被提及。

**标签**: `#offline browsing`, `#web archiving`, `#static site tools`, `#single binary`

---

<a id="item-6"></a>
## [Alan Perlis 1982 年编程箴言重新浮现](https://www.cs.yale.edu/homes/perlis-alan/quotes.html) ⭐️ 7.0/10

1982 年 Alan Perlis 提出的 116 条关于编程和计算机科学的箴言集在网上分享，引发了关于它们在 LLM 时代相关性的新讨论。 Perlis 的箴言提供了关于编程语言设计和软件开发本质的永恒见解，与当今关于自然语言界面和 AI 的讨论产生共鸣。 这些语录包括如'不影响你对编程思考方式的语言不值得学习'等观察，以及关于自然语言和编程的几条，评论者指出这些在大型语言模型时代尤为相关。

hackernews · tosh · 6月14日 14:56 · [社区讨论](https://news.ycombinator.com/item?id=48527820)

**背景**: Alan Perlis 是计算机科学的先驱，也是首位图灵奖得主，以其在编程语言和编译器方面的工作而闻名。他的箴言于 1982 年出版，是一组关于编程技艺和文化的深刻真理的单行总结。

**社区讨论**: 评论者强调了在 LLM 时代似乎具有先见之明的语录，例如'当有人说我想要一种只需说出愿望就能完成的编程语言时，给他一根棒棒糖。'他们还分享了原始 PDF 的链接，以及以 Perl 程序员风格朗诵的视频。

**标签**: `#programming`, `#quotes`, `#computer science`, `#history`, `#wisdom`

---

<a id="item-7"></a>
## [将 SQLite 结果列映射回源表.列](https://simonwillison.net/2026/Jun/13/sqlite-column-provenance/#atom-everything) ⭐️ 7.0/10

Simon Willison 使用 Claude Code (Opus 4.8) 探索了编程性识别 SQLite 任意 SQL 查询结果中每个结果列的源表和列的方法，包括处理连接和 CTE。 这一能力将使 Datasette 等工具能够用源元数据丰富查询结果，改善数据探索和血缘追踪。它展示了针对微妙的数据库内省问题的实用 AI 辅助问题解决。 探索了三种方法：使用 APSW 库访问列元数据，使用 ctypes 调用 SQLite 内部未对 Python 暴露的 sqlite3_column_table_name() C 函数，以及分析 EXPLAIN 的输出。该研究记录在 Simon Willison 的 GitHub 研究仓库中。

rss · Simon Willison · 6月13日 23:05

**背景**: SQLite 内部会计算每个结果列源自哪个表和列，但 Python 默认的 sqlite3 模块无法直接访问此信息。Datasette 是一个用于探索和发布表格数据的开源工具，通常以 SQLite 为后端。列溯源——追踪查询结果中每个列的来源——对于数据血缘和 UI 增强很有价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/13/sqlite-column-provenance/">Research: Mapping SQLite result columns back to their source...</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**标签**: `#SQLite`, `#Datasette`, `#SQL parsing`, `#column provenance`, `#AI-assisted development`

---

<a id="item-8"></a>
## [Adobe RMSDK 导致 Kobo 电子书渲染问题](https://andreklein.net/your-epub-is-fine-kobo-disagrees-blame-adobe/) ⭐️ 6.0/10

一篇博客文章揭露，Adobe 的专有 Reader Mobile SDK (RMSDK) 是导致 Kobo 设备上渲染问题的罪魁祸首，尽管 ePub 文件本身是有效的。用户们讨论了一些解决办法，例如将 ePub 转换为 Kobo 的 kepub 格式。 这凸显了专有电子书软件长期存在的问题，导致兼容性问题和用户困扰。它强调了电子书生态系统中开放标准和更好互操作性的必要性。 Kobo 设备在文件命名为 .kepub.epub 扩展名时使用更高级的渲染引擎，可以绕过 RMSDK 问题。然而，正如一位评论者指出，RMSDK 因许可和缺乏支持而对独立开发者不可访问。

hackernews · sohkamyung · 6月14日 22:54 · [社区讨论](https://news.ycombinator.com/item?id=48533848)

**背景**: RMSDK（Reader Mobile SDK）是 Adobe 的专有软件开发工具包，许多电子书阅读系统用它来处理 DRM 和渲染。它因漏洞多且支持差而受到批评。Kobo 电子阅读器对标准 ePub 文件使用 RMSDK，但拥有渲染更好的专有 kepub 格式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.adobe.com/solutions/ebook/rmsdk/faq.html">Adobe Content Server and RMSDK / FAQ</a></li>
<li><a href="https://medium.com/@jiminypan/five-interesting-facts-about-adobe-legacy-ebook-rmsdk-b7be0123c874">Five interesting facts about Adobe legacy eBook RMSDK | by Jiminy Panoz | Medium</a></li>
<li><a href="https://wiki.mobileread.com/wiki/Adobe_Digital_Editions">MobileRead Wiki - Adobe Digital Editions</a></li>

</ul>
</details>

**社区讨论**: 许多评论者对 Adobe 的软件质量和商业行为表示失望，其中一位指出 RMSDK 对独立开发者完全不可及。其他人分享了像使用 kepubify 这样的解决方法，或批评 ePub 规范本身。总体情绪对 Adobe 和专有 DRM 持负面态度。

**标签**: `#e-books`, `#Adobe`, `#Kobo`, `#RMSDK`, `#digital rights management`

---

<a id="item-9"></a>
## [Trace：离线 Mac 会议转录应用，支持会议中标记关键点](https://traceapp.info/) ⭐️ 6.0/10

Trace 是一款全新的 Mac 应用，通过全局快捷键激活，完全在设备上录制和转录会议；它独特地允许用户在通话过程中标记关键时刻并添加内联笔记。 该应用解决了会议转录中的常见痛点：非侵入式激活和实时笔记记录，不打断会议流程。同时，它通过将音频和转录内容保存在本地来强调隐私，吸引了担心数据泄露的用户。 Trace 使用 macOS 麦克风和系统录制 API 将对话双方分别录制为独立音轨，并通过设备本地说话人分离技术将说话者标记为“Speaker 1”、“Speaker 2”等。应用已沙盒化，不会上传任何音频或转录内容；唯一网络请求是从 Hugging Face 一次性下载模型（约 500MB）。

hackernews · AG342 · 6月13日 20:41 · [社区讨论](https://news.ycombinator.com/item?id=48521236)

**背景**: 像 MacWhisper 这样的会议转录应用已变得流行，但许多需要在通话前进行设置，且经常崩溃或缺乏离线能力。Trace 旨在通过初始模型下载后完全离线转录，提供更可靠和注重隐私的体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepgram.com/voice-ai-apps/macwhisper">MacWhisper : Secure & Accurate AI Transcription App for Mac</a></li>
<li><a href="https://www.mactools.pro/MacWhisper">MacWhisper for Mac — Free Audio Transcription App | MacTools</a></li>

</ul>
</details>

**社区讨论**: 社区反馈总体上非常积极，赞扬了其概念和实现。关注点包括在需要双方同意的州的法律合规性（用户 nightpool）、仅限于 Mac App Store（用户 denbyc）以及企业设备策略阻止安装（用户 addozhang）。一些用户建议改进，如自动麦克风切换和菜单栏激活。

**标签**: `#meeting transcription`, `#Mac app`, `#offline`, `#productivity`

---

<a id="item-10"></a>
## [luau-wasm 0.1a0：首个通过 Pyodide 将 Lua 带到 WebAssembly 的 Alpha 版本](https://simonwillison.net/2026/Jun/13/luau-wasm/#atom-everything) ⭐️ 6.0/10

luau-wasm 0.1a0 首次以 alpha 版本发布，将 Luau 脚本语言打包成 WebAssembly wheel，可供 Pyodide 使用，从而直接在浏览器中执行 Lua 代码。 此版本通过 Pyodide 将 Lua、WebAssembly 和 Python 生态系统连接起来，使开发者无需服务器即可在 Web 应用中运行 Lua 脚本，为游戏脚本和嵌入式逻辑开辟了新的可能。 Luau 是一种快速、渐进类型的脚本语言，源自 Lua，由 Roblox 开发并以 MIT 许可证发布。该 wheel 是实验性的，处于早期 alpha 阶段，相关博客文章也提到了向 PyPI 发布 WASM wheels 的细节。

rss · Simon Willison · 6月13日 23:14

**背景**: Pyodide 是一个编译到 WebAssembly 的 Python 解释器，使 Python 代码能在浏览器中运行。WebAssembly (Wasm) 是一种二进制指令格式，允许在 Web 环境中高性能执行来自 C++ 等语言的代码。Luau 是 Lua 的衍生语言，注重性能和安全性，常用于 Roblox 游戏开发。该项目将 Luau 的 C++ 引擎打包成 Wasm wheel，供 Pyodide 加载，从而在浏览器中与 Python 一起执行 Lua 脚本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pyodide.org/en/stable/usage/index.html">Using Pyodide — Version 314.0.0</a></li>
<li><a href="https://simonwillison.net/2026/Jun/13/luau-wasm/">Release: luau-wasm 0.1a0 - Simon Willison's Weblog</a></li>
<li><a href="https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/">Publishing WASM wheels to PyPI for use with Pyodide</a></li>

</ul>
</details>

**标签**: `#lua`, `#webassembly`, `#pyodide`, `#wasm`, `#python`

---