print('{:=^26}'.format('DESAFIO 64'))
c = 0
cont = -1
soma = 0
while c != 999:
    soma += c
    cont += 1
    c = int(input('Digite um número (ou 999 para parar): '))
print('___________________________________________')
if cont == 0:
    print('Nenhum valor foi digitado!')
else:
    print(f'A soma dos {cont} valores digitados é {soma}')
print('___________________________________________')
