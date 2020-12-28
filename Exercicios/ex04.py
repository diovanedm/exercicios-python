"""
Ler dois números inteiros e salva-los nas variáveis A e B. Em seguida, troque dos valores das
duas variáveis de forma que a variável A passe a ter o valor da variável B e vice-versa. No final,
mostre os valores finais
"""
def inverter_valores (a, b):
    temp = a
    a = b
    b = temp
    return a, b

def mostrar_valores(a, b):
    print(f' a: {a} \n b: {b}')

a = int(input(" Digite um valor: "))
b = int(input(" Digite outro valor: "))
mostrar_valores(a, b)

a, b = inverter_valores(a,b)
mostrar_valores(a, b)




