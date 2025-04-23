def broji_rijeci(recenica):
    rijeci = 1
    for slovo in recenica:
        if slovo == " ":
            rijeci += 1
    return rijeci

broj = broji_rijeci("Python je zabavan programski jezik.")
print(broj)