from random import randint
print(f'{'DESAFIO 74':=^26}')
lista = (randint(-100,100), randint(-100,100), randint(-100,100),
         randint(-100,100), randint(-100, 100))
print('Os números sorteados foram: ')
for pos, c in enumerate(lista):
    if pos == 0 or pos == 1 or pos == 2 or pos == 3:
        print(f'{c}, ', end='')
    else:
        print(f'{c}')
    if pos == 0:
        menor = maior = c
    else:
        if c < menor:
            menor = c
        elif c > maior:
            maior = c
print('_' * 30)
print(f'O maior valor da lista é {maior}')
print(f'O menor valor da lista é {menor}')
