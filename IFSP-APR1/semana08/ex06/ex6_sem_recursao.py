lista = []
ordenada = lista.copy()
k = 0
for i in range(0, len(ordenada)-1):
    for j in range(i+1, len(ordenada)):
        if ordenada[i] > ordenada[j]:
            k = ordenada[j]
            ordenada[i] = k
            ordenada[j] = ordenada[i]

print(ordenada == lista)
