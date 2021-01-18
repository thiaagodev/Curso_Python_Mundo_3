valores = []

for i in range(0, 5):
    num = int(input(f'Digite o {i + 1}° valor: '))

    if i == 0:
        valores.append(num)
        print(f'{num} adicionado ao final da lista!')
    elif num > max(valores):
        valores.append(num)
        print(f'{num} adicionado ao final da lista!')
    elif num < min(valores):
        valores.insert(0, num)
        print(f'{num} adicionado na posição 0!')
    else:
        for pos, valor in enumerate(valores):
            if num < valor:
                valores.insert(pos, num)
                print(f'{num} adicionado na posição {pos}!')
                break

print(valores)
