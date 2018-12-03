# coding:utf-8
# 行数をカウントせよ．確認にはwcコマンドを用いよ．(正解は24行)

cnt = 0
file = open("hightemp.txt")
for i in file:
    cnt += 1
print(cnt)
file.close()
# 模範解答
# print(sum(1 for line in open("hightemp.txt")))
