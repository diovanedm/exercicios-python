"""
Fazer um programa para ler ‘n’ números inteiros e imprimir a soma deles. O valor de ‘n‘ valor
deve ser lido do teclado
"""

def somar_numeros(n):
    array = list(str(n))
    resultado = 0
    for num in array:
        resultado = resultado + num

    print(resultado)


n = int(input("Digite um numero: "))
somar_numeros(n)