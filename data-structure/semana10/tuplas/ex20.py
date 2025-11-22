def contaLetras(string):
    tupla = ()
    for i in range(len(string)):
        letra = (string[i],)
        contador = 0
        for j in range(len(string)):
            if string[i] == string[j]:
                contador += 1
        letra += contador,
        if letra not in tupla:
            tupla += (letra,)
    return tupla


txt = input("Digite algo: ")
print(contaLetras(txt))
