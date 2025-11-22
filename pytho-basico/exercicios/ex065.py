print('{:=^26}'.format('DESAFIO 65'))
cont = soma = int(0)
n = 0
q = 1
while n != 2:
    if n == 0:
        k = int(input('Quantos números inteiros você quer analisar? '))
    else:
        k = int(input('Mais quantos números você quer analisar? '))
    if k == 0:
        exit()
    print('_________________________________________________________')
    t = q + k
    while q < t:
        c = int((input(f'{q}º valor: ')))
        if q == 1:
            maior = menor = c
        if c > maior:
            maior = c
        if c < menor:
            menor = c
        soma += c
        cont += 1
        q += 1
    print('_________________________________________________________')
    print(f'A média dos {cont} valores digitados é {soma / cont:.2f}')
    print(f'O maior valor digitado foi {maior} e o menor foi {menor}')
    print('_________________________________________________________')
    print('''[1] para continuar
[2] para sair''')
    n = int(input('Sua escolha: '))
print('_________________________________________________________')
print('FIM DO PROGRAMA')
