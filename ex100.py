from random import randint
from time import sleep


def sorteio(lst):
    lst.clear()
    print('Sorteando os valores da lista: ', end='')
    for c in range(0, 5):
        num = randint(0, 10)
        lst.append(num)
        print(f'{num} ', end='')
        sleep(0.2)
    print('PRONTO!')


def somapar(lst):
    soma = 0
    for num in lst:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {lst}, temos {soma}')


def bahh():
    lista = list()
    sorteio(lista)
    somapar(lista)


bahh()
bahh()
bahh()
