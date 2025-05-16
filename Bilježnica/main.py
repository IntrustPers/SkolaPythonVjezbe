import time


def prikazi_izbornik():
    print("\n--- Jednostavna Bilježnica ---")
    print("1. Dodaj novu bilješku")
    print("2. Pregledaj sve bilješke")
    print("3. Izlaz")
    print("------------------------------\n")


def dodaj_biljesku():
    unos = input("Unesi bilješku: ")
    with open("biljeske.txt", "a") as biljeznica:
        biljeznica.write(f"{unos}\n")
    print("Bilješka je uspješno spremljena.")
    time.sleep(0.5)


def otvori_biljeske():
    with open("biljeske.txt", "r") as biljeznica:
        sadrzaj = biljeznica.read()

        if not sadrzaj:
            print("Nema spremljenih bilješki.")
        else:
            print(sadrzaj)
        time.sleep(0.5)


def napravi_biljznicu():
    """Funkcija koja izradi text file 'biljeske.txt' """
    with open("biljeske.txt", "w") as biljeznica:
        pass


napravi_biljznicu()
radi = True
while radi:
    prikazi_izbornik()

    lista_opcija = {1, 2, 3}
    opcija = int(input("Unesite opciju(1-3): "))
    while opcija not in lista_opcija:
        opcija = int(input(f"Neispravan odabir.\nMolimo unesite broj između 1 i 3: "))

    if opcija == 1:
        dodaj_biljesku()
    elif opcija == 2:
        otvori_biljeske()
    elif opcija == 3:
        print("Doviđenja!")
        radi = False
