print(f'{'DESAFIO 66':=^26}')
soma = cont = 0
while True:
    n = int(input('Digite um número [ou 999 para parar]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print('_' * 44)
if cont == 0:
    print('Você não digitou nenhum número.')
elif cont == 1:
    print(f'Você digitou apenas o número {soma}')
else:
    print(f'Você digitou {cont} números e a soma deles é {soma}')
