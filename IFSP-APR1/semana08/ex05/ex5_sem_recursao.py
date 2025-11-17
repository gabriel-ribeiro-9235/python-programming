string = input("Digite algo: ")
cont = 0
for letra in string:
    if letra.lower() in "aeiouáàãâéèêíìóòõôúù":
        cont += 1
print(f"Número de vogais: {cont}")
