# coding: utf-8

from wido.client import client_with_access_token


class Bi(object):
    def __init__(self, uid, uids):
        self.uid = uid
        self.uids = uids

    @classmethod
    def get(cls, owner_access_token,
            uid, count=50, page=1, sort=0):
        client = client_with_access_token(owner_access_token)

        r = client.friendships.friends.bilateral.ids.get(uid=uid,
                                                         count=count,
                                                         page=page,
                                                         sort=sort)

        uids = r.ids

        return cls(uid, uids)
