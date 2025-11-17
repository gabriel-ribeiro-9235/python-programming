entrada1 = input("Digite o número ou endereço: ").upper()
entrada = ""
numero = ""
for i in range(len(entrada1)):
    if entrada1[i] != " ":
        entrada += entrada1[i]
for i in range(len(entrada)):
    if entrada[i] == "-":
        numero += "-"
    elif entrada[i] in "ABC":
        numero += "2"
    elif entrada[i] in "DEF":
        numero += "3"
    elif entrada[i] in "GHI":
        numero += "4"
    elif entrada[i] in "JKL":
        numero += "5"
    elif entrada[i] in "MNO":
        numero += "6"
    elif entrada[i] in "PQRS":
        numero += "7"
    elif entrada[i] in "TUV":
        numero += "8"
    elif entrada[i] in "WXYZ":
        numero += "9"
    else:
        numero += entrada[i]
print(numero)
    
