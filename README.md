<div align="center">

# 🌅 Horizon

**你只需享受新闻，剩下交给 Horizon。**

[![Daily Summary](https://github.com/qwtoe/horizon/actions/workflows/daily-summary.yml/badge.svg?style=flat-square)](https://qwtoe.github.io/horizon/)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](LICENSE)

</div>

---

这是一个基于 [Horizon](https://github.com/Thysrael/Horizon) 的个性化 AI 新闻日报系统，每天自动抓取、分析并生成中文技术资讯摘要，部署到 GitHub Pages。

## 📡 信息源

| 来源 | 内容 |
|------|------|
| **Hacker News** | 热门技术文章 |
| **RSS** | [Simon Willison](https://simonwillison.net/) |
| **Reddit** | r/MachineLearning |
| **GitHub** | torvalds 动态、astral-sh/uv releases |

## 🤖 AI 配置

- **模型**: DeepSeek `deepseek-v4-flash`
- **语言**: 中文
- **评分阈值**: 6.0（只保留重要内容）

## 🌐 在线日报

**https://qwtoe.github.io/horizon/**

## ⏰ 自动运行

每天 **北京时间 08:30** 通过 GitHub Actions 自动抓取、分析并部署。

## 🚀 快速开始

```bash
# 本地运行
git clone https://github.com/qwtoe/horizon.git
cd horizon
cp .env.example .env
cp data/config.example.json data/config.json
# 编辑 .env 填入 API Key，编辑 data/config.json 自定义信息源
docker compose run --rm horizon
```

## 📁 项目结构

```
.
├── .github/workflows/     # GitHub Actions 定时任务
├── data/
│   ├── config.json        # 信息源与 AI 配置
│   └── summaries/         # 生成的日报
├── docs/                  # GitHub Pages 站点
│   ├── _posts/            # Jekyll 文章
│   └── _config.yml        # Pages 配置
├── src/                   # 核心代码
└── .env                   # API Keys
```

## 🔧 自定义配置

编辑 `data/config.json`：

```json
{
  "ai": {
    "provider": "deepseek",
    "model": "deepseek-v4-flash",
    "api_key_env": "DEEPSEEK_API_KEY",
    "languages": ["zh"]
  },
  "sources": {
    "github": [...],
    "hackernews": {...},
    "rss": [...],
    "reddit": {...}
  }
}
```

## 📄 License

[MIT](LICENSE) | 基于 [Thysrael/Horizon](https://github.com/Thysrael/Horizon)
