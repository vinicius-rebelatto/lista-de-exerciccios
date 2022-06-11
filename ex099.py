from time import sleep


def maior(* numeros):
    cont = mai = 0
    print('-=' * 30)
    print('Analizando os valores passados...')
    sleep(1.5)
    #Resolução do professor.
    for n in numeros:
        print(f'{n} ', end='')
        if cont == 0:
            mai = n
        else:
            if mai < n:
                mai = n
        cont += 1

    #Minha resolução.
    # if len(numeros) > 0:
    #     m = numeros[0]
    #     for n in numeros:
    #         print(f'{n} ', end='')
    #         sleep(0.4)
    #         if m < n:
    #             m = n
    # else:
    #     m = 0

    print(f'Foram informados {len(numeros)} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')


maior(2, 9, 7, 4, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
