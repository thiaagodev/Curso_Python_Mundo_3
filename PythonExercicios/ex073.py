tabela_brasileirao = ('São Paulo', 'Atlético-MG', 'Internacional', 'Grêmio', 'Flamengo', 'Palmeiras', 'Fluminense', 'Santos', 'Corinthians', 'Athletico-PR', 'Ceará', 'Atlético-GO', 'Bragantino', 'Sport', 'Vasco', 'Fortaleza', 'Bahia', 'Goiás', 'Dezoito', 'Coritiba', 'Botafogo')

print(f'Os 5 primeiros colocados: {tabela_brasileirao[:5]}')
print('='*30)
print(f'Últimos 4 colocados: {tabela_brasileirao[-4:]}')
print('='*30)
print(f'Lista dos times em ordem alfabética: {sorted(tabela_brasileirao)}')
print('='*30)
print(f'O Atlético-GO está na posição {tabela_brasileirao.index("Atlético-GO") + 1}')
print('='*30)
