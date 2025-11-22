def multiplicaImpar(lista):
    if len(lista) == 0:
        return "Lista vazia!"
    elif len(lista) == 1:
        if lista[0] % 2 == 1:
            return lista[0]
        else: 
            return 1
    else:
        if lista[0] % 2 == 1:
            mult = lista[0] * multiplicaImpar(lista[1:])
        else:
            mult = multiplicaImpar(lista[1:])
        return mult
    

lista = [1, 2, 3, 4, 10]
print(multiplicaImpar(lista))
