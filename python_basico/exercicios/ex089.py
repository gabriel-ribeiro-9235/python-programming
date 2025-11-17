print(f'{'DESAFIO 89':=^26}')
notas = list()
aluno = list()
boletim = list()
while True:
    print('_' * 26)
    nome = str(input('Nome: ')).strip().title()
    aluno.append(nome)
    nota1 = float(input('Nota 1: '))
    notas.append(nota1)
    nota2 = float(input('Nota 2: '))
    notas.append(nota2)
    media = (nota1 + nota2) / 2
    print('_' * 26)
    aluno.append(notas[:])
    notas.clear()
    aluno.append(media)
    boletim.append(aluno[:])
    aluno.clear()
    resp = str(input('Cadastrar mais aluno?[S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Opção inválida! Cadastrar mais aluno?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('_' * 26)
print(f'{'Nº':5}{'Aluno':<10}{'Média':^5}')
for pos, aluno in enumerate(boletim):
    print(f'{pos+1:<5}{boletim[pos][0]:<10}{boletim[pos][2]:^5.1f}')
print('_' * 26)
while True:
    n = int(input('Digite o número do aluno que você deseja ver as notas (ou 999 para sair): '))
    if n == 999:
        break
    elif n <= len(boletim):
        print(f'\nNotas de {boletim[n-1][0]}: {boletim[n-1][1]}\n')
