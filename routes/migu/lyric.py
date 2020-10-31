from flask_restful import Resource, reqparse
from flask_restful import request as Req

from music.extions import cache
from util.migu_request import request

# 歌词的参数解析
parser = reqparse.RequestParser()
parser.add_argument('id', type=str, default='60084600554', trim=True)

# 歌词
class Lyric(Resource):
    def get(self):
        args = parser.parse_args()
        id = args.get('id')

        url = f'https://music.migu.cn/v3/api/music/audioPlayer/getLyric?copyrightId={id}'
        data = request(url)

        cache.set(Req.url, data, timeout=120)
        return data