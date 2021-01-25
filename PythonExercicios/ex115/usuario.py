import json

def cadastrar(usuario):
    try:
        arquivo = open('usuarios.txt', 'a')
        arquivo.write(json.dumps(usuario) + '\n')
        arquivo.close()
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
        arquivo.close()
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
    while True:
        try:
            n = int(input(txt))  
        except KeyboardInterrupt:
            print('O usuário não quis digitar.')
            return 0
        except (ValueError, TypeError):
            print('ERRO: digite uma idade válida!')
            continue
        else:
            return n
