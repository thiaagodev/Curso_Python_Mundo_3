produtos = ('Pão', 1, 'Frango', 10.90, 'Batata', 5.80, 'Peixe', 12, 'Carne', 49)

print('-'*52)
print('LISTAGEM DE PREÇOS'.center(52))
print('-'*52)

for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:.<40}R$   {produtos[i + 1]:>7.2f}')


print('-'*52)
