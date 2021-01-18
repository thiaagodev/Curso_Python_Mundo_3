tupla = (int(input('Digite um número: ')), int(input('Digite outro: ')), int(input('Digite outro: ')), int(input('Digite outro: ')))

print(f'O número 9 apareceu {tupla.count(9)} vezes')

if(tupla.count(3)):
    print(f'O valor 3 foi digitado pela primeira vez na posição {tupla.index(3)}')
else:
    print('O número 3 não foi digitado')

print('Números pares: ', end='')

for num in tupla:
    if num % 2 == 0:
        print(num, end=' ')
