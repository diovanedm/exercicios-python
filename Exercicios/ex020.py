def contar_caracteres(file):
    file = open(file, "r")
    text = file.read()
    array_text = list(str(text))
    array_text.remove(' ')
    print(text)
    print()
    count = 0
    for caracteres in array_text:
        count = count + 1

    print(f"Este documento tem {count} caracteres")

file = input("Digite o nome do arquivo: ")

contar_caracteres(f"{file}.txt")
