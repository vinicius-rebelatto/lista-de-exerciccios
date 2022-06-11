from liby.interface import *
from liby.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resp == 3:
        title('Saindo do Sistema... Até logo!')
        break
    elif resp == 2:
        title(f'Opção 2')
    elif resp == 1:
        title('PESSOAS CADASTRADAS')
        lerArquivo(arq)
    else:
        print('\033[31mERRO! Digíte uma opção válida!\033[m')
        sleep(2)
