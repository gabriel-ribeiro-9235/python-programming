string = input("Digite algo: ")
nova = ""
letra = string[0]
c = 0
for i in range(len(string)):
    if letra == string[i]:
        c += 1
    else:
        nova += letra + str(c)
        letra = string[i]
        c = 1
nova += letra + str(c)
print(nova)
