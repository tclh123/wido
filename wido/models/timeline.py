# coding=utf-8

from wido.client import client_with_access_token
from wido.consts import WEIBO_TYPE_VIDEO

# from wido.lib.text import get_urls_from_text
from wido.lib.weibo import make_statuses


class Timeline(object):
    def __init__(self, owner_uid, owner_access_token, r):
        self.owner_uid = owner_uid
        self.owner_access_token = owner_access_token
        self.r = r

    @classmethod
    def get(cls, owner_uid, owner_access_token,
            since_id=0, max_id=0, count=20, page=1):
        client = client_with_access_token(owner_access_token)

        r = None
        while not r:
            try:
                r = client.statuses.home_timeline.get(feature=WEIBO_TYPE_VIDEO,
                                                      since_id=since_id,
                                                      max_id=max_id,
                                                      count=count,
                                                      page=page)
            except Exception as e:
                print repr(e)

        make_statuses(r.statuses)

        return cls(owner_uid, owner_access_token, r)


def user_timeline(owner_access_token, uid, count=3, hrs_limit=48):
    c = client_with_access_token(owner_access_token)
    try:
        r = c.statuses.user_timeline.get(uid=uid,
                                         feature=WEIBO_TYPE_VIDEO,
                                         count=count)
    except:
        return []

    # TODO
    statuses = [s for s in r.statuses if s.created_at]
    return statuses


# FIXME: 批量获取没有权限啊哥哥
def user_timeline_batch(owner_access_token, uids, count=3, hrs_limit=48):
    c = client_with_access_token(owner_access_token)
    try:
        r = c.statuses.timeline_batch.get(uids=uids,
                                          feature=WEIBO_TYPE_VIDEO,
                                          count=count)
    except Exception as e:
        print repr(e)
        return []

    # TODO
    print r
    return r
    statuses = [s for s in r.statuses if s.created_at]
    return statuses
