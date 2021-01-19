s = [x.strip(".") for x in "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split()]
num = [0, 4, 5, 6, 7, 8, 14, 15, 18]
dic = {}
for i in range(len(s)):
    dic[i+1] = s[i][:1] if i in num else s[i][:2]
print(dic)

"""
{1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 
6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne', 
11: 'Na', 12: 'Mi', 13: 'Al', 14: 'Si', 15: 'P', 
16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca'}
"""