string = input("Digite algo: ")
nova = ""
n = int(input("Digite n para fazer cifra de césar: "))
while n < 0:
    n = int(input("n não pode ser menor que zero! Tente novamente: "))
alfabeto = "abcdefghijklmnopqrstuvwxyz"
if n == 0:
    cifra = alfabeto
else:
    cifra = alfabeto[n:] + alfabeto[:n]
for i in range(len(string)):
    if string[i] in alfabeto:
        c = 0
        letra = string[i]
        for j in range(len(alfabeto)):
            if alfabeto[j] == letra:
                c = j
        nova += cifra[c]
    else:
        nova += string[i]
print(nova)
