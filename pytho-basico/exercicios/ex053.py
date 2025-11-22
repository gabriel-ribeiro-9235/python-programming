print('{:=^26}'.format('DESAFIO 53'))
print('TESTE DE PALÍNDROMOS')
frase = str(input('Digite uma palavra ou frase: ')).strip()
maiusculo = frase.upper().replace(' ', '')
s = 0
for c in range(0, len(maiusculo)):
    if maiusculo[c] != maiusculo[len(maiusculo) -1 -c]:
        s += 1
print('_' * (len(frase) + 20))
print('"{}" de trás pra frente fica'.format(maiusculo), end=' "')
for c in range(len(maiusculo) - 1, -1, -1):
    print(maiusculo[c], end='')
print('", então')
if s == 0:
    print('É um \033[32mpalíndromo\033[m!'.format(frase.capitalize()))
    print('_' * (len(frase) + 20))
else:
    print('Não é um \033[31mpalíndromo\033[m!'.format(frase.capitalize()))
    print('_' * (len(frase) + 23))
