produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.9)

print('-' * 40)
print('{:^40}'.format('Listagem de produtos'))
print('-' * 40)

n1 = 1

for item in produtos:
    if n1 % 2 != 0:
        print(f'{item:.<30}', end='')
    else:
        print(f'R${item:>7.2f}')
    n1 += 1
print('-' * 40)
