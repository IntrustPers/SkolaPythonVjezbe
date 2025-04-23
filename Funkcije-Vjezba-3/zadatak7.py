def filtriraj_po_duljini(rijeci, duljina):
    dulje_rijeci = []
    for rijec in rijeci:
        if len(rijec) > 3:
            dulje_rijeci.append(rijec)
    return dulje_rijeci

rijeci = ["pas", "mačka", "miš", "slon", "žirafa"]
print(filtriraj_po_duljini(rijeci, 3))