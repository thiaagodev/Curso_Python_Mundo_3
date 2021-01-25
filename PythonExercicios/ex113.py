def leiaint(txt):
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
                n = input('ERRO! DIGITE UM NÚMERO INTEIRO: ')
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
       

def isFloat(num):
    try:
        num = float(num)
    except Exception as error:
        return False
    else:
        return True


def leiafloat(txt):
    try:
        n = input(txt)
        if isFloat(n):
            n = float(n)
        if isFloat(n) == False:
            while True:
                n = input('ERRO! DIGITE UM NÚMERO FLUTUANTE: ')
                if isFloat(n):
                    n = float(n)
                    break
        
    except Exception as erro:
        print(f'Tivemos um erro: {erro}')
    except KeyboardInterrupt:
        print('O usuário não quis digitar.')
        return 0
    else:
        return n

n = leiaint('Digite um número inteiro: ')
nfloat = leiafloat('Digite um número flutuante: ')
print(f'Você digitou o número inteiro {n} e o número flutuante {nfloat}')