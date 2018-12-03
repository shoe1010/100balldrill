# coding:utf-8
# 各行の 1 列目だけを抜き出したものを col1.txt に, 2 列目だけを抜き出したものを col2.txt としてファイルに保存せよ.確認には cut コマンドを用いよ.

input = open("hightemp.txt")
col1 = open("col1.txt", "w")
col2 = open("col2.txt", "w")

for s in input:
    list = s.split()
    col1.write(list[0]+"\n")
    col2.write(list[1]+"\n")

input.close()
col1.close()
col2.close()
