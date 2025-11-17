from datetime import date
print(f'{'DESAFIO 92':=^26}')
dados = dict()
dados['Nome'] = str(input('Nome: ')).strip().title()
nasc = int(input('Ano de Nascimento: '))
CTPS = int(input('Número da Carteira de Trabalho (se não tiver digite 0): '))
dados['Idade'] = date.today().year - nasc
if CTPS != 0:
    dados['CTPS'] = CTPS
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    tempo = 35 - (date.today().year - dados['Ano de contratação'])
    salario = float(input('Salário: R$'))
    dados['Salário'] = f'R${salario:.2f}'
    if tempo + dados['Idade'] > dados['Idade']:
        dados['Idade para se aposentar'] = tempo + dados['Idade']
    else:
        dados['Idade para se aposentar'] = f'{dados['Nome']} já tem idade para se aposentar!'
print('_' * 40)
for k, v in dados.items():
    print(f'{k}: {v}')
