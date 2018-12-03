# coding:utf-8
# 記事中に含まれるセクション名とそのレベル(例えば "== セクション名 ==" なら 1 )を表示せよ.

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


for line in re.compile("(={2,})\\s*(.*?)\\s*={2,}").findall(get_uk()):
    print(line[1]+" "+str(len(line[0])-1))
