from ex115 import usuario
import json

while True:
    print('-'*40)
    print('MENU PRINCIPAL'.center(40))
    print('-'*40)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    print('-'*40)

    opcao = int(input('Sua opção: '))

    if opcao == 1:
        pessoas = usuario.listar()
        print('-'*40)
        print('PESSOAS CADASTRADAS'.center(40))
        print('-'*40)
        for pessoa in pessoas:
            print(f'{pessoa["nome"]:<38}', end='')
            print(f'{pessoa["idade"]:>2}')
        
    elif opcao == 2:
        print('-'*40)
        print('NOVO CADASTRO'.center(40))
        print('-'*40)
        novo_usuario = {}
        novo_usuario['nome'] = input('Nome: ').strip().title()
        novo_usuario['idade'] = usuario.leiaidade('Idade: ')

        usuario.cadastrar(novo_usuario)
    elif opcao == 3:
        break
    else: 
        print('ERRO! DIGITE UMA OPÇÃO VÁLIDA!!!')

