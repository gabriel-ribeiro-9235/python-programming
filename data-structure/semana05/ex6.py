N = int(input("Número de atletas: "))
M = int(input("Número de saltos por atleta: "))
vencedor = ""
maior = 0
for i in range(N):
    print("-" * 40)
    nome = input(f"Atleta {i+1}: ")
    for j in range(M):
        salto = float(input(f"Salto {j+1}: "))
        if salto > maior:
            vencedor = nome
            maior = salto
        elif salto == maior:
            vencedor += f" e {nome}"
print("-" * 40)
if " e " in vencedor:
    print(f"Os vencedores foram {vencedor} com um salto de {maior:.2f} m".replace(".", ",") + ".")
else:
    print(f"O vencedor foi {vencedor} com um salto de {maior:.2f} m".replace(".", ",") + ".")
