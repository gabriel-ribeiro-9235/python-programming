n = int(input("Número de postos de hidratação: "))
while n < 2:
    n = int(input("Tem que ter mais de 2! Tente novamente: "))
m = int(input("Distância intermediária do atleta: "))
while m < 0 or m > 42195:
    m = int(input("Impossível! Tente novamente: "))
p = 0
k = p
situacao = "S"
print("Posto 1 = 0")
for i in range(1, n):
    p = int(input(f"Posto {i+1} = "))
    while p <= k:
        p = int(input(f"Posto inválido!\nPosto {i+1} = "))
    if (p - k) > m:
        situacao = "N"
    k = p
p = 42195
if (p - k) > m:
    situacao = "N"
print(situacao)
