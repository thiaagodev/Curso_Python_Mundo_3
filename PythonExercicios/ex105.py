def notas(* notas, sit = False):
    """
        -> Recebe várias notas e mostra o total, a maior e a menor nota e a média da turma
        :param notas: Quantas notas quiser
        :return: Dicionário com as informações da turma
    """
    turma = {}
    turma['total'] = len(notas)
    turma['maior'] = max(notas)
    turma['menor'] = min(notas)
    turma['média'] = sum(notas) / len(notas)

    if sit == True:
        if turma['média']  >= 7:
            turma['situação'] = 'BOA'
        elif turma['média']  >= 5:
            turma['situação'] = 'RAZOÁVEL'
        else:
            turma['situação'] = 'RUIM'

    return turma


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
