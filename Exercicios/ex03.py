# Faça   um   programa   que   leia   um   caractere   (entre   A   e   Z)   e   mostre   na   tela   o   número   inteiro  correspondente   ao   caractere   na   tabela   ASCII

letra = input("Digite uma letra: ")
numero = ord(letra)
if numero >= 65 and numero <= 90:
    print(ord(letra))
else:
    print('Letra inválida')
