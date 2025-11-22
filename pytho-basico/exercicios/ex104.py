def leiaint(msg):
    k = str(input(msg)).strip()
    while True:
        if k.isnumeric():
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            k = str(input(msg)).strip()
    return k



print(f'{"DESAFIO 104":=^26}')
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
