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



## 在线文档

[W_PlatformMusicApi Doc](https://github-zc.github.io/W_PlatformMusicApi/)



## 安装

```shell
$ git clone https://github.com/GitHub-ZC/W_PlatformMusicApi.git
$ cd W_PlatformMusicApi/
$ pip install -r package.n -i https://mirrors.aliyun.com/pypi/simple/
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

```shell
$ python app.py runserver -p 8080 -h 0.0.0.0 --threaded
```



## 守护进程模式运行

> 考虑到框架自带服务器的性能问题，此版本新添加生产服务器 `uwsgi`
>
> 同时可以配置 服务器 以 **守护进程** 模式 运行 

> 安装 uwsgi

```shell
$ pip install uwsgi -i https://mirrors.aliyun.com/pypi/simple/
```

> 说明：centos、ubuntu、debian、mac、window  具体 每个平台 请自行百度



> 命令行启动 `uwsgi`

```shell
$ uwsgi --http 0.0.0.0:80 --wsgi-file app.py --callable app
```

> --http 0.0.0.0:80   **0.0.0.0** 代表 允许 外网主机访问；**80** 代表服务器端口
>
> 如果你使用 Centos 需要自行 配置 防火墙 放行 此端口



> 守护进程运行

```shell
$ uwsgi --http 0.0.0.0:80 --wsgi-file app.py --callable app --pidfile uwsgi.pid --daemonize uwsgi.log
```

> `--virtualenv`    添加 python 虚拟环境
>
> `--enable-threads`    如果你想要维护Python线程支持，而不为你的应用启动多线程，那么仅需添加 `--enable-threads` 选项



常用的服务器启动配置

1、有虚拟环境

```shell
$ uwsgi --http 0.0.0.0:80 --wsgi-file app.py --callable app --enable-threads --virtualenv ./env/ --pidfile uwsgi.pid --daemonize uwsgi.log
```

2、无虚拟环境

```shell
$ uwsgi --http 0.0.0.0:80 --wsgi-file app.py --callable app --enable-threads --pidfile uwsgi.pid --daemonize uwsgi.log
```



> 停止服务器

```shell
$ uwsgi --stop uwsgi.pid        # 前提(必须在当前项目的 根 目录下面)
```

> 重载服务器

```shell
$ uwsgi --reload uwsgi.pid      # 前提(必须在当前项目的 根 目录下面)
```





## 用户须知

!> 当前服务器为框架自带服务器，考虑到性能问题，可以使用专门web服务器与本项目对接，例如`nginx`，具体的搭建方法还请用户自行百度，这里不做演示

!> 该项目仅做接口转发，部分接口通过修改 `Referer` 实现，所有数据均不做存储处理，部分接口采用缓存，大家还是理性的保护好自己的个人信息，谨防诈骗

!> QQ音乐登陆的这个问题还是难绕过去，目前还是需要登陆获取 https://y.qq.com 的 `cookie`，注入本项目， 如果又什么更好的解决办法，欢迎大家提 pr 给我

!> 咪咕音乐不提供登录内容，具体后期再不断完善

!> 目前本项目刚刚开始，只提供QQ、咪咕两大音乐平台，后期再不断完善

!> 本项目仅供学习使用,请尊重版权，请勿利用此项目从事商业行为



## 更新记录

v0.1.0：项目刚开始启动，目前只有**QQ**平台Api

v0.2.0：添加**migu**平台Api，对部分QQ平台接口添加了错误处理

v0.2.1：添加 **uwsgi**生产服务器，添加**守护进程**的启动模式(修改app.py文件)



# 接口文档

## QQ

### 搜索

#### 搜索

接口：`/qq/search/`

说明：调用此接口 , 传入搜索关键词可以搜索该音乐 / 专辑 / 歌手 / 歌单 / 用户(需要自己传入type参数) , 默认会自动去除 关键词 前后的**空白字符** 

可选参数：

`key`：关键字 默认 暗号

`limit`：每一页返回的数量，默认30

`offset`：页码，默认1

`type`：搜索类型 默认为0 取值意义 type: 0：单曲，2：歌单，3:用户 ,7：歌词，8：专辑，9：歌手，12：mv

示例：[/qq/search/?key=暗号](http://iecoxe.top:3500/qq/search/?key=暗号)



#### 热搜

接口：`/qq/search/hot/`

说明：调用此接口，默认会进行缓存处理

示例：[/qq/search/hot/](http://iecoxe.top:3500/qq/search/hot/)



#### 搜索建议

接口：`/qq/search/suggest/`

必选参数：`key`

示例：[/qq/search/suggest/?key=周杰伦](http://iecoxe.top:3500/qq/search/suggest/?key=周杰伦)



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

示例：[/qq/song/url/?mid=0039MnYb0qxYhV,004Z8Ihr0JIu5s&br=flac](http://iecoxe.top:3500/qq/song/url/?mid=0039MnYb0qxYhV,004Z8Ihr0JIu5s&br=flac)



### 歌词

接口：`/qq/lyric/`

可选参数：`mid` 默认 `004O1DHG4MjYOi`

示例：[/qq/lyric/?mid=004O1DHG4MjYOi](http://iecoxe.top:3500/qq/lyric/?mid=004O1DHG4MjYOi)



### 排行榜

#### 获取榜单列表

接口：`/qq/top/category/`

说明：这个接口数据，包含了榜单名、榜单 id、更新时间、播放量，都是作为下一个接口的请求参数

示例：[/qq/top/category/](http://iecoxe.top:3500/qq/top/category/)



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

示例：[/qq/top/?topId=26](http://iecoxe.top:3500/qq/top/?topId=26)



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

示例：[/qq/getcookie/](http://iecoxe.top:3500/qq/getcookie/)





## 咪咕

### 搜索

#### 搜索

接口：`/migu/search/`

可选参数：

`key`：关键字 默认 暗号

`limit`：每一页返回的数量，默认30

`offset`：页码，默认 1

`type`：默认 2 ；     //  歌曲： 2   歌手：1  专辑： 4 歌单：6  MV：5  歌词：7

说明：调用此接口 , 传入搜索关键词可以搜索该音乐 / 专辑 / 歌手 / 歌单 / 用户(需要自己传入type参数) , 默认会自动去除 关键词 前后的**空白字符** 

示例：[/migu/search/](http://iecoxe.top:3500/migu/search/)



#### 热搜

接口：`/migu/search/hot/`

说明：调用此接口，默认会进行缓存处理

示例：[/migu/search/hot/](http://iecoxe.top:3500/migu/search/hot/)



#### 搜索建议

接口：`/migu/search/suggest/`

必选参数：`key`

示例：[/migu/search/suggest/?key=周杰伦](http://iecoxe.top:3500/migu/search/suggest/?key=周杰伦)



### 歌曲url，图片，专辑详情

接口：`/migu/song/url/`

说明：

- 由于目前时间紧促，目前此接口只能获取**128k**歌曲
- migu没有采取 Cookie ，本人没有账号
- 服务器会自动去除 id 以及之间的**空白字符**

可选参数：

`id`：歌曲的`copyrightId`，默认`60054701923`

示例：[/migu/song/url/?id=60054701923](http://iecoxe.top:3500/migu/song/url/?id=60054701923)



### 歌词

接口：`/migu/lyric/`

可选参数：`id`  歌曲的copyrightId      默认 `60084600554`

示例：[/migu/lyric/?mid=60084600554](http://iecoxe.top:3500/migu/lyric/?mid=60084600554)



### 排行榜

接口：`/migu/top/`

说明：由于自我认为官方的 ajax 接口返回的数据太少，以及接口不健全，于是自己通过爬虫爬取获取的排行榜数据

可选参数：`topId`  默认 2，热歌榜

`1`：尖叫新歌榜

`2`：尖叫热歌榜

`3`：尖叫原创榜

`4`：音乐榜

`5`：影视榜

`6`：内地榜

`7`：港台榜

`8`：欧美榜

`9`：日韩榜

`10`：彩铃榜

`11`：KTV榜

`12`：网络榜

`13`：新专辑榜

示例：[/migu/top/?topID=2](http://iecoxe.top:3500/migu/top/?topID=2)



### 歌手

#### 歌手详情

接口：`/migu/singer/info/`

可选参数：

`artistId`：歌手ID  ，默认 18196

示例：[/migu/singer/info/?artistId=18196](http://iecoxe.top:3500/migu/singer/info/?artistId=18196)



#### 歌手歌曲列表

接口：`/migu/singer/songinfo/`

说明：由于自我认为官方的 ajax 接口返回的数据太少，以及接口不健全，于是自己通过爬虫爬取获取的歌手歌曲列表数据

可选参数：

`artistId`：歌手ID，默认 18196

`offset`：分页，默认 1

示例：[/migu/singer/songinfo/?artistId=18196&offset=1](http://iecoxe.top:3500/migu/singer/songinfo/?artistId=18196&offset=1)



### 歌单

#### 歌单

接口：`/migu/playlist/`

说明：由于官方接口原因，默认每一页返回 10 条数据

可选参数：

`offset`：分页， 默认 1

`type`：1： 推荐 ； 2： 最新， 默认 推荐

示例：[/migu/playlist/](http://iecoxe.top:3500/migu/playlist/)

返回字段含义：`contentCount` 歌单 歌曲 的总数量，可用于 下面接口 中  `limit` 参数



#### 歌单详情

接口：`/migu/playlist/info/`

说明：`playListId`、`limit` 根据上面的接口( `/migu/playlist/` )返回数据中获取

​			`limit` 对应上面接口中的 `contentCount`

可选参数：

`playListId`：歌单的 ID，默认 179730639

`limit`：返回数据的数量，默认 30

示例：[/migu/playlist/info/](http://iecoxe.top:3500/migu/playlist/info/)