def leiaDinheiro(val):
    while True:
        number = input(val).replace(',', '.')
        res = des = ''
        if '.' in number or ',' in number:
            for en, el in enumerate(number):
                if el in '.,':
                    des = number[en + 1:]
                    res = number[:en]
            if des.isnumeric() and res.isnumeric():
                return float(number)
        elif number.isnumeric():
            return float(number)
        else:
            print(f'\033[1;31mERRO: "{number}" é um preço inválido!\033[m')
    # valido = False
    # while not valido:
    #     entrada = input(val).replace(',', '.').strip()
    #     if entrada.isalpha():
    #         print(f'\033[1;31mERRO: "{n}" é um preço inválido!\033[m')
    #     else:
    #         valido = True
    #         return float(entrada)


def leiaInt(numero):
    print('-' * 20)
    while True:
        n = str(input(numero))
        if n.isnumeric():
            return int(n)
        print('\033[31m ERRO! Digite um número inteiro válido. \033[m')


# n = leiaInt('Digite um numero: ')
# print(f"Voce acabou de digitar o número {n}.")

