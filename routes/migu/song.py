from flask_restful import Resource, reqparse

from util.migu_request import request

parser = reqparse.RequestParser()
parser.add_argument('id', type=str, default='60054701923', trim=True)
# parser.add_argument('br', type=str, default='128', choices=['m4a', '128', '320', 'flac', 'ape'], trim=True)

# 获取 音乐 播放地址 180，320，flac，m4a
class SongUrl(Resource):
    def get(self):
        args = parser.parse_args()
        # br = args.get('br')
        id = args.get('id')

        # 批量匹配
        # midArr = ','.join(map(lambda x: f'"{x.strip()}"', mid.split(',')))


        url = f'https://m.music.migu.cn/migu/remoting/cms_detail_tag?cpid={id}'

        data = request(url)

        return data