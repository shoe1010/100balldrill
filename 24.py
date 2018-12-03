# coding:utf-8
# 記事から参照されているメディアファイルをすべて抜き出せ.

import gzip
import json
import re


def get_uk():

    f = gzip.open("jawiki-country.json.gz", "r", "utf-8")

    for line in f:
        obj = json.loads(line)
        if obj[u"title"] == u"イギリス":
            return (obj["text"])
    f.close()


for line in re.compile(u".*(?:File|ファイル):(.+?)\\|").findall(get_uk()):
    print(line)
