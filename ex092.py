from datetime import date
pessoa = dict()
while True:
    ano = date.today()
    ano = ano.year
    pessoa['nome'] = str(input('Nome: '))
    nasc = int(input('Ano de nascimento: '))
    pessoa['idade'] = ano - nasc
    pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
    if pessoa['ctps'] == 0:
        break
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = pessoa['contratação'] + 35 - nasc
    break
print('-=' * 50)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
