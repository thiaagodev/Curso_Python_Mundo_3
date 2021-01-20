def escreva(txt):
    print('-'* (len(txt) + 8))
    print(txt.center((len(txt) + 8)))
    print('-'* (len(txt) + 8))


escreva(input('Digite uma frase qualquer: '))
