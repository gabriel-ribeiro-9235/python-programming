dec = num = int(input("Digite um número: "))
binario = ""
if num == 0:
    binario = "0"
else:
    while not num == 0:
        resto = num % 2
        binario = str(resto) + binario
        num = num // 2

print(f"\"{dec}\" em binário é \"{binario}\"")
