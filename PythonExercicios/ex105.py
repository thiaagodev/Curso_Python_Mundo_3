def notas(* notas, sit = False):
    """
        -> Recebe várias notas e mostra o total, a maior e a menor nota e a média da turma
        :param notas: Quantas notas quiser
        :return: Dicionário com as informações da turma
    """
    maior_nota = menor_nota = media_turma = 0
    total = len(notas)
    for pos, nota in enumerate(notas):
        if pos == 0:
            maior_nota = nota
            menor_nota = nota
        if nota > maior_nota:
            maior_nota = nota
        elif nota < menor_nota:
            menor_nota = nota
        media_turma += nota

    media_turma = media_turma / total
    turma = {'total': total, 'maior': maior_nota, 'menor': menor_nota, 'média': media_turma}
    if sit == True:
        if media_turma >= 7:
            turma['situação'] = 'BOA'
        elif media_turma >= 5:
            turma['situação'] = 'RASOAVEL'
        else:
            turma['situação'] = 'RUIM'

    return turma


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
