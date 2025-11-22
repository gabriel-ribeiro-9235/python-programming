print('{:=^26}'.format('DESAFIO 59'))
n = 0
while n != 5:
    n = 0
    a = float(input('1º valor: '))
    if a == int(a):
        a = int(a)
    b = float(input('2º valor: '))
    if b == int(b):
        b = int(b)
    while n != 4 and n != 5:
        print('''________________________
O que você quer fazer
com esses valores?
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
        n = int(input('Sua escolha: '))
        print('________________________')
        if n == 1:
            print(f'{a} + {b} = {a + b}')
        elif n == 2:
            print(f'{a} * {b} = {a * b}')
        elif n == 3:
            print(f'O maior valor é {max(a, b)}')
        elif n != 4 and n != 5:
            print('Opção inválida! Tente novamente.')
print('FIM')
