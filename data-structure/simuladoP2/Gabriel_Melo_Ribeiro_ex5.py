def tiraElementos(lista, retira):
    if lista == []:
        return []
    else:
        ultimo = lista[-1]
        nova = tiraElementos(lista[:-1], retira)
        if ultimo not in retira:
            nova.append(ultimo)
        return nova


numeros = [21, 9, 35, 9, 43, 7]
tirar = [7, 21]
print(tiraElementos(numeros, tirar))
