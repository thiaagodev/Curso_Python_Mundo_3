matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
valores_pares = valores_terceira_coluna = maior_valor_segunda_linha = 0

for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f'Digite um valor na posição [{i}, {c}]: '))

print('-='*40)

for linha in matriz:
    for valor in linha:
        print(f'[ {valor:^5} ]', end=' ')
        if valor % 2 == 0:
            valores_pares += valor
    print()

print('-='*40)

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
