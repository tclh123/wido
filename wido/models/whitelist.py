# coding: utf-8

"""
白名单策略：
(大V && 粉>10w) || 白名单用户


待改，存死的列表
"""

# from wido.client import client_with_access_token


class Whitelist(object):
    """ store in mysql or file """
    def __init__(self):
        pass

    @classmethod
    def get(cls):
        return set()


def check(user):
    if user.followers_count >= 100000 and user.verified:
        return True


def rule(users):
    ret = set()

    white = Whitelist.get()
    ret_add = ret.add
    for u in users:
        if u.id in white or check(u):
            ret_add(u.id)

    return ret
