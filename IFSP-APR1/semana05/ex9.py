#validando a entrada
string = input("Digite uma palavra: ")

k = 0
for letra in string:
    if letra in "áéíóúàâêôãõ":
        k += 1
if k != 0:
    acento = True
else:
    acento = False

while " " in string or acento:
    string = input("Digite apenas uma palavra e sem espaço nem acento: ")
    k = 0
    for letra in string:
        if letra in "áéíóúàâêôãõ":
            k += 1
    if k != 0:
        acento = True
    else:
        acento = False

#procurando e printando repetições
nova = string
c = 0
repeticao = False
for letra in string:
    c = 0
    for j in range(len(nova)):
        if nova[j] == letra and not repeticao:
            c += 1
            if c > 1:
                repeticao = True
                print(letra, end=' ')
    if repeticao:
        repeticao = False
        parametro = nova
        nova = ""
        for i in range(len(parametro)):
            if parametro[i] != letra:
                nova += parametro[i]

#verificando e printando se não há repetições
if nova == string:
    print("Não há repetição de carctéres na string!")
