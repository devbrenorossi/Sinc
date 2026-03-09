import os
from time import sleep 

import modulos.functions as fun


# variavel estoque armazena os produtos.
ESTOQUE = {}
# proximo_id variavel para sempre mostrar um ID nos produtos e nunca repetir.
proximo_id = 1

# while principal com o Menu.
while True:
    fun.limpartela()
    # Apresentacao do programa com o nome.
    fun.saudacao()
    # print com as informacoes do programa.
    fun.print_opcoes()
    try:
        # variavel escolha armazena a escolha do usuario.
        escolha = int(input('O que deseja fazer? '))
        fun.limpartela()
        if escolha <= 0 or escolha >= 6:
            print("digite de 1 a 5")
            sleep(2.5)
            fun.limpartela()
            continue

    except ValueError:
            fun.limpartela()
            # tratamento de erro se o usuario digitar letras.
            print('Digite somente numeros ou (5) para sair...')
            sleep(2.5)
            fun.limpartela()
            continue

    # cadastro de produto.
    if escolha == 1:
        fun.cadastrar_produto(ESTOQUE, proximo_id)


    # listar produtos
    elif escolha == 2:

        # se nao tiver produto cadastrado ele informa.
        if not ESTOQUE:
            print('lista vazia, adicione produtos para conseguir vizualizar.')
            print('Precione ENTER para sair...')
            input()
            fun.limpartela()

        # se tiver ele mostra na tela.
        else:
            for id, dados in ESTOQUE.items():
                print(f'{id} - "nome": {dados["nome"]} - "quantidade": {dados["quantidade"]}')
            print('Precione ENTER para sair...')
            input()
            fun.limpartela()

    # Atualiza o produto.
    elif escolha == 3:
        try:
            id_produto = int(input('Digite o ID do produto: '))
            fun.limpartela()
        
            # Se o ID nao existir
            if id_produto not in ESTOQUE:
                print('ID nao encontrado....')
                print('Precione ENTER para sair...')
                input()
                fun.limpartela()
                continue

        except ValueError:
            print("digite somente numeros.")
            print('Precione ENTER para sair...')
            input()
            fun.limpartela()

        # Atualiza o ID informado
        else:
            ESTOQUE[id_produto]["nome"] = input('Digite novo nome: ').title()
            try:
                ESTOQUE[id_produto]["quantidade"] = int(input('Digite a nova quantidade: '))

                print('produto atualizado com sucesso....')
                print('Precione ENTER para sair...')
                input()
                fun.limpartela()
                
            except ValueError:
                print("digite somente numeros.")
                print('Precione ENTER para sair...')
                input()

    # remover um produto.
    elif escolha == 4:

        # se estoque vazio
        if not ESTOQUE:
            print('estoque vazio, adicione produtos..')
            print('Precione ENTER para sair...')
            input()
        
        # se tiver produto aqui ele remove.
        else:
            id_produto = int(input('digite o ID do produto a remover. '))
            
            if id_produto in ESTOQUE:
                nome_removido = ESTOQUE[id_produto]["nome"]

                del ESTOQUE[id_produto]

                print(f'{nome_removido}, Removido com sucesso....')
                print('Precione ENTER para sair...')
                input()
                fun.limpartela()

            # se nao encontrar produto
            else:
                print('Produto nao encontrado....')
                print('Precione ENTER para sair...')
                input()
    
    # Aqui encerra o programa
    else:
        print("=-"*21)
        print(" Sinc versão 1.0 criado por Breno Rossi ")
        print("=-"*21)
        sleep(3)
        break