# coding:utf-8
# タブ 1 文字につきスペース 1 文字に置換せよ.確認には sed コマンド, tr コマンド,もしくは expand コマンドを用いよ.
input = open("hightemp.txt")
output = open("ans11.txt", "w")

for s in input:
    output.write(s.replace("\t", " "))

input.close()
output.close()
