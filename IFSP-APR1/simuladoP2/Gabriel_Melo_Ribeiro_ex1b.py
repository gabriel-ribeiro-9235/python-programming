def retornaMelhor(alunos, notas, materia):
    maior = 0
    indice = [0]
    so_materia = []
    for i in range(len(notas)):
        linha = []
        for lista in notas[i]:
            if lista[0] == materia:
                linha.append(lista)
        so_materia.append(linha)
    for i in range(len(so_materia)):
        for j in range(len(so_materia[i])):
            if j == 0 and i == 0:
                maior = so_materia[i][j][2]
            else:
                if maior < so_materia[i][j][2]:
                    maior = so_materia[i][j][2]
                    indice = [i]
                elif maior == so_materia[i][j][2] and i not in indice:
                    indice.append(i)
    melhores = []
    for i in indice:
        melhores.append(alunos[i])
    nomes_e_nota = [melhores, maior]
    return nomes_e_nota


Alunos=[ ['João Pedro Souza', 18], ['Isabela Moraes', 17], ['Daniel Silva', 19] ]
Notas = [[ ['MAT', 'P1', 5.8], ['ALG', 'P1', 7.4], ['WEB', 'P1', 8.9], ['ALG', 'P2', 9.6] ], 
[ ['ALG', 'P1', 9.2], ['WEB', 'P1', 6.7], ['WEB', 'P2', 9.3] ],
[ ['MAT', 'P1', 5.8], ['ALG', 'P1', 9.6], ['MAT', 'P2', 8.1], ['MAT', 'P3', 8.1] ]]
resultado = retornaMelhor(Alunos, Notas, 'ALG')
print("     Melhor(es) aluno(s)")
for i in range(len(resultado[0])):
    print('-'*30)
    print(f"Aluno: {resultado[0][i][0]}\nIdade: {resultado[0][i][1]} anos")
print('-'*30)
print(f"Nota: {resultado[1]}")
