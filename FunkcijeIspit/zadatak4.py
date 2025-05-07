def pronadji_min_max(lista):
    return min(lista), max(lista)

broj_unosa = int(input("Koliko brojeva zelis unijeti?: "))
unos = []
for x in range(broj_unosa):
    broj = int(input("Unesi novi broj: "))
    unos.append(broj)

print(f"Od nesenih brojeva najmanji i najveci su: {pronadji_min_max(unos)}")