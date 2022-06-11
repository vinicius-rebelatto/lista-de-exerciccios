from random import randint
print('-' * 50)
print('{:^40}'.format('JOGA NA MEGA SENA'))
print('-' * 50)

geral = list()
mega = list()
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
c = 0

for jogo in range(0, qtd):
    while True:
        num = randint(0, 60)
        if num not in geral:
            geral.append(num)
            c += 1
        if c >= 6:
            break
    mega.append(geral[:])
    geral.clear()
    c = 0

print('{:-^50}'.format(f' SORTEANDO {qtd} JOGOS '))
for n, jogo in enumerate(mega):
    print(f'Jogo {n + 1}: {jogo}')
print('{:-^50}'.format('<  BOA SORTE  >'))
