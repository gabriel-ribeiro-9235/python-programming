lista = [2, 0, 4, 10]
par = []

for numero in lista:
    if numero % 2 == 0:
        par.append(numero)

if len(par) == 0:
    print('Lista vazia!')
elif par == lista:
    print("Todos pares!")
else:
    print("Nem todos são pares!")
