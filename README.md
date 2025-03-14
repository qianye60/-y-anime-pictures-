### 项目展示

![image](https://github.com/user-attachments/assets/461929b4-06e4-4f9b-9d2b-991f1bf5e348)

# 🌸 Anime-Pictures 爬虫：二次元美图，一键get！🌸

[![GitHub stars](https://img.shields.io/github/stars/qianye60/AnimePicCrawler.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/qianye60/AnimePicCrawler/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/qianye60/AnimePicCrawler.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/qianye60/AnimePicCrawler/network/)
[![GitHub license](https://img.shields.io/github/license/qianye60/AnimePicCrawler.svg)](https://GitHub.com/qianye60/AnimePicCrawler/blob/master/LICENSE)

## 🌟 项目简介

还在为找不到心仪的二次元美图发愁吗？还在手动一张张保存图片到手抽筋吗？

别担心，**Anime-Pictures 爬虫**来拯救你啦！🚀

本项目基于 Python 和强大的 Selenium 库，专为 [Anime-Pictures.net](https://anime-pictures.net/) 设计，让你轻松爬取海量高质量动漫美图。无论是想批量下载壁纸，还是想建立自己的图库，它都能满足你！

### ✨ 特色功能

*   **🎯 精准定位**：指定关键词、页面范围，想爬什么就爬什么！
*   **🛡️ 防御拉满**：采用 `undetected_chromedriver`，有效规避反爬虫机制。
*   **🔑 登录无忧**：支持登录状态爬取，解锁更多高清大图！
*   **⚙️ 高级设置**：自定义每页图片数量，灵活控制爬取速度。
*   **🖱️ 模拟操作**：模拟人工浏览，降低被封风险。
*   **📈 断点续爬**：支持从上次中断处继续，省时省力。

## 🛠️ 环境准备

1.  **Python 环境**：确保已安装 Python 3.6 或更高版本。
2.  **Chrome 浏览器**：需要安装 Chrome 浏览器。
3.  **ChromeDriver**(可能不需要): 下载与你的 Chrome 浏览器版本对应的 ChromeDriver，并将其路径添加到系统环境变量中，或者在代码中指定其路径。

## 📦 安装依赖

```bash
pip install -r requirements.txt
```

## 🚀 快速开始

1.  **克隆项目**：

    ```bash
    git clone https://github.com/你的用户名/你的仓库名.git
    cd 你的仓库名
    ```

2.  **运行爬虫**：

    ```bash
    python crawler.py
    ```

3.  **根据提示输入**：
    *   是否需要登录（0：否，1：是）
    *   如果选择登录，请输入用户名和密码，用`-`隔开
    *   上次爬取的页面数、上次爬取的图片数、每页显示的图片数（用`-`隔开）

    示例：

    ```
    是否注册(0:否,1:是):0
    上次页数-上次张数-每页张数:0-1-100
    ```

## ⚙️ 代码结构

*   `crawler.py`：爬虫主程序。
*   `login.py`：处理用户登录。
*   `set_maxpage.py`：设置每页显示的图片数量。

## 📝 使用说明

### `crawler.py`

核心爬虫程序，包含以下类和函数：

*   `class photos`：
    *   `__init__(self, url, number, last_number, login_flag=0, start=0, end=1)`：初始化爬虫对象。
        *   `url`：目标网站的基础 URL。
        *   `number`：每页要爬取的图片数量。
        *   `last_number`：上一次爬取到的图片编号（用于断点续爬）。
        *   `login_flag`：是否需要登录（0 或 1）。
        *   `start`：起始页面。
        *   `end`：结束页面。
    *   `page(self, count)`：加载指定页码的页面。
    *   `all(self, last_number)`：爬取当前页面的所有图片。
    *   `run(self)`：启动爬虫。

### `login.py`

*   `login(driver, username, password)`：处理用户登录，不登陆将不能爬取R18+内容，并且不能设置每页页数。

### `set_maxpage.py`

*   `set(driver, number)`：设置每页显示的图片数量。

## 💡 进阶玩法

*   **自定义搜索关键词**：修改 `url` 中的 `search_tag` 参数，例如 `search_tag=girl` 改为 `search_tag=boy`。
*   **调整爬取范围**：修改 `start` 和 `end` 参数，控制爬取的页面范围。
*   **定时任务**：结合操作系统的定时任务功能（如 Linux 的 cron），实现定期自动爬取。

## ⚠️ 注意事项

*   请尊重网站的 robots.txt 协议，合理控制爬取频率，避免对服务器造成过大压力。
*   爬取到的图片仅供个人学习、欣赏使用，请勿用于商业用途。
*   本项目仅供学习交流，开发者不对任何滥用行为负责。
*   不登陆将不能爬取R18+内容，并且不能设置每页页数。
*   大陆建议开启 VPN 使用！
  
## 🤝 贡献代码

欢迎提交 Pull Request，一起完善这个项目！

## 📜 开源协议

本项目采用 MIT 许可证，详情请参见 [LICENSE](LICENSE) 文件。

---

**觉得好用的话，别忘了给个 Star 哦！** ⭐
