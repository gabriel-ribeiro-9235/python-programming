def contador(* num):
    print('-=' * 15)
    print(f'{num} tem {len(num)} elementos')
    print(f'O maior valor é {max(num)}')
    print('-=' * 15)


print(f'{'DESAFIO 99':=^26}')
contador(2, 9, 5, 7, 1)
contador(4, 4, 4, 0)
contador(2, 0, 2)
contador(8, 0)
contador(6, 0, 2)
