def izracunaj_prosjek(lista):
    zbroj = 0
    for element in lista:
        zbroj += element
    if len(lista) >= 1:
        return zbroj / len(lista)
    else:
        return 0

print(izracunaj_prosjek([1, 2, 3, 4, 5]))
print(izracunaj_prosjek([]))