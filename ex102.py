def fatorial(n, show):
    """
    -> Calcula um fatorial de um número.
    :param n: Número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    print('-' * 20)
    soma = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        soma *= c
    return soma


cod = input("Deseja mostrar o código completo? [T = True / F = False]").upper()
if cod == 'T':
    cod = True
else:
    cod = False

print(fatorial(5, show=cod))
# help(fatorial)
