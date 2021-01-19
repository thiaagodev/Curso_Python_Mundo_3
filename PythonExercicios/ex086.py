matriz = [[0, 0, 0], [0, 0, 0], [0 , 0, 0 ]]

for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f'Digite um valor na posição [{i}, {c}]: '))

for linha in matriz:
    for valor in linha:
        print(f'[{valor:^5}]', end=' ')
    print()
