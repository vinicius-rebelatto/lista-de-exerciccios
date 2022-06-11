numeros = []
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0 or num > numeros[-1]:
        numeros.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f'Adicionando na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 35)
print(f'Os números em ordem crescente ficam {numeros}')
