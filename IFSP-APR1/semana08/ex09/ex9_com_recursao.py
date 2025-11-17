def verificaMaiusc(string, n):
    if string == "":
        return 'String vazia!'
    elif len(string) == 1:
        return string[0].upper()
    else:
        nova = string[0].upper() + verificaMaiusc(string[1:], n)
        if len(nova) == n:
            if nova == string:
                return 'Todas as letras são maiúsculas!'
            else:
                return 'Há letras que não são maiúsculas!'
        else:
            return nova
        

txt = input("Digite algo: ")
print(verificaMaiusc(txt, len(txt)))
