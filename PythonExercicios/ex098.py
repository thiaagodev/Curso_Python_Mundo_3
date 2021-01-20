from time import sleep

def contador(inicio, fim, passo = 1):
    if inicio > fim and passo > 0:
        passo = -passo
    elif inicio > fim and passo == 0:
        passo = -1
    
    for i in range(inicio, fim, passo):
        print(i, end=' ', flush=True)
        sleep(0.5)
    print('FIM!')


print('-='*30)
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 11, 1)
print('-='*30)

print('Contagem de 10 até 0 de 2 em 2')
contador(10, -1, -2)
print('-='*30)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

print('-='*30)
print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
contador(inicio, fim, passo)
print('-='*30)
