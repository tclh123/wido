# coding=utf-8

from wido.client import client_with_access_token

from wido.models.timeline import user_timeline
from wido.models.utils import make_statuses

# from wido.models.whitelist import check


class Rec(object):
    def __init__(self):
        pass

    @classmethod
    def get(cls, owner_access_token, start=0, limit=3):
        c = client_with_access_token(owner_access_token)

        r = None
        while not r:
            try:
                r = c.suggestions.users.may_interested.get(
                        count=100)
            except Exception as e:
                print repr(e)

        uids = [u.uid for u in r[start:limit]]

        statuses = [t for uid in uids for t in user_timeline(owner_access_token, uid)]
        make_statuses(owner_access_token, statuses)
        return statuses
