def divisores(n):
    if n == 0:
        return 'Com excessão de ele mesmo, todos os números são divisores de zero'
    else:
        div = []
        for i in range(1, n+1):
            if n % i == 0:
                div.append(i)
        return div


num = int(input("Digite um número: "))
print(divisores(num))
