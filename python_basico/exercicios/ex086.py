print(f'{'DESAFIO 86':=^26}')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor da posição [{l+1}, {c+1}]: '))
print('-=' * 19)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:>5}', end='')
    print()
