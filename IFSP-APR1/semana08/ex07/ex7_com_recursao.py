def contaMaior(lista, n):
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        if lista[0] > n:
            return 1
        else:
            return 0
    else:
        if lista[0] > n:
            cont = 1 + contaMaior(lista[1:], n)
        else:
            cont = contaMaior(lista[1:], n)
        return cont


lista = [1, 2, 3, 4, 5]
k = int(input("Digite um número: "))
print(f"{contaMaior(lista, k)} números da lista são maiores que {k}")
