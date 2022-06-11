pess = list()
galera = list()
while True:
    pess.append(str(input('Nome: ')))
    pess.append(float(input('Peso: ')))
    galera.append(pess[:])
    pess.clear()
    while True:
        cont = str(input('Deseja continuar? [S/N]: ')).upper()
        if cont in 'SN':
            break
        print('Opção inválida! ', end='')
    if cont == 'N':
        break
print(f'Ao todo, você cadastrou {len(galera)} pessoas.')
mai = men = 0
for e, p in enumerate(galera):
    if e == 0:
        mai = men = p[1]
    elif mai < p[1]:
        mai = p[1]
    elif men > p[1]:
        men = p[1]
print(f'O maior peso foi de {mai:.2f}. Peso de ', end='')
for p in galera:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {men:.2f}. Peso de ', end='')
for p in galera:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
