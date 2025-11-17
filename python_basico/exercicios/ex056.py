print('{:=^26}'.format('DESAFIO 56'))
print('Digite as informações de 4 pessoas')
print('_' * 26)
medidade = 0
hmais = 0
velho = 'nada'
shmais = 'nada'
thmais = 'nada'
qhmais = 'nada'
mm20 = 0
mulher = 0
for c in range(1, 5):
    print('{}ª pessoa'.format(c))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade (anos): '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo == 'MASCULINO' or sexo == 'MASC' or sexo == 'HOMEM':
        sexo = 'M'
    elif sexo == 'FEMININO' or sexo == 'FEM' or sexo == 'MULHER':
        sexo = 'F'
    elif sexo != 'M' and sexo != 'F':
        print('Sexo inválido!')
        exit()
    medidade += idade
    if sexo == 'F':
        mulher +=1
    if sexo == 'M':
        if idade == hmais:
            if shmais != 'nada':
                if thmais != 'nada':
                    qhmais = nome
                else:
                    thmais = nome
            else:
                shmais = nome
        elif idade >= hmais:
            hmais = idade
            shmais = 'nada'
            thmais = 'nada'
            qhmais = 'nada'
            velho = nome
    if sexo == 'F' and idade < 20:
        mm20 += 1
    print('_' * 26)
if shmais != 'nada':
    if thmais != 'nada':
        if qhmais != 'nada':
            print('Todos os homens têm a mesma idade,\nlogo a média de idade é {} anos,\nque é a idade deles.'.format(idade))
            exit()
        else:
            print('{}, {} e {} são os homens mais velhos e têm {} anos.'.format(velho, shmais, thmais, hmais))
    else:
        print('{} e {} são os homens mais velhos e têm {} anos.'.format(velho, shmais, hmais))
else:
    print('{} é o homem mais velho e tem {} anos.'.format(velho, hmais))
if medidade / 4 == int(medidade / 4):
    print('A média de idade das 4 pessoas é {:.0f} anos.'.format(medidade / 4))
else:
    print('A média de idade das 4 pessoas é {:.1f} anos.'.format(medidade/4))
if mm20 != 0:
    print('O número de mulheres com menos de 20 anos é {}.'.format(mm20))
elif mulher != 0:
    print('Nenhuma mulher tem menos de 20 anos.')
else:
    print('Dentre as 4 pessoa nenhuma é mulher.')
print('_' * 26)
