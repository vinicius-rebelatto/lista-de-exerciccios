def dobro(n=0, form=False):
    res = n * 2
    return res if form is False else moeda(res)


def metade(n=0, form=False):
    res = n / 2
    return res if form is False else moeda(res)


def aumento(n=0, a=0, form=False):
    res = n + (n / 100 * a)
    return res if form is False else moeda(res)


def redução(n, r=0, form=False):
    res = n - (n / 100 * r)
    return res if form is False else moeda(res)


def moeda(n, cifrão='R$'):
    return f'{cifrão}{n:.2f}'.replace('.', ',')
