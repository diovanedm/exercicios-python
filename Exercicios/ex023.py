"""
Escreva um programa em C que determine o valor máximo, o valor mínimo e a média
desses valores armazenados no arquivo. Imprima esses valores na tela
"""
file = open('valores.txt')
valores = file.readlines()
array = []
media = 0

for valor in valores:
    x = valor.strip('\n')
    array.append(x)
    media = media + float(x)

print("maior: ", max(array))
print("menor: ",min(array))
print("media: ",media / len(array))

