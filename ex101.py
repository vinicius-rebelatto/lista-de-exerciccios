def voto(ano_nascimento):
    from datetime import date
    ano = date.today().year
    idade = ano - ano_nascimento
    if idade < 16:
        return f'Com {idade} ano: NÃO VOTA.'
    elif 18 <= idade <= 65:
        return f'Com {idade} ano: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} ano: Voto OPCIONAL.'


print('-' * 30)
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
