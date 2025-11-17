print('{:=^26}'.format('DESAFIO 31'))
km = float(input('\033[34mDistânica da viagem (km): '))
if km <= 200:
    print('Valor da viagem: \033[33mR${:.2f}\033[m'.format(km*0.50))
else:
    print('Valor da viagem: \033[33mR${:.2f}\033[m'.format(km*0.45))
