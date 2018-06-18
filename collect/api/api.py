# facebook api wrapper functions

from urllib.parse import urlencode
from .web_request import json_request   # 함수 import

# BASE_URL_FB_API = 'https://graph.facebook.com/v3.0' # python에는 상수 없음 대문자로 표시
# ACCESS_TOKEN = "EAACEdEose0cBAO8ZCte5X0iMoE7127sa6IwcZCCV8P3tNolp2s6nnJTyJHiFndbJsquw9sZAZAp7dWSASwxBSE7X5nGXpxqJ87dC7oklmVBOAoKtpesZCxqqfC7MTZCBctJuVz27uBZCRmbwAuEnsdpWihlly01UNFXz8LcdRyZCBqWJEyYxgOAVoZB9BL0FJb9QZD"


def fb_gen_url(base_url='', node='', **params):       # **params : dict 형대로 받기

    url = '%s/%s/?%s' % (base_url, node, urlencode(params))    # dict을 파라미터로 바꿔주는 함수
    return url


def fb_name_to_id(base_url, pagename, access_token):            # ex) jtbcnews id 값 받아오기
    url = fb_gen_url(base_url=base_url, node=pagename, access_token = access_token)
    json_result = json_request(url=url)

    return json_result.get('id')

def fb_fetch_posts(base_url, pagename, since, until, access_token):        # 중요!!! crawler
    url = fb_gen_url(base_url=base_url, node=fb_name_to_id(base_url, pagename,  access_token) +"/posts",
                     fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
                     since=since, until=until, limit=50, access_token=access_token)

    isnext = True   # 판단 확인
    while isnext is True:
        json_result = json_request(url=url)

        paging = None if json_result is None else json_result.get('paging')

        posts = None if json_result is None else json_result.get('data')
        url = None if paging is None else paging.get('next')
        isnext = url is not None

        yield posts

""" 
삼항 연산자로 변경
if json_result is None:
    paging = None
else:
    paging = json_result.get('paging')
"""