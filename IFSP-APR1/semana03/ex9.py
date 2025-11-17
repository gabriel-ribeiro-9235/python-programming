alfabeto = "abcdefghijklmnopqrstuvwxyz"
string = input("Digite algo: ")
nova = ""
flag = False
for i in range(len(string)):
    posicao = 0
    for j in range(len(alfabeto)):
        if alfabeto[j] == string[i]:
            posicao = j
    posicao += i
    if posicao < len(alfabeto):
        nova += alfabeto[posicao]
    else:
        flag = True
if flag:
    print("A string digitada não respeita os limites do alfabeto")
else:
    print(nova)
