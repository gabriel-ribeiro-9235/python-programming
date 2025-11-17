string = input("Digite algo: ")
impares = ""
pares = ""
for i in range(len(string)):
    if i % 2 == 0:
        impares += string[i]
    else:
        pares += string[i]
print(f"Caractéres ímpares: {impares}")
print(f"Caractéres pares: {pares}")
print(f"String final: {impares+pares}")
