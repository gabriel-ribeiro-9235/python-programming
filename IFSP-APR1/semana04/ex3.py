k = int(input("Número de caractéres do alfabeto alienígina: "))
n = int(input("Número de caractéres da mensagem: "))

alfabeto = input("Alfabeto: ")
'''while len(alfabeto) != k:
    alfabeto = input("As informações passadas não batem, digite novamente: ")'''
flag = True
while flag:
    c = 0
    for i in range(0, len(alfabeto)-1):
        for j in range(i+1, len(alfabeto)):
            if alfabeto[i] == alfabeto[j] and c == 0:
                c += 1
    if c == 0 and len(alfabeto) == k:
        flag = False
    else:
        alfabeto = input("Não repita o mesmo caracter, nem digite mais ou menos que o informado!\nTente novamente: ")

msg = input("Mensagem: ")
while len(msg) != n:
    msg = input("As informações passadas não batem, digite novamente: ")
    
validade = True
for i in range(len(msg)):
    if msg[i] not in alfabeto:
        validade = False

if validade:
    print("S")
else:
    print("N")
