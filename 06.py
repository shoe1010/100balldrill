# coding:utf-8

# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

def char_Ngram(N,str):
    str = str.replace(" ","")
    return([str[i:i+N] for i in range(len(str)-(N-1))])

word_x = "paraparaparadise"
word_y = "paragraph"

x = set(char_Ngram(2,word_x))
y = set(char_Ngram(2,word_y))

print("X:"+str(x))
print("Y:"+str(y))
print("和集合:"+str(x | y))
print("積集合:"+str(x & y))
print("差集合(X-Y):"+str(x - y))
print("差集合(Y-X):"+str(y - x))
print("se in X? "+str("se" in x))
print("se in Y? "+str("se" in y))
