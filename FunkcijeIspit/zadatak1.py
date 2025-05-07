def osnovne_operacije(broj1, broj2):
    return broj1 + broj2, broj1 - broj2, broj1 * broj2


prvi = float(input("Unesite prvi broj: "))
drugi = float(input("Unesite drugi broj: "))

rezultat = osnovne_operacije(prvi, drugi)
print(f"Suma, razlika i umnozak unesenih brojeva su: {rezultat}")