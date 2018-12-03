# coding:utf-8

# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

import random


def typoglycemia(chr_line):
    results = []
    for word in chr_line.split():
        if len(word) <= 4:
            results.append(word)
        else:
            rand = list(word[1:-1])
            random.shuffle(rand)
            results.append(word[:1] + "".join(rand) + word[-1])
    return " ".join(results)


target = input("文字列を入力してください\n")

print(typoglycemia(target))
