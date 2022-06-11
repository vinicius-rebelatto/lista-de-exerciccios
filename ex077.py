palavras = ('APRENDER', 'PROGRAMAR',
            'LINHGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO',
            'PROGRAMADOR', 'FUTURO')

for pal in palavras:
    vog = ''
    for letra in pal:
        if letra in 'AEIOU':
            vog += letra + ' '
    print(f'Na palavra {pal} temos {vog.lower()}')
