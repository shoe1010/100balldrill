# coding:utf-8
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
import re

str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
print([len(word) for word in re.sub(r'[,.]', " ", str).split()])
# print([])---リスト内包表記，リストを作るならこれが良い．動作が早い．
# リスト内包表記---だいたい[処理 for if]で作る．ただし，if elseのときはforの前に書くこと
# re.sub(置換したい文字(正規表現),"置換する文字",置換する文字列)---置換したい文字が複数あるときに使う．一つならreplace関数で良い．
