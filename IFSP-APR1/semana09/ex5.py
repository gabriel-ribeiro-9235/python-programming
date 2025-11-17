def calculaExpressoes(string):
    if len(string) == 0:
        return 'String vazia!'
    else:
        s_espaco = ''
        for char in string:
            if char != ' ':
                s_espaco += char
        if '(' in s_espaco and ')' in s_espaco:
            parenteses = ''
            abre = fecha = 0
            for i in range(len(s_espaco)):
                if s_espaco[i] == '(':
                    abre = i
                elif s_espaco[i] == ')':
                    fecha = i
            parenteses = s_espaco[abre+1:fecha]

            numeros = []
            operadores = []
            num_atual = ''
            for i in range(len(parenteses)):
                if parenteses[i] in '1234567890' or parenteses[i] == '.':
                    num_atual += parenteses[i]
                else:
                    numeros.append(float(num_atual))
                    num_atual = ''
                    operadores.append(parenteses[i])
            numeros.append(float(num_atual))

            i = 0
            while i < len(operadores):
                if operadores[i] == '*' or operadores[i] == '/':
                    if operadores[i] == '*':
                        result = numeros[i] * numeros[i+1]
                    else:
                        result = numeros[i] / numeros[i+1]
                    numeros[i] = result
                    del numeros[i+1]
                    del operadores[i]
                else:
                    i += 1

            i = 0
            while i < len(operadores):
                if operadores[i] == '+':
                    result = numeros[i] + numeros[i+1]
                else:
                    result = numeros[i] - numeros[i+1]
                numeros[i] = result
                del numeros[i+1]
                del operadores[i]

            s_parenteses = s_espaco[:abre] + str(numeros[0]) + s_espaco[fecha+1:]
        else:
            s_parenteses = s_espaco
        if '[' in s_parenteses and ']' in s_parenteses:
            colchetes = ''
            for i in range(len(s_parenteses)):
                if s_parenteses[i] == '[':
                    abre = i
                elif s_parenteses[i] == ']':
                    fecha = i
            colchetes = s_parenteses[abre+1:fecha]

            numeros = []
            operadores = []
            num_atual = ''
            for i in range(len(colchetes)):
                if colchetes[i] in '1234567890' or colchetes[i] == '.':
                    num_atual += colchetes[i]
                else:
                    numeros.append(float(num_atual))
                    num_atual = ''
                    operadores.append(colchetes[i])
            numeros.append(float(num_atual))

            i = 0
            while i < len(operadores):
                if operadores[i] == '*' or operadores[i] == '/':
                    if operadores[i] == '*':
                        result = numeros[i] * numeros[i+1]
                    else:
                        result = numeros[i] / numeros[i+1]
                    numeros[i] = result
                    del numeros[i+1]
                    del operadores[i]
                else:
                    i += 1

            i = 0
            while i < len(operadores):
                if operadores[i] == '+':
                    result = numeros[i] + numeros[i+1]
                else:
                    result = numeros[i] - numeros[i+1]
                numeros[i] = result
                del numeros[i+1]
                del operadores[i]

            s_colchetes = s_parenteses[:abre] + str(numeros[0]) + s_parenteses[fecha+1:]
        else:
            s_colchetes = s_parenteses
        if '{' in s_colchetes and '}' in s_colchetes:
            chaves = ''
            for i in range(len(s_colchetes)):
                if s_colchetes[i] == '{':
                    abre = i
                elif s_colchetes[i] == '}':
                    fecha = i
            chaves = s_colchetes[abre+1:fecha]

            numeros = []
            operadores = []
            num_atual = ''
            for i in range(len(chaves)):
                if chaves[i] in '1234567890' or chaves[i] == '.':
                    num_atual += chaves[i]
                else:
                    numeros.append(float(num_atual))
                    num_atual = ''
                    operadores.append(chaves[i])
            numeros.append(float(num_atual))

            i = 0
            while i < len(operadores):
                if operadores[i] == '*' or operadores[i] == '/':
                    if operadores[i] == '*':
                        result = numeros[i] * numeros[i+1]
                    else:
                        result = numeros[i] / numeros[i+1]
                    numeros[i] = result
                    del numeros[i+1]
                    del operadores[i]
                else:
                    i += 1

            i = 0
            while i < len(operadores):
                if operadores[i] == '+':
                    result = numeros[i] + numeros[i+1]
                else:
                    result = numeros[i] - numeros[i+1]
                numeros[i] = result
                del numeros[i+1]
                del operadores[i]
            s_chaves = s_colchetes[:abre] + str(numeros[0]) + s_colchetes[fecha+1:]
        else:
            s_chaves = s_colchetes
        if s_espaco[0] != '{' or s_espaco[-1] != '}':
            numeros = []
            operadores = []
            num_atual = ''
            for i in range(len(s_chaves)):
                if s_chaves[i] in '1234567890' or s_chaves[i] == '.':
                    num_atual += s_chaves[i]
                else:
                    numeros.append(float(num_atual))
                    num_atual = ''
                    operadores.append(s_chaves[i])
            numeros.append(float(num_atual))

            i = 0
            while i < len(operadores):
                if operadores[i] == '*' or operadores[i] == '/':
                    if operadores[i] == '*':
                        result = numeros[i] * numeros[i+1]
                    else:
                        result = numeros[i] / numeros[i+1]
                    numeros[i] = result
                    del numeros[i+1]
                    del operadores[i]
                else:
                    i += 1

            i = 0
            while i < len(operadores):
                if operadores[i] == '+':
                    result = numeros[i] + numeros[i+1]
                else:
                    result = numeros[i] - numeros[i+1]
                numeros[i] = result
                del numeros[i+1]
                del operadores[i]

        return numeros[0]


expressao = " 3 + {100 - [4 + (15-7) ] * 7}"
print(calculaExpressoes(expressao))
