from math import pow
print('{:=^26}'.format('DESAFIO 43'))
print('-=' * 13)
print('CALCULADORA DE IMC')
print('-=' * 13)
peso = float(input('PESO (kg): '))
altura = float(input('ALTURA (cm): '))
altura = altura / 100
imc = peso / pow(altura, 2)
print('-=' * 13)
print('IMC: {:.2f}'.format(imc))
if imc < 18.5:
    print('\033[31mVOCÊ ESTÁ ABAIXO DO PESO IDEAL!\033[m')
elif imc <= 25:
    print('\033[32mVOCÊ ESTÁ NO PESO IDEAL!\033[m')
elif imc <= 30:
    print('\033[33mVOCÊ ESTÁ EM SOBREPESO!\033[m')
elif imc <= 40:
    print('\033[31mVOCÊ ESTÁ COM OBESIDADE!\033[m')
else:
    print('\033[1;31mVOCÊ ESTÁ COM OBESIDADE MÓRBIDA!\033[m')
