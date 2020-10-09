from flask_restful import Resource, reqparse

from music.extions import cache
from util.migu_request import request

# 设置 '/' 参数解析对象
parser = reqparse.RequestParser()
parser.add_argument('key', type=str, default='暗号', trim=True)
parser.add_argument('limit', type=int, default=30, trim=True)
parser.add_argument('offset', type=int, default=1, trim=True)
# type：歌曲 2  歌手：1  专辑： 4 歌单：6  ​MV：5 ​ 歌词：7
parser.add_argument('type', type=int, default=2, choices=[1,2,4,5,6,7], trim=True)

# 设置 ‘/suggest’ 参数解析对象
sub_parser = reqparse.RequestParser()
sub_parser.add_argument('key', type=str, trim=True, required=True, help='key is required')


# 关键字搜索（type：歌曲 2  歌手：1  专辑： 4 歌单：6  ​MV：5 ​ 歌词：7）
class Search(Resource):
    def get(self):
        args = parser.parse_args()
        key = args.get('key')
        limit = args.get('limit')
        offset = args.get('offset')
        type = args.get('type')

        url = f'https://m.music.migu.cn/migu/remoting/scr_search_tag?rows={limit}&type={type}&keyword={key}&pgc={offset}'
        data = request(url)

        return data

# 热们搜索
class HotSearch(Resource):
    @cache.cached(timeout=60)
    def get(self):
        url = 'https://music.migu.cn/v3/api/search/hotwords'
        data = request(url)

        return data

# 搜索建议
class SuggestSearch(Resource):
    def get(self):
        args = sub_parser.parse_args()
        key = args.get('key')

        url = f'https://m.music.migu.cn/migu/remoting/autocomplete_tag?keyword={key}'

        data = request(url)
        return data