numeros = []
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)

    cont = input("Deseja continuar? [S/N]: ").upper()
    while cont not in 'SN':
        cont = input("Opção inválida! Deseja continuar? [S/N]: ").upper()
    if cont == 'N':
        break
print('-=' * 40)
print(f'A lista com os números digitados ficou {numeros}')

par = []
imp = []

for n in numeros:
    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)
print(f'Os números pares digitados foram: {par}')
print(f'Os números Ímpares digitados foram: {imp}')
