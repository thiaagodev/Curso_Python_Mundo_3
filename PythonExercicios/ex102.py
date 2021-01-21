from time import sleep

def fatorial(num = 1, show = False):
    """
        -> Calcula o Fatorial de um número.
        :param n: O número a ser calculado
        :param show: (Opcional) Mostrar ou não a conta.
        :return: O Valor do Fatorial
    """
    result = 0
    f = 1
    if show:
        for count in range(num, 0, -1):
            f *= count
            print(count, end=' ')
            if count > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    else:
        for count in range(num, 0, -1):
            f *= count
    return f


print(fatorial(5))
print(fatorial(5, show=True))
