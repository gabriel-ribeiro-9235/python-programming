str1 = input("String 1: ")
str2 = input("String 2: ")
nova = maior = ""
if len(str1) < len(str2):
    menor = len(str1)
    maior = str2
    resto = len(str2) - len(str1)
elif len(str2) < len(str1):
    menor = len(str2)
    maior = str1
    resto = len(str2) - len(str1)
else:
    menor = len(str1)
    resto = 0
if str1 != "" and str2 != "":
    for i in range(menor):
        nova += str1[i] + str2[i]
    if resto != 0:
        nova += maior[-resto:]
    print(f"Resultado: {nova}")
else:
    print(f"Resultado: {str1+str2}")
