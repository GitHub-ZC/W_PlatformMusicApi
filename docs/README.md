# migu

## 搜索

https://m.music.migu.cn/migu/remoting/scr_search_tag?rows=20&type=2&keyword=%E8%AE%B8%E5%B5%A9&pgc=1

type：

​			歌曲： 2

​			歌手： 1

​			专辑： 4

​			歌单： 6

​			MV：   5

​			歌词： 7

row：  返回数目

pgc：   分页



## 排行榜

原创榜：https://m.music.migu.cn/migu/remoting/cms_list_tag?nid=23604032&pageSize=200&pageNo=0

网络榜：https://m.music.migu.cn/migu/remoting/cms_list_tag?nid=23604058&pageSize=200&pageNo=0

音乐榜：https://m.music.migu.cn/migu/remoting/cms_list_tag?nid=23603703&pageSize=200&pageNo=0

影视榜：https://m.music.migu.cn/migu/remoting/cms_list_tag?nid=23603721&pageSize=200&pageNo=0



## 搜索建议

移动端：https://m.music.migu.cn/migu/remoting/autocomplete_tag?keyword=%E8%AE%B8%E5%B5%A9

keyword： 关键字

PC端：https://music.migu.cn/v3/api/search/suggest?keyword=许嵩

keyword： 关键字（Referer请求头）



## 实时热搜

https://music.migu.cn/v3/api/search/hotwords  （Referer请求头）



## 歌词

https://music.migu.cn/v3/api/music/audioPlayer/getLyric?copyrightId=60084600554（Referer请求头）



## 精选歌单

推荐

https://m.music.migu.cn/migu/remoting/playlist_bycolumnid_tag?playListType=2&type=1&columnId=15127315&tagId=&startIndex=0

最新

https://m.music.migu.cn/migu/remoting/playlist_bycolumnid_tag?playListType=2&type=1&columnId=15127272&tagId=&startIndex=0

歌单详情

https://m.music.migu.cn/migu/remoting/playlistcontents_query_tag?playListType=2&playListId=179730639&contentCount=12

https://m.music.migu.cn/migu/remoting/playlistcontents_query_tag?playListType=2&playListId=179294333&contentCount=22





## 获取歌曲url、封面

https://m.music.migu.cn/migu/remoting/cms_detail_tag?cpid=60054701923

cpid：歌曲ID



## 获取歌手信息

https://m.music.migu.cn/migu/remoting/cms_artist_detail_tag?artistId=18196



## 获取歌手的歌曲信息

https://m.music.migu.cn/migu/remoting/cms_artist_song_list_tag?pageSize=20&pageNo=0&artistId=18196



# QQ

## 搜索

移动端

原生

https://c.y.qq.com/soso/fcgi-bin/search_for_qq_cp?_=1601273937730&g_tk=5381&uin=&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&g_tk_new_20200303=757507025&w=许嵩&zhidaqu=1&catZhida=1&t=0&flag=1&ie=utf-8&sem=1&aggr=0&perpage=20&n=20&p=1&remoteplace=txt.mqq.all



简化

https://c.y.qq.com/soso/fcgi-bin/search_for_qq_cp?format=json&w=许嵩&t=0&n=3&p=1



PC

原生

https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.center&searchid=45902364243238443&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=晴天&g_tk_new_20200303=757507025&g_tk=757507025&jsonpCallback=MusicJsonCallback6975585413143889&loginUin=153140965&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0

无cookie

https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.center&searchid=52707181609011704&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=周杰伦&g_tk_new_20200303=5381&g_tk=5381&jsonpCallback=MusicJsonCallback9905084231824244&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0



简化

https://c.y.qq.com/soso/fcgi-bin/client_search_cp?t=0&cr=1&p=1&n=10&w=暗号&format=json



歌单

https://c.y.qq.com/soso/fcgi-bin/client_music_search_songlist?remoteplace=txt.yqq.playlist&searchid=116824162771124473&flag_qc=0&page_no=0&num_per_page=5&query=芒种&g_tk_new_20200303=757507025&g_tk=757507025&jsonpCallback=MusicJsonCallback9861953451066818&loginUin=153140965&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0

简化

https://c.y.qq.com/soso/fcgi-bin/client_music_search_songlist?remoteplace=txt.yqq.playlist&page_no=0&num_per_page=5&query=芒种&format=json



用户

https://c.y.qq.com/soso/fcgi-bin/client_search_user?ct=24&qqmusic_ver=1298&p=1&n=10&searchid=241014031194265199&remoteplace=txt.yqq.user&w=芒种&g_tk_new_20200303=757507025&g_tk=757507025&jsonpCallback=MusicJsonCallback21387249027880384&loginUin=153140965&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0



t: **0：单曲**，2：歌单，3：用户, **7：歌词**，**8：专辑**，**9：歌手**，**12：mv**

## 热门推荐

原生

https://c.y.qq.com/splcloud/fcgi-bin/gethotkey.fcg?g_tk_new_20200303=757507025&g_tk=757507025&jsonpCallback=hotSearchKeysmod_top_search&loginUin=153140965&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0

简化

https://c.y.qq.com/splcloud/fcgi-bin/gethotkey.fcg?format=json



## 搜索建议

原生

https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg?is_xml=0&key=汪&g_tk_new_20200303=757507025&g_tk=757507025&jsonpCallback=SmartboxKeysCallbackmod_search7504&loginUin=153140965&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0

简化

https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg?key=汪&format=json





## 歌曲url

原生

https://u.y.qq.com/cgi-bin/musicu.fcg?callback=getplaysongvkey8148666066702909&g_tk=1641458741&jsonpCallback=getplaysongvkey8148666066702909&loginUin=153140965&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data={"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"658650575","songmid":["004Gq0xE1YC8xp"],"songtype":[0],"uin":"153140965","loginflag":1,"platform":"20"}},"comm":{"uin":153140965,"format":"json","ct":24,"cv":0}}



无cookie

https://u.y.qq.com/cgi-bin/musicu.fcg?callback=getplaysongvkey8282962640405127&g_tk=5381&jsonpCallback=getplaysongvkey8282962640405127&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data={"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"6784379255","songmid":["003CMXGI2yRUDo"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":24,"cv":0}}



简化

https://u.y.qq.com/cgi-bin/musicu.fcg?format=json&data={"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{**"filename":["F000001Js78a40BZU6.flac"]**,"guid":"658650575","songmid":["**001Js78a40BZU6**"],"songtype":[0],"uin":"1528773794","loginflag":1,"platform":"20"}},"comm":{"uin":1528773794,"format":"json","ct":24,"cv":0}}

需要配合cookie使用

'Cookie': 'RK=rBAU2mUTf3; ptcz=67e538625364d30a46c259b73931e697c67d86f999cc662e54652d60e76e3989; pgv_pvi=5638619136; pgv_pvid=658650575; ts_refer=www.baidu.com/link; ts_uid=4351235281; tvfe_boss_uuid=993d5eb499ca1d59; LW_sid=61N5Z9D4E2Q5L7C2E1s3S7c1a9; LW_uid=X1p5C9x46205T664o1x3s8v9t2; eas_sid=81B5v9S4A2Y5G6h4H1u3l9a0c8; o_cookie=153140965; yq_index=7; userAction=1; tmeLoginType=2; euin=oK4ANeSloiSq7n**; qqmusic_key=Q_H_L_28VYoz50eOaK7hzysrR-fG8rcfhkPga8KtOW-HKzvuZpTATQrjZkMdYyCNbSC_8; psrf_access_token_expiresAt=1609117938; psrf_musickey_createtime=1601341938; yqq_stat=0; pgv_si=s1154993152; pgv_info=ssid=s7400935225; yplayer_open=1; yq_playschange=0; yq_playdata=; player_exist=1; qqmusic_fromtag=66; _qpsvr_localtk=0.6164186832232864; psrf_qqopenid=65372CE285689F72E89B5F99E0F94C73; psrf_qqaccess_token=731EA40D1650FB0C82E30264C242554C; psrf_qqrefresh_token=08382EB50992E6395EBBD6F094074A6F; qm_keyst=Q_H_L_28VYoz50eOaK7hzysrR-fG8rcfhkPga8KtOW-HKzvuZpTATQrjZkMdYyCNbSC_8; uin=1528773794; psrf_qqunionid=; ts_last=y.qq.com/portal/search.html'



## 排行榜

### 排行榜信息（移动端）

原生

https://u.y.qq.com/cgi-bin/musicu.fcg?_=1601389640007&data={"comm":{"g_tk":308189849,"uin":1528773794,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"h5","needNewCode":1,"ct":23,"cv":0},"topList":{"module":"musicToplist.ToplistInfoServer","method":"GetAll","param":{}}}



### 热歌榜

原生

https://u.y.qq.com/cgi-bin/musicu.fcg?callback=getUCGI856765622180173&g_tk=308189849&jsonpCallback=getUCGI856765622180173&loginUin=1528773794&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data={"detail":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail","param":{"topId":26,"offset":0,"num":20,"period":"2020_39"}},"comm":{"ct":24,"cv":0}}



简化

https://u.y.qq.com/cgi-bin/musicu.fcg?format=json&data={"detail":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail","param":{"topId":26,"offset":0,"num":200,"period":"2020_39"}},"comm":{"ct":24,"cv":0}}



### 飙升榜

https://u.y.qq.com/cgi-bin/musicu.fcg?callback=getUCGI6925113299501857&g_tk=308189849&jsonpCallback=getUCGI6925113299501857&loginUin=1528773794&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data={"detail":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail","param":{"topId":62,"offset":0,"num":20,"period":"2020-09-29"}},"comm":{"ct":24,"cv":0}}



简化

https://u.y.qq.com/cgi-bin/musicu.fcg?format=json&data={"detail":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail","param":{"topId":62,"offset":0,"num":20,"period":"2020-09-29"}},"comm":{"ct":24,"cv":0}}



## 歌词

接口一：原生

https://szc.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg?nobase64=1&musicid=102296985&callback=jsonp1&g_tk_new_20200303=5381&g_tk=5381&jsonpCallback=jsonp1&loginUin=1528773794&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0



简化

https://szc.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg?nobase64=1&musicid=102296985&format=json

接口二：原生

https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_new.fcg?callback=MusicJsonCallback_lrc&pcachetime=1601440046695&songmid=000b3wiQ3z0VbG&g_tk_new_20200303=5381&g_tk=5381&jsonpCallback=MusicJsonCallback_lrc&loginUin=1528773794&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0

简化 

https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_new.fcg?songmid=002mZevo3wHvsc&format=json&nobase64=1

