parenteses = []
exp = input('Digite a Expressão: ')

pilha = []
for el in exp:
    if el == '(':
        pilha.append(el)
    elif el == ')':
        if len(pilha) > 0:
            pilha.pop()

if len(pilha) > 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')

# for el in exp:
#     if el in '()':
#         parenteses.append(el)
# abre = 0
# fecha = 0
# for par in parenteses:
#     if par == '(':
#         abre += 1
#     else:
#         fecha += 1
#
# if abre == fecha:
#     print('A expressão está correta!')
# else:
#     print('Sua expressão está errada!')
