N = int(input("Quantidade de números: "))
print("-" * 40)
semordem = False
for i in range(N):
    num = int(input(f"{i+1}º número: "))
    if i == 1:
        if anterior <= num:
            crescente = True
        else:
            crescente = False
    if i > 1 and not semordem:
        if crescente and anterior > num:
            semordem = True
        if not crescente and anterior < num:
            semordem = True
    anterior = num
print("-" * 40)
if N == 0:
    print("Nenhum número foi inserido!")
elif N == 1:
    print(f"Apenas o número {num} foi inserido!")
else:
    if semordem:
        print(0)
    elif not semordem and crescente:
        print(1)
    else:
        print(-1)
