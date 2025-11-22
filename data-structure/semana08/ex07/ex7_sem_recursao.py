lista = [1, 2, 3, 4, 5]
n = int(input("Digite um número: "))
cont = 0
for num in lista:
    if num > n:
        cont += 1

print(f"{cont} números da lista são maiores que {n}")
