print(f'{'DESAFIO 84':=^26}')
pessoas = list()
dados = list()
leve = list()
pesado = list()
while True:
    dados.append(str(input('Nome: ')).strip().title())
    peso = float(input('Peso (kg): '))
    if peso == int(peso):
        peso = int(peso)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer inserir mais pessoas?[S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Opção inválida! Quer inserir mais pessoas?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('_' * 38)
print(f'Foram cadastradas {len(pessoas)} pessoas!')
for pos, p in enumerate(pessoas):
    if pos == 0:
        maior = menor = p[1]
    elif p[1] > maior:
        maior = p[1]
    elif p[1] < menor:
        menor = p[1]
for p in pessoas:
    if p[1] == menor:
        leve.append(p[0])
    if p[1] == maior:
        pesado.append(p[0])
print(f'O maior peso foi {maior}kg, que é o peso de {pesado}')
print(f'O menor peso foi {menor}kg, que é o peso de {leve}')
