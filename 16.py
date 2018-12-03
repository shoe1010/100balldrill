# coding:utf-8
# 自然数 N をコマンドライン引数などの手段で受け取り,入力のファイルを行単位で N 分割せよ.同様の処理をsplit コマンドで実現せよ.

f = open("hightemp.txt")

n = int(input("Please key in natural number.\n"))

num = 0
for i, str in enumerate(f):
    if i % n == 0:
        if i != 0:
            ans.close()
        num += 1
        ans = open("ans16_{number}.txt".format(number=num), "w")

    ans.write(str.rstrip()+"\n")
ans.close()
f.close()
