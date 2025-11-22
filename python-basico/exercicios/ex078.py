print(f'{'DESAFIO 78':=^26}')
lista = [int(input('Digite um valor para a posição 0: ')),
         int(input('Digite um valor para a posiçõa 1: ')),
         int(input('Digite um valor para a posição 2: ')),
         int(input('Digite um valor para a posição 3: ')),
         int(input('Digite um valor para a posição 4: '))]
print(f'Você digitou os valores {lista}')
if lista.count(max(lista)) == 1:
    print(f'O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista))}')
else:
    print(f'O maior valor digitado foi {max(lista)} nas posições', end=' ')
    for pos, valor in enumerate(lista):
        if valor == max(lista):
            print(f'{pos}...', end=' ')
        if pos == len(lista) - 1:
            print()
if lista.count(min(lista)) == 1:
    print(f'O menor valor digitado foi {min(lista)} na posição {lista.index(min(lista))}')
else:
    print(f'O menor valor digitado foi {min(lista)} nas posições', end=' ')
    for pos, valor in enumerate(lista):
        if valor == min(lista):
            print(f'{pos}...', end=' ')
        if pos == len(lista) - 1:
            print()
