def duljina_rijeci(lista):
    duljine = []
    for rijec in lista:
        duljine.append(len(rijec))
    return duljine

print(duljina_rijeci(["Suncokret", "Trava", "Monitor"]))