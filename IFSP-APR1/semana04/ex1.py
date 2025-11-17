s = input("Digite algo: ").lower()
flag = True
while flag:
    cont = 0
    for i in range(len(s)):
        if s[i] in " áéíóúãõâêôà":
            cont += 1
    if cont != 0:
        s = input("Digite sem acento e espaços: ").lower()
    else:
        flag = False
afbt = "abcdefghijklmnopqrstuvxz"
vogais = "aeiou"
ia = 0
ie = 4
ii = 8
io = 14
iu = 20
cifra = ""
for i in range(len(s)):
    cifra += s[i]
    if s[i] not in vogais:
        for j in range(len(afbt)):
            if s[i] == afbt[j]:
                indice = j
        vogpro = ""
        if indice <= 2:
            cifra += "a"
        elif indice <= 6:
            cifra += "e"
        elif indice <= 11:
            cifra += "i"
        elif indice <= 17:
            cifra += "o"
        else:
            cifra += "u"
        if s[i] != "z":
            if afbt[indice+1] not in vogais:
                cifra += afbt[indice+1]
            else:
                cifra += afbt[indice+2]
        else:
            cifra += "z"
print(cifra)
