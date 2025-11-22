string = input("Digite algo: ")
par = ""
impar = ""
nova = ""
for i in range(len(string)):
    if i % 2 == 0:
        par += string[i]
    else:
        impar += string[i]
nova = par + impar
print(nova)
