from time import sleep
print('{:=^26}'.format('DESAFIO 36'))
print('\033[31m-=' * 13)
print('Analisador de empréstimos')
print('-=' * 13, '\033[m')
casa = float(input('Valor do imóvel: \033[32mR$\033[m'))
salario = float(input('Seu salário: \033[32mR$\033[m'))
anos = float(input('Em quantos anos você quer pagar o imóvel? '))
anos = anos * 12
parcela = casa / anos
print('_' * 26)
print('Analisando...')
print('_' * 26)
sleep(1.5)
if parcela > 0.3 * salario:
    print('\033[31mEMPRÉSTIMO NEGADO!')
    print('O valor das parcelas comprometerá mais que 30% da sua renda mensal.\033[m')
else:
    print('\033[32mEMPRÉSTIMO ACEITO!\033[m')
    print('Número de parcelas: \033[36m{:.0f}\033[m'.format(anos))
    print('Valor das parcelas: \033[36mR${:.2f}\033[m'.format(parcela))
