def leiaDinheiro(txt):
    ok = False
    while True:
        n = input(txt)
        n = n.replace(',', '.')
        if n.isalnum() and n.isdecimal() or n.isnumeric() or isFloat(n):
            if isFloat(n):
                n = float(n)
                ok = True
            elif n.isnumeric():
                n = int(n)
                ok = True
        else:
            print(f'ERRO! {n} não é um preço válido!')
        
        if ok:
            break
    return n

def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
