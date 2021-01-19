import re
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print(list(map(lambda x: len(x), re.sub("[,.]", "", s).split())))
