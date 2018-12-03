# coding:utf-8
# 各行を 3 コラム目の数値の逆順で整列せよ(注意 : 各行の内容は変更せずに並び替えよ).確認には sort コマンドを用いよ(この問題はコマンドで実行した時の結果と合わなくてもよい)

f = open("hightemp.txt")

list = f.readlines()

sorted(list, key=lambda f: float(f.split()[2]), reverse=True)

for s in list:
    print(s.rstrip())

f.close()
