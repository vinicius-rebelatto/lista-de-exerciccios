from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2)
    if passo == 0:
        passo += 1
    if fim < inicio:
        if passo > 0:
            passo *= -1
        fim -= 1
    else:
        if passo < 0:
            passo *= -1
        fim += 1
    for num in range(inicio, fim, passo):
        print(num, end=' ')
        sleep(0.4)
    print('FIM!')


contador(0, 10, 1)
contador(10, 0, 2)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
