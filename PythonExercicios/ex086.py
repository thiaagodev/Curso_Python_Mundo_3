matriz = [[], [], []]

matriz[0].append((input('Digite um valor para [0, 0]: ')))
matriz[0].append((input('Digite um valor para [0, 1]: ')))
matriz[0].append((input('Digite um valor para [0, 2]: ')))

matriz[1].append((input('Digite um valor para [1, 0]: ')))
matriz[1].append((input('Digite um valor para [1, 1]: ')))
matriz[1].append((input('Digite um valor para [1, 2]: ')))

matriz[2].append((input('Digite um valor para [2, 0]: ')))
matriz[2].append((input('Digite um valor para [2, 1]: ')))
matriz[2].append((input('Digite um valor para [2, 2]: ')))

for linha in matriz:
    for valor in linha:
        print(f'[ {valor} ]', end=' ')
    print()
