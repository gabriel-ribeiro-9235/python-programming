'''Função'''
def Xcal(mat_A, mat_B, linhas, colunas):
    # Calcular os valores das médias das matrizes A e B
    soma_A = soma_B = cont = 0
    for i in range(linhas):
        for j in range(colunas):
            soma_A += mat_A[i][j]
            soma_B += mat_B[i][j]
            cont += 1
    if cont != 0:
        media_A = soma_A / cont
        media_B = soma_B / cont

    # Calcula o valor do numerador e do que está DENTRO DAS RAÍZES
    numerador = raiz1 = raiz2 = 0
    for i in range(linhas):
        for j in range(colunas):
            raiz1 += (mat_B[i][j] - media_B) * (mat_B[i][j] - media_B)  # se puder use **2
            raiz2 += (mat_A[i][j] - media_A) * (mat_A[i][j] - media_A)  # se puder use **2
            numerador += (mat_B[i][j] - media_A) * (mat_A[i][j] - media_B)

    # Agora tira a raiz quadrada dos valores encontrados, multiplica e coloca no denominador
    raiz1 = raiz1 ** (1/2)
    raiz2 = raiz2 ** (1/2)
    denominador = raiz1 * raiz2

    # Verifica possível erro de divisão por zero e retorna o valor final
    if denominador == 0:
        return "ERRO! Divisão por zero!"
    else:
        return round(numerador / denominador, 2)


'''Programa Principal'''
A = list()  # Pode ser [] também
B = list()  # Pode ser [] também
n = int(input("Número de linhas das matrizes A e B: "))
m = int(input("Número de colunas das matrizes A e B: "))

# Ler os valores das matrizes A e B
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(float(input(f"Insira o valor de A[{i+1}, {j+1}]: ")))
    A.append(linha)
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(float(input(f"Insira o valor de B[{i+1}, {j+1}]: ")))
    B.append(linha)

resultado = Xcal(A, B, n, m)
print(resultado)
