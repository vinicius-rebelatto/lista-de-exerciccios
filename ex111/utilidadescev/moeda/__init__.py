def dobro(n=0, form=False):
    res = n * 2
    return res if form is False else moeda(res)


def metade(n=0, form=False):
    res = n / 2
    return res if form is False else moeda(res)


def aumento(n=0, a=0, form=False):
    res = n + (n / 100 * a)
    return res if form is False else moeda(res)


def redução(n=0, r=0, form=False):
    res = n - (n / 100 * r)
    return res if form is False else moeda(res)


def moeda(n=0, cifrão='R$'):
    return f'{cifrão}{n:.2f}'.replace('.', ',')


def resumo(n=0, a=10, r=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analizado: \t{moeda(n)}')
    print(f'Dobro do Preço: \t{dobro(n, True)}')
    print(f'Metade do Preço: \t{metade(n, True)}')
    print(f'{a}% de aumento: \t{aumento(n, a, True)}')
    print(f'{r}% de redução: \t{redução(n, r, True)}')
    print('-' * 30)
