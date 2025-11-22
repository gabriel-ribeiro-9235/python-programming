print(f'{'DESAFIO 82':=^26}')
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja inserir mais valores?[S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção invállida! Deseja inserir mais valores?[S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
pares = []
impares = []
for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print('_' * 38)
print(f'Você digitou os seguinte valores {lista}')
print(f'Desses, são pares {pares}')
print(f'e são ímpares {impares}')
