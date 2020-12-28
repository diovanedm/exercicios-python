texto = "Considere Escreva Fazer"
texto = list(texto)

x = 0

for letra in texto:
    if letra.islower():
        x = x + 1

print(x)