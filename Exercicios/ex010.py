"""
Fazer um programa com um método capaz de lidar com dados com valores em cadeias de
caracteres (String). Separar os símbolos alfanuméricos (letras e algarismos) em cada cadeia.
"""

import re

palavra = ["Teste1-", "teste2.", "teste3"]

for teste in palavra:
    if teste.isalnum():
        print(teste)
    else:
        regex = re.findall("[a-z, A-Z, 0-9]", teste)
        print(regex)

