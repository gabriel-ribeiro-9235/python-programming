def verificaOrdem(lista):
    if len(lista) == 0 or len(lista) == 1:
        return True
    else:
        if lista[0] > lista[1]:
            return False
        else:
            return True and verificaOrdem(lista[1:])


lista = [2, 1]
print(verificaOrdem(lista))
