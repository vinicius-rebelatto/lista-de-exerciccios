numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

num = int(input("Digite um número [0 à 20]: "))
while num not in range(0, 21):
    num = int(input("Tente novamente. Digite um número de 0 à 20: "))
print(f'Você digitou o número {numeros[num]}')
