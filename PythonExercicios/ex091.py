from random import randint
from time import sleep

jogador1 = {'nome': 'jogador1', 'jogada': randint(1, 6)}
jogador2 = {'nome': 'jogador2', 'jogada': randint(1, 6)}
jogador3 = {'nome': 'jogador3', 'jogada': randint(1, 6)}
jogador4 = {'nome': 'jogador4', 'jogada': randint(1, 6)}
jogadores = [jogador1, jogador2, jogador3, jogador4]
jogadas = []

print('Valores sorteados: ')

for jogador in jogadores:
    print(f'   O {jogador["nome"]} tirou {jogador["jogada"]}')
    jogadas.append(jogador['jogada'])
    sleep(1)

jogadas.sort(reverse = True)

for jogador in jogadores:
    if jogador['jogada'] == jogadas[0]:
        print(f'1° lugar: {jogador["nome"]} com {jogador["jogada"]}')
        break
sleep(1)

for jogador in jogadores:
    if jogador['jogada'] == jogadas[1]:
        print(f'2° lugar: {jogador["nome"]} com {jogador["jogada"]}')
        break
sleep(1)

for jogador in jogadores:
    if jogador['jogada'] == jogadas[2]:
        print(f'3° lugar: {jogador["nome"]} com {jogador["jogada"]}')
        break
sleep(1)

for jogador in jogadores:
    if jogador['jogada'] == jogadas[3]:
        print(f'4° lugar: {jogador["nome"]} com {jogador["jogada"]}')
        break
sleep(1)

