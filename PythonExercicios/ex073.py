tabela_brasileirao = ('São Paulo', 'Atlético-MG', 'Internacional', 'Grêmio', 'Flamengo', 'Palmeiras', 'Fluminense', 'Santos', 'Corinthians', 'Athletico-PR', 'Ceará', 'Atlético-GO', 'Bragantino', 'Sport', 'Vasco', 'Fortaleza', 'Bahia', 'Goiás', 'Dezoito', 'Coritiba', 'Botafogo')

print(f'Os 5 primeiros colocados: {tabela_brasileirao[:5]}')
print(f'Últimos 4 colocados: {tabela_brasileirao[-1], tabela_brasileirao[-2], tabela_brasileirao[-3], tabela_brasileirao[-4]}')
print(f'Lista dos times em ordem alfabética:')
print(sorted(tabela_brasileirao))
print(f'O Atlético-GO está na posição {tabela_brasileirao.index("Atlético-GO") + 1}')
