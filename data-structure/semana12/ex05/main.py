def abasteceDic(caminho):
    arq = open(caminho, "r")
    alunos = {}
    for linha in arq:
        linha = linha[:-1]
        key, notas = linha.split("\t")[0], linha.split("\t")[1:]
        alunos[key] = notas
    return alunos


def mais6notas(caminho):
    dic = abasteceDic(caminho)
    lista = []
    for key in dic:
        if len(dic[key]) > 6:
            lista.append(key)
    return lista


def calculaMedia(caminho):
    alunos = abasteceDic(caminho)
    medias = {}
    for aluno in alunos:
        qnt = len(alunos[aluno])
        soma_notas = 0
        for nota in alunos[aluno]:
            soma_notas += float(nota)
        media = round((soma_notas / qnt), 2)
        medias[aluno] = media
    return medias


def minMax(caminho):
    alunos = abasteceDic(caminho)
    novo = {}
    for key, val in alunos.items():
        menor = maior = float(val[0])
        for nota in val:
            nota = float(nota)
            if nota > maior:
                maior = nota
            if nota < menor:
                menor = nota
        novo[key] = [menor, maior]
    return novo


path = "data-structure/semana12/ex05/estudantes.dat"
mais6 = mais6notas(path)
med = calculaMedia(path)
maior_menor_nota = minMax(path)
