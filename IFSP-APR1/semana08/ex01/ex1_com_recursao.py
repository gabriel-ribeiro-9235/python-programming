def todosPares(lista):
    if len(lista) == 0:
        return ''
    elif len(lista) == 1:
        if lista[0] % 2 == 1:
            return 1
        else:
            return 0
    else:
        impar = todosPares(lista[1:])
        if lista[0] % 2 == 1:
            impar += 1
        return impar


numeros = []
if todosPares(numeros) == '':
    print('Lista vazia!')
elif todosPares(numeros) != 0:
    print("Nem todos os números são pares!")
else:
    print("Todos são pares!")
