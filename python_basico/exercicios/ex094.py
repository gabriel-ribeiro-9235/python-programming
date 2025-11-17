print(f'{'DESAFIO 94':=^26}')
lista = list()
mulheres = list()
acimamed = list()
total = 0
while True:
    dict = {'Nome': str(input('Nome: ')).strip().title(),
            'Sexo': str(input('Sexo [M/F]: ')).strip().upper()[0],
            'Idade': int(input('Idade: '))
            }
    while dict['Sexo'] not in 'MF':
        dict['Sexo'] = str(input('Sexo inválido! escolha M (masculino) ou F (feminino): ')).strip().upper()[0]
    lista.append(dict.copy())
    dict.clear()
    print('=~' * 35)
    resp = str(input('Quer inserir mais pessoas?[S/N] ')).strip().upper()[0]
    while resp not in 'NS':
        resp = str(input('Opção inválida! Quer inserir mais pessoas?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    print('=~' * 35)
print('=~' * 35)
print(f'Você cadastrou {len(lista)} pessoas.')
for i in lista:
    total += i['Idade']
media = total / len(lista)
print(f'A média de idade das {len(lista)} pessoas cadastradas é {media:.1f} anos.')
for i in lista:
    if i['Sexo'] == 'F':
        mulheres.append(i['Nome'])
print(f'As mulheres cadastradas foram: {mulheres}')
for i in lista:
    if i['Idade'] > media:
        acimamed.append(i['Nome'])
        acimamed.append(i['Idade'])
print(f'{int(len(acimamed)/2)} pessoas com idade acima da média foram cadastradas.')
for v in range(0, len(acimamed), 2):
    print(f'  =>{acimamed[v]} com {acimamed[v+1]} anos.')
