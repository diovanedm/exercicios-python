f = open("read1.txt", "r")

texto = f.read()
array_texto = texto.split()
print(array_texto)
print(len(array_texto))
