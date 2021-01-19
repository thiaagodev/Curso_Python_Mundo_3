expressao = input('Escreva uma expressão: ')

if expressao.count('(') == 0:
    print('Isso não é uma expressão!')
elif expressao.index(')') > expressao.index('('):
    if expressao.count('(') == expressao.count(')'):
        print('Sua expressão é válida!')
    else: 
        print('Sua expressão é inválida!')
else: 
    print('Sua expressão é inválida!')
