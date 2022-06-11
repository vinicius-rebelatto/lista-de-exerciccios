galera = list()
pessoa = dict()
soma = media = f = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo: [M/F] ')).upper()
        if sexo in 'MF':
            break
        print('ERRO! por favor, digite apenas M ou F.')
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    soma += pessoa['idade']
    if pessoa['sexo'] == 'F':
        f += 1
    while True:
        cont = str(input('Deseja continuar? [S/N]: ')).upper()
        if cont in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if cont == 'N':
        break
media = soma / len(galera)
print('-=' * 40)
print(f'A) O grupo tem {len(galera)} pessoas.')
print(f'B) A média de idade é de {media} anos.')
if f > 0:
    print('C) As mulheres cadastradas foram:', end=' ')
    for pess in galera:
        if pess['sexo'] == 'F':
            print(f'{pess["nome"]}; ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for pess in galera:
    if pess['idade'] > media:
        print('     ', end='')
        for k, v in pess.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')