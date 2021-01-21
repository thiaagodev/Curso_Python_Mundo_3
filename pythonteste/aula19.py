pessoas = {
    'nome': 'Thiago',
    'sexo': 'M',
    'idade': 17
}

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

del pessoas['sexo']
pessoas['idade'] = 18
pessoas['peso'] = 50

for key, value in pessoas.items():
    print(f'{key} = {value}')

brasil = []
estado = {}
for i in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla: ')
    brasil.append(estado.copy())

print(brasil)
#ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #Colocar um dicionário em ordem com sorted