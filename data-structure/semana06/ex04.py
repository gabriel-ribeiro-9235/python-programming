lista_A = list()
lista_B = list()
lista_10 = list()
lista_C = list()
for i in range(5):
    lista_A.append(int(input(f'Insira o {i+1}º número de A: ')))
for i in range(5):
    lista_B.append(int(input(f'Insira o {i+1}º número de B: ')))
print('Agora digite 10 números:')
for i in range(10):
    lista_10.append(int(input(f'{i+1}º número: ')))
for i in range(len(lista_10)):
    if i < 5:
        lista_A.append(lista_10[i])
    else:
        lista_B.append(lista_10[i])
'''print(lista_A)
print(lista_B)
'''
for i in range(10):
    lista_C.append(int(lista_A[i]) + int(lista_B[i]))
print(f'''Lista A: {lista_A}
Lista B: {lista_B}
Lista C: {lista_C}''')
