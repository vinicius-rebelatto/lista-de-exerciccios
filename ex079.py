numeros = []
while True:
    num = int(input("Digite um número: "))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    cont = input('Deseja continuar? [S/N]: ').upper()
    while cont not in 'SN':
        cont = input('Código ivalido! Deseja continuar? [S/N]: ').upper()
    if cont == 'N':
        break
print('-=' * 40)
numeros.sort()
print(f'Você digitou os números {numeros}')
