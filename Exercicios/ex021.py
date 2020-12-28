"""
 Escreva um programa em C que solicite ao usuário a digitação do nome de um arquivo texto já
existente, e que então gere um outro arquivo, que será uma cópia do primeiro
"""
def clonar_arquivo(file):
    file1 = open(f'{file}.txt', "r")
    file_content = file1.read()
    file2 = open(f"{file}-copia.txt", "w")
    file2.write(file_content)



file = input("Digite o arquivo que deseja clonar: ")
clonar_arquivo(file)
