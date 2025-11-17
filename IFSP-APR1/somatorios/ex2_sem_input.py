'''Função'''
def Xcal(mat_A, mat_B, linhas, colunas):
    #Calcular os valores das médias das matrizes A e B
    soma_A = soma_B = cont = 0
    for i in range(linhas):
        for j in range(colunas):
            soma_A += mat_A[i][j]
            soma_B += mat_B[i][j]
            cont += 1
    if cont != 0:
        media_A = soma_A / cont
        media_B = soma_B / cont
    
    #Calcula o valor do numerador e do que está DENTRO DAS RAÍZES
    numerador = raiz1 = raiz2 = 0
    for i in range(linhas):
        for j in range(colunas):
            raiz1 += (mat_B[i][j] - media_B) * (mat_B[i][j] - media_B)  # se puder use **2
            raiz2 += (mat_A[i][j] - media_A) * (mat_A[i][j] - media_A)  # se puder use **2
            numerador += (mat_B[i][j] - media_A) * (mat_A[i][j] - media_B)
    
    #Agora tira a raiz quadrada dos valores encontrados, multiplica e coloca no denominador
    raiz1 = raiz1 ** (1/2)
    raiz2 = raiz2 ** (1/2)
    denominador = raiz1 * raiz2

    #Verifica possível erro de divisão por zero e retorna o valor final
    if denominador == 0:
        return "ERRO! Divisão por zero!"
    else:
        return round(numerador / denominador, 2)


'''Programa Principal'''
#Sem input, você coloca os valores das matrizes no próprio código
A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]

resultado = Xcal(A, B, len(A), len(A[0]))
print(resultado)
