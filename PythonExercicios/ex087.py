matriz = [[], [], []]
valores_pares = valores_terceira_coluna = maior_valor_segunda_linha = 0

matriz[0].append(int((input('Digite um valor para [0, 0]: '))))
matriz[0].append(int((input('Digite um valor para [0, 1]: '))))
matriz[0].append(int((input('Digite um valor para [0, 2]: '))))

matriz[1].append(int((input('Digite um valor para [1, 0]: '))))
matriz[1].append(int((input('Digite um valor para [1, 1]: '))))
matriz[1].append(int((input('Digite um valor para [1, 2]: '))))

matriz[2].append(int((input('Digite um valor para [2, 0]: '))))
matriz[2].append(int((input('Digite um valor para [2, 1]: '))))
matriz[2].append(int((input('Digite um valor para [2, 2]: '))))

print('-='*40)

for linha in matriz:
    for valor in linha:
        print(f'[ {valor} ]', end=' ')
    print()

print('-='*40)

for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            valores_pares += valor

for linha in matriz:
    for pos, valor in enumerate(linha):
        if pos == 2:
            valores_terceira_coluna += valor

for valor in matriz[1]:
    if maior_valor_segunda_linha == 0:
        maior_valor_segunda_linha = valor
    elif valor > maior_valor_segunda_linha:
        maior_valor_segunda_linha = valor

print(f'A soma de todos os valores pares digitados é {valores_pares}')
print(f'A soma dos valores da terceira coluna é {valores_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_valor_segunda_linha}')
