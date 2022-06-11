numeros = list()
for c in range(0, 5):
    numeros.append(int(input(f"Digite um valor para a posição {c}: ")))
maior = menor = numeros[0]
c1 = list()
c2 = c1[:]
for cont, num in enumerate(numeros):

    if maior < num:
        maior = num
        c1.clear()
    if maior == num:
        c1.append(cont)

    if menor > num:
        menor = num
        c2.clear()
    if menor == num:
        c2.append(cont)

print('=-' * 25)
print(f'Você digitou os valores {numeros}')
print(f'O maior número foi {maior} e ele está nas posições: ', end='')
for n in c1:
    print(f' {n}...', end='')
print()
print(f'O menor número foi {menor} e ele está nas posições: ', end='')
for n in c2:
    print(f' {n}...', end='')
