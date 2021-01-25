import json

def cadastrar(usuario):
    try:
        arquivo = open('usuarios.txt', 'a')
        arquivo.write(json.dumps(usuario) + '\n')
    except Exception as error:
        return error
    else:
        return True


def listar():
    try:
        arquivo = open('usuarios.txt', 'r')
        usuarios = []
        for linha in arquivo:
            usuarios.append(json.loads(linha))
    except Exception as error:
        return error
    else:
        return usuarios


def leiaidade(txt):
    """
        -> Recebe um texto que irá ser apresentado num input, após isso recebe o resultado do input e verifica se é ou não um número inteiro
        :param txt: pergunta do input
        :return: o número, caso seja inteiro
    """
    try:
        n = input(txt)
        if n.isnumeric():
            n = int(n)
        elif n.isnumeric() == False:
            while True:
                n = input('ERRO! DIGITE UMA IDADE VÁLIDA: ')
                if n.isnumeric():
                    n = int(n)
                    break
    except Exception as erro:
        print(f'Tivemos um erro: {erro}')
    except KeyboardInterrupt:
        print('O usuário não quis digitar.')
        return 0
    else:
        return n
