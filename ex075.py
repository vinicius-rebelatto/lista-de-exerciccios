n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número '))
n4 = int(input('Digite o ultimo número: '))
numeros = (n1, n2, n3, n4)

print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
c = 0
for num in numeros:
    if num % 2 == 0:
        c += 1
if c != 0:
    print(f'Foram digitado ao todo {c} números pares')
else:
    print('Não foi digitado nenhum valor par.')
