"""
Faça   um   programa   que   leia   um   número   inteiro   (entre   65   e   90)   e   mostre   na   tela   o   caractere  correspondente   a   ele   na   tabela   ASCII
"""
numero = int(input("Digite um número: "))
if numero >= 65 and numero <= 90:
    print(chr(numero))
else:
    print('Não existe uma letra que corresponde a este número na tabela ASCII')


