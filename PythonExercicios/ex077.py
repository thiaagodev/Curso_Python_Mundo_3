palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar')

for palavra in palavras:
    print(f'Na palavra {palavra} nós temos', end=' ')
    if palavra.lower().count('a'):
        print('a', end=' ')
    if palavra.lower().count('e'):
        print('e', end=' ')
    if palavra.lower().count('i'):
        print('i', end=' ')
    if palavra.lower().count('o'):
        print('o', end=' ')
    if palavra.lower().count('u'):
        print('u', end=' ')
    print('')
