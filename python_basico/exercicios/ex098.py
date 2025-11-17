from time import sleep
def contador(i, f, p):
    if p < 0:
        p = -p
    elif p == 0:
        p = 1
    print('=' * 30)
    print(f'Contando de {i} até {f}\npulando de {p} em {p}...')
    if i > f:
        for c in range(i, f-1, -p):
            print(c, end=' ', flush=True)
            sleep(0.4)
    else:
        for c in range(i, f+1, p):
            print(c, end=' ', flush=True)
            sleep(0.4)
    print('FIM!')
    print('=' * 30)


print(f'{'DESAFIO 98':=^26}')
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora a sua vez de fazer a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
