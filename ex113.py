def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31m ERRO! Digite um número inteiro válido. \033[m')
            continue
        else:
            return num


def leia_Float(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31m ERRO! Digite um número real válido. \033[m')
            continue
        else:
            return num


numInt = leiaInt('Digite um Inteiro: ')
numFloat = leia_Float('Digite um Real: ')
print(f'O valor inteiro foi {numInt} e o valor real foi {numFloat}')
