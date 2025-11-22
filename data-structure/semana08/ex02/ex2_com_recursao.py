def selecionaMenor(lista):
    if len(lista) == 0:
        return 'Lista vazia!'
    elif len(lista) == 1:
        return lista[0]
    else:
        menor = selecionaMenor(lista[1:])
        if menor > lista[0]:
            menor = lista[0]
        return menor


nmr = [1, 0, 2, 22]
print(selecionaMenor(nmr))
