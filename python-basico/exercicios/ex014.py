print('{:=^26}'.format('DESAFIO 14'))
temperatura = float(input('Insira a temperatura em graus Celcius: '))
print('\033[32m{}ºC\033[m valem \033[31m{:.1f}ºF\033[m'.format(temperatura, (9*temperatura/5)+32))
