jogadores = []

while True:
    jogador = {}
    gols = []
    total_gols = partidas = 0

    jogador['nome'] = input('Nome: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for i in range(0, partidas):
        gols_marcados = int(input(f'Quantos gols na partida {i + 1}? '))
        gols.append(gols_marcados)
        total_gols += gols_marcados

    jogador['gols'] = gols
    jogador['total'] = total_gols

    jogadores.append(jogador.copy())

    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp in 'N':
        break

print('-='*40)
print('cod  nome                   gols    total')
print('-='*30)

for pos, jogador in enumerate(jogadores):
    print(f'{pos:>3}', end=' ')
    print(f'{jogador["nome"]:<25}', end=' ')
    print(f'{jogador["gols"]}', end='')
    print(f'{jogador["total"]:>20}', end=' ')
    print()

cod_jogador = -1

while cod_jogador != 999:
    cod_jogador = int(input('Deseja ver as informações de qual jogador? (999 encerra o programa): '))
    if cod_jogador > len(jogadores) - 1:
        print('Esse jogador não existe!')
    else:
        for pos, gols in enumerate(jogadores[cod_jogador]['gols']):
            print(f'Na {pos + 1}° partida ele marcou {gols} gols')
