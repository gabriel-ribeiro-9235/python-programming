print(f'{'DESAFIO 87':=^26}')
soma = 0
maior2 = 0
soma3 = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor da posição [{l+1}, {c+1}]: '))
        if c == 2:
            soma3 += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior2:
                maior2 = matriz[l][c]
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
print('-=' * 12)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:>5}', end='')
    print()
print('-=' * 12)
print(f'A soma dos valores pares da matriz é {soma}')
print(f'A soma dos valores da 3ª coluna é {soma3}')
print(f'O maior valor da 2ª linha é {maior2}')
