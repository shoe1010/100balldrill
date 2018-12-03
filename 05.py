# coding: utf-8

# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

str = "I am an NLPer"
N = 2

line = str.split()
print([" ".join(line[i:i+N]) for i in range(len(line)-(N-1))])

str = str.replace(" ","")
print([str[i:i+N] for i in range(len(str)-(N-1))])

# 文字列 = ‘区切り文字’.join(リスト)
