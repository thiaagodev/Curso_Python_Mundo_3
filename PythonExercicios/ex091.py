from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
ranking = {}

print('Valores sorteados: ')

for key, value in jogo.items():
    print(f'{key} tirou {value} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('RANKING'.center(30))
for i, value in enumerate(ranking):
    print(f'{i + 1}° lugar: {value[0]} com {value[1]}')
    sleep(0.5)
