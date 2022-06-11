numeros = list()
pares = list()
impares = list()
numeros.append(pares)
numeros.append(impares)
for c in range(1, 8):
    num = int(input(f'Digite o {c}° Número: '))
    if num % 2 == 0:
        numeros[0].append(num)
        numeros[0].sort()
    else:
        numeros[1].append(num)
        numeros[1].sort()
print('-=' * 40)
print(f'Os valores pares digitados foram {numeros[0]}')
print(f'Os valores ímpares digitados foram {numeros[1]}')
