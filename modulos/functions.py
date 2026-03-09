import os
from time import sleep


def limpartela():
    os.system('cls' if os.name == 'nt' else 'clear')


def saudacao():
    print("=-"*12)
    print("   Bem vindo ao Sinc")
    print("=-"*12)
    sleep(0.5)

def print_opcoes():
    print('''01 - Cadastrar Produto.
02 - Listar Produtos.
03 - Atualizar Produto.
04 - Remover Produtos.
05 - Sair do Programa.''')
    print("=-"*12)

def cadastrar_produto(ESTOQUE, proximo_id):
    try:
        nome_produto = input("Digite o nome do produto: ").title()

        for lista_nome in ESTOQUE.values():
            if lista_nome["nome"] == nome_produto:
                print('este produto ja esta cadastrado.')
                print('Precione ENTER para sair...')
                input()
                limpartela()
            
        quantidade_produto = int(input("Digite a quantidade de produto: "))
        ESTOQUE[proximo_id] = {
    "nome": nome_produto,
    "quantidade": quantidade_produto
        }
        print(f"{nome_produto} - {quantidade_produto}, adicionado com sucesso")
        print('Precione ENTER para sair...')
        input()
        limpartela()

    except ValueError:
        print('Digite somente numeros...')
        print('Precione ENTER para sair...')
        input()
        limpartela()
        
    return proximo_id + 1


    