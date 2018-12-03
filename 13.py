# coding:utf-8
# col1.txt と col2.txt を結合し,元のファイルの 1 列目と 2 列目をタブ区切りで並べたテキストファイルを作成せよ.確認には paste コマンドを用いよ.

col1 = open("col1.txt")
col2 = open("col2.txt")
ans = open("ans13.txt", "w")

for s1, s2 in zip(col1, col2):
    ans.write(s1.rstrip() + '\t' + s2.rstrip() + '\n')

col1.close()
col2.close()
ans.close()
