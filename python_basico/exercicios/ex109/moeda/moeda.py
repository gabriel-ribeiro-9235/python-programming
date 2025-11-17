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
