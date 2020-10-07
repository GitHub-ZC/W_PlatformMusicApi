# W_PlatformMusicApi

Whole Platform Music Python API service

这是一个基于 **Flask** + **Requests**的 **Python** 项目，提供`Whole Platform`音乐的API接口



## 灵感来源

[Binaryify/NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi)

[jsososo/QQMusicApi](https://github.com/jsososo/QQMusicApi/)



## 环境要求

需要 python 3.6+ 环境



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

## 接口文档

### 搜索

#### 搜索

接口：`/search/`

参数：

`key`：关键字 必填

`limit`：每一页返回的数量

`offset`：页码，默认1

`type`：搜索类型 默认为0 // t: 0：单曲，2：歌单，3:用户 ,7：歌词，8：专辑，9：歌手，12：mv

示例：[/search/url/]()
