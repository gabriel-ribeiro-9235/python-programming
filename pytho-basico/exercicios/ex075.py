print(f'{'DESAFIO 75':=^26}')
print('______________________')
print('Digite 4 valores')
lista = (int(input('1º valor: ')),
         int(input('2º valor: ')),
         int(input('3º valor: ')),
         int(input('4º valor: ')))
print('______________________')
print(f'O 9 foi digitado {lista.count(9)} vezes' if lista.count(9)!=0 else 'O 9 não foi digitado')
print(f'O 3 foi o {lista.index(3)+1}º número digitado' if 3 in lista else 'O 3 não foi digitado')
print('Os números pares digitados foram: ', end='')
cont = 0
for n in lista:
    if n % 2 == 0:
        cont +=1
        if cont == 1:
            print(n, end='')
        else:
            print(f', {n}', end='')
