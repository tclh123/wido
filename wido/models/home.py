# coding=utf-8

from wido.client import client_with_access_token

from wido.models.whitelist import rule
from wido.models.bi import Bi
from wido.models.timeline import user_timeline

from wido.lib.weibo import make_statuses


class Home(object):
    def __init__(self):
        pass

    @classmethod
    def big_v_user_ids(cls, owner_access_token, uid):
        c = client_with_access_token(owner_access_token)

        # TODO: 待改，用 ids 的，然后跟死列表比较
        r = None
        while not r:
            try:
                r = c.friendships.friends.get(uid=uid,
                                              count=200)
            except Exception as e:
                print repr(e)

        follows = r.users
        big_v = rule(follows)

        return list(big_v)

    @classmethod
    def bi_user_ids(cls, owner_access_token, uid):
        bi_uids = Bi.get(owner_access_token, uid, count=2000).uids

        return list(set(bi_uids))

    # 弃用
    @classmethod
    def user_ids(cls, owner_access_token, uid):
        c = client_with_access_token(owner_access_token)

        # TODO: cache 考虑持久化
        # 目前只能处理200个关注用户里的大V
        # FIXME: 性能 批量获得 用户关注的用户里面的情况
        # r = c.friendships.friends.ids.get(uid=uid,
        #                                   count=5000)
        r = c.friendships.friends.get(uid=uid,
                                      count=200)
        follows = r.users
        bi_uids = Bi.get(owner_access_token, uid, count=2000).uids

        big_v = rule(follows)

        return list(set(bi_uids) | big_v)

    @classmethod
    def get(cls, owner_access_token, owner_uid, start=0, limit=3):
        """由大V微博剖出"""

        user_ids = cls.big_v_user_ids(owner_access_token, owner_uid)
        # print len(user_ids), user_ids
        user_ids = user_ids[start:limit]
        # return user_timeline_batch(owner_access_token, user_ids)
        statuses = [t for uid in user_ids for t in user_timeline(owner_access_token, uid)]
        make_statuses(statuses)
        return statuses
