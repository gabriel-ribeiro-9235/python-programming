print('{:=^26}'.format('DESAFIO 38'))
n = float(input('Escreva o primeiro valor: '))
k = float(input('Escreva o segundo valor: '))
print('_' * 26)
if n > k:
    print('O \033[31mprimeiro valor\033[m é o maior!')
elif n < k:
    print('O \033[31msegundo valor\033[m é o maior!')
else:
    print('Não existe valor maior, os dois \033[31msão iguais\033[m!')
