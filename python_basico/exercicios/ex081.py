print(f'{'DESAFIO 81':=^26}')
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja inserir mais valores?[S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção invállida! Deseja inserir mais valores?[S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('_' * 38)
print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente foram {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
