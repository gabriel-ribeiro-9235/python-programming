print(f'{'DESAFIO 79':=^26}')
lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
    continuar = str(input('Deseja inserir mais valores?[S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção invállida! Deseja inserir mais valores?[S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
lista.sort()
print('_' * 38)
print(f'Os números digitos em ordem crescente foram {lista}')
