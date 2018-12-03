# coding:utf-8
# 各行の 1 列目の文字列の出現頻度を求め,その高い順に並べて表示せよ.確認には cut, uniq, sort コマンドを用いよ.

from collections import Counter

f = open("hightemp.txt")

for n in Counter([s.split()[0] for s in f]).most_common():
    s, i = n
    print(str(i) + " " + s)

f.close()
