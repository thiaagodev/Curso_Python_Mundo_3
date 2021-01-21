print('SISTEMA DE AJUDA PyHELP')
print('-='*30)
while True:
    resp = input('Função ou Biblioteca > ')
    if resp.upper() == 'FIM':
        print('Até Logo!')
        break
    print(help(resp))

