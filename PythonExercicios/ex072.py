numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
            'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
            'Doze', 'Treze', 'Quatorze', 'Quinze',
            'Dezesseis', 'Dezessete', 'Dezoito',
            'Dezenove', 'Vinte')

num = -1
num = int(input('Digite um número de 0 a 10 que vou te mostrar em extenso: '))
while num < 0 or num > 20:
    num = int(input('Tente novamente. Digite um número de 0 a 10 que vou te mostrar em extenso: '))

if num >= 0 and num <= 20:
    print(numeros[num])
