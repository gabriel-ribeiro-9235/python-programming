def somaPar(n):
    if n == 0:
        return n
    else:
        if n % 2 == 1:
            soma = somaPar(n-1)
        else:
            soma = somaPar(n-2) + n
        return soma
    

n = int(input("Digite um número n: "))
print(f"Soma de todos os pares de 1 até n: {somaPar(n)}")
