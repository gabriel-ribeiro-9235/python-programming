def mdc(lista):
    if len(lista) == 0:
        return 'Lista vazia'
    else:
        maiordiv = 1
        for num in range(1, lista[0] + 1):
            divcomun = True
            for i in range(len(lista)):
                if lista[i] % num != 0:
                    divcomun = False
            if divcomun and num > maiordiv:
                maiordiv = num
        return maiordiv


numeros = [1000, 4, 36, 12, 24]
print(mdc(numeros))
