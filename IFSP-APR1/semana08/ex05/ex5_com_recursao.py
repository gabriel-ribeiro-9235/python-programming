def contaVogais(string):
    if len(string) == 0:
        return 0
    else:
        if string[0].lower() in "aeiouáàãâéèêíìóòõôúù":
            cont = 1 + contaVogais(string[1:])
        else:
            cont = contaVogais(string[1:])
        return cont


txt = input("Digite algo: ")
print(contaVogais(txt))
