lista = [1, 2, 3, 4, 10]
mult = 1
for num in lista:
    if num % 2 == 1:
        mult *= num
print(f"A multiplicação de todos os números ímpares da lista vale: {mult}")
