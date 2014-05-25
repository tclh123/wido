# coding=utf-8

from wido.client import client_with_access_token

from wido.lib.video import resolve


class VideoURL(object):
    def __init__(self):
        pass

    @classmethod
    def get_long_urls(cls, owner_access_token, urls):
        """ return dict (short_url -> long_url) """
        c = client_with_access_token(owner_access_token)

        r = None
        while not r:
            try:
                # URLencoded
                r = c.short_url.expand.get(url_short=urls)
            except Exception as e:
                print repr(e)

        return r.urls

    @classmethod
    def expand(cls, owner_access_token, urls):
        """ return dict (short_url -> long_url) """

        rurls = []
        if len(urls) <= 20:
            rurls = cls.get_long_urls(owner_access_token, urls)

        while len(urls) > 20:
            urls_20 = urls[:20]
            urls = urls[20:]
            rurls += cls.get_long_urls(owner_access_token, urls_20)

        dic = {}
        for d in rurls:
            if d.result:
                if d.type == 1 or d.type == 39 or (d.type > 5):
                    ret = resolve(d.url_long)
                    if type(ret) is list:
                        ret = ret[0]
                    dic[d.url_short] = dict(real_url=ret,
                                            is_video=True,
                                            is_broken=False)
                else:
                    dic[d.url_short] = dict(real_url=d.url_long,
                                            is_video=False,
                                            is_broken=False)
            else:
                dic[d.url_short] = dict(real_url=None,
                                        is_video=None,
                                        is_broken=True)

        return dic
