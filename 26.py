# coding:utf-8
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ

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
    print(u"{key} : {value}".format(
        key=key, value=re.sub("'{2,5}", "", value)))
