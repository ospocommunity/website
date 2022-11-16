# website
OSPO Community static website contents.

# 静态网站技术

网站采用了

* [hugo](https://gohugo.io/)  用于网站模版，从Markdown生成HTML
* 配合模版：[hugo-hero-theme](https://www.zerostatic.io/theme/hugo-hero/)
* GitHub Page
* 自动化采用了 GitHub Actions

## 中英文双语支持

网站的所有内容都在[content](https://github.com/ospocommunity/website/tree/main/content)目录下：

* [en](https://github.com/ospocommunity/website/tree/main/content/en) 英文
* [zh](https://github.com/ospocommunity/website/tree/main/content/zh) 中文

通常情况下，内容创作者是根据自己最擅长的语言进行创作，所以翻译的工作，很可能不是同一个人，所以需要其它的创作者加入。

### 中译英

在中文目录下找到对应的markdown和html文件，例如网页[关于](https://ospo.events/zh/about/) 所对应的中文markdown文件是:[zh/pages/about](https://github.com/ospocommunity/website/tree/main/content/zh/pages/about) ，那么对应的英文文件就是：[en/pages/about](https://github.com/ospocommunity/website/tree/main/content/en/pages/about)。

打开对应的Markdown文件，分别翻译对应的字符串即可。

### 英译中

将上述的过程反过来。