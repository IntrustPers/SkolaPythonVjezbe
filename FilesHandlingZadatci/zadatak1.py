with open("test.txt", "r") as file:
    # Citanje cjele datoteke
    #content = file.read()
    #print(content)

    # Citanje jedne linije teksta
    #one_line = file.readline()
    #print(one_line)

    #Citanje s for petljom
    for line in file:
        print(line.strip())


