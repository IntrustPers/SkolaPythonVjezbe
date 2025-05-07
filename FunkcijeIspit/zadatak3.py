def zbroj_znamenki(broj):
    zbroj = 0
    for znamenka in str(broj):
        zbroj += int(znamenka)
    return zbroj

unos = input("Unesi neki cijeli broj: ")
print(f"Zbroj znamenki unesenog broja je: {zbroj_znamenki(unos)}")
