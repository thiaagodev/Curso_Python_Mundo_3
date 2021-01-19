from random import randint
from time import sleep

print('-'*30)
print('JOGO MEGA SENA'.center(30))
print('-'*30)

jogos = []
qtd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

for i in range(0, qtd_jogos):
    jogo = []
    while len(jogo) != 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogos.append(jogo[:])
    jogo.clear()

print(f'-=-=-= SORTEANDO {qtd_jogos} JOGOS -=-=-=')
sleep(1)

for pos, jogo in enumerate(jogos):
    jogo.sort()
    print(f'Jogo {pos + 1}: {jogo}')
    sleep(0.5)

print('-=-=-=-=-= < BOA SORTE > -=-=-=-=-=')
