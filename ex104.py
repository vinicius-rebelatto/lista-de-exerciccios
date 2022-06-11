def leiaInt(numero):
    print('-' * 20)
    while True:
        n = str(input(numero))
        if n.isnumeric():
            return int(n)
        print('\033[31m ERRO! Digite um número inteiro válido. \033[m')


n = leiaInt('Digite um numero: ')
print(f"Voce acabou de digitar o número {n}.")
