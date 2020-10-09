from flask_restful import Resource, reqparse

from music.extions import cache
from util.qq_request import request

# 设置 '/' 参数解析对象
parser = reqparse.RequestParser()
parser.add_argument('key', type=str, default='暗号', trim=True)
parser.add_argument('limit', type=int, default=30, trim=True)
parser.add_argument('offset', type=int, default=1, trim=True)
# t: 0：单曲，2：歌单，3:用户 ,7：歌词，8：专辑，9：歌手，12：mv
parser.add_argument('type', type=int, default=0, choices=[0,2,3,7,8,9,12], trim=True)

# 设置 ‘/suggest’ 参数解析对象
sub_parser = reqparse.RequestParser()
sub_parser.add_argument('key', type=str, trim=True, required=True, help='key is required')


# 关键字搜索（t: 0：单曲，2：歌单，3:用户 ,7：歌词，8：专辑，9：歌手，12：mv）
class Search(Resource):
    def get(self):
        args = parser.parse_args()
        key = args.get('key')
        limit = args.get('limit')
        offset = args.get('offset')
        type = args.get('type')

        if type in [0, 7, 8, 9, 12]:
            url = f'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?t={type}&cr=1&p={offset}&n={limit}&w={key}&format=json'
        elif type in [2]:
            url = f'https://c.y.qq.com/soso/fcgi-bin/client_music_search_songlist?remoteplace=txt.yqq.playlist&page_no={offset-1}&num_per_page={limit}&query={key}&format=json'
        elif type in [3]:
            url = f'https://c.y.qq.com/soso/fcgi-bin/client_search_user?p={offset}&n={limit}&searchid=241014031194265199&remoteplace=txt.yqq.user&w={key}&format=json'
        data = request(url)

        return data

# 热们搜索
class HotSearch(Resource):
    @cache.cached(timeout=60)
    def get(self):
        url = 'https://c.y.qq.com/splcloud/fcgi-bin/gethotkey.fcg?format=json'
        data = request(url)

        return data

# 搜索建议
class SuggestSearch(Resource):
    def get(self):
        args = sub_parser.parse_args()
        key = args.get('key')

        url = f'https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg?key={key}&format=json'

        data = request(url)
        return data