from flask import Blueprint
from flask_cors import CORS
from flask_restful import Api

from routes.migu.index import Index
from routes.migu.lyric import Lyric
from routes.migu.playlist import PlayList, PlayListInfo
from routes.migu.search import Search, HotSearch, SuggestSearch
from routes.migu.singer import SingerInfo, SingerSongInfo
from routes.migu.song import SongUrl
from routes.migu.top import Top

blue_migu = Blueprint('blue_migu', __name__, url_prefix='/migu')
api = Api(blue_migu)
CORS(blue_migu)

api.add_resource(Index, '/')

## 搜索 主题
# 搜索
api.add_resource(Search, '/search/')
# 热门搜索
api.add_resource(HotSearch, '/search/hot/')
# 搜索建议
api.add_resource(SuggestSearch, '/search/suggest/')


## 排行榜  主题
# 排行榜类别
api.add_resource(Top, '/top/')


## 歌曲  主题
# 获取歌曲 url
api.add_resource(SongUrl, '/song/url/')


## 歌单  主题
# 各种 种类 歌单
api.add_resource(PlayList, '/playlist/')
# 歌单 详情
api.add_resource(PlayListInfo, '/playlist/info/')


## 歌词 主题
api.add_resource(Lyric, '/lyric/')

## 歌手  主题
# 歌手简介
api.add_resource(SingerInfo, '/singer/info/')
# 歌手的歌曲列表
api.add_resource(SingerSongInfo, '/singer/songinfo/')