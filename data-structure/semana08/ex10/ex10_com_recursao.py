def contaSubstring(string, sbstring):
    if len(string) == 0:
        return "String vazia ou menor que a substring!"
    elif len(string) == len(sbstring):
        if string == sbstring:
            return 1
        else:
            return 0
    else:
        if string[0:len(sbstring)] == sbstring:
            cont = 1 + contaSubstring(string[1:], sbstring)
        else:
            cont = contaSubstring(string[1:], sbstring)
        return cont


txt = input("Digite algo: ")
parte = input("Digite uma substring: ")
print(contaSubstring(txt, parte))
