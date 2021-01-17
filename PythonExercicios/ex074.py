from random import randint

n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)

tupla = (n1, n2, n3, n4, n5)

maior = 0
menor = 0

for pos, num in enumerate(tupla):
    if pos == 0:
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f'Os valores sorteados foram {tupla}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
