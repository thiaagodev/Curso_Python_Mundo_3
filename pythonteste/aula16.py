lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#Tuplas são imutáveis
# lanche[1] = 'Refrigerante'

for comida in lanche:
    print(f'Eu vou comer {comida}')


for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')  


print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b 

print(c.count(5))
print(c.index(8))

pessoa = ('Gustavo', 39, 'Masculino', 99.88)
del(pessoa)
