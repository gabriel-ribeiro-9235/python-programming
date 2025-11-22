print('{:=^26}'.format('DESAFIO 29'))
velocidade = float(input('Velocidade do veículo (km/h): '))
if velocidade > 80:
    print('\033[31mMULTADO!\033[m Você está {:.0f} km/h acima do limite de velocidade!'.format(velocidade-80))
    print('Valor da multa: \033[33mR${:.2f}\033[m'.format((velocidade-80)*7))
else:
    print('\033[36mVelocidade dentro do limite!')
    print('\033[32mPode prosseguir!\033[m')
