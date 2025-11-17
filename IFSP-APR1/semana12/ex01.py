def numLinhas(arquivo):
    linhas = arquivo.split('\n')
    return len(linhas)


arq = open('Exercícios IFSP/Semana 12/test.txt', 'r')
print(f'O arquivo tem  {numLinhas(arq.read())} linhas')
arq.close()
