# coding:utf-8
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し,辞書オブジェクトとして格納せよ.

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


dict_data = {line[0]: line[1]
             for line in re.compile(r"^\|(.*?)\s=\s(.*?)\n(?=[^\*])", re.MULTILINE+re.DOTALL).findall(get_uk())}

for key, value in dict_data.items():
    print(u"{key} : {value}".format(key=key, value=value))
