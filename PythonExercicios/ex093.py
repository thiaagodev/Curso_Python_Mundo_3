jogador = {}
gols = []
total_gols = partidas = 0

jogador['nome'] = input('Nome: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(0, partidas):
    gols_marcados = int(input(f'Quantos gols na partida {i + 1}? '))
    gols.append(gols_marcados)
    total_gols += gols_marcados

jogador['gols'] = gols[:]
jogador['total'] = total_gols

print('-='*50)
print(jogador)
print('-='*50)

for key, value in jogador.items():
    print(f'O campo {key} tem o valor {value}')

print('-='*50)
print(f'O jogador {jogador["nome"]} jogou {partidas} jogos')
for pos, partida in enumerate(gols):
    print(f'=> na partida {pos + 1}, fez {partida} gols')
    
print(f'Foi um total de {jogador["total"]} gols')