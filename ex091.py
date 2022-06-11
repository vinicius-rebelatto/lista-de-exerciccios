from random import randint
from time import sleep
from operator import itemgetter
dados = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for j, v in dados.items():
    print('{:>22}'.format(f'O {j} tirou {v}'))
    sleep(1)
print('Ranking dos jogadores: ')
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for e, j in enumerate(ranking):
    print('{:>30}'.format(f'{e + 1}° lugar: {j[0]} tirou {j[1]}'))
    sleep(1)
