print('{:=^26}'.format('DESAFIO 44'))
preco = float(input('Preço normal: \033[32mR$\033[m'))
print('_ ' * 23)
print('Formas de pagamento:')
print("""[1] à vista \033[36mdinheiro/cheque\033[m: \033[31m10%\033[m de desconto
[2] à vista no \033[36mcartão\033[m: \033[31m5%\033[m de desconto
[3] em até \033[36m2x no cartão\033[m: preço normal
[4] \033[36m3x ou mais\033[m no cartão: \033[31m20%\033[m de juros""")
escolha = int(input('Escolha sua opção: '))
if escolha == 4:
    k = int(input('Número de parcelas: '))
print('_ ' * 23)
if escolha == 1:
    print('Valor a ser pago: \033[1mR${:.2f}\033[m'.format(0.9*preco))
elif escolha == 2:
    print('Valor a ser pago: \033[1mR${:.2f}\033[m'.format(0.95*preco))
elif escolha == 3:
    print('Valor a ser pago: \033[1mR${:.2f}\033[m em \033[1m2x de R${:.2f}\033[m'.format(preco, preco/2))
elif escolha == 4:
    print('Valor a ser pago: \033[1mR${:.2f}\033[m em \033[1m{}x de R${:.2f}\033[m'.format(1.2*preco, k, 1.2*preco/k))
else:
    print('\033[1;31mOPÇÃO INVÁLIDA! Tente novamente.\033[m')
