import json, re

from flask_restful import Resource, reqparse
from flask_restful import request as Req

from music.extions import cache
from util.migu_request import request

# 参数解析
parser = reqparse.RequestParser()
parser.add_argument('artistId', type=int, default=18196, trim=True)


# 各种种类歌单
class SingerInfo(Resource):
    def get(self):
        args = parser.parse_args()
        artistId = args.get('artistId')

        url = f'https://m.music.migu.cn/migu/remoting/cms_artist_detail_tag?artistId={artistId}'

        data = request(url)

        cache.set(Req.url, data, timeout=120)
        return data

# 参数解析
sub_parser = reqparse.RequestParser()
sub_parser.add_argument('artistId', type=int, default=18196, trim=True)
sub_parser.add_argument('offset', type=int, default=1, trim=True)

# 歌手的歌曲详情列表
# 每一页数据都是 默认 20 首
class SingerSongInfo(Resource):
    def get(self):
        args = sub_parser.parse_args()
        artistId = args.get('artistId')
        offset = args.get('offset')

        url = f'https://music.migu.cn/v3/music/artist/{artistId}/song?page={offset}'

        data = request(url, isJson=False)

        # 正则匹配规则定义
        re_str = re.compile(r'(?s)<div class="add-to-playlist J_AddToPlaylist">.*?data-aid="(.*?)".*?data-mids="(.*?)".*?data-cids="(.*?)".*?data-share=\'(.*?)\'.*?</a>')
        re_total = re.compile(r'<span>全部歌曲（(.*?)）</span>')

        # 正则匹配
        songlist = re_str.findall(data)
        total = re_total.findall(data)

        js_data = []
        status = 200

        # 数据处理
        for i, x in enumerate(songlist):
            if len(x) == 4:
                try:
                    song = json.loads(x[-1])
                except Exception:
                    js_data = ['error server']
                    status = 400
                    break

                song.update(copyrightId=x[-2])
                song.update(albumId=x[0])
                song.update(id=x[1])
            js_data.append(song)

        js_data = {
            'data': {
                'status': status,
                'total': total,
                'num': len(js_data),
                'songlist': js_data
            }
        }

        cache.set(Req.url, js_data, timeout=120)
        return js_data