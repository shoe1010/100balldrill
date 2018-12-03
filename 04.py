#coding : utf-8

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
line = [1, 5, 6, 7, 8, 9, 15, 16, 19]

print({i: word[:1] if i in line else word[:2]
       for i, word in enumerate(str.replace(".", " ").split(), 1)})
