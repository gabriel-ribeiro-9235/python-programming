N = int(input("Número de nadadores: "))
M = int(input("Número de provas por nadador: "))
vencedor = ""
menor = 0
for i in range(N):
    print("-" * 40)
    nome = input(f"Nadador {i+1}: ")
    for j in range(M):
        tempo = float(input(f"Tempo {j+1}: "))
        if i == 0 and j == 0:
            menor = tempo
        if tempo < menor:
            vencedor = nome
            menor = tempo
        elif tempo == menor:
            vencedor += f" e {nome}"
print("-" * 40)
if " e " in vencedor:
    print(f"Os vencedores foram {vencedor} com um tempo de {menor:.1f} s".replace(".", ",") + ".")
else:
    print(f"O vencedor foi {vencedor} com um tempo de {menor:.1f} s".replace(".", ",") + ".")
