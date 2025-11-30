def mais6notas(caminho):
    arq = open(caminho, "r")
    lista = []
    for linha in arq:
        linha = linha[:-1]
        nome, notas = linha.split("\t")[0], linha.split("\t")[1:]
        if len(notas) > 6:
            lista.append(nome)
    arq.close()
    return lista


path = "data-structure/semana12/ex05/estudantes.dat"
mais6 = mais6notas(path)
