print(f'{'DESAFIO 83':=^26}')
expressao = str(input('Digite a expressão: ')).strip()
if '()' in expressao or ')(' in expressao[:2] or ')(' in expressao[-2:]:
    print('Sua expressão está incorreta!')
elif expressao.count('(') == expressao.count(')'):
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')
