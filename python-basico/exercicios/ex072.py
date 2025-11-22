print(f'{'DESAFIO 72':=^26}')
num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
       'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
       'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
       'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Escolha um número de 0 a 20: '))
    if 0 <= n <= 20:
        break
    else:
        print('Número inválido! ', end='')
print(f'{n} por extenso é "{num[n].upper()}"')
