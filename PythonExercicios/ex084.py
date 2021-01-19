pessoas = []
dados = []
total_pessoas = maior_peso = menor_peso = 0
pessoas_mais_pesadas = []
pessoas_mais_leves = []

while True:
    dados.append(input('Nome: '))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    total_pessoas += 1  

    dados.clear()
    resposta = input('Deseja continuar? [S / N]: ').strip().upper()[0]
    if resposta in 'N':
        break


for pos, pessoa in enumerate(pessoas):
    if pos == 0:
        maior_peso = pessoa[1]
        menor_peso = pessoa[1]
    elif pessoa[1] > maior_peso:
        maior_peso = pessoa[1]
    elif pessoa[1] < menor_peso:
        menor_peso = pessoa[1]

for pessoa in pessoas:
    if pessoa[1] == maior_peso:
        pessoas_mais_pesadas.append(pessoa[0])
    elif pessoa[1] == menor_peso:
        pessoas_mais_leves.append(pessoa[0])

print(f'Ao todo, você cadstrou {total_pessoas} pessoas')
print(f'O maior peso foi {maior_peso}Kg. peso de {pessoas_mais_pesadas}')
print(f'O menor peso foi {menor_peso}Kg. peso de {pessoas_mais_leves}')
