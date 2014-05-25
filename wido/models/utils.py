# coding=utf-8

from wido.lib.text import get_urls_from_text

from wido.models.video_url import VideoURL


# http://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-python-whilst-preserving-order
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if x not in seen and not seen_add(x)]


def make_statuses(owner_access_token, statuses_jsondict, is_expand=False):
    all_urls = []
    for s in statuses_jsondict:
        urls = get_urls_from_text(s.text)
        if 'retweeted_status' in s:
            urls_2 = get_urls_from_text(s.retweeted_status.text)
            urls = list(set(urls) | set(urls_2))

        all_urls += urls

    all_urls = f7(all_urls)

    if is_expand:
        maps = VideoURL.expand(owner_access_token, all_urls)

    for s in statuses_jsondict:
        urls = get_urls_from_text(s.text)
        if 'retweeted_status' in s:
            urls_2 = get_urls_from_text(s.retweeted_status.text)
            urls = list(set(urls) | set(urls_2))

        urls = f7(urls)

        if is_expand:
            urls = [maps['real_url'][url] for url in urls if url in maps]

        s['video_urls'] = urls
