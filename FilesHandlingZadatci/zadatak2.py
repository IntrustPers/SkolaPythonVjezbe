with open("rezultat.txt", "w") as file:
    file.write("1.Neki tekst\n")
    file.write("2.Neki drugi tekst\n")
    file.write("3.Jos neki tekst\n")

with open("rezultat.txt", "r") as file:
    content = file.read()
    print(content)

with open("rezultat.txt", "a") as file:
    file.write("Sutra \n")
    file.write("Pišemo matematiku \n")

with open("rezultat.txt", "r") as file:
    content = file.read()
    print(content)