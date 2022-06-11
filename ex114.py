import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('\033[31mNão foi possível acessar o site Pudim ~°_°~ !\033[m')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
    # print(site.read())
