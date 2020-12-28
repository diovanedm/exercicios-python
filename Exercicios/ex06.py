"""
Ler dois caracteres e escreve-los em ordem alfabética
"""

letra1 = ord(input(" Digite uma letra: "))
letra2 = ord(input(" Digite outra letra: "))

primeiro = letra1
segundo = letra2

if primeiro > segundo:
    primeiro = letra2
    segundo = letra1

print(chr(primeiro))
print(chr(segundo))

