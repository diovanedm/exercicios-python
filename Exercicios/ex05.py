"""
Ler dois valores reais, determinar e escrever o menor e o maior
"""
try:
    a = float(input(" Digite um valor: "))
    b = float(input(" Digite outro valor: "))

    if a < b:
        print(a)
        print(b)
    else:
        print(b)
        print(a)

except ValueError:
    print(" Só são aceito numeros ")

