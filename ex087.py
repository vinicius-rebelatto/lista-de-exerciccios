matriz = [[], [], []]
somapar = cl2 = 0
for cl in range(0, 3):
    for n in range(0, 3):
        num = int(input(f'Digite um valor para [{cl}, {n}]: '))
        matriz[cl].append(num)
        if num % 2 == 0:
            somapar += num
        if n == 2:
            cl2 += num
print('-=' * 40)
for n, cl in enumerate(matriz):
    for c in matriz[n]:
        print(f'[  {c}  ]', end='')
    print()
print('-=' * 40)
cl1 = max(matriz[1])
print(f'O a soma de todos os números pares é {somapar}.')
print(f'A soma dos valores da terceira coluna é {cl2}')
print(f'O maior valor da segunda fileira é {cl1}')
