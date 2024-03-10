# yt_dlp_subscriber
 A wrapper of yt_dlp for download multi-channels as a schedule.个人自用的多频道订阅的yt_dlp封装器



# Usage

nicoSpider supports crawl search result of nicovideo,especially by tags.

nicoSpider支持下载nicoVideo的搜索结果，特别是基于tag的搜索结果。

nicoSubscribeSpider is a wrapper to download multiple links into different path in a action.

nicoSubscribeSpider 是一个多链接封装器，能够比较简单的下载多个不同的链接到不同的文件夹。

# How to use

nicoSpider is deprecate now and is not recommend to use its main method until I try to restore it :)

配置好requests_constants的option，并且配置一下users就能下载了。

# Next todo

- 良好调整nicoSpider使其真正可用；
- 将nicoSubscribeSpider切换到数据库上，并且引入时间戳来方便下载（用于减少无用工作之类，因为yt_dlp对冗余下载控制的支持很差）。



