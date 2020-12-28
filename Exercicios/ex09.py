"""
Ler um número inteiro. Se ele for par calcular e escrever o seu quadrado e se for ímpar calcular
e escrever seu cubo
"""

numero = int(input(" Digite um numero: "))

if numero % 2 == 0:
    print(numero ** 2)
else:
    print(numero ** 3)