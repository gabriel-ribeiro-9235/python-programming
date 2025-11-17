primeira = input("Digite algo: ")
segunda = ""
nova = ""
while len(segunda) != len(primeira):
    segunda = input("Digite algo do mesmo tamanho que a primeira entrada que você digitou: ")
for i in range(len(primeira)):
    nova += primeira[i] + segunda[i]
print(nova)
