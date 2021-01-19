import re
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print(list(map(lambda x: len(x), re.sub("[,.]", "", s).split()))) # -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
