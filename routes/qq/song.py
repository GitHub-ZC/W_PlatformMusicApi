from flask_restful import Resource, reqparse
from flask_restful import request as Req

import util.qq_request
from music.extions import cache
from util.qq_request import request

parser = reqparse.RequestParser()
parser.add_argument('mid', type=str, default='004O1DHG4MjYOi', trim=True)
parser.add_argument('br', type=str, default='128', choices=['m4a', '128', '320', 'flac', 'ape'], trim=True)

# 获取 音乐 播放地址 180，320，flac，m4a
class SongUrl(Resource):
    def get(self):
        args = parser.parse_args()
        br = args.get('br')
        mid = args.get('mid')

        uin = util.qq_request.cookie_dict.get('uin', 0)

        typeMap = {
            'm4a': {
                's': 'C400',
                'e': '.m4a',
            },
            '128': {
                's': 'M500',
                'e': '.mp3',
            },
            '320': {
                's': 'M800',
                'e': '.mp3',
            },
            'ape': {
                's': 'A000',
                'e': '.ape',
            },
            'flac': {
                's': 'F000',
                'e': '.flac',
            }
        }

        # 批量匹配
        midArr = ','.join(map(lambda x: f'"{x.strip()}"', mid.split(',')))
        fileArr = ','.join(map(lambda x: f'"{typeMap[br].get("s") + x.strip()*2 + typeMap[br].get("e")}"', mid.split(',')))

        url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?format=json&data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"658650575","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"filename":[%s],"guid":"658650575","songmid":[%s],"songtype":[0],"uin":"%s","loginflag":1,"platform":"20"}},"comm":{"uin":%s,"format":"json","ct":24,"cv":0}}'\
              % (fileArr, midArr, uin, uin)

        data = request(url, is_cookie=True)

        # 防止dict函数 转化 报错
        try:
            js_data = {
                'data': {
                    'url': dict([ [url.get('songmid'), 'http://112.29.192.37/amobile.music.tc.qq.com/' + url.get('purl')] for url in data.get('req_0').get('data').get('midurlinfo') if url.get('purl')])
                },
                'status': 200
            }
        except Exception as err:
            js_data = {
                'status': 400,
                'info': 'Songmid Invalid format or Server Invalid format'
            }

        cache.set(Req.url, js_data, timeout=120)
        return js_data