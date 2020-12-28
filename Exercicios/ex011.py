"""
Ler um nome de pessoa. Verificar se é igual ou não ao seu nome, escrevendo mensagem
adequada
"""

def verificar_nome(nome_um, nome_dois):
    if nome_um == nome_dois:
        print(f'{nome_um} é igual a {nome_dois}')
    else:
        print(f'{nome_um} é diferente de {nome_dois}')


nome_um = input(' Digite um nome: ')
nome_dois = input(' Digite o segundo nome: ')

verificar_nome(nome_um, nome_dois)