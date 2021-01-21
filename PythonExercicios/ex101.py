from datetime import date

def voto(ano_nasc):
    """
        Recebe o ano de nascimento e retorna se uma pessoa pode ou não votar
        :param ano_nasc -> ano de nascimento
    """
    idade = date.today().year - ano_nasc
    if idade >= 65 or idade == 16 or idade == 17:
        return 'voto opcional!'
    elif idade >= 18:
        return 'o voto é obrigatório!'
    elif idade < 18:
        return 'ainda não pode votar!'


ano_nasc = int(input('Em que ano você nasceu? '))
print(f'Com {date.today().year - ano_nasc} anos: {voto(ano_nasc)}')
