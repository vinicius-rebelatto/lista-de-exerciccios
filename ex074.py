from random import randint

while True:
    numeros = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
    print(f'a tupla criada é: {numeros}')
    menor = min(numeros)
    maior = max(numeros)
    print(f'O menor valor sorteado foi {menor}')
    print(f'O maior valor sorteado foi {maior}')
    cont = input('Deseja criar uma nova tupla [S/N]: ')
    print('-' * 40)
    while cont not in 'snSN':
        cont = input('Digite um código válido. Deseja criar uma nova tupla [S/N]: ')
        print('-'*40)

    if cont in 'nN':
        break
