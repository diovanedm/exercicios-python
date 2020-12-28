"""
Ler   do   teclado   um   número   inteiro   com   três   dígitos   (no   formato   CDU   -   centena,  dezena   e  unidade)   e   mostrar   o   número   invertido   (no   formato   UDC).   O   número   invertido   deve   ser  armazenado   em   outra   variável   antes   de   ser   mostrado
"""

cdu = input("Digite um numero: ")

i = len(cdu) - 1
udc = ''

while i >= 0:
    udc = udc + cdu[i]
    i = i - 1

print(f'{cdu} em udc fica {udc}')

