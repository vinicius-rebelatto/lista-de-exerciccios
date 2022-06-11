from time import sleep
c = ('\033[m',          # 0 - Sem cores
     '\033[0;30;41m',   # 1 - Vermelho
     '\033[0;30;42m',   # 2 - Verde
     '\033[0;30;43m',   # 3 - Amarelo
     '\033[0;30;44m',   # 4 - Azul
     '\033[0;30;45m',   # 5 - Roxo
     '\033[7m'       # 6 - Branco
     )


def ajuda(cmd):
    texto(f'Acessando o manual de comando \'{cmd}\'', 4)
    print(c[6], end='')
    help(cmd)
    sleep(1.5)
    print(c[0], end='')


def texto(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    sleep(1.5)
    print(c[0], end='')


while True:
    texto('SISTEMA DE AJUDA PyHELP', 3)
    comando = str(input('Função ou biblioteca > ')).lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)
texto('Volte logo!', 2)


# def ajuda():
#     while True:
#         print('\033[m\033[1;41m~' * 50)
#         print('{:^50}'.format('SISTEMA DE AJUDA HELP'))
#         print('~' * 50)
#         funcao = str(input('\033[mFunção ou Biblioteca> ')).strip().lower()
#         if funcao == 'fim':
#             break
#         print('\033[1;45m~' * 50)
#         print(f"Acessando o manual de comando '{funcao}'")
#         print('~' * 50)
#         print(f'\033[;7m')
#         help(funcao)
#     print('\033[1;100m~' * 50)
#     print('{:^50}'.format('VOLTE LOGO!'))
#     print('~' * 50)
#
#
# ajuda()
