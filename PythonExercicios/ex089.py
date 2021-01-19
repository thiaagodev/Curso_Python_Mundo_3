alunos = []

while True:
    pessoa = []
    nota = []
    pessoa.append(input('Nome: '))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))

    pessoa.append(nota[:])
    alunos.append(pessoa[:])
    pessoa.clear()
    nota.clear()

    resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if resp in 'N':
        break

print('-='*40)
print('No. NOME       MÉDIA')
print('-'*20)
for pos, aluno in enumerate(alunos):
    print(pos, end='   ')
    print(aluno[0], end='     ')
    print(f'  {(aluno[1][0] + aluno[1][1]) / 2:4>}')

num_aluno = -1
while num_aluno != 999:
    num_aluno = int(input('Mostrar as notas de que aluno? (999 interrompe): '))
    if num_aluno > len(alunos) - 1:
        print('Esse aluno não existe!')
    else:
        print(f'As notas de {alunos[num_aluno][0]} são {alunos[num_aluno][1]}')
