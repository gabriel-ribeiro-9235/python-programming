n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Terceiro número: "))
if n1 == n2 == n3:
    print("Os três números são iguais!")
elif n1 == n2 and n1 > n3:
    print("O primeiro e o segundo número são iguais e são os maiores!")
elif n1 == n3 and n1 > n2:
    print("O primeiro e o terceiro número são iguais e são os maiores!")
elif n1 > n2 and n1 > n3:
    print("O primeiro número é o maior!")
elif n2 == n3 and n2 > n1:
    print("O segundo e o terceiro número são iguais e são os maiores!")
elif n2 > n1 and n2 > n3:
    print("O segundo número é o maior!")
else:
    print("O terceiro número é o maior")
