numeros = []
c = 0
while True:

    num = int(input("Digite um número: "))
    numeros.append(num)
    c += 1

    cont = input('Deseja continuar? [S/N]: ').upper()
    while cont not in 'SN':
        cont = input('Opção inválida! Deseja continuar? [S/N]: ').upper()
    if cont == 'N':
        break

print('-=' * 40)

numeros.sort(reverse=True)
print(f'Ao todo foram digitados {c} números')

print(f'Os números na forma decrescente ficam {numeros}')

if 5 in numeros:
    print(f'O número 5 faz parte da lista!')
else:
    print('O número 5 não está presente na lista!')
