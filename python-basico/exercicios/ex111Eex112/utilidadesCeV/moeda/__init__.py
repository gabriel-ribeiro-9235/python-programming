def moeda(p, cifra='R$'):
    return f'{cifra}{p:.2f}'.replace('.', ',')

def metade(p, form=False):
    if form:
        return moeda(p / 2)
    else:
        return p / 2

def dobro(p, form=False):
    if form:
        return moeda(p * 2)
    else:
        return p * 2

def aumentar(p, a, form=False):
    if form:
        return moeda((1 + a / 100) * p)
    else:
        return (1 + a / 100) * p

def diminuir(p, d, form=False):
    if form:
        return moeda((1 - d / 100) * p)
    else:
        return (1 - d / 100) * p

def resumo(p, a=0, b=0):
    print('_' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('_' * 30)
    print(f'Preço analisado:   {moeda(p)}')
    print(f'Dobro do preço:    {dobro(p, True)}')
    print(f'Metade do preço:   {metade(p, True)}')
    if a != 0:
        print(f'{a}% de aumento:    {aumentar(p, a, True)}')
    if b != 0:
        print(f'{b}% de redução:    {diminuir(p, b, True)}')
    print('_' * 30)
