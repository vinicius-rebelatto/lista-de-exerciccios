def ficha(n='<DESCONHECIDO>', g=0):
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


print('-' * 20)
nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)

