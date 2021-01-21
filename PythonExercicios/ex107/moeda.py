def metade(num = 0, format = False):
    """
        -> Recebe um número e mostra a metade
        :param num: Número
        :return: Metade do número
    """
    if format == True:
        return moeda(num * 0.5)
    else:
        return num * 0.5


def dobro(num = 0, format = False):
    """
        -> Recebe um número e mostra o dobro
        :param num: Número
        :return: Dobro de número
    """
    if format == True:
        return moeda(num * 2)
    else:
        return num * 2


def aumentar(num = 0, qtd = 0, format = False):
    """
        -> Recebe um número e uma quantidade e mostra a soma
        :param num: Número
        :param qtd: Quantidade a ser aumentada
        :return: Número + qtd
    """
    percent = (num * qtd )/ 100
    if format == True:
        return moeda(num + percent)
    else:
        return num + percent


def diminuir(num = 0, qtd = 0, format = False):
    """
        -> Recebe um número e uma quantidade e mostra a subtração
        :param num: Número
        :param qtd: Quantidade a ser diminuida
        :return: Número - qtd
    """
    percent = (num * qtd )/ 100
    if format == True:
        return moeda(num - percent)
    else:
        return num - percent


def resumo(num = 0, qtd_aumentar = 10, qtd_diminuir = 5):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'Preço analisado:  \t {moeda(num)}')
    print(f'Dobro de preço:  \t {dobro(num, True)}')
    print(f'Metade do preço:  \t {metade(num, True)}')
    print(f'{qtd_aumentar}% de aumento:  \t {aumentar(num, qtd_aumentar, True)}')
    print(f'{qtd_diminuir}% de redução:  \t {diminuir(num, qtd_diminuir, True)}')
    print('-'*40)


def moeda(dinheiro = 0, moeda = 'R$'):
    return f'{moeda}{dinheiro:.2f}'.replace(".", ",")


