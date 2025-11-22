import math
print('{:=^26}'.format('DESAFIO 18'))
n = math.pi / 180
angulo = float(input('Insira um ângulo: '))
if angulo == int(angulo):
    angulo = int(angulo)
print('\033[32msen({}) = {:.3f}'.format(angulo, math.sin(angulo*n)))
print('\033[34mcos({}) = {:.3f}'.format(angulo, math.cos(angulo*n)))
print('\033[31mtan({}) = {:.3f}\033[m'.format(angulo, math.tan(angulo*n)))
