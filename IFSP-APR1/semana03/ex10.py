alfabeto = "abcdefghijklmnopqrstuvwxyz"
string = input("Digite algo: ")
nova = ""
for i in range(len(string)):
    if string[i].lower() in 'aáàãâeéêiíoóõôuú':
        nova += "* "
    else:
        posicao = 0
        for j in range(len(alfabeto)):
            if alfabeto[j] == string[i].lower():
                posicao = j + 1
        nova += str(posicao) + " "
print(nova)
