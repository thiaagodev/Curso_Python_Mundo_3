from datetime import date

pessoa = {}

pessoa['nome'] = input('Nome: ')
pessoa['ano_nasc'] = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - pessoa['ano_nasc']
carteira = int(input('Carteira de trabalho (0 não tem): '))
if carteira != 0:
    pessoa['carteira'] = carteira
    pessoa['ano_contratacao'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: '))
    pessoa['aposentadoria'] =  (pessoa['ano_contratacao'] + pessoa['idade'] + 35) - date.today().year

print('-'*40)

for key, value in pessoa.items():
    print(f'{key} tem o valor {value}')
