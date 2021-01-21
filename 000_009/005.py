import typing 
from typing import List

# n-gram
def word_n_gram(text: str, n:int) -> List[List[str]]:
    res = []
    words = text.split(" ")
    for i in range(len(words)-n+1):
        res.append(words[i:i+n])
    return res

def letter_n_gram(text: str, n:int) -> List[str]:
    res = []
    for i in range(len(text)-n+1):
        res.append(text[i:i+n])
    return res

s = "I am an NLPer"
print(word_n_gram(s, 2)) # [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
print(letter_n_gram(s, 2)) # ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']

