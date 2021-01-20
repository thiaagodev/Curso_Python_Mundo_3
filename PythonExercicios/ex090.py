aluno = {}
aluno['nome'] = input('Nome: ').strip().title()
aluno['media'] = float(input('Média: '))

if aluno['media'] < 7:
    aluno['situacao'] = 'REPROVADO'
else:
    aluno['situacao'] = 'APROVADO'

print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["situacao"]}')
