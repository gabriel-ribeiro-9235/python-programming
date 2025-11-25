def numChar(arquivo):
    tudo = arquivo.read()
    cont = 0
    for char in tudo:
        if char not in '\n\t':
            cont += 1
    return cont


arq = open('Exercícios IFSP/Semana 12/test.txt', 'r')
print(f'O arquivo tem {numChar(arq)} caractéres')
arq.close()
