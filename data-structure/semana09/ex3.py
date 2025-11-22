def retornaPrimo(n):
    if n == 0:
        return 'Não há número primo na posição zero'
    else:
        primos = []
        cont = 1
        while len(primos) < n:
            div_num = []
            for i in range(1, cont+1):
                if cont % i == 0:
                    div_num.append(i)
            if len(div_num) == 2:
                primos.append(cont)
            cont += 1
        return primos[-1]


num = int(input("Digite um número: "))
print(retornaPrimo(num))
