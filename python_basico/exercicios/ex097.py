def escreva(txt):
    print('~' * (len(txt) + 2))
    print(f' {txt}')
    print('~' * (len(txt) + 2))


print(f'{'DESAFIO 97':=^26}')
msg = str(input('Digite algo: ')).strip()
escreva(msg)
