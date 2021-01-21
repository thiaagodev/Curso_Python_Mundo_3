def ficha(nome = '<desconhecido>', gols = 0):
    """
        -> Recebe o nome de um jogador e seus gols marcados e mostra a ficha 
        :param nome: Nome do jogador
        :param gols: Número de gols marcados
        :return: Ficha do jogador
    """
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


nome = input('Nome do jogador: ')
gols = input('Número de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    print(ficha(gols=gols))
else:
   print(ficha(nome, gols))