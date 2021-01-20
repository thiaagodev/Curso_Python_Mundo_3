aluno = {}
aluno['nome'] = input('Nome: ').strip().title()
aluno['media'] = float(input('Média: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif aluno['media'] >=5 and aluno['media'] < 7:
    aluno['situacao'] = 'RECUPERAÇÃO'
else:
    aluno['situacao'] = 'REPROVADO'

print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["situacao"]}')
