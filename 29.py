# coding:utf-8
# テンプレートの内容を利用し，国旗画像のURLを取得せよ．

import gzip
import json
import re
import requests


def get_uk():

    f = gzip.open("jawiki-country.json.gz", "r", "utf-8")

    for line in f:
        obj = json.loads(line)
        if obj[u"title"] == u"イギリス":
            return (obj["text"])
    f.close()


dict_data = {line[0]: line[1]
             for line in re.compile(r"^\|(.*?)\s=\s(.*?)\n(?=[^\*])", re.MULTILINE+re.DOTALL).findall(get_uk())}

file_name = re.sub(r"\{\{(?:[^]]+?\|)?([^|]+?)\}\}", r"\1", re.sub(
    r"\[\[(?:[^]]+?\|)?([^|]+?)\]\]", r"\1", re.sub(r"'{2,5}|<.*?>|\[http.*\]", "", dict_data[u"国旗画像"])))

url_requests = 'https://en.wikipedia.org/w/api.php?' \
    + 'action=query' \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&titles=File:' + file_name\
    + '&iiprop=url'

html = requests.get(url_requests)
url_fig = json.loads(html.text)['query']['pages'].popitem()[
    1]['imgeinfo'][0]['url']
print(url_fig)
