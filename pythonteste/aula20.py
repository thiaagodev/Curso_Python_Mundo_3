def contador(* num):
    print(len(num))


contador(1, 2, 8, 6, 7)
contador(2, 5, 86)
 
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1 

valores = [1, 5, 2, 8, 69]
dobra(valores)
print(valores)

def soma(* num):
    s = 0
    for valor in num:
        s += valor
    return s


print(soma(2, 2, 2))
print(soma(3, 3, 3, 5))
