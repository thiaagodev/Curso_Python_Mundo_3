from random import randint

def sorteia(nums):
    nums = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
    return nums


def somaPar(nums):
    soma = 0
    for num in nums:
        if num % 2 == 0:
            soma += num
    return soma


numeros = sorteia([])
print(f'Sorteando 5 valores da lista: {numeros}')
print(f'A soma dos valores pares de {numeros} é {somaPar(numeros)}')
