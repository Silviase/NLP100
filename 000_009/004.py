s = [x.strip(".") for x in "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split()]
num = [0, 4, 5, 6, 7, 8, 14, 15, 18]
dic = {}
for i in range(len(s)):
    dic[i+1] = s[i][:1] if i in num else s[i][:2]
print(dic)
