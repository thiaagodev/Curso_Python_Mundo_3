def maior(* valores):
    maior = 0
    count = 0
    for pos, valor in enumerate(valores):
        if pos == 0:
            maior = valor
        if valor > maior:
            maior = valor
        print(valor, end=' ')
        count += 1

    print(f'Foram informados {count} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

print('-='*30)
print('Analisando os valores passados...')
maior(2, 9, 4, 5, 7, 1)
print('-='*30)
