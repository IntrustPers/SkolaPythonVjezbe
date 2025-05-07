def filtriraj_rijeci(lista, n):
    dulje_od_n = []
    for rijec in lista:
        if len(rijec) > n:
            dulje_od_n.append(rijec)
    return dulje_od_n

print(filtriraj_rijeci(["Lubenica", "KFC", "Kool-aid", "Žir", "Jabuka"], 3))