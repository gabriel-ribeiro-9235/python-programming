print(f'{'DESAFIO 69':=^26}')
maior = 0
homem = 0
mulher20 = 0
while True:
    print('___________________________')
    print('    CADASTRE UMA PESSOA')
    print('___________________________')
    idade = int(input('Idade: '))
    if idade > 18:
        maior += 1
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        print('Sexo inválido. Tente novamente.')
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    print('___________________________')
    print('''[1] para cadastrar mais uma pessoa
[2] para sair''')
    escolha = int(input('Sua escolha: '))
    while escolha not in (1, 2):
        print('_' * 35)
        print('''[1] para cadastrar mais uma pessoa
[2] para sair''')
        escolha = int(input('Sua escolha: '))
    if escolha == 2:
        break
print(f'{'FIM DO PROGRAMA':~^36}')
print(f'{maior} pessoas com mais de 18 anos de idade foram cadastradas.' if maior > 1 else 'Nenhuma pessoa com mais de 18 anos foi cadastrada.' if maior == 0 else f'1 pessoa maior de 18 anos foi cadastrada.')
print(f'{homem} homens foram cadastrados.' if homem > 1 else 'Nenhum homem foi cadastrado.' if homem == 0 else f'1 homem foi cadastrado.')
print(f'{mulher20} mulheres com menos de 20 anos de idade foram cadastradas.' if mulher20 > 1 else 'Nenhuma mulher com menos de 20 anos foi cadastrada.' if mulher20 == 0 else '1 mulher com menos de 20 anos foi cadastrada.')
