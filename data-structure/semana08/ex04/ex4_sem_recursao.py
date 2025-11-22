n = int(input("Digite um número: "))
soma = 0
for i in range(0, n+1, 2):
    soma += i
print(f"Soma de todos os números pares de 1 até n: {soma}")
