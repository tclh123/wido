# coding=utf-8

from wido.client import client_with_access_token


class VideoURL(object):
    def __init__(self):
        pass

    @classmethod
    def expand(cls, owner_access_token, urls):
        c = client_with_access_token(owner_access_token)

        r = None
        while not r:
            try:
                # URLencoded
                r = c.short_url.expand.get(url_short=urls)
            except Exception as e:
                print repr(e)

        long_urls = r.urls

        return r
