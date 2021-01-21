# 9. Typoglycemia
import random

def randomize(text: str, length: int=4):
    res = []
    for word in text.split(" "):
        add = ""
        if len(word) <= length:
            add = word
        else:
            add += word[0]
            add += "".join(random.sample(word[1:-1], len(word[1:-1])))
            add += word[-1]
        res.append(add)
    res = " ".join(res)
    return res

s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(randomize(s))
