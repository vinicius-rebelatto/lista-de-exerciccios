from ex107 import moeda

num = float(input('Digíte um número: '))
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'Aumentando 10%, temos {moeda.aumento(num, 10)}')
print(f'Diminuindo 13%, temos {moeda.redução(num, 13)}')
