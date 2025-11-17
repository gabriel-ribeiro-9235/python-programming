a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = 0

if a > b:
    c = b
    b = a
    a = c

print(f"A = {a}, B = {b}")
