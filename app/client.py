# coding: utf-8

import os
from snspy import APIClient
from snspy import SinaWeiboMixin

from config import APP_KEY, APP_SECRET, CALLBACK_URL

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

client = APIClient(SinaWeiboMixin,
                   app_key=APP_KEY, app_secret=APP_SECRET,
                   redirect_uri=CALLBACK_URL,
                   access_token=access_token, expires=expires)


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
                                          feature=3)
    print r


if __name__ == '__main__':
    test_home_timeline()
