from flask import Blueprint
from flask_cors import CORS
from flask_restful import Api

from routes.qq.cookie import GetCookie, SetCookie
from routes.qq.index import Index
from routes.qq.lyric import Lyric
from routes.qq.search import Search, HotSearch, SuggestSearch
from routes.qq.song import SongUrl
from routes.qq.top import TopCategory, Top

blue_qq = Blueprint('blue_qq', __name__, url_prefix='/qq')
api = Api(blue_qq)
CORS(blue_qq)

## 主页 主题
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
api.add_resource(TopCategory, '/top/category/')
api.add_resource(Top, '/top/')

## 歌词 主题
api.add_resource(Lyric, '/lyric/')

## 歌曲  主题
# 获取歌曲 url
api.add_resource(SongUrl, '/song/url/')

## Cookie 主题
# 获取服务器的公共cookie
api.add_resource(GetCookie, '/getcookie/')
# 设置服务器的公共cookie（字符串形式cookie）
api.add_resource(SetCookie, '/setcookie/')