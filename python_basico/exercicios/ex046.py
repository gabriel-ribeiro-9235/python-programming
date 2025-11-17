from time import sleep
print('{:=^26}'.format('DESAFIO 46'))
print('FOGOS EM')
for c in range(10, -1, -1):
    if c == 0:
        print('\033[31m++BOOM!++\033[m')
    else:
        print('{:2}!'.format(c))
    sleep(1)
