M = int(input("Tamanho da primeira palavra: "))
p1 = input("Palavra 1: ")
while len(p1) != M:
    p1 = input(f"Palavra 1 não pode ter mais de {M} caractéres! Tente novamente: ")
N = int(input("Tamanho da segunda palavra: "))
p2 = input("Palavra 2: ")
while len(p2) != N:
    p2 = input(f"Palavra 2 não pode ter mais de {N} caractéres! Tente novamente: ")
if p1[0] != p2[0]:
    continua = False
else:
    continua = True
if M > N:
    menor = N
elif M < N:
    menor = M
else:
    menor = M
c = 0
for i in range(menor):
    if continua and p1[i] == p2[i]:
        c = i + 1
print(c)
