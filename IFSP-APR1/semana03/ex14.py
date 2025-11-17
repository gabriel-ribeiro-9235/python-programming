string = input("Digite algum número romano com as letras acima: ").upper()
flag = True
cont = total = 0
while flag:
    cont = 0
    for i in range(len(string)):
        if string[i] in "IVXLCDM":
            cont += 1
    if cont == len(string):
        flag = False
    else:
        string = input("Número inválido! Tente novamente: ").upper()

for i in range(len(string)):
    if string[i] == "I":
        atual = 1
    elif string[i] == "V":
        atual = 5
    elif string[i] == "X":
        atual = 10
    elif string[i] == "L":
        atual = 50
    elif string[i] == "C":
        atual = 100
    elif string[i] == "D":
        atual = 500
    else:
        atual = 1000
    j = i + 1
    if j < len(string):
        if string[j] == "I":
            prox = 1
        elif string[j] == "V":
            prox = 5
        elif string[j] == "X":
            prox = 10
        elif string[j] == "L":
            prox = 50
        elif string[j] == "C":
            prox = 100
        elif string[j] == "D":
            prox = 500
        else:
            prox = 1000
    else:
        prox = 0
    if prox > atual:
        total -= atual
    else:
        total += atual
print(total)
