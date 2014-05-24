# coding: utf-8

import os
from snspy import APIClient
from snspy import SinaWeiboMixin

APP_KEY = '185639834'                                   # app key
APP_SECRET = '8c9aa1623e8126dd5eec680f930bda8b'         # app secret
CALLBACK_URL = 'http://127.0.0.1:8888/callback'         # callback url

here = os.path.abspath(os.path.dirname(__file__))


def get_access_token():
    try:
        with open(os.path.join(os.path.dirname(here),
                  'access_token.bak'), 'r') as f:
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


if __name__ == '__main__':
    print client.statuses.user_timeline.get()
