"""
13. Faça um programa que leia um caractere e se esse for uma letra maiúscula, imprima
“Maiúscula”.

14. Senão, se ele for uma letra minúscula, imprima “Minúscula”. Senão, se for um dígito, imprima
dígito. Senão imprima “Outro caractere”
"""

def verifica_digito(caracter):
    if caracter.isalnum():
        if(caracter.isnumeric()):
            print('Dígito')
        elif(caracter != caracter.lower()):
            print('Maiuscula')
        elif(caracter == caracter.lower()):
            print('Minuscula')
    else:
        print("Outro caractere")

caracter = input('Digite: ')
verifica_digito((caracter))





