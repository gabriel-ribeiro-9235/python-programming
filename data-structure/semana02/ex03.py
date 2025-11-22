N = int(input("Número de termos: "))
print("_" * 30, "\n")
soma = 0
for i in range(0, N):
    T = int(input(f"T{i+1} = "))
    while T < 10:
        T = int(input(f"O número tem que ser maior que 10. T{i+1} = "))
    p = int(T % 10)
    T = int((T - p) / 10)
    soma = soma + (T**p)
print("_" * 30)
print(soma)
