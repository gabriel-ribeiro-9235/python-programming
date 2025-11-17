import math
print('{:=^26}'.format('DESAFIO 17'))
cateto1 = float(input('\033[31mCateto 1: \033[m'))
cateto2 = float(input('\033[33mCateto 2: \033[m'))
hipotenusa = math.hypot(cateto1, cateto2)
if hipotenusa == int(hipotenusa):
    hipotenusa = int(hipotenusa)
    print('\033[34mA hipotenusa vale:\033[32m {}\033[m'.format(hipotenusa))
else:
    print('\033[34mA hipotenusa vale: \033[32m{:.2f}\033[m'.format(hipotenusa))
