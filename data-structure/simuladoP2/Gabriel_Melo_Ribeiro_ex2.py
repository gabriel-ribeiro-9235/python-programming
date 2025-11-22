def pintaFita(lista):
    pintados = []
    for i in range(len(lista)):
        if lista[i] == 0:
            pintados.append(i)
    nova = []
    for i in range(len(lista)):
        if lista[i] != 0:
            menor = distancia = 0
            for j in range(len(pintados)):
                distancia = i - pintados[j]
                if distancia < 0:
                    distancia *= -1
                if j == 0:
                    menor = distancia
                else:
                    if distancia < menor:
                        menor = distancia
            if menor <= 9:
                nova.append(menor)
            else:
                nova.append(9)
        else:
            nova.append(0)
    return nova
                        


entrada = [-1, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, 0]
print(pintaFita(entrada))
