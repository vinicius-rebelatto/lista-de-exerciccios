media = list()
aluno = list()
classe = list()
while True:
    aluno.append(str(input('Nome: ')))
    media.append(float(input('Nota 1: ')))
    media.append(float(input('Nota 2: ')))
    aluno.append(media[:])
    classe.append(aluno[:])
    aluno.clear()
    media.clear()
    while True:
        cont = str(input('Deseja continuar. [S/N]: ')).upper()
        if cont in 'SN':
            break
        print('Opção inválida! ', end='')
    if cont == 'N':
        break
print('-=' * 40)
print('{:<5}'.format('No.'), end='')
print('{:<14}'.format('NOME'), end='')
print('MÉDIA')
print('-' * 35)
for en, est in enumerate(classe):
    med = sum(est[1]) / 2
    print('{:<5}'.format(en), end='')
    print('{:<17}'.format(est[0]), end='')
    print(med)
print('-' * 35)
while True:
    nota = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if nota == 999:
        break
    elif nota >= len(classe):
        print('Opção inválida! ', end='')
    else:
        est = classe[nota]
        print(f'Notas de {est[0]} são: {est[1]}')
        print('-' * 35)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')


# aluno = list()
# classe = list()
# while True:
#     aluno.append(str(input('Nome: ')))
#     aluno.append(float(input('Nota 1: ')))
#     aluno.append(float(input('Nota 2: ')))
#     classe.append(aluno[:])
#     aluno.clear()
#     while True:
#         cont = str(input('Deseja continuar. [S/N]: ')).upper()
#         if cont in 'SN':
#             break
#         print('Opção inválida! ', end='')
#     if cont == 'N':
#         break
# print('-=' * 40)
# print('{:<5}'.format('No.'), end='')
# print('{:<14}'.format('NOME'), end='')
# print('MÉDIA')
# print('-' * 35)
# for en, est in enumerate(classe):
#     media = (est[1] + est[2]) / 2
#     print('{:<5}'.format(en), end='')
#     print('{:<17}'.format(est[0]), end='')
#     print(media)
# print('-' * 35)
# while True:
#     nota = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
#     if nota == 999:
#         break
#     elif nota >= len(classe):
#         print('Opção inválida! ', end='')
#     else:
#         est = classe[nota]
#         print(f'Notas de {est[0]} são: [{est[1]}, {est[2]}]')
#         print('-' * 35)
# print('FINALIZANDO...')
# print('<<< VOLTE SEMPRE >>>')
