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

每天 **北京时间 08:20 开始抓取、08:30 前后部署上线**（覆盖到当天早上为止的最新资讯）。

GitHub 的 `schedule` 触发普遍比 cron 设定时间晚（本项目 144 次运行实测：中位数 +4.3 小时，
最慢 +11 小时），所以工作流在北京时间 02:00（UTC 18:00）就提前触发，再由
[`scripts/wait_for_window.py`](scripts/wait_for_window.py) 等到北京时间 08:20（UTC 00:20）
才开始抓取，使每日更新稳定在早上 9 点前发布。

> 若某天 GitHub 延迟特别久（历史上出现过 9~11 小时），更新会相应晚一些。
> 需要精确到分钟的话，可用外部定时器（如 cron-job.org）调用 `workflow_dispatch`
> 接口触发，这条路径不受 `schedule` 延迟影响。

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
