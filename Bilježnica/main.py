def prikazi_izbornik():
    print("--- Jednostavna Bilježnica ---")
    print("1. Dodaj novu bilješku")
    print("2. Pregledaj sve bilješke")
    print("3. Izlaz")
    print("Odaberite opciju (1-3): ")

def dodaj_biljesku():
    unos = input("Unesi bilješku: ")
    with open("biljeske.txt", "a") as biljeznica:
        biljeznica.write(f"{unos}\n")
        biljeznica.close()
    print("Bilješka je uspješno spremljena.")

def otvori_biljeske():
    with open("biljeske.txt", "r") as biljeznica:
        sadrzaj = biljeznica.read()
        print(sadrzaj)
