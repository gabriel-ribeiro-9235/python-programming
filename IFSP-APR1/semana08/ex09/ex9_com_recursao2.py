def verificaMaiusc(string):
    if string == '':
        return 'String vazia!'
    elif len(string) == 1:
        if string[0] in 'abcdefghijklmnopqrstuvwxyzáàãâóòõôéèẽêíìĩîúùũû':
            return False
        else:
            return True
    else:
        if string[0] in 'abcdefghijklmnopqrstuvwxyzáàãâóòõôéèẽêíìĩîúùũû':
            retorno = False
        else:
            retorno = True
        retorno = retorno and verificaMaiusc(string[1:])
        return retorno


txt = input('Digite um texto: ')
if verificaMaiusc(txt):
    print('Tudo maiúsculo!')
else:
    print('Há letras que não são maiúsculas!')
