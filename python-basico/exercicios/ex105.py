def notas(*num, sit=False):
    """
    -> Faz um relatório das notas de um aluno
    :param num: Notas do aluno
    :param sit: Caso queira saber se o aluno está aprovado ou reprovado
    :return: retorna um dicionário com diversos dados sobre as notas do aluno
    """
    tudo = dict()
    soma = sum(num)
    tudo['Total'] = len(num)
    tudo['Maior'] = max(num)
    tudo['Menor'] = min(num)
    tudo['Média'] = f'{soma/tudo["Total"]:.1f}'
    if sit:
        media = float(tudo['Média'])
        if media > 6:
            tudo['Situação'] = 'Aprovado'
        else:
            tudo['Situação'] = 'Reprovado'
    return tudo


print(f'{"DESAFIO 105":=^26}')
resp = notas(10, 9.5, 9, 7, sit=True)
print(resp)
