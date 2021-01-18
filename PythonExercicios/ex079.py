valores = []

while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Valor duplicado! Tente novamente.')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    
    resposta = input('Quer continuar? [S / N]: ').strip().upper()[0]
    while resposta not in 'SN':
        resposta = input('Resposta inválida! Deseja continuar? [S / N]: ').strip().upper()[0]

    if resposta in 'N':
        break

print('='*40)
print(f'Você digitou os valores {sorted(valores)}')
