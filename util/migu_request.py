import requests

# cookie = 'pgv_pvi=1986420736; pgv_pvid=2513132609; ts_uid=2001149360; RK=EPhAYJFjb2; ptcz=cea81665485ca84f2ae2cc148b6b4a118d7f74121a01f436e9255f50bceddc59; tmeLoginType=2; euin=NK4s7Kc57ioq; o_cookie=956581739; pac_uid=1_56581739; tvfe_boss_uuid=e29ed385dc7d68f4; yq_index=6; ts_refer=ADTAGmyqq; ptui_loginuin=956581739@qq.com; yqq_stat=0; pgv_si=s3487360000; pgv_info=ssid; userAction=1; ts_last=y.qq.com/; psrf_qqrefresh_token=25BACF1650EE2592D06BCC19EEAD7AD6; psrf_access_token_expiresAt=1609666640; qqmusic_key=Q_H_L_20Lwwz50eeIGVP7uQep6x2Z2DACs6J0RTja77axmeDeTbvnpevHtsR-QLJ68h_C; psrf_qqaccess_token=6B0C62126368CA1ACE16C932C679747D; uin=956581739; psrf_musickey_createtime=1601890640; psrf_qqopenid=239ACC14853AA1038A3A539429D0AC48; qm_keyst=Q_H_L_20Lwwz50eeIGVP7uQep6x2Z2DACs6J0RTja77axmeDeTbvnpevHtsR-QLJ68h_C; psrf_qqunionid='
# 默认 Cookie
# cookie = 'yqq_stat=0; pgv_info=ssid=s1520392; ts_last=y.qq.com/portal/player.html; pgv_pvid=1233495754; ts_uid=5486601780; pgv_pvi=4007713792; pgv_si=s6654436352; userAction=1; _qpsvr_localtk=0.8025676546673662; yq_index=0; yplayer_open=1; player_exist=1; qqmusic_fromtag=66'
# Cookie字符串 转 字典
# cookie_dict = {}

# try:
#     arr = dict([i.split('=', 1) for i in cookie.split('; ')])
#     cookie_dict = arr
#     print(' * The Current Cookie: ', arr)
# except Exception as err:
#     print(' * The Current Error: ',str(err))


def request(url, isJson=True):
    # 构建请求头
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
        'Referer': 'https://m.music.migu.cn/'
    }

    # if is_cookie:
    #     header.update(Cookie=cookie)

    res = requests.get(url, headers=header)

    if isJson:
        # 添加json转化出错的 错误捕获
        try:
            js_data = res.json()
        except Exception as err:
            js_data = {'error': 'Conversion error'}
    else:
        js_data = res.text


    return js_data
