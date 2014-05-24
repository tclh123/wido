# coding: utf-8

from wido.lib.text import get_urls_from_text


ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def base62_encode(num, alphabet=ALPHABET):
    """Encode a number in Base X

    `num`: The number to encode
    `alphabet`: The alphabet to use for encoding
    """
    if (num == 0):
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def base62_decode(string, alphabet=ALPHABET):
    """Decode a Base X encoded string into the number

    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for encoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num


# def mid_decode(string):

def mid_encode(num):
    id3 = num % 10000000
    id2 = num / 10000000 % 10000000
    id1 = num / 10000000 / 10000000

    str1 = base62_encode(id1)
    str2 = base62_encode(id2)
    str3 = base62_encode(id3)

    return ''.join([str1, str2, str3])


def make_statuses(statuses_jsondict):
    for s in statuses_jsondict:
        # if s.user.id == owner_uid:
        #     continue

        # note: urls dedup
        urls = get_urls_from_text(s.text)
        if 'retweeted_status' in s:
            urls_2 = get_urls_from_text(s.retweeted_status.text)
            urls = list(set(urls) | set(urls_2))

        # http://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-python-whilst-preserving-order
        def f7(seq):
            seen = set()
            seen_add = seen.add
            return [x for x in seq if x not in seen and not seen_add(x)]

        s['video_urls'] = f7(urls)
