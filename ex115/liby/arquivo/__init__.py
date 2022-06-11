def lin(tam=50):
    print('-' * tam)


def title(msg, n=50):
    lin(n)
    print(msg.center(n))
    lin(n)


def arquivoExiste(txt):
    try:
        a = open(txt, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(txt):
    try:
        a = open(txt, 'wt+')
        a.close()
    except:
        print('Houve algum ERRO de criação')
    else:
        print(f'Arquivo {txt} criado com sucesso!')


def lerArquivo(txt):
    try:
        a = open(txt, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        title('PESSOAS CADASTRADAS')
        print(a.read())
