matriz = [[], [], []]
for cl in range(0, 3):
    for n in range(0, 3):
        num = int(input(f'Digite um valor para [{cl}, {n}]'))
        matriz[cl].append(num)
print('-=' * 40)
for n, cl in enumerate(matriz):
    for c in matriz[n]:
        print(f'[  {c}  ]', end='')
    print()
