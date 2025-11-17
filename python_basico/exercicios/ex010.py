print('{:=^26}'.format('DESAFIO 10'))
n = float(input('Digite o valor que você tem: \033[32mR$\033[m'))
print('Hoje \033[31m(11/06/2025)\033[m, você pode comprar \033[32mUS${:.2f}\033[m'.format(n/5.55), end = ' ')
print('com \033[32mR${:.2f}\033[m'.format(n))
