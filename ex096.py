def area(l, c):
    ar = l * c
    print(f'A área de um terreno {l}x{c} é de {ar}m².')


print('   Controle de terrenos')
print('-' * 30)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)
