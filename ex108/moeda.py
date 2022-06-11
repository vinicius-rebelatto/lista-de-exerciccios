def dobro(n=0):
    return n * 2


def metade(n=0):
    return n / 2


def aumento(n=0, a=0):
    soma = (n / 100) * a
    return n + soma


def redução(n, r=0):
    sub = (n / 100) * r
    return n - sub


def moeda(n, cifrão='R$'):
    return f'{cifrão}{n:.2f}'.replace('.', ',')
