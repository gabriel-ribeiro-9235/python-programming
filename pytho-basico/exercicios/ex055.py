print('{:=^26}'.format('DESAFIO 55'))
print('Digite o peso (kg) de 5 pessoas')
maior = 0
print('_' * 26)
for c in range(1, 6):
    peso = float(input('{}ª pessoa: '.format(c)))
    if c == 1:
        menor = peso
    if peso >= maior:
        maior = peso
    if peso <= menor:
        menor = peso
print('_' * 26)
if maior == int(maior):
    maior = int(maior)
if menor == int(menor):
    menor = int(menor)
print('Maior peso: {}kg'.format(maior))
print('Menor peso: {}kg'.format(menor))
print('_' * 26)
