# coding=utf-8

from wido.client import client_with_access_token
from wido.consts import WEIBO_TYPE_VIDEO

from wido.lib.text import get_urls_from_text


class Timeline(object):
    def __init__(self, owner_uid, owner_access_token, r):
        self.owner_uid = owner_uid
        self.owner_access_token = owner_access_token
        self.r = r

    @classmethod
    def get(cls, owner_uid, owner_access_token,
            since_id=0, max_id=0, count=20, page=1):
        client = client_with_access_token(owner_access_token)
        r = client.statuses.home_timeline.get(feature=WEIBO_TYPE_VIDEO,
                                              since_id=since_id,
                                              max_id=max_id,
                                              count=count,
                                              page=page)
        for s in r.statuses:
            # if s.user.id == owner_uid:
            #     continue

            # note: urls dedup
            urls = get_urls_from_text(s.text)
            if not urls:
                urls = get_urls_from_text(s.retweeted_status.text)

            # http://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-python-whilst-preserving-order
            def f7(seq):
                seen = set()
                seen_add = seen.add
                return [x for x in seq if x not in seen and not seen_add(x)]

            s['video_urls'] = f7(urls)

        return cls(owner_uid, owner_access_token, r)
