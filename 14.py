# coding:utf-8
# 自然数 N をコマンドライン引数などの手段で受け取り,入力のうち先頭の N 行だけを表示せよ.確認には headコマンドを用いよ

f = open("hightemp.txt")

n = int(input("Please key in natural number.\n"))

for i, str in enumerate(f):
    if i >= n:
        break
    print(str.rstrip())
f.close()
