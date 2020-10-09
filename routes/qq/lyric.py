from flask_restful import Resource, reqparse

from util.qq_request import request

# 歌词的参数解析
parser = reqparse.RequestParser()
parser.add_argument('mid', type=str, default='004O1DHG4MjYOi', trim=True)

# 歌词
class Lyric(Resource):
    def get(self):
        args = parser.parse_args()
        mid = args.get('mid')

        url = f'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_new.fcg?songmid={mid}&format=json&nobase64=1&g_tk=5381'
        data = request(url)
        return data