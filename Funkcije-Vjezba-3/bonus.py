def je_anagram(rijec1, rijec2):
    slova1 = set(rijec1.lower())
    slova2 = set(rijec2.lower())
    if slova1 == slova2:
        return True
    else:
        return False

print(je_anagram("Listen", "Silent"))
print(je_anagram("Hello", "World"))