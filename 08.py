# coding:utf-8

# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．


def cipher(string):
    result = ""

    for c in string:
        if c.islower():
            result += chr(219 - ord(c))
        else:
            result += c

    return result


string = input("文字列を入力してください\n")
result = cipher(string)
print("暗号化:" + result)
print("復号化:" + cipher(result))
