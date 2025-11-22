n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Terceiro número: "))
maximo = max(n1, n2, n3)
if maximo == int(maximo):
    maximo = int(maximo)
print(f"O maior número digitado foi {maximo}.")
