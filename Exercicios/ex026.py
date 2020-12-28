f = open('nomes.txt', 'r')
nomes = f.read().split(' ')

x = 0
for nome in nomes:
    if nome[0].upper() == 'A':
        print(nome)
        x = x + 1
print()
print(f'{x} nomes começam com a letra A')