s = input("Digite algo: ")
inverso = s[::-1]
maior = ""
for i in range(len(inverso)):
    for j in range(len(inverso)):
        if j+i <= len(inverso):
            atual = inverso[i:j+i]
            if atual in s and len(atual) > len(maior) and atual == atual[::-1]:
                maior = atual
print(f"O maior palíndromo dentro de \"{s}\" é \"{maior}\"")
