#!/usr/bin/env python
# coding: utf-8

from snspy import APIClient
from snspy import SinaWeiboMixin

from config import APP_KEY, APP_SECRET, CALLBACK_URL

client = APIClient(SinaWeiboMixin, app_key=APP_KEY, app_secret=APP_SECRET,
                   redirect_uri=CALLBACK_URL)

authorize_url = client.get_authorize_url()
print 'please go %s with your browser. LOL' % authorize_url

code = raw_input("input CODE:")  # 166e02a2502c6804ae6b54912dde1bc3

r = client.request_access_token(code)
access_token = r.access_token  # access token，e.g., abc123xyz456
expires = r.expires      # token expires time, UNIX timestamp, e.g., 1384826449.252 (10:01 am, 19 Nov 2013, UTC+8:00)

print "access_token: %s\nexpires: %s" % (access_token, expires)

# FIXME: can't store???
# TODO: auto get_access_token...!!!!
with open('access_token.bak', 'w') as f:
    f.write("%s\n" % access_token)
    f.write("%s\n" % expires)

# access_token: 2.007xjRoB0s5vYMc99d8b88fePfaoaD
# expires: 1558585961


# 2.007xjRoB4FD2YC43bbb2dda6z7W7KE
# 1403550002
