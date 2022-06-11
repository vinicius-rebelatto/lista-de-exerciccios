def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31m ERRO! Digite um número inteiro válido. \033[m')
            continue
        else:
            return num


def lin(tam=50):
    print('-' * tam)


def title(msg, n=50):
    lin(n)
    print(msg.center(n))
    lin(n)


def menu(lst):
    while True:
        title('MENU PRINCIPAL')
        for e, op in enumerate(lst):
            print(f'\033[33m{e + 1} - \033[34m{op}\033[m')
        lin(50)
        cont = leiaInt('\033[33mSua opção: \033[m')
        return cont
