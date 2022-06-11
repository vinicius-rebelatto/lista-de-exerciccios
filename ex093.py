jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
qtd = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = partidas[:]
for c in range(0, qtd):
    jogador['gols'].append(int(input(f'Quantos gols na partida {c + 1}? ')))
print('-=' * 50)
jogador['total'] = sum(jogador['gols'])
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 50)
print(f'O jogador {jogador["nome"]} jogou {qtd} partidas.')
for e, p in enumerate(jogador['gols']):
    print(f'    => Na partida {e + 1}, fez {p} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
