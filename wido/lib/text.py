# coding: utf-8

import re


def get_urls_from_text(text):
    return re.findall(r'http://[\w/.]+', text)
