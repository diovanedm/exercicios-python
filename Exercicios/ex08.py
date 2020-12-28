"""
Ler a idade de uma pessoa e dizer a faixa etária de acordo com as seguintes restrições:

Jovem (até 19 anos), Adulto (entre 20 e 59), Idoso (mais de 60 anos)
"""

idade = int(input(" Digite sua idade: "))

if idade < 20:
    print(" Jovem ")
elif idade < 60:
    print(" Adulto ")
else:
    print(" Idoso ")