# coding:utf-8
# 1列目の文字列の種類(異なる文字列の集合)を求めよ.確認には sort, uniq コマンドを用いよ.

f = open("hightemp.txt")

ans = {s.split()[0] for s in f}

for n in ans:
    print(n)

f.close()
