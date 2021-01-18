valores = []

for i in range(0, 5):
    valores.append(int(input(f'Digite o {i + 1}° valor: ')))

print(f'O maior valor foi {max(valores)} e está nas posições ', end='')
if valores.count(max(valores)) > 1: 
    for pos, valor in enumerate(valores):
        if valor == max(valores):
            print(pos, end='... ')
else:
    print(valores.index(max(valores)), end='... ')

print(f'\nO menor valor foi {min(valores)} e está nas posições ', end='')
if valores.count(max(valores)) > 1:   
    for pos, valor in enumerate(valores):
        if valor == min(valores):
            print(pos, end='... ')
else: 
    print(valores.index(min(valores)), end='... ')
