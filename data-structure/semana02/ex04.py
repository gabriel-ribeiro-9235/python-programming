#NÃO SAI SEM LISTAS
N = int(input("Número de termos: "))
t = int(input("T1 = "))
num_pa = 1
for i in range(1, N):
    k = int(input(f"T{i+1} = "))
    if i == 1:
        c = k - t
    if k - t != c:
        c = k - t
        num_pa = num_pa + 1
    t = k
print(num_pa)
'''
N = int(input("Número de termos: "))
a = list()
for i in range(0, N):
    a.append(int(input(f"T{i+1} = ")))
num_pa = 1
if N >= 2:
    razao = a[1] - a[0]
    for i in range(2, N):
        if a[i] - a[i-1] != razao:
            num_pa += 1
            if i+1 < N:
                razao = a[i+1] - a[i]
print(num_pa)
'''
