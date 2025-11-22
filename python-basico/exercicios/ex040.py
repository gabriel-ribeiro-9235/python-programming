print('{:=^26}'.format('DESAFIO 40'))
aluno = str(input('Nome do aluno: ')).strip()
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print('_' * 26)
media = (n1 + n2) / 2
print('O(A) aluno(a) {} ficou com média {:.1f} e está'.format(aluno.title(), media), end = ' ')
if media < 5:
    print('\033[31mREPROVADO(A)\033[m!'.format(aluno))
elif 5 <= media < 7:
    print('\033[36mDE RECUPERAÇÃO\033[m!'.format(aluno))
else:
    print('\033[32mAPROVADO(A)\033[m!'.format(aluno))
