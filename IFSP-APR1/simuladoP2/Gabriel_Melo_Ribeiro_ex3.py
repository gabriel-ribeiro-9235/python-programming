def trocaCentro(matriz):
    if len(matriz) != len(matriz[0]) or len(matriz) % 2 == 0:
        return matriz
    else:
        ordem = len(matriz)
        centro = ordem // 2
        linha_central = matriz[centro]
        coluna_central = []
        for linha in matriz:
            coluna_central.append(linha[centro])
        for i in range(ordem):
            matriz[i][centro] = linha_central[i]
            matriz[centro][i] = coluna_central[i]
        return matriz
        


mat= [[1, 2, 3],  #[1, 4, 3]
      [4, 5, 6],  #[2, 5, 8]
      [7, 8, 9]]  #[7, 6, 9]
print('Original: ')
for linha in mat:
    print(linha)
trocaCentro(mat)
print('-'*20)
print('Centros transpostos:')
for linha in mat:
    print(linha)
