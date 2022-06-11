aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Media de {aluno["Nome"]}: '))
for k, v in aluno.items():
    print(f'{k} é igual à {v}')
if 7 <= aluno['Média'] <= 10:
    print('Situação é igual à Aprovado!')
elif 10 > aluno['Média'] >= 5:
    print('Situação é igual à Recuperação')
elif 0 <= aluno['Média'] < 10:
    print('Situação é igual à Reprovado!')
else:
    print('Média Impossível!')

# aluno = {'nome': str(input('Nome: '))}
# aluno['média'] = float(input(f'Digite a média de {aluno["nome"]}: '))
# aluno['situação'] = 'aprovado' if aluno['média'] >= 7 else 'reprovado' if aluno['média'] <6 else 'recuperação'
# for key, value in aluno.items():
# 	print(f'{key}:', value)
