string = input("String: ")
simbolo = input("Símbolo para substituir vogais minúsculas: ")
nova = ""
for letra in string:
    if letra in "aeiou":
        nova += simbolo
    else:
        nova += letra
print(f"Resultado: {nova}")
