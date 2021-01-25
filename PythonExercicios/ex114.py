import urllib.request

try:
    url = urllib.request.urlopen('http://pudim.com.br/')
    x = url.read()
except Exception as error:
    print('Não consegui acessar o site do Pudim!')
else:
    print('Consegui acessar o site do Pudim!')
