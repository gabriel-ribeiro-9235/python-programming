from random import randint
print(f'{'DESAFIO 68':=^26}')
print(f'{'PAR OU ÍMPAR':-^30}')
cont = 0
while True:
    cont += 1
    cpu = randint(0, 10)
    print('_' * 43)
    print('''Ímpar ou par?
[1] ímpar
[2] par''')
    escolha = int(input('Sua escolha: '))
    print('_' * 43)
    while escolha not in (1, 2):
        print('''Escolha inválida!
Ímpar ou par?
[1] ímpar
[2] par''')
        escolha = int(input('Sua escolha: '))
        print('_' * 43)
    jogador = int(input('Escolha um número de 0 a 10: '))
    while jogador not in range(0, 11):
        print('Escolha inválida!')
        print('_' * 43)
        jogador = int(input('Escolha um número de 0 a 10: '))
    numero = jogador + cpu
    print(f'O computador escolheu {cpu}')
    if numero % 2 == 0:
        if escolha == 1:
            print(f'{numero} é PAR! Você perdeu!')
            break
        else:
            print(f'{numero} é PAR! Você ganhou!')
    else:
        if escolha == 2:
            print(f'{numero} é ÍMPAR! Você perdeu!')
            break
        else:
            print(f'{numero} é ÍMPAR! Você ganhou!')
print('_' * 43)
if cont == 1:
    print('Você não ganhou nenhuma vez!')
elif cont == 2:
    print('Você ganhou uma apenas uma vez!')
else:
    print(f'Você teve {cont-1} vitórias consecutivas!')
print('FIM')
