import string

def cipher(text: str) -> str:
    s = ""
    for c in text:
        s += chr(219 - ord(c)) if c in list(string.ascii_lowercase) else c
    return s

s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
print(cipher(s)) # Llivn rkhfn wloli hrg znvg, xlmhvxgvgfi zwrkrhxrmt vorg, hvw wl vrfhnlw gvnkli rmxrwrwfmg fg ozyliv vg wloliv nztmz zorjfz.

# どっちみちわからん。