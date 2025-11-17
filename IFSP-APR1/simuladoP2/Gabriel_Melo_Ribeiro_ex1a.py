def retornaNotas(alunos, notas, aluno):
    indice = 0
    for i in range(len(alunos)):
        if alunos[i][0] == aluno:
            indice = i
    materias = []
    for lista in notas[indice]:
        if lista[0] not in materias:
            materias.append(lista[0])
    medias = []
    for i in range(len(materias)):
        cont = soma = media = 0
        for lista in notas[indice]:
            if materias[i] == lista[0]:
                cont += 1
                soma += lista[2]
        media = soma / cont
        medias.append(media)
    final = []
    for i in range(len(medias)):
        final.append([materias[i], medias[i]])
    return final
        


Alunos=[ ['João Pedro Souza', 18], ['Isabela Moraes', 17], ['Daniel Silva', 19] ]
Notas = [ [['MAT', 'P1', 5.8], ['ALG', 'P1', 7.4], ['WEB', 'P1', 8.9], ['ALG', 'P2', 9.6]], 
[['ALG', 'P1', 9.2], ['WEB', 'P1', 6.7], ['WEB', 'P2', 9.3]], 
[['MAT', 'P1', 5.8], ['ALG', 'P1', 9.6], ['MAT', 'P2', 8.1], ['MAT', 'P3', 8.1]] ]
boletim = retornaNotas(Alunos, Notas, 'Daniel Silva')
for lista in boletim:
    print('-'*30)
    print(f"Matéria: {lista[0]}\nMédia: {lista[1]:.2f}")
print('-'*30)
