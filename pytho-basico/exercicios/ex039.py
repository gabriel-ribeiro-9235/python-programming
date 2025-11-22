from datetime import date
print('{:=^26}'.format('DESAFIO 39'))
print('Alistamento militar')
print('_ ' * 13)
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print('Você tem ou fará {} anos em {}.'.format(idade, date.today().year))
if idade == 18:
    print('\033[1;31mE deve se alistar ainda neste ano!\033[m')
elif idade < 18:
    print('\033[1;31mE deve se alistar em {}!\033[m'.format(date.today().year + (18 - idade)))
else:
    print('\033[1;31mE já deve ter se alistado em {}!\033[m'.format(ano + 18))
