def calculaMedia(lista, n):
    if len(lista) == 0:
        return 'Lista Vazia!'
    elif len(lista) == 1:
        return lista[0] / n
    else:
        media = calculaMedia(lista[1:], n) + (lista[0] / n)
        return media


numeros = [10]
print(calculaMedia(numeros, len(numeros)))
