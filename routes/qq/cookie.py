from flask_restful import Resource, reqparse

import util.qq_request


# 获取 cookie
class GetCookie(Resource):
    def get(self):

        js_data = {
            'status': 200,
            'data': {'cookie': util.qq_request.cookie_dict}
        }
        return js_data

# 获取cookie的字符串
parser = reqparse.RequestParser()
parser.add_argument('cookie', type=str, required=True)

# 设置 cookie
class SetCookie(Resource):
    def post(self):
        args = parser.parse_args()
        cookie = args.get('cookie')

        try:
            arr = dict([i.split('=', 1) for i in cookie.split('; ')])
        except Exception as err:
            print(str(err))
            return {
                'status': 400,
                'info': 'Cookie Invalid format'
            }

        util.qq_request.cookie = cookie
        util.qq_request.cookie_dict = arr

        return {
            'status': 200,
            'info': 'Cookie Set up the success'
        }