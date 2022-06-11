time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    qtd = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = partidas[:]
    for c in range(0, qtd):
        jogador['gols'].append(int(input(f'    Quantos gols na partida {c + 1}? ')))
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())
    while True:
        cont = str(input('Deseja continuar? [S/N]: ')).upper()
        if cont in 'SN':
            break
        print('Opção inválida!')
    if cont == 'N':
        break
print('-=' * 40)
print('Cod  ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for e, jog in enumerate(time):
    print(f'  {e:<3}', end='')
    for v in jog.values():
        print(f'{str(v):<15}', end='')
    print()
print('-' * 40)
while True:
    num = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if num == 999:
        break
    elif num >= len(time) or num < 0:
        print(f'ERRO! Não existe jogador com código {num}')
    else:
        print(f' -- Levantamento do jogador {time[num]["nome"]}:')
        for e, g in enumerate(time[num]['gols']):
            print(f'    No jogo {e + 1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
