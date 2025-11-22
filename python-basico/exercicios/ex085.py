print(f'{'DESAFIO 85':=^26}')
todos = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º valor: '))
    if n % 2 == 0:
        todos[0].append(n)
    else:
        todos[1].append(n)
todos[0].sort()
todos[1].sort()
print(f'Os valores pares digitados, em ordem crescente, foram: {todos[0]}')
print(f'Os valores ímpares digitados, em ordem crescente, foram: {todos[1]}')
