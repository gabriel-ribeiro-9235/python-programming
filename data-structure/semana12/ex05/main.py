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


path = "data-structure/semana12/ex05/estudantes.dat"
mais6 = mais6notas(path)
