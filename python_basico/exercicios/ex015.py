print('{:=^26}'.format('DESAFIO 15'))
dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))
print('O valor a ser pago é \033[1;4;33mR${:.2f}\033[m'.format((60*dias) + (km*0.15)))
