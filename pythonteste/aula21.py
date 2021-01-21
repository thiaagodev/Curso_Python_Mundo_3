def fatorial(num = 1):
    """
        Recebe um número e retorna o seu fatorial
        :param n -> numero recebido 
    """
    f = 1
    for count in range(num, 0, -1):
        f *= count
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
