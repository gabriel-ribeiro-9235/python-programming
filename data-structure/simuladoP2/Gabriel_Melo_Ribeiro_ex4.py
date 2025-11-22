def tiraUltima(string, letra):
    if len(string) == 0:
        return 'String vazia!'
    elif len(string) == 1:
        if string[0] == letra:
            return ''
        else:
            return string
    else:
        if string[-1] != letra:
            nova = tiraUltima(string[:-1], letra) + string[-1]
        else:
            nova = tiraUltima(string[:-1], 'Já foi retirada')
        return nova


txt = 'paralelepípedo'
print(tiraUltima(txt, 'p'))
