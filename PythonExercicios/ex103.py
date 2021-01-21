def ficha(nome = '<desconhecido>', gols = 0):
    """
        -> Recebe o nome de um jogador e seus gols marcados e mostra a ficha 
        :param nome: Nome do jogador
        :param gols: Número de gols marcados
        :return: Ficha do jogador
    """
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


nome = input('Nome do jogador: ').strip()
gols = input('Número de gols: ')
if nome != '' and gols != '':
    print(ficha(nome, int(gols)))
elif nome == '' and gols == '':
    print(ficha())
elif nome == '':
    print(ficha(gols=int(gols)))
elif gols == '':
    print(ficha(nome=nome))
