def somaMatriz(mat, colunas):
    if len(mat[0]) == 0:
        return 'Matriz vazia!'
    elif len(mat) == 1:
        soma = 0
        for i in range(colunas):
            soma += mat[0][i]
        return soma
    else:
        linha = 0
        for i in range(colunas):
            linha += mat[0][i]
        return linha + somaMatriz(mat[1:], colunas)


matriz = [[1, 3, 5], [1, 1, 1]]
print(somaMatriz(matriz, len(matriz[0])))
