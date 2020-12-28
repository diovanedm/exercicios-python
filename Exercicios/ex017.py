"""
Fazer uma função double um_sobre_impar(n) que recebe um número inteiro ‘n’ e retorna o n-
ésimo termo da sequência 1/3, 1/5, 1/7, 1/9, 1/11 ...
"""


def um_sobre_impar(n):
    denominador = (2 * n) + 1
    return 1 / denominador


valor = um_sobre_impar(9)
print(valor)