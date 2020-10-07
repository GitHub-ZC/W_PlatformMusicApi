# W_PlatformMusicApi

Whole Platform Music Python API service

这是一个基于 **Flask** + **Requests**的 **Python** 项目，提供`Whole Platform`音乐的API接口



## 灵感来源

[Binaryify/NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi)

[jsososo/QQMusicApi](https://github.com/jsososo/QQMusicApi/)



## 环境要求

需要 python 3.6+ 环境



## 工作原理

跨站请求伪造 (CSRF), 伪造请求头 , 调用官方 API



## 安装

```shell
$ git clone https://github.com/GitHub-ZC/W_PlatformMusicApi.git
$ cd W_PlatformMusicApi/
$ pip i -r package.n -i https://mirrors.aliyun.com/pypi/simple/
```

## 运行

```shell
$ python app.py runserver
```

> 服务器启动默认端口为 5000,若不想使用 5000 端口,可使用以下命令: Mac/Linux/Windows
>
> 服务器启动默认在本机启动，外网访问不到

```shell
$ python app.py runserver -p 80
$ python app.py runserver -h 0.0.0.0
```

> 服务器默认单线程模式，请求频繁会造成卡顿，这时可以开启**多线程模式**

```shell
$ python app.py runserver --threaded
```

## 用户须知

!> 当前服务器为框架自带服务器，考虑到性能问题，可以使用专门web服务器与本项目对接，例如`nginx`，具体的搭建方法还请用户自行百度，这里不做演示

!> 该项目仅做接口转发，部分接口通过修改 `Referer` 实现，所有数据均不做存储处理，部分接口采用缓存，大家还是理性的保护好自己的个人信息，谨防诈骗

!> QQ音乐登陆的这个问题还是难绕过去，目前还是需要登陆获取 https://y.qq.com 的 `cookie`，注入本项目， 如果又什么更好的解决办法，欢迎大家提 pr 给我

!> 咪咕音乐不提供登录内容，具体后期再不断完善

!> 目前本项目刚刚开始，只提供QQ、咪咕两大音乐平台，后期再不断完善

!> 本项目仅供学习使用,请尊重版权，请勿利用此项目从事商业行为

## 更新记录

v0.1.0：项目刚开始启动，目前只有QQ平台Api

# 接口文档

## QQ

### 搜索

#### 搜索

接口：`/qq/search/url`

说明：调用此接口 , 传入搜索关键词可以搜索该音乐 / 专辑 / 歌手 / 歌单 / 用户(需要自己传入type参数) , 默认会自动去除 关键词 前后的**空白字符** 

可选参数：

`key`：关键字 默认 暗号

`limit`：每一页返回的数量，默认30

`offset`：页码，默认1

`type`：搜索类型 默认为0 取值意义 type: 0：单曲，2：歌单，3:用户 ,7：歌词，8：专辑，9：歌手，12：mv

示例：[/qq/search/url/?key=暗号]()



#### 热搜

接口：`/qq/search/hot/`

说明：调用此接口，默认会进行缓存处理

示例：[/qq/search/hot/]()



#### 搜索建议

接口：`/qq/search/suggest/`

必选参数：`key`

示例：[/qq/search/suggest/?key=周杰伦]()



### 歌曲url

接口：`/qq/song/url/`

说明：

- 这个接口依赖服务器的 Cookie 信息的，支持批量获取，不一定是全部的歌曲都有无损、高品的， 要注意结合 size320，sizeape，sizeflac 等参数先判断下是否有播放链接
- 服务器内置默认的 Cookie ，如果是未登陆或非 vip 用户的 `cookie`，只能获取到非 vip 用户可听的歌曲
- 服务器 Cookie 的设置，可以使用 [/qq/setcookie/](//#/?id=设置用户cookie)
- 服务器会自动去除mid，br以及songmid之间的**空白字符**

可选参数：

`mid`：歌曲的`songmid`，默认`004O1DHG4MjYOi`

`br`：默认 128 

取值意义： 128：mp3 128k，320：mp3 320k，m4a：m4a格式 128k，flac：flac格式 无损，ape：ape格式 无损

示例：[/qq/song/url/?mid=0039MnYb0qxYhV,004Z8Ihr0JIu5s&br=flac]()



### 歌词

接口：`/qq/lyric/`

可选参数：`mid` 默认 `004O1DHG4MjYOi`

示例：[/qq/lyric/?mid=004O1DHG4MjYOi]()



### 排行榜

#### 获取榜单列表

接口：`/qq/top/category`

说明：这个接口数据，包含了榜单名、榜单 id、更新时间、播放量，都是作为下一个接口的请求参数

示例：[/top/category]()



#### 获取榜单详情

接口：`/qq/top/`

可选参数：

`topId`: 默认 26，从上面的`/top/category/`中取值

`limit`: 默认 200 // 部分接口不支持这个字段，所以这里默认选择200

`period`: 榜单的时间，从上面的 `/top/category/` 中取值，不填默认返回 **最新** 的排行榜数据

`offset`：每一页返回的歌曲数量，默认 1

返回数据说明

`time`: 当前榜单的发布时间，可能是天，也可能是周

```
timeType`: 当前榜单的时间格式 `YYYY_W` 或 `YYYY-MM-DD
```

`rank`: 在榜单的排名

`rankType`: 1 上升，2 减少，3 持平，4 新歌，6 上升百分比

`rankValue`: 排名改变值

示例：[/qq/top/?topId=26]()



### Cookie



#### 设置服务器Cookie(POST)

接口：`/qq/setcookie/`

说明：具有 QQ 绿钻的用户，通过浏览器查看 Cookie ，通过此接口设置以后，需要登陆的接口可以获取登录才能获取的内容，比如 歌曲播放地址(无损)

必须参数：

`cookie`：

> 格式：aaa=bbb; ccc=ddd; ....

> 例子：yqq_stat=0; pgv_info=ssid=s1520392; ts_last=y.qq.com/portal/player.html; pgv_pvid=1233495754; ts_uid=5486601780; pgv_pvi=4007713792; pgv_si=s6654436352; userAction=1; _qpsvr_localtk=0.8025676546673662; yq_index=0; yplayer_open=1; player_exist=1; qqmusic_fromtag=66



#### 查看当前Cookie

接口：`/qq/getcookie/`

说明：cookie 已经在服务器端，进行的 Json 转化

示例：[/qq/getcookie/]()

