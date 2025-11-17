S = int(input("Soma dos dígitos: "))
A = int(input("Início: "))
B = int(input("Fim: "))
contador = 0
while A > B:
    B = int(input("O fim não pode ser menor que o início! Tente novamente: "))
for i in range(A, B+1):
    k = 1
    digitos = 0
    soma = 0
    while i % k != i:
        k = k * 10
        digitos = digitos + 1
    for c in range(0, digitos):
        soma = int(soma + (i % 10))
        i = (i - (i % 10)) / 10
    if soma == S:
        contador = contador + 1
print(contador)
