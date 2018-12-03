# coding:utf-8
# 自然数 N をコマンドライン引数などの手段で受け取り,入力のうち末尾の N 行だけを表示せよ.確認には tail コマンドを用いよ.

f = open("hightemp.txt")

n = int(input("Please key in natural number.\n"))

line = f.readlines()

for i, str in enumerate(line[-n::]):
    if i >= n:
        break
    print(str.strip())

f.close()
