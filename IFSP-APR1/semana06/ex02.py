n = int(input("Informe o número de pessoas: "))
lista = list()
for i in range(n):
    lista.append(float(input(f"Altura da pessoa {i+1}: ")))
    if i == 0:
        menor = lista[0]
        posicao = 0
    else:
        if lista[i] < menor:
            menor = lista[i]
            posicao = i
print(lista)
print(f"Altura do menor: {menor:.2f}m")
print(f"Índice do menor na lista: {posicao}")
