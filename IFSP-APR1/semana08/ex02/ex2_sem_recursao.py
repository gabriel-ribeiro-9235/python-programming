lista = [1, 2, -3, 4, 5]
for i in range(len(lista)):
    if i == 0:
        menor = lista[0]
    else:
        if lista[i] < menor:
            menor = lista[i]

print(f"Menor: {menor}")
