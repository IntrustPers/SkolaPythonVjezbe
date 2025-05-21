import tkinter as tk


def dodaj_biljesku():
    bilješka = unos_biljeske.get()
    if bilješka:
        with open("biljeske.txt", "a") as biljeznica:
            biljeznica.write(f"{bilješka}\n")
        unos_biljeske.delete(0, tk.END)
        status_label.config(text="Bilješka je uspješno spremljena.")
    else:
        status_label.config(text="Unesite bilješku prije spremanja.")


def otvori_biljeske():
    if not open("biljeske.txt", "r"):
        biljeske_label.config(text="Bilježnica nije pronađena.")
    else:
        with open("biljeske.txt", "r") as biljeznica:
            sadrzaj = biljeznica.read()
            if sadrzaj:
                biljeske_label.config(text=sadrzaj)
            else:
                biljeske_label.config(text="Nema spremljenih bilješki.")


def napravi_gui():
    global unos_biljeske, biljeske_label, status_label

    prozor = tk.Tk()
    prozor.title("Bilježnica")

    unos_biljeske_label = tk.Label(prozor, text="Unesite bilješku:")
    unos_biljeske_label.pack(pady=10)

    unos_biljeske = tk.Entry(prozor, width=40)
    unos_biljeske.pack(pady=10)

    dodaj_button = tk.Button(prozor, text="Dodaj Bilješku", command=dodaj_biljesku)
    dodaj_button.pack()

    pregled_button = tk.Button(prozor, text="Pregledaj Bilješke", command=otvori_biljeske)
    pregled_button.pack(pady=10)

    status_label = tk.Label(prozor, text="", fg="green")
    status_label.pack(pady=5)

    biljeske_label = tk.Label(prozor, text="", justify="left", anchor="nw")
    biljeske_label.pack(pady=10)

    prozor.mainloop()


napravi_gui()
