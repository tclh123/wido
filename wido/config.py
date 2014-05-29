# coding: utf-8

# add config here

# from weiciyuan, https://github.com/qii/weiciyuan/blob/479168a3d2458cbc8a9dcdfb2be5616fc1ccdd7a/src/org/qii/weiciyuan/dao/URLHelper.java#L14
APP_KEY = '1065511513'                                          # app key
APP_SECRET = 'df428e88aae8bd31f20481d149c856ed'                 # app secret
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'      # callback url


try:
    from local_config import *
except:
    pass
