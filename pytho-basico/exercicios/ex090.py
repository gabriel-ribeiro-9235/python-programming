print(f'{'DESAFIO 90':=^26}')
aluno = dict()
aluno['Nome'] = str(input('Nome: ')).strip().title()
aluno['Média'] = float(input('Média: '))
if aluno['Média'] >= 6:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
print('_' * 26)
for k, v in aluno.items():
    print(f'{k}: {v}')
