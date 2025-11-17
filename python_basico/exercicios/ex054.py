from datetime import date
print('{:=^26}'.format('DESAFIO 54'))
print('Digite o ano de nascimento\nde cada uma das 7 pessoas')
maior = 0
menor = 0
print('_' * 26)
for c in range(1, 8):
    ano = int(input('{}ª pessoa: '.format(c)))
    idade = date.today().year - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1
    print('_' * 26)
print('''      CONTAGEM
Maiores de idade: {}
Menores de idade: {}'''.format(maior, menor))
print('_' * 26)
