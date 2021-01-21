# set
from typing import List

def letter_n_gram(text: str, n:int) -> List[str]:
    res = []
    for i in range(len(text)-n+1):
        res.append(text[i:i+n])
    return res

s = "paraparaparadise"
t = "paragraph"

s_bi = set(letter_n_gram(s, 2))
t_bi = set(letter_n_gram(t, 2))

print("Union:", s_bi | t_bi) # Union: {'ar', 'ra', 'gr', 'ad', 'ap', 'se', 'pa', 'ph', 'is', 'ag', 'di'}
print("Difference:",s_bi - t_bi) # Difference: {'is', 'se', 'ad', 'di'}
print("Intersection:", s_bi & t_bi) # Intersection: {'ar', 'pa', 'ap', 'ra'}
print("se" in s_bi) # True