def fatorial(n, show=False):
    """
    -> Função usada para calcular o fatorial de um número
    e retorna as contas feitas se o usuário quiser
    :param n: fatorial a ser calculado
    :param show: se o usuário quer ou não ver as contas feitas
    :return: sem retorno
    """
    if n < 0:
        print('Não existe fatorial de negativo.')
        exit()
    k = 1
    if n == 0:
        print(f'{n}! = 1')
    else:
        for c in range(n, 0, -1):
            k *= c
        if show:
            print(f'{n}! = ', end='')
            for c in range(n, 0, -1):
                if c > 1:
                    print(f'{c}', end=' x ')
                else:
                    print(f'{c}', end=' = ' )
            print(f'{k}')
        else:
            print(f'{k}')


print(f'{"DESAFIO 102":=^26}')
fatorial(5, True)
