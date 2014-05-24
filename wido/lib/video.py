#!/usr/bin/env python
# coding=utf-8

import re
import urllib
import requests


WANDOUJIA_SERVICE_PATTERN = 'http://dservice.wandoujia.com/convert?target=%s&type=VIDEO'
FLVCD_SERVICE_PATTERN = 'http://www.flvcd.com/parse.php?kw=%s'

YIXIA_PATTERN = 'http://paikeimg.video.sina.com.cn/stream/%s.mp4'


def wandoujia(url):
    r = requests.get(WANDOUJIA_SERVICE_PATTERN % url)
    if r.status_code == requests.codes.ok:
        d = r.json()
        if 'result' in d:
            return d['result'][0]['url']
    return None


def flvcd(url):
    r = requests.get(FLVCD_SERVICE_PATTERN % urllib.quote(url),
                     headers={'host': 'www.flvcd.com'})
    if r.status_code == requests.codes.ok:
        pattern = re.compile('<input\s+type="hidden"\s+name="inf"\s+value="([^"]+)')
        match = pattern.search(r.text)
        if match:
            urls = match.group(1)
            urls = urls.split('|')[:-1]
            return urls
    return None


def yixia(url):
    """ 秒拍
    input: http://yixia.com/show/Rz0glRihYKKYDTOdxuN~iQ__.htm
    output: http://paikeimg.video.sina.com.cn/stream/Rz0glRihYKKYDTOdxuN~iQ__.mp4
    """
    pattern = re.compile('http://yixia.com/show/(.*?).htm')
    match = pattern.search(url)
    if match:
        id_ = match.group(1)
        url = YIXIA_PATTERN % id_
        return url
    return None


def meipai(url):
    """ 美拍
    input: www.meipai.com/media/12134948
    output: http://mvvideo1.meitudata.com/5380b808b06cb3526.mp4
    """
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        pattern = re.compile('data-video="(.*?)"')
        match = pattern.search(r.text)
        if match:
            url = match.group(1)
            return url
    return None


def resolve(url):
    """ 由视频页地址 解析到 视频源文件地址 """
    if url.startswith('http://www.yixia.com'):
        return yixia(url)
    elif url.startswith('http://www.meipai.com'):
        return meipai(url)

    ret = wandoujia(url)
    if not ret:
        ret = flvcd(url)

    return ret


if __name__ == '__main__':
    assert wandoujia('http://t.cn/zYAjJZH') == 'http://vr.tudou.com/v2proxy/v2?it=162214698&st=52'
    assert wandoujia('http://bilibili.kankanews.com/video/av1120091/') is None

    assert flvcd('http://bilibili.kankanews.com/video/av1120091/')
    assert flvcd('http://v.youku.com/v_show/id_XNzE2MTExMTIw_ev_1.html')
    assert flvcd('http://www.tudou.com/programs/view/ubrrVcYGweA/') is None

    assert yixia('http://yixia.com/show/Rz0glRihYKKYDTOdxuN~iQ__.htm') == 'http://paikeimg.video.sina.com.cn/stream/Rz0glRihYKKYDTOdxuN~iQ__.mp4'

    assert meipai('http://www.meipai.com/media/12134948') == 'http://mvvideo1.meitudata.com/5380b808b06cb3526.mp4'

    assert resolve('http://bilibili.kankanews.com/video/av1120091/')
    assert resolve('http://www.meipai.com/media/12134948')

    print 'fine.'
