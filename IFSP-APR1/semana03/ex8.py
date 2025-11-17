string = input("Digite uma string comprimida: ")
letras = numeros = nova = ""
for i in range(len(string)):
    if i % 2 == 0:
        letras += string[i]
    else:
        numeros += string[i]
for i in range(len(numeros)):
    nova += letras[i] * int(numeros[i])
print(nova)
