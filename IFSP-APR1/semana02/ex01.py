N = int(input("Nº de estações: "))
C = int(input("Nº de comandos: "))
S = int(input("Nº da estação mais próxima a área devastada: "))
while S < 1 or S > N:
    S = int(input("Nº da estação mais próxima a área devastada: "))
posicao = 1
if S == 1:
    cont_S = 1
else:
    cont_S = 0
for i in range(1, C+1):
    sentido = int(input(f"Comando {i} (1 para horário e -1 para anti-horário): "))
    while sentido != 1 and sentido != -1:
        sentido = int(input(f"Comando {i} (1 para horário e -1 para anti-horário): "))
    if sentido == 1:
        posicao = posicao + 1
    else:
        posicao = posicao - 1
    posicao = posicao % N
    if posicao == 0:
        posicao = N
    if posicao == S:
        cont_S = cont_S + 1
print(cont_S)
