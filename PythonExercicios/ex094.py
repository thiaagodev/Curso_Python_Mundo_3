pessoas = []
mulheres = []
pessoas_com_idade_acima_da_media = []
total_idade = pessoas_cadastradas = 0

while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo: [M/F] ').strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))

    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    
    total_idade += pessoa['idade']
    pessoas_cadastradas += 1
    pessoas.append(pessoa.copy())

    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp in 'N':
        break

print('-='*40)

media_idade = total_idade / pessoas_cadastradas

for pessoa in pessoas:
    if pessoa['idade']  > media_idade:
        pessoas_com_idade_acima_da_media.append(pessoa.copy())

print(f'-- O grupo tem {pessoas_cadastradas} pessoas.')
print(f'-- A média de idade é de {media_idade} anos.')
print(f'-- As mulheres cadastradas foram: {mulheres}.')
print(f'-- Lista das pessoas com idade acima da média:  ')

for pessoa in pessoas_com_idade_acima_da_media:
    for key, value in pessoa.items():
        print(f'{key} = {value}', end='; ')
    print()
