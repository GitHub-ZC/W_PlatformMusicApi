from flask_restful import Resource, reqparse

from util.migu_request import request


parser = reqparse.RequestParser()
parser.add_argument('offset', type=int, default=1, trim=True)
parser.add_argument('type', type=int, default=1, trim=True)

# 各种种类歌单
# 每一页默认返回 10 首,  1 推荐  2 最新
class PlayList(Resource):
    def get(self):
        args = parser.parse_args()
        offset = args.get('offset')
        type = args.get('type')

        if type == 1:
            url = f'https://m.music.migu.cn/migu/remoting/playlist_bycolumnid_tag?playListType=2&type=1&columnId=15127315&tagId=&startIndex={(offset - 1) * 10}'
        elif type == 2:
            url = f'https://m.music.migu.cn/migu/remoting/playlist_bycolumnid_tag?playListType=2&type=1&columnId=15127272&tagId=&startIndex={(offset - 1) * 10}'

        data = request(url)

        return data


sub_parser = reqparse.RequestParser()
sub_parser.add_argument('playListId', type=int, default=179730639, trim=True)
sub_parser.add_argument('limit', type=int, default=30, trim=True)

# 歌单详情
# 默认 每一页 30
class PlayListInfo(Resource):
    def get(self):
        args = sub_parser.parse_args()
        playListId = args.get('playListId')
        limit = args.get('limit')

        url = f'https://m.music.migu.cn/migu/remoting/playlistcontents_query_tag?playListType=2&playListId={playListId}&contentCount={limit}'

        data = request(url)
        return data