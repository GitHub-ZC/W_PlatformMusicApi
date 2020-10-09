import json
import re

from flask_restful import Resource, reqparse

from music.extions import cache
from util.migu_request import request


# 排行榜各榜单详情
parser = reqparse.RequestParser()
parser.add_argument('topId', type=int, default=2, trim=True, choices=[1,2,3,4,5,6,7,8,9,10,11,12,13])

class Top(Resource):
    # @cache.cached(timeout=120)
    def get(self):
        args = parser.parse_args()
        topId = args.get('topId')

        topList = {
            '1': 'jianjiao_newsong',
            '2': 'jianjiao_hotsong',
            '3': 'jianjiao_original',
            '4': 'migumusic',
            '5': 'movies',
            '6': 'mainland',
            '7': 'hktw',
            '8': 'eur_usa',
            '9': 'jpn_kor',
            '10': 'coloring',
            '11': 'ktv',
            '12': 'network',
            '13': 'newalbum'
        }

        url = f'https://music.migu.cn/v3/music/top/{topList[str(topId)]}'

        res = request(url, isJson=False)

        re_str = re.compile(r'<script>\s{0,}var\s{0,}listData\s{0,}=\s{0,}({.*})\s{0,}</script>')

        data = re_str.findall(res)
        if data:
            try:
                js_data = json.loads(data[0])
            except Exception:
                js_data = {
                    'status': 400,
                    'error': 'Json Invalid format'
                }
        else:
            js_data = {
                'status': 400,
                'error': 'service error'
            }

        return js_data