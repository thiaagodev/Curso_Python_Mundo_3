valores = []
count = 0

while True:
    valores.append(int(input('Digite um número: ')))
    count += 1

    resposta = input('Deseja continuar? [S / N]: ').strip().upper()[0]
    while resposta not in 'SN':
        resposta = input('Resposta inválida! Deseja continuar? [S / N]: ').strip().upper()[0]
    if resposta == 'N':
        break

print(f'Foram digitados {count} números')
print('Lista de valores ordenada em decrescente:')
print(sorted(valores, reverse = True))

if 5 in valores:
    print(f'O valor 5 está na lista e foi digitado {valores.count(5)} vezes')
else:
    print('O valor 5 não está na lista')
