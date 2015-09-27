# Scheduler

## Features

- 输入 URl 返回 json
    + 输入 URL 如果没有缓存则后台抓取文章
    + 后台抓取文章后缓存到 MongoDB url_response_cache
        * url
        * body
        * timestamp
        * datetime
        * status 1/-1
    + 如果后台有缓存则直接输出
    + 可以在前端反馈抓取错误 将 status = -1
- 前端显示文章纯文本正文
    + id
    + title
    + body
    + tags
    + keywords
- 预览文章(类似 github) 用 markdown2 输出 html
- 提供整页预览 URL 保存到 evernote
- 预览时在前端适配代码高亮
- 提供 evernote 授权 将笔记导出到 evernote

## Mile Stone

- 0.1 20150921 Week
    + [ ] 输入 URL 返回文章
    + [ ] 抓取错误反馈
    + [ ] 抓取缓存
- 0.2
    + [ ] 用户系统
    + [ ] 页内预览文章
    + [ ] 代码高亮
    + [ ] 整页预览
- 0.3
    + [ ] 笔记保存
    + [ ] evernote 授权
    + [ ] 导出到 evernote
    + [ ] 导出时更新 evernote 中的笔记
- 0.4
    + [ ] 适配移动页面
