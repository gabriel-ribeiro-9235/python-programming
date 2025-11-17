print('{:=^26}'.format('DESAFIO 27'))
nome = str(input('Digite um nome completo: ')).strip()
print('Primeiro nome: \033[32m{}\033[m'.format(nome.title()[:nome.find(' ')]))
print('Último nome: \033[32m{}\033[m'.format(nome.title()[nome.rfind(' ')+1:]))
