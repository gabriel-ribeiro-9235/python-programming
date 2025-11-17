from random import randint

def sorteia(lst):
    for cont in range(0, 5):
        lst.append(randint(1, 20))
    print(f'Lista sorteada: {lst}')

def somapar(lst):
    soma = 0
    for c in lst:
         if c % 2 == 0:
             soma += c
    print(f'A soma dos valores pares sorteados é {soma}')


print(f'{'DESAFIO 100':=^26}')
lista = list()
sorteia(lista)
somapar(lista)
