'''Função'''
def R2(vetor_x, vetor_y, n):
    #Calcular a média do vetor x
    soma_x = 0
    for i in range(n):
        soma_x += vetor_x[i]
    if n != 0:
        media_x = soma_x / n

    #Calcular separadamente o numerador e o denominador
    numerador = denominador = 0
    for i in range(n):
        numerador += (vetor_x[i] - vetor_y[i]) * (vetor_x[i] - vetor_y[i])  # se puder use **2
        denominador += (vetor_x[i] - media_x) * (vetor_x[i] - media_x)  # se puder use **2

    #Verificar possível erro de divisão por 0 e retornar o valor final
    if denominador == 0:
        return "ERRO! Divisão por zero!"
    else:
        divisao = numerador / denominador
        return round(1 - divisao, 2)


'''Programa Principal'''
x = list()  #pode ser [] também
y = list()  #pode ser [] também
mod = int(input("Digite o tamnaho dos vetores x e y: "))

#Ler os valores dos vetores x e y
for i in range(mod):
    x.append(float(input(f"Insira o valor de x[{i+1}]: ")))
for j in range(mod):
    y.append(float(input(f"Insira o valor de y[{j+1}]: ")))

resultado = R2(x, y, mod)
print(resultado)
