def leiaint(txt):
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
            print('ERRO: digite um número inteiro válido!')
            continue
        else:
            return n
       

def leiafloat(txt):
    while True:
        try:
            n = float(input(txt))     
        except Exception as erro:
            print(f'Tivemos um erro: {erro}')
        except KeyboardInterrupt:
            print('O usuário não quis digitar.')
            return 0
        except (ValueError, TypeError):
            print('ERRO: digite um número flutuante válido!')
            continue
        else:
            return n

n = leiaint('Digite um número inteiro: ')
nfloat = leiafloat('Digite um número flutuante: ')
print(f'Você digitou o número inteiro {n} e o número flutuante {nfloat}')