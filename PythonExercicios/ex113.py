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
    else:
        return n
       


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')