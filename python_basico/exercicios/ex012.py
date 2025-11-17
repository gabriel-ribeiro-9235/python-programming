print('{:=^26}'.format('DESAFIO 12'))
preco = float(input('Preço inicial: \033[32mR$\033[m'))
print('Com desconto de \033[32m5%\033[m o preço cai de \033[31m{}\033[m para \033[32mR${:.2f}\033[m'.format(preco, preco * 0.95))
