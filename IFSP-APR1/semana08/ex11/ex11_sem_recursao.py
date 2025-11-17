matriz = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[1])):
        soma += matriz[i][j]
print(f"A soma dos elementos da matriz vale: {soma}")
