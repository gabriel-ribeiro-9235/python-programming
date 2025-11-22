print('{:=^26}'.format('DESAFIO 57'))
sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()[0]
    if sexo != 'F' and sexo != 'M':
        print('Sexo inválido. Tente novamente.')
if sexo == 'F':
    print('_________________________')
    print('Sexo escolhido: Feminino')
    print('_________________________')
elif sexo == 'M':
    print('__________________________')
    print('Sexo escolhido: Masculino')
    print('__________________________')
