times = ('Flamengo', 'Internacional', 'Atlético-MG',
         'São Paulo', 'Fluminense', 'Gremio', 'Palmeiras',
         'Santos', 'Athletico-PR', 'Chapecoense', 'Ceará SC',
         'Corinthians', 'Athletico-GO', 'Bahia', 'Sport Recife',
         'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba',
         'Botafogo')

print('=' * 40)
print('Os 5 melhores times do Brasileirão são:')
print('-' * 40)
for c in range(0, 5):
    print(f'Em {c + 1} lugar está o {times[c]}')

print('=' * 40)
print('Os ultimos 4 colocados são:')
print('-' * 40)

for c in range(16, len(times)):
    print(f'Em {c + 1} lugar está o {times[c]}')

print('=' * 40)
print('Os times em ordem alfabética fica : ')
print('-' * 40)

for c in sorted(times):
    print(f'{c}')

print('=' * 50)
print(f'O time da chapecoense se encontra na {times.index("Chapecoense") + 1}° posição')
