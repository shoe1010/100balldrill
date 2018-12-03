# coding:utf-8
# wikipedia記事の JSON ファイルを読み込み,「イギリス」に関する記事本文を表示せよ.問題 21-29 では,ここで抽出した記事本文に対して実行せよ.

import gzip
import json

f = gzip.open("jawiki-country.json.gz", "r", "utf-8")

for line in f:
    obj = json.loads(line)
    if obj[u"title"] == u"イギリス":
        print(obj["text"])
        break

f.close()
