num = [2, 5, 9, 1]
num[2] = 3 
num.append(7)
num.sort(reverse = True)
num.insert(2, 0)
num.pop(2)
num.insert(2, 2)
num.remove(2)

print(num)

print(f'Essa lista tem {len(num)} elementos')

valores = []

for count in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for pos, valor in enumerate(valores):
    print(f'Na posição {pos} tem o valor {valor}!')
print('Final da lista')

a = [2, 3, 4, 7]
#b = a cria uma ligação entre as listas
b = a[:] # cria uma cópia da lista a

b[2] = 8

print(a)
print(b)
