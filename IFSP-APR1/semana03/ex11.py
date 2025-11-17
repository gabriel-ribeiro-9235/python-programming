string = input("Digite algo: ") + " "
parametro = ""
nova = ""
espaco = False
for i in range(len(string)):
    if string[i] == " ":
        espaco = True
    if not espaco:
        parametro += string[i]
    else:
        if parametro[-1] in ",.;<>:!?/][}{()-_=+*&%$#@":
            parametro = parametro[-2::-1] + parametro[-1]
        else:
            parametro = parametro[::-1]
        espaco = False
        nova += parametro + " "
        parametro = ""
print(nova)
