"""
Ler dois caracteres e escreve-los em ordem alfabética
"""
#

def ordenar_palavras(palavra1, palavra2, indice1, indice2):
    if ord(palavra1[indice1]) > ord(palavra2[indice2]):
        temp = palavra1
        palavra1 = palavra2
        palavra2 = temp
        return palavra1, palavra2
    return  palavra1, palavra2


palavra1 = input(" Digite uma palavra: ")
palavra2 = input(" Digite outra palavra: ")

if palavra1[0] == palavra2[0]:
    final_palavra1 = len(palavra1) - 1
    final_palavra2 = len(palavra2) - 1
    palavra1, palavra2 = ordenar_palavras(palavra1, palavra2, final_palavra1, final_palavra2)
else:
    palavra1, palavra2 = ordenar_palavras(palavra1, palavra2, 0, 0)

print(palavra1, palavra2)






