from flask_restful import Resource, reqparse
from flask_restful import request as Req

from music.extions import cache
from util.qq_request import request


class TopCategory(Resource):
    def get(self):
        # uin = util.qq_request.cookie_dict.get('uin', 0)

        url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?_=1601389640007&data={"comm":{"g_tk":308189849,"uin":1528773794,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"h5","needNewCode":1,"ct":23,"cv":0},"topList":{"module":"musicToplist.ToplistInfoServer","method":"GetAll","param":{}}}'
        data = request(url)

        cache.set(Req.url, data, timeout=120)
        return data

# 排行榜各榜单详情
parser = reqparse.RequestParser()
parser.add_argument('topId', type=int, default=26, trim=True)
parser.add_argument('period', type=str, trim=True)
parser.add_argument('limit', type=int, default=200, trim=True)
parser.add_argument('offset', type=int, default=1, trim=True)

class Top(Resource):
    def get(self):
        args = parser.parse_args()
        topId = args.get('topId')
        period = args.get('period')
        offset = args.get('offset')
        limit = args.get('limit')

        if period:
            url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?format=json&data={"detail":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail","param":{"topId":%s,"offset":%s,"num":%s,"period":"%s"}},"comm":{"ct":24,"cv":0}}'\
                  % (topId, (offset - 1) * limit, limit, period)
        else:
            url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?format=json&data={"detail":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail","param":{"topId":%s,"offset":%s,"num":%s}},"comm":{"ct":24,"cv":0}}'\
                  % (topId, (offset - 1) * limit, limit)
        data = request(url)

        cache.set(Req.url, data, timeout=120)
        return data