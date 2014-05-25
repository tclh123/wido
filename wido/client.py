# coding: utf-8

import os
from snspy import APIClient
from snspy import SinaWeiboMixin

from wido.config import APP_KEY, APP_SECRET, CALLBACK_URL

here = os.path.abspath(os.path.dirname(__file__))


def get_access_token():
    try:
        with open(os.path.join(here, 'access_token.bak'), 'r') as f:
            text = f.read()
            res = text.splitlines()
        return res
    except Exception as e:
        print 'Error with get_access_token()'
        raise e

access_token, expires = get_access_token()


def client_with_access_token(a):
    c = APIClient(SinaWeiboMixin,
                  app_key=APP_KEY, app_secret=APP_SECRET,
                  redirect_uri=CALLBACK_URL,
                  access_token=a, expires=expires)
    return c

client = client_with_access_token(access_token)


def test_home_timeline():
    r = client.statuses.home_timeline.get(feature=3)
    for s in r.statuses:
        print s.user.screen_name

        from lib.weibo import mid_encode
        from lib.text import get_urls_from_text

        print 'http://weibo.com/%s/%s' % (s.user.id, mid_encode(int(s.mid)))

        # note: urls dedup
        urls = get_urls_from_text(s.text)
        if not urls:
            urls = get_urls_from_text(s.retweeted_status.text)
        print urls


def test_user_timeline():
    r = client.statuses.user_timeline.get(screen_name='wheam_',
                                          feature=3,
                                          count=1)
    print r


# note: broken
def test_by_status():
    r = client.suggestions.users.by_status.get(content="""
    豆瓣 CODE 两年历程回顾：git 不是万能的，没有 review 是万万不能的 http://t.cn/8FOHQjc
    """,
                                               num=10)
    print r


def test_short():
    r = client.short_url.expand.get(url_short=['http://t.cn/RvZTqbR', 'http://t.cn/RvUIY6K'])
    print r


if __name__ == '__main__':
    # test_home_timeline()
    # test_user_timeline()
    # test_by_status()
    test_short()
