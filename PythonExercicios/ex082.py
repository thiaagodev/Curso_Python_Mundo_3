valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um número: ')))

    resposta = input('Deseja continuar? [S / N]: ').strip().upper()[0]
    while resposta not in 'SN':
        resposta = input('Resposta inválida! Deseja continuar? [S / N]: ').strip().upper()[0]
    if resposta == 'N':
        break

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(f'Lista: {valores}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')
