def metade(num, format = False):
    """
        -> Recebe um número e mostra a metade
        :param num: Número
        :return: Metade do número
    """
    if format == True:
        return moeda(num * 0.5)
    else:
        return num * 0.5


def dobro(num, format = False):
    """
        -> Recebe um número e mostra o dobro
        :param num: Número
        :return: Dobro de número
    """
    if format == True:
        return moeda(num * 2)
    else:
        return num * 2


def aumentar(num, qtd, format = False):
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


def diminuir(num, qtd, format = False):
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


def resumo(num, qtd_aumentar, qtd_diminuir):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'Preço analisado:                {moeda(num)}')
    print(f'Dobro de preço:                 {dobro(num, True)}')
    print(f'Metade do preço:                {metade(num, True)}')
    print(f'{qtd_aumentar}% de aumento:                 {aumentar(num, qtd_aumentar, True)}')
    print(f'{qtd_aumentar}% de redução:                 {diminuir(num, qtd_diminuir, True)}')
    print('-'*40)


def moeda(dinheiro):
    dinheiro_formatado = round(dinheiro, 2)
    return f'R${str(dinheiro_formatado).replace(".", ",")}'


