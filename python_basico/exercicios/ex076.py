print(f'{'DESAFIO 76':=^26}')
lista = ('Lápis', 1.50, 'Borracha', 2.00, 'Caderno', 15.90,
         'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('_' * 40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('_' * 40)
for c in range(0, len(lista), 2):
    print(f'{lista[c]:.<30}', end='')
    print(f'R${lista[c+1]:6.2f}')
print('_' * 40)
