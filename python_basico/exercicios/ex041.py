from datetime import date
print('{:=^26}'.format('DESAFIO 41'))
atleta = str(input('Nome do atleta: ')).strip()
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print('Neste ano, o(a) atleta \033[32m{}\033[m completa \033[32m{}\033[m anos e é da categoria'.format(atleta.title(), idade), end = ' ')
if idade < 9:
    print('\033[33mMIRIM\033[m')
elif idade < 14:
    print('\033[33mINFANTIL\033[m')
elif idade < 19:
    print('\033[33mJUNIOR\033[m')
elif idade < 25:
    print('\033[33mSÊNIOR\033[m')
else:
    print('\033[33mMASTER\033[m')
