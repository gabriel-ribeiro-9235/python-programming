print('{:=^26}'.format('DESAFIO 34'))
salario = float(input('Salário atual: \033[32mR$\033[m'))
if salario > 1250:
    salario = salario * 1.1
    print('Aumento de \033[34m10%\033[m')
else:
    salario = salario * 1.15
    print('Aumento de \033[34m15%\033[m')
print('Novo salário: \033[34mR${:.2f}\033[m'.format(salario))
