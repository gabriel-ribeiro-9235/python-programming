def retornaSqrt(string):
    if len(string) == 0:
        return 'Nada foi digitado!'
    else:
        string += ' '
        lista = []
        num = ''
        for i in range(len(string)):
            if string[i] in '1234567890':
                num += string[i]
            elif string[i] == ' ' and len(num) > 0:
                lista.append(int(num))
                num = ''
        raizes = []
        for n in lista:
            raizes.append(round(n**(1/2), 2))
        return raizes


numeros = "100 4 1600"
print(retornaSqrt(numeros))
